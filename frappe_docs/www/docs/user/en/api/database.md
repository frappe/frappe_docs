---
add_breadcrumbs: 1
title: Database - API
metatags:
 description: >
  API methods for querying, updating or creating records in Frappe
---

# Database API

## frappe.db.get_list
`frappe.db.get_list(doctype, filters, or_filters, fields, order_by, group_by, start, page_length)`

- Also aliased to `frappe.get_list`

Returns a list of records from a `doctype` table. ORM Wrapper for a `SELECT`
query. Will also apply user permissions for the records for the session user. Only returns the document names if the `fields` keyword argument is not given. By default this method returns a list of `dict`s, but, you can pluck a particular field by giving the `pluck` keyword argument:

```python
frappe.db.get_list('Employee')

# output
[{'name': 'HR-EMP-00008'},
 {'name': 'HR-EMP-00006'},
 {'name': 'HR-EMP-00010'},
 {'name': 'HR-EMP-00005'}
]

# with pluck
frappe.db.get_list('Employee', pluck='name')

# output
['HR-EMP-00008',
 'HR-EMP-00006',
 'HR-EMP-00010',
 'HR-EMP-00005'
]
```

Combining filters and other arguments:

```python
frappe.db.get_list('Task',
	filters={
		'status': 'Open'
	},
	fields=['subject', 'date'],
	order_by='date desc',
	start=10,
	page_length=20,
	as_list=True
)

# output
(('Update Branding and Design', '2019-09-04'),
('Missing Documentation', '2019-09-02'),
('Fundraiser for Foundation', '2019-09-03'))

# Tasks with date after 2019-09-08
frappe.db.get_list('Task', filters={
	'date': ['>', '2019-09-08']
})

# Tasks with date between 2020-04-01 and 2021-03-31 (both inclusive)
frappe.db.get_list('Task', filters=[[
	'date', 'between', ['2020-04-01', '2021-03-31']
]])

# Tasks with subject that contains "test"
frappe.db.get_list('Task', filters={
	'subject': ['like', '%test%']
})

# Count number of tasks grouped by status
frappe.db.get_list('Task',
	fields=['count(name) as count', 'status'],
	group_by='status'
)
# output
[{'count': 1, 'status': 'Working'},
 {'count': 2, 'status': 'Overdue'},
 {'count': 2, 'status': 'Open'},
 {'count': 1, 'status': 'Filed'},
 {'count': 20, 'status': 'Completed'},
 {'count': 1, 'status': 'Cancelled'}]
```

## frappe.db.get_all
`frappe.db.get_all(doctype, filters, or_filters, fields, order_by, group_by, start, page_length)`

- Also aliased to `frappe.get_all`

Same as `frappe.db.get_list` but will fetch all records without applying permissions.

## frappe.db.get_value
`frappe.db.get_value(doctype, name, fieldname)` or `frappe.db.get_value(doctype, filters, fieldname)`

- Also aliased to `frappe.get_value` and `frappe.db.get_values`

Returns a document's field value or a list of values.

```python
# single value
subject = frappe.db.get_value('Task', 'TASK00002', 'subject')

# multiple values
subject, description = frappe.db.get_value('Task', 'TASK00002', ['subject', 'description'])

# as dict
task_dict = frappe.db.get_value('Task', 'TASK00002', ['subject', 'description'], as_dict=1)
task_dict.subject
task_dict.description

# with filters, will return the first record that matches filters
subject, description = frappe.db.get_value('Task', {'status': 'Open'}, ['subject', 'description'])
```

## frappe.db.get\_single\_value
`frappe.db.get_single_value(doctype, fieldname)`

Returns a field value from a Single DocType.

```python
timezone = frappe.db.get_single_value('System Settings', 'timezone')
```

## frappe.db.set_value
`frappe.db.set_value(doctype, name, fieldname, value)`

- Also aliased to `frappe.db.update`

Sets a field's value in the database, does not call the ORM triggers but updates
the modified timestamp (unless specified not to).

```python
# update a field value
frappe.db.set_value('Task', 'TASK00002', 'subject', 'New Subject')

# update multiple values
frappe.db.set_value('Task', 'TASK00002', {
	'subject': 'New Subject',
	'description': 'New Description'
})

# update without updating the `modified` timestamp
frappe.db.set_value('Task', 'TASK00002', 'subject', 'New Subject', update_modified=False)
```

> This method won't call ORM triggers like `validate` and `on_update`. Use this
> method to update hidden fields or if you know what you are doing.

## frappe.db.exists
`frappe.db.exists(doctype, name)`

Returns true if a document record exists.

```python
# check if record exists by name
frappe.db.exists('Task', 'TASK00002') # True

# check if record exists by filters
frappe.db.exists({
	'doctype': 'Task',
	'status': 'Open',
	'subject': 'New Task'
})
```

## frappe.db.count
`frappe.db.count(doctype, filters)`

Returns number of records for a given `doctype` and `filters`.

