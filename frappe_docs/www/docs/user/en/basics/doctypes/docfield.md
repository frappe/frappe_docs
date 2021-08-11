---
add_breadcrumbs: 1
title: DocField
metatags:
 description: >
  A DocField defines a property (or a field) of a DocType
---
# DocField

A DocField defines a property (or a field) of a DocType. You can define the column name, label, datatype and more for DocFields. For instance, a ToDo doctype has fields `description`, `status` and `priority`. These ultimately become columns in the database table `tabToDo`.

**Example**

The DocField stores meta-data about the field. Some of them are described below.

```json
[
    {
        "label": "Description",     // the value shown to the user (Form, Print, etc)
        "fieldname": "description", // the property name we refer in code, also the column name
        "fieldtype": "Text Editor", // the fieldtype which also decides how to store this value
        "reqd": 1                   // whether this field is mandatory
    },
    {
        "label": "Status",
        "fieldname": "status",
        "fieldtype": "Select",
        "options": [
            "Open",
            "Pending",
            "Closed"
        ]
    },
    {
        "label": "Priority",
        "fieldname": "priority",
        "fieldtype": "Select",
        "options": [				// list of options for select
            "Low",
            "Medium",
            "High"
        ],
        "default": "Low"            // the default value to be set
    },
    {
        "label": "Completed By",
        "fieldname": "completed_by",
        "fieldtype": "Link",
        "options": "User",
        "depends_on": "eval: doc.status == 'Closed'", // the condition on which this field's display depends
    },
    {
        "collapsible": 1,
        "collapsible_depends_on": "eval:doc.status!='Closed'", // determines if a Section Break field is collapsible
        "fieldname": "sb_details",
        "fieldtype": "Section Break",
        "label": "Details"
    },
    {
        "fieldname": "amount",
        "fieldtype": "Currency", // Currency field
        "label": "Amount",
        "non_negative": 1, // determines whether this field value can be negative
        "options": "INR",
    }
]
```

Similar to the `depends_on` property which determines whether a field will be displayed or not,
in Version 12 we have introduced two new properties:

- `mandatory_depends_on`: If this condition is satisfied, the field will be mandatory.
- `read_only_depends_on`: If this condition is satisfied, the field will be read only.


Frappe comes with more than 30 different fieldtypes out-of-the-box.
These fieldtypes serve a variety of use-cases. You can learn more about fieldtypes in the next page.

{next}
