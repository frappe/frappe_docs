---
add_breadcrumbs: 1
title: Single DocType
image: /docs/assets/img/single-doctype.png
metatags:
 description: >
  Single DocTypes have only one record / instance. Ideal to hold "Settings" and using DocTypes as Views
---
# Single DocType

A Single DocType is a DocType that has only one instance in the database. It is useful
for persisting things like *System Settings*, which don't make sense to have multiple
records.

![Single DocType](/docs/assets/img/doctypes/single-doctype.png)

```python
>>> settings = frappe.get_doc('System Settings')
>>> settings.notification_frequency
'Daily'
```

### Schema

Single DocTypes are stored in the `tabSingles` table in the database, with each property having its own record.

Columns:

- `doctype`
- `field`
- `value`
