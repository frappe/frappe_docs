---
add_breadcrumbs: 1
title: Query Builder - API
metatags:
  description: API methods for building SQL queries
---

# Query Builder

`frappe.qb` is a query builder written around PyPika to build a single interface for cross-db queries

While developing apps, you'll often need to retrieve some specific data from the database. One way to do this is to use `frappe.db.sql` and write raw SQL queries.

Maybe something like

```python
result = frappe.db.sql(
	f"""
	SELECT `path`,
			COUNT(*) as count,
			COUNT(CASE WHEN CAST(`is_unique` as Integer) = 1 THEN 1 END) as unique_count
	FROM `tabWeb Page View`
	WHERE `creation` BETWEEN {some_date} AND {some_later_date}
	"""
)
```

The query builder API makes this easier by providing a simple pythonic API to build SQL queries without limiting the flexibility of handwritten SQL.

The same query in the query builder would look something like

```python
import frappe
from frappe.query_builder.functions import Count

WebPageView = frappe.qb.DocType("Web Page View")
count_all = frappe.qb.fn.Count('*').as_("count")

case = frappe.qb.terms.Case().when(WebPageView.is_unique == "1", "1")
count_is_unique = Count(case).as_("unique_count")

query = (
	frappe.qb.from_(WebPageView)
		.select(WebPageView.path, count_all, count_is_unique)
		.where(Web_Page_View.creation[some_date:some_later_date])
)

result = frappe.db.sql(query)
```

## frappe.qb

Returns a Pypika query object which lets you build queries. One of its methods is -

### frappe.qb.from\_(table)

lets you construct a from query to select data

**Select query**

```python
query = frappe.qb.from_('customers').select('id', 'fname', 'lname', 'phone')
```

The SQL query built is

```sql
SELECT `id`,`fname`,`lname`,`phone` FROM `tabcustomers`
```

**A complex Select examlple**

```python
customers = frappe.qb.DocType('customers')
q = (
	frappe.qb.from_(customers)
		.select(customers.id, customers.fname,customers.lname, customers.phone)
		.where((customers.fname == 'Max') | (customers.id.like('RA%')) )
		.where(customers.lname == 'Mustermann')
)
```

The SQL query built is

```sql
SELECT `id`,`fname`,`lname`,`phone` FROM `tabcustomers` WHERE (`fname`='Max' OR `id` LIKE 'RA%') AND `lname`='Mustermann'
```

Some noteworthy things

- We have created a `customers` variable to refer to the table in the query.
- Select can take any number of arguments, selecting various Fields.
- The '|' (pipe) or '&' (ampersand) operators can be used to refer to 'OR' or 'AND'.
- Chaining the `where()` method appends 'AND' by default

You can read more about the other functions at the [Pypika](https://github.com/kayak/pypika) repo.

### frappe.qb.Doctype(name\_of\_table)

Returns a pypika table object which can be used elsewhere. It will automatically add 'tab' if necessary.

### frappe.qb.Table(name\_of\_table)

Does the same thing as `frappe.qb.DocType` but will not append 'tab'. It's intended to be used with '\_\_Auth' like tables.

> Note: You should only use this if you know what you are doing.

### frappe.qb.Field(name\_of\_coloum)

Return a pypika field object, this represents a column. They are usually used to compare columns with values.

One example would be

```python
lname = frappe.qb.Field("lname")
q = frapppe.qb.from_("customers").select("*").where(lname == 'Mustermann')
```

## frappe.query_builder.functions

This module provides standard functions you might need while building queries, like `Count()` and `Sum().`

### Simple functions

Say you want to count all the entries in a Notes table. You could do something like

```python
from frappe.query_builder.functions import Count

Notes = frappe.qb.DocType("Notes")
count_pages = Count(Notes.content).as_("Pages")

result = frappe.db.sql(frappe.qb.from_(Notes).select(count_pages))
```

### Custom Functions

`frappe.query_builder.functions` is a superset of `pypika.functions`, so it has all pypika functions and some custom ones we made. You can make your custom functions by importing the `CustomFunction` class from pypika

One implementation of the DateDiff function

```python
from pypika import CustomFunction

customers = Tables('customers')
DateDiff = CustomFunction('DATE_DIFF', ['interval', 'start_date', 'end_date'])

q = Query.from_(customers).select(
	DateDiff('day', customers.created_date, customers.updated_date)
)
```

If we print `q`, we would get

```SQL
SELECT DATE_DIFF('day',"created_date","updated_date") FROM "customer"
```

> Notice how we specify arguments and the actual SQL text. The exact format might not work for more complex functions. The advanced section covers more complicated methods.

## Advanced

### Special functions

One such function is [Match Against](https://mariadb.com/kb/en/match-against/). It's different because it has a chained against argument. To implement something like this you need to inherit from PyPika's `DistinctOptionFunction` class.

The current MATCH class looks something like

```python

from pypika.functions import DistinctOptionFunction
from pypika.utils import builder

class MATCH(DistinctOptionFunction):
	def __init__(self, column: str, *args:
		super(MATCH, self)._init_(" MATCH", column, *args)
		self._Against = False

	def get_function_sql(self, **kwargs):
		s = super(DistinctOptionFunction, self).get_function_sql(**kwargs)

		if self._Against:
			return f"{s} AGAINST (f'+{self._Against}*') IN BOOLEAN MODE)"
		return s

	@builder
	def Against(self, text: str):
		self._Against = text
```

- The `__init__()` method works similar to CustomFunction class above. You mention all the arguments and the SQL text.
- The `Against()` method only stores a value that will be used in the `get_function_sql()`
- It also has the `@builder` wrapper. In short, it lets these functions be chainable by making a copy of the object.
- We have wrapped the `get_function_sql()` method, which allows us to append the required SQL text for Against.
- this can further be extended to use any number other chains.

In use, the Match class looks like this

```python
from frappe.query_builder.functions import Match

match = Match("Coloum name").Against("Some_text_match")
# MATCH('Coloum name') AGAINST ('+Some_text_match*' IN BOOLEAN MODE)
```

### Utils

**ImportMapper(dict)**

In the rare case where you have different functions for different SQL dialects, Which do the same thing, you can use the ImportMapper Utility. It maps functions based on the SQL dialect, so one query works across different SQL dialects.

It takes in a dict which maps functions to databases.

For example the the mapping for GroupConat looks like this

```python

from frappe.query_builder.utils import ImportMapper, db_type_is
from frappe.query_builder.custom import GROUP_CONCAT, STRING_AGG

GroupConcat = ImportMapper(
	{
		db_type_is.MARIADB: GROUP_CONCAT,
		db_type_is.POSTGRES: STRING_AGG
	}
)
```
