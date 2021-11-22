---
add_breadcrumbs: 1
title: Testing
metatags:
 description: >
  Frappe provides some basic tooling to write automated tests. We use the standard
  library unittest provided by Python.
---

# Testing

Frappe provides some basic tooling to write automated tests. There are some
basic rules:

1. Test can be anywhere in your repository but must begin with `test_` and
   should be a `.py` file.
1. The test runner will automatically build test records for dependent DocTypes
   identified by the `Link` type field (Foreign Key).
1. For non-DocType tests, you can write simple unit tests and prefix your file
   names with `test_`.


## Writing Tests

When you create a new DocType (in developer mode), the boilerplate files also
contain the `test_{doctype}.py` file. The test file should handle creating
dependencies and cleaning them up.

Here is a sample test file referred from `test_event.py`.

```py
import frappe
import unittest

def create_events():
	if frappe.flags.test_events_created:
		return

	frappe.set_user("Administrator")
	doc = frappe.get_doc({
		"doctype": "Event",
		"subject":"_Test Event 1",
		"starts_on": "2014-01-01",
		"event_type": "Public"
	}).insert()

	doc = frappe.get_doc({
		"doctype": "Event",
		"subject":"_Test Event 3",
		"starts_on": "2014-01-01",
		"event_type": "Public"
		"event_individuals": [{
			"person": "test1@example.com"
		}]
	}).insert()

	frappe.flags.test_events_created = True


class TestEvent(unittest.TestCase):
	def setUp(self):
		create_events()

	def tearDown(self):
		frappe.set_user("Administrator")

	def test_allowed_public(self):
		frappe.set_user("test1@example.com")
		doc = frappe.get_doc("Event", frappe.db.get_value("Event",
			{"subject":"_Test Event 1"}))
		self.assertTrue(frappe.has_permission("Event", doc=doc))

	def test_not_allowed_private(self):
		frappe.set_user("test1@example.com")
		doc = frappe.get_doc("Event", frappe.db.get_value("Event",
			{"subject":"_Test Event 2"}))
		self.assertFalse(frappe.has_permission("Event", doc=doc))
```


## Writing Tests for Commands

To write tests for your Bench commands, you can group your tests under a
Class that extends `BaseTestCommands` from `frappe.tests.test_commands` and
`unittest.TestCase` so that it runs during the `bench run-tests` command.

For reference, here is are some tests written for the `bench execute` command.

```py
class TestCommands(BaseTestCommands, unittest.TestCase):
	def test_execute(self):
		# test 1: execute a command expecting a numeric output
		self.execute("bench --site {site} execute frappe.db.get_database_size")
		self.assertEqual(self.returncode, 0)
		self.assertIsInstance(float(self.stdout), float)

		# test 2: execute a command expecting an errored output as local won't exist
		self.execute("bench --site {site} execute frappe.local.site")
		self.assertEqual(self.returncode, 1)
		self.assertIsNotNone(self.stderr)

		# test 3: execute a command with kwargs
		# Note:
		# terminal command has been escaped to avoid .format string replacement
		# The returned value has quotes which have been trimmed for the test
		{% raw -%}
		self.execute("""bench --site {site} execute frappe.bold --kwargs '{{"text": "DocType"}}'""")
		{%- endraw %}
		self.assertEqual(self.returncode, 0)
		self.assertEqual(self.stdout[1:-1], frappe.bold(text='DocType'))
```

You can also give inputs to your commands by using `"cmd_input"` as a key
in kwargs parameter in `execute` method by providing the value as byte string.

For reference, here is a test written for frappe's `make-app` command.

```py
class TestCommands(BaseTestCommands, unittest.TestCase):
	def test_make_app(self):
		user_input = [
			b"Test App", # title
			b"This app's description contains 'single quotes' and \"double quotes\".", # description
			b"Test Publisher", # publisher
			b"example@example.org", # email
			b"", # icon
			b"", # color
			b"MIT" # app_license
		]
		app_name = "testapp0"
		apps_path = os.path.join(frappe.utils.get_bench_path(), "apps")
		test_app_path = os.path.join(apps_path, app_name)
		self.execute(f"bench make-app {apps_path} {app_name}", {"cmd_input": b'\n'.join(user_input)})
		self.assertEqual(self.returncode, 0)
		self.assertTrue(
			os.path.exists(test_app_path)
		)

		# cleanup
		shutil.rmtree(test_app_path)
```

## Running Tests

Running tests could require additional dependencies specified by apps in their `dev-requirements.txt` file. Before running tests, make sure all apps have development dependencies installed using `bench setup requirements --dev`.

Run the following command to run all your tests. It will build all
the test dependencies once and run your tests. You should run tests from
`frappe_bench` folder.

