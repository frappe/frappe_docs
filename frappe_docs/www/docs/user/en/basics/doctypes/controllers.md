---
add_breadcrumbs: 1
title: Controllers
metatags:
 description: >
  Controllers help add functionality to DocTypes by adding event handlers in a Python Class
---
# Controllers

A Controller is a normal Python class which extends from `frappe.model.Document` base class. This base class is the core logic of a DocType. It handles how values are loaded from the database, how they are parsed and saved back to the database.

When you create a DocType named `Person`, a python file is created by the name `person.py` and the contents look like:

```python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Person(Document):
	pass

```

All the fields are available to the class as attributes.

### Controller Methods

You can add custom methods to your Controller and it will be callable using the `doc` object. For example,

```python
# controller definition
class Person(Document):
	def get_full_name(self):
        "Returns the person's full name"
        return self.first_name + ' ' + self.last_name

# somewhere in your code
>>> doc = frappe.get_doc('Person', '000001')
>>> doc.get_full_name()
John Doe
```

You can also override the pre-defined document methods to add your own behaviour. For e.g to override the `save()` method,

```python
class Person(Document):
	def save(self, *args, **kwargs):
        do_something()
        super().save(*args, **kwargs) # call the base save method
        do_something_else()
```

There are a lot of methods provided by default on the `doc` object. You can find the complete [list here](/docs/user/en/api/document#document-methods).


### Controller Hooks

To add custom behaviour during the lifecycle of a document, we have controller hooks.

Method Name | Description
-----------------------------|-------------
`before_submit`              | Called before a document is submitted.
`before_cancel`              | This is called before a submitted document is cancelled.
`before_update_after_submit` | This is called *before* a submitted document values are updated.
`before_insert`              | This is called before a document is inserted into the database.
`before_naming`              | This is called before the `name` property of the document is set.
`autoname`                   | This is an optional method which is called only when it is defined in the controller at document creation. Use this method to customize how the `name` property of the document is set.
`validate`                   | Use this method to throw any validation errors and prevent the document from saving.
`before_save`                | This method is called before the document is saved.
`after_insert`               | This is called after the document is inserted into the database.
`on_update`                  | This is called when values of an existing document is updated.
`on_submit`                  | This is called when a document is submitted.
`on_update_after_submit`     | This is called *when* a submitted document values are updated.
`on_cancel`                  | This is called when a submitted is cancelled.
`on_change`                  | This is called to indicate that a document's values has been changed.
`before_rename`              | This is called before a document is renamed.
`after_rename`               | This is called after a document is renamed.
`on_trash`                   | This is called when a document is being deleted.
`after_delete`               | This is called after a document has been deleted.

To use a controller hook, just define a class method with that name. For e.g

```python
class Person(Document):
	def validate(self):
        if self.age > 60:
            frappe.throw('Age must be less than 60')

    def after_insert(self):
        frappe.sendmail(recipients=[self.email], message="Thank you for registering!")
```

#### 1. Create a document

To create a new document and save it to the database,

```python
doc = frappe.get_doc({
    'doctype': 'Person',
    'first_name': 'John',
    'last_name': 'Doe'
})
doc.insert()

doc.name # 000001
```

#### 2. Load a document

To get an existing document from the database,

```python
doc = frappe.get_doc('Person', '000001')

# doctype fields
doc.first_name # John
doc.last_name # Doe

# standard fields
doc.creation # datetime.datetime(2018, 9, 20, 12, 39, 34, 236801)
doc.owner # faris@erpnext.com
```

### Document

A Document is an instance of a DocType. It usually maps to a single row in the
database table. We refer to it as `doc` in code.

**Example**

Let's say we have a DocType **ToDo** with the following fields:

- `description`
- `status`
- `priority`

Now, if we want to query a document from the database, we can use the [ORM](#orm).

```python

>>> doc = frappe.get_doc('ToDo', '0000001')
<frappe.desk.doctype.todo.todo.ToDo at 0x1128d35d0>

>>> doc.as_dict()
{u'creation': datetime.datetime(2018, 8, 14, 12, 57, 4, 568148),
 u'description': u'Buy Groceries',
 u'modified': datetime.datetime(2018, 8, 14, 12, 57, 16, 622779),
 u'modified_by': u'faris@erpnext.com',
 u'name': u'0000001',
 u'owner': u'faris@erpnext.com',
 u'priority': u'Medium',
 u'status': u'Open',
 ...
 }
```

You get the values of `description`, `status` and `priority`, but you also get fields like `creation`, `owner` and `modified_by` which are fields added by default by the framework on all `docs`.