```python
# total number of Task records
frappe.db.count('Task')

# total number of Open tasks
frappe.db.count('Task', {'status': 'Open'})
```

## frappe.db.delete
`frappe.db.delete(doctype, filters)`

Delete `doctype` records that match `filters`.
This runs a DML command, which means it can be rolled back.
If no filters specified, all the records of the doctype are deleted.

```python
frappe.db.delete("Route History", {
	"modified": ("<=", last_record_to_keep[0].modified),
	"user": user
})

frappe.db.delete("Error Log")
frappe.db.delete("__Test Table")
```

You may pass the doctype name or an internal table name. Conventionally,
internal tables in Frappe are prefixed with `__`. The API follows this.
The above commands run an unconditional `DELETE` query over tables **tabError Log**
and **__Test Table**.

## frappe.db.truncate
`frappe.db.truncate(doctype)`

Truncate a table in the database. This runs a DDL command `TRUNCATE TABLE`, a
commit is triggered before the statement is executed. This action cannot be
rolled back. You may want to use this for clearing out log tables periodically.

```python
frappe.db.truncate("Error Log")
frappe.db.truncate("__Test Table")
```

The above commands run a `TRUNCATE` query over tables **tabError Log**
and **__Test Table**.

## frappe.db.commit
`frappe.db.commit()`

Commits current transaction. Calls SQL `COMMIT`.

> In most cases you don't need to commit manually. Refer Frappe's [Database transaction model](#database-transaction-model) below.

## frappe.db.rollback
`frappe.db.rollback()`

Rollbacks current transaction. Calls SQL `ROLLBACK`.

> Frappe will automatically run `frappe.db.rollback()` if an exception is thrown
> during a Web Request of type `POST` or `PUT`. Use this if you have to rollback
> early in a transaction.

## frappe.db.sql
`frappe.db.sql(query, values, as_dict)`

Execute an arbitrary SQL query. This may be useful for complex server side reports with join statements, adjusting the database to new features, etc.

Example:

```python
values = {'company': 'Frappe Technologies Inc'}
data = frappe.db.sql("""
	SELECT
		acc.account_number
		gl.debit
		gl.credit
	FROM `tabGL Entry` gl
		LEFT JOIN `tabAccount` acc
		ON gl.account = acc.name
	WHERE gl.company = %(company)s
""", values=values, as_dict=0)
```

> Avoid using this method as it will bypass validations and integrity checks. It's always better to use [frappe.get\_doc](https://frappeframework.com/docs/user/en/api/document#frappeget_doc), [frappe.db.get\_list](#frappedbget_list), etc., if possible.

## frappe.db.multisql
`frappe.db.multisql({'mariadb': mariadb_query, 'postgres': postgres_query})`

Execute the suitable SQL statement for any supported database engine.

## frappe.db.rename_table

`frappe.db.rename_table(old_name, new_name)`

Executes a query to change table name. Specify the DocType or internal table's name directly to rename the table.

Example:

```python
frappe.db.rename_table("__internal_cache", "__temporary_cache")
frappe.db.rename_table("todo", "ToDo")
```

The second example should be used only if you understand the ramifications of it.

> Don't use this to rename DocType tables. Use `frappe.rename_doc` for that instead

## frappe.db.describe

`frappe.db.describe(doctype)`

Returns a tuple of the table description for given DocType.

## frappe.db.change\_column\_type

`frappe.db.change_column_type(doctype, column, new_type)`

Changes the type of column for specified DocType.

## frappe.db.add_index

`frappe.db.add_index(doctype, fields, index_name)`

Creates indexes for doctypes for the specified fields. 

> Note: if you want an index on a TEXT or a BLOB field, you must specify a fixed length to do that.

Example:

```py
frappe.db.add_index("Notes", ["id(10)", "content(500)"], index_name)
```

## Database transaction model

Frappe's database abstractions implement a sane transaction model by default. So in most cases, you won't have to deal with SQL transactions manually. A broad description of this model is described below:

### Web requests

- While performing `POST` or `PUT`, if any writes were made to the database, they are committed at end of the successful request.
- AJAX calls made using `frappe.call` are `POST` by default unless changed.
- `GET` requests do not cause an implicit commit.
- Any **uncaught** exception during handling of request will rollback the transaction.

### Background/scheduled Jobs

- Calling a function as background or scheduled job will commit the transaction after successful completion.
- Any **uncaught** exception will cause rollback of the transaction.

### Patches

- Successful completion of the patch's `execute` function will commit the transaction automatically.
- Any **uncaught** exception will cause rollback of the transaction.

### Unit tests

- Transaction is committed after running one test module. Test module means any python test file like `test_core.py`.
- Transaction is also committed after finishing all tests.
- Any **uncaught** exception will exit the test runner, hence won't commit.

> Note: If you're catching exceptions anywhere, then database abstraction does not know that something has gone wrong hence you're responsible for the correct rollback of the transaction.
