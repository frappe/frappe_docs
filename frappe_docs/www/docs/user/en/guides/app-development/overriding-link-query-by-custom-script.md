<!-- add-breadcrumbs -->
# Overriding Link Query By Custom Script

You can override the standard link query by using `set_query` via the Client Script DocType from the desk.

### 1. Adding Filters

You can add filters to the query:

```js
frappe.ui.form.on("Bank Reconciliation", "onload", function(frm) {
	frm.set_query("bank_account", function() {
		return {
			"filters": {
				"account_type": "Bank",
				"group_or_ledger": "Ledger"
			}
		};
	});
});
```

A more complex query:

```js
frappe.ui.form.on("Bank Reconciliation", "onload", function(frm){
	frm.set_query("bank_account", function(){
		return {
			"filters": [
				["Bank Account", "account_type", "=", "Bank"],
				["Bank Account", "group_or_ledger", "!=", "Group"]
			]
		}
	});
});
```
---

### 2. Calling a Different Method to Generate Results

You can also set a server side method to be called on the query:

```js
frm.set_query("item_code", "items", function() {
	return {
		query: "erpnext.controllers.queries.item_query",
		filters: frm.doc.enquiry_type === "Maintenance" ?
			{"is_service_item": "Yes"} : {"is_sales_item": "Yes"}
	};
});
```


#### Custom Method

The custom method should return a list of items for auto select. If you want to send additional data, you can send multiple columns in the list.

Parameters to the custom method are:

```py
def custom_query(doctype, txt, searchfield, start, page_len, filters)
```

**Example:**

```py
# searches for leads which are not converted
@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def lead_query(doctype, txt, searchfield, start, page_len, filters):
	return frappe.db.sql("""
		SELECT name, lead_name, company_name
		FROM `tabLead`
		WHERE docstatus &lt; 2
			AND ifnull(status, '') != 'Converted'
			AND ({key} LIKE %(txt)s
				OR lead_name LIKE %(txt)s
				OR company_name LIKE %(txt)s)
			{mcond}
		ORDER BY
			IF(LOCATE(%(_txt)s, name), LOCATE(%(_txt)s, name), 99999),
			IF(LOCATE(%(_txt)s, lead_name), LOCATE(%(_txt)s, lead_name), 99999),
			IF(LOCATE(%(_txt)s, company_name), LOCATE(%(_txt)s, company_name), 99999),
			name, lead_name
		LIMIT %(start)s, %(page_len)s
	""".format(**{
			'key': searchfield,
			'mcond':get_match_cond(doctype)
		}), {
		'txt': "%{}%".format(txt),
		'_txt': txt.replace("%", ""),
		'start': start,
		'page_len': page_len
	})
```

**Note:** `@frappe.whitelist()` is used to expose `lead_query` to the client-side
and `@frappe.validate_and_sanitize_search_inputs` decorator is used to validate and sanitize user inputs sent through API or client-side request to avoid possible SQLi.

For more examples see:

[https://github.com/frappe/erpnext/blob/develop/erpnext/controllers/queries.py](https://github.com/frappe/erpnext/blob/develop/erpnext/controllers/queries.py)

<!-- markdown -->
