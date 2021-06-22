---
add_breadcrumbs: 1
title: Child / Table DocType
image: /docs/assets/img/child-doctype.png
metatags:
 description: >
  Child / Table DocType are DocTypes that are embedded into other DocTypes. They are not usually accessed on their own, and are ideal for adding vector properties to DocTypes
---
# Child / Table DocType

Up until now we have only seen DocTypes that can have a single value for each field.
However, there might be a need for storing multiple records against one record, also
known as many-to-one relationships. A Child DocType is doctype which can only be linked
to a parent DocType. To make a Child DocType make sure to check **Is Child Table** while
creating the doctype.

![Child DocType](/docs/assets/img/doctypes/child-doctype.png)

To link a Child Doctype to its parent, add another row in Parent Doctype with field
type **Table** and options as **Child Table**.

![Child Table](/docs/assets/img/doctypes/child-table-field.png)

Child DocType records are directly attached to the parent doc.

```python
>>> person = frappe.get_doc('Person', '000001')
>>> person.as_dict()
{
	'first_name': 'John',
	'last_name': 'Doe',
	'qualifications': [
		{'title': 'Frontend Architect', 'year': '2017'},
		{'title': 'DevOps Engineer', 'year': '2016'},
	]
}
```