```bash
# run all tests
bench --site [sitename] run-tests

# run tests for only frappe app
bench --site [sitename] run-tests --app frappe

# run tests for the Task doctype
bench --site [sitename] run-tests --doctype "Task"

# run a test using module path
bench --site [sitename] run-tests --module frappe.tests.test_api

# run a specific test from a test file
bench --site [sitename] run-tests --module frappe.tests.test_api --test test_insert_many

# run tests without creating test records
bench --site [sitename] run-tests --skip-test-records --doctype "Task"

# profile tests and show a report after tests execute
bench --site [sitename] run-tests --profile --doctype "Task"
.
----------------------------------------------------------------------
Ran 1 test in 0.010s

OK

9133 function calls (8912 primitive calls) in 0.011 seconds

Ordered by: cumulative time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
	2    0.000    0.000    0.008    0.004 /home/frappe/frappe-bench/apps/frappe/frappe/model/document.py:187(insert)
	1    0.000    0.000    0.003    0.003 /home/frappe/frappe-bench/apps/frappe/frappe/model/document.py:386(_validate)
	13   0.000    0.000    0.002    0.000 /home/frappe/frappe-bench/apps/frappe/frappe/database.py:77(sql)
	255  0.000    0.000    0.002    0.000 /home/frappe/frappe-bench/apps/frappe/frappe/model/base_document.py:91(get)
	12   0.000    0.000    0.002    0.000


# verbose log level for tests
bench --site [sitename] --verbose run-tests
```

## Running Tests Parallelly

As the number of tests grows in the project, it takes a long time for tests to complete if it runs serially on one machine.
Running tests in parallel across many test machines can save time in Continuous Integration (CI).

### Parallel Tests

**Command:**

```bash
bench --site [sitename] --app [app-name] run-parallel-tests --build-id <build-number> --total-build <total-number-of-builds>
```

**Usage:**

If you want to run tests across 2 CI instances your command will be as follows:

```bash
# in first CI instance
bench --site [sitename] run-parallel-tests --build-id 1 --total-builds 2

# in second CI instance
bench --site [sitename] run-parallel-tests --build-id 2 --total-builds 2
```

**Note:** The command will split all test files into 2 parts and execute them in those CI instances.
The first half of the test list will be executed in the first instance and the second half of the test list will be executed in the second instance.

### Parallel tests with orchestrator

It may happen that each test takes a different amount of time for completion which may result in imbalanced time across CI builds. To mitigate this you can use [test orchestrator](https://github.com/frappe/test-orchestrator) which runs the next test based on the availability of CI instance. The command to use the test orchestrator for the parallel test is as follows.

**Command:**

```bash
bench --site [sitename] --app [app-name] run-parallel-tests --use-orchestrator
```

**Usage:**

If you want to run tests across 2 CI instances your command will be as follows

```bash
# in first CI instance
bench --site [sitename] run-parallel-tests --use-orchestrator

# in second CI instance
bench --site [sitename] run-parallel-tests --use-orchestrator
```

**Note:** Environment variables `CI_BUILD_ID` and `ORCHESTRATOR_URL` are required for this command. `CI_BUILD_ID` is the unique ID that you get for each build run of CI.
`ORCHESTRATOR_URL` is the publicly accessible URL that you get after hosting the [orchestrator](https://github.com/frappe/test-orchestrator).

### Comparison

For clarity on how the above variants of parallel test commands may work check the following example.

Suppose there are 4 test files as follows

```sh
test_module_one.py      4 mins (execution time)
test_module_two.py      2 mins
test_module_three.py    1 min
test_module_four.py     1 min
```

Time required without parallel test command.

```sh
test_module_one.py      4 mins
test_module_two.py      2 mins
test_module_three.py    1 min
test_module_four.py     1 min
==============================
Total Wait Time         8 mins
```

Time required with the first command that auto splits test files across 2 test instances.

```sh
# First instance                  # Second instance
test_module_one.py    4 mins      test_module_three.py   1 min
test_module_two.py    2 mins      test_module_four.py    1 min
----------------------------      ----------------------------
                      6 mins                            2 mins

==============================
Total Wait Time         6 mins
```

It may happen that the time required with the second command that uses orchestrator which runs tests based on availability across 2 test instances.

```sh
# First instance                  # Second instance
test_module_one.py    4 mins      test_module_two.py    2 mins
----------------------------      test_module_three.py  1 mins
                      4 mins      test_module_four.py   1 min
                                  ----------------------------
                                                        4 mins
==============================
Total Wait Time         4 mins
```

**Note:** Only one test file is executed on the first instance because it is busy for 4 mins. By that time, the 2nd instance is able to execute other test files which help in balancing time across builds.
