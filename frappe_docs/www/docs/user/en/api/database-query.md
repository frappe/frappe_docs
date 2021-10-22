---
add_breadcrumbs: 1
title: DatabaseQuery - API
metatags:
 description: >
  API methods for querying records in Frappe
---

# DatabaseQuery

It's the engine powers the List, Report and some of the favourite developer APIs
like `frappe.get_all` and `frappe.get_list`

## Filters

DatabaseQuery likes it's filters in a specific format....okay, it supports
various different formats, but it generally looks something like this =>

> Table > Column > Operator > Value

So here Table may be optional. So you'd have a filter (one where condition) look
like [["column", "=", "value"]] or {"column": "value"}. Because of this
restriction, you can only ever compare columns to values. This PR aims to add
support for Column to Column comparison.

There's a few broader ways of writing filters

### Dict Notation

Find out which documents have been modified after their initial creation (Compare two datetime columns)

Check if search_field value has been used in description (Check if dynamic value in document is used elsewhere [like])

```python
In [1]: from frappe.query_builder import Column

In [2]: frappe.get_all("Note", {"modified": (">", Column("creation"))})
Out[2]: [{'name': 'SUjXJ1Wa0R'}, {'name': 'tUSNajSteH'}, {'name': '2sC3n9l0N0'}]
```

### List Notation

> TODO: Add introductory content & examples

### Filter Object Notation


This allows ```frappe.qb``` objects to be passed directly as filters.

```python
In [1] from frappe.query_builder import DocType

In [2] test_table = DocType("Test Table")

In [3]: frappe.db.delete(test_table, filters=(test_table.name=="TestUser") | (test_table.age==10), run=False)
Out[3]: DELETE FROM "tabTest Table" WHERE "name"=\'TestUser\' OR "age"=10
```

Query below selects `name` form `tabUser` matching the filters passed as `frappe.qb` objects.

```python
In [1]: test_table = DocType("User")

In [2]: frappe.db.get_value(test_table,
		filters=(test_table.email=="admin@localhost.com") | (test_table.name.like("Administrator")),
		fieldname=["name"], debug=True)
Out[2]: SELECT "name" FROM "tabUser" WHERE "email"='example@localhost.com' OR "name" LIKE 'Example'
		 Execution time: 0.1 sec
		 'Administrator'
```
## frappe.db.get_list

`frappe.get_list(doctype, filters, or_filters, fields, order_by, group_by,
start, page_length)`

- Also aliased to `frappe.get_list`

Returns a list of records from a `doctype` table. ORM Wrapper for a `SELECT`
query. Will also apply user permissions for the records for the session user.
Only returns the document names if the `fields` keyword argument is not given.
By default this method returns a list of `dict`s, but, you can pluck a
particular field by giving the `pluck` keyword argument:

```python
In [1]: frappe.db.get_list('Employee')
Out [1]: [{'name': 'HR-EMP-00008'}, {'name': 'HR-EMP-00006'}, {'name': 'HR-EMP-00010'}]

# with pluck
In [2]: frappe.db.get_list('Employee', pluck='name')
Out [2]: ['HR-EMP-00008', 'HR-EMP-00006', 'HR-EMP-00010']
```

Combining filters and other arguments:

```python
In [1]: frappe.db.get_list('Task',
	filters={
		'status': 'Open'
	},
	fields=['subject', 'date'],
	order_by='date desc',
	start=10,
	page_length=20,
	as_list=True
)
Out [1]: (('Update Branding and Design', '2019-09-04'),
('Missing Documentation', '2019-09-02'),
('Fundraiser for Foundation', '2019-09-03'))
```

To fetch tasks with date after 2019-09-08
```python
In [2]: frappe.db.get_list('Task', filters={
	'date': ['>', '2019-09-08']
})
```

To fetch tasks with date between 2020-04-01 and 2021-03-31 (both inclusive)
```python
In [3]: frappe.db.get_list('Task', filters=[[
	'date', 'between', ['2020-04-01', '2021-03-31']
]])
```

To fetch tasks with subject that contains "test"
```python
In [4]: frappe.db.get_list('Task', filters={
	'subject': ['like', '%test%']
})
```

To get the count of tasks grouped by status
```python
In [5]: frappe.db.get_list('Task',
	fields=['count(name) as count', 'status'],
	group_by='status'
)
Out [5]: [{'count': 1, 'status': 'Working'},
 {'count': 2, 'status': 'Overdue'},
 {'count': 2, 'status': 'Open'},
 {'count': 1, 'status': 'Filed'},
 {'count': 20, 'status': 'Completed'},
 {'count': 1, 'status': 'Cancelled'}]
```

## frappe.get_all

`frappe.get_all(doctype, filters, or_filters, fields, order_by, group_by,
start, page_length)`

- Also aliased to `frappe.db.get_all`

Same as `frappe.get_list` but will fetch all records without applying
permissions.
