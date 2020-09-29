---
add_breadcrumbs: 1
title: Common Utilities - API
image: /assets/frappe_io/images/frappe-framework-logo-with-padding.png
metatags:
 description: >
  API methods for creating and managing controls in Frappe
---


# Common Utilities API

## frappe.model.mapper.get\_mapped\_doc
`get_mapped_doc(from_doctype, from_docname, table_maps, target_doc=None, postprocess=None, ignore_permissions=False, ignore_child_tables=False)`

Maps the source document to the target document.
```py
# map values from the current Dunning document to a new Sales Invoice document
get_mapped_doc("Sales Invoice", source_name,	{
		"Sales Invoice": {
			"doctype": "Dunning",
		}
	}, target_doc, set_missing_values)
```
