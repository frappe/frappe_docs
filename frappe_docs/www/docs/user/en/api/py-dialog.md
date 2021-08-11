---
add_breadcrumbs: 1
title: Dialog - API
metatags:
 description: >
  API methods for creating and managing Dialogs in Frappe using Python
---

# Dialog API
Frappe provides a group of standard, interactive and flexible dialogs that are
easy to configure and use. There's also a more extensive API for [Javascript](/docs/user/en/api/dialog).

### frappe.msgprint
`frappe.msgprint(msg, title, raise_exception, as_table, as_list, indicator, primary_action)`

This method works only within a request / response cycle. It shows a message to
the user logged in to Desk who initiated the request.

The argument list includes:

- `msg`: The message to be displayed
- `title`: Title of the modal
- `as_table`: If `msg` is a list of lists, render as HTML table
- `as_list`: If `msg` is a list, render as HTML unordered list
- `primary_action`: Bind a primary server/client side action.
- `raise_exception`: Exception

```py
frappe.msgprint(
	msg='This file does not exist',
	title='Error',
	raise_exception=FileNotFoundError
)
```
![frappe.msgprint](/docs/assets/img/api/dialog-api-msgprint-py.png)
*frappe.msgprint*

`primary_action` can contain a `server_action` **or** `client_side` action which
must contain dotted paths to the respective methods. The JavaScript function
must be a globally available function.

```py
# msgprint with server and client side action
frappe.msgprint(msg='This file does not exist',
	title='Error',
	raise_exception=FileNotFoundError
	primary_action={
		'label': _('Perform Action'),
		'server_action': 'dotted.path.to.server.method',
		'client_action': 'dotted.path.to.client.method',
		'args': args
	}
)
```

![frappe.msgprint with primary action](/docs/assets/img/api/dialog-api-msgprint-py-with-primary-action.png)
*frappe.msgprint with primary action*

### frappe.throw
`frappe.throw(msg, exc, title)`

This method will raise an exception as well as show a message in Desk. It is
essentially a wrapper around `frappe.msgprint`.

`exc` can be passed an optional exception. By default it will raise a `ValidationError` exception.

```py
frappe.throw(
	title='Error',
	msg='This file does not exist',
	exc=FileNotFoundError
)
```
![Throw-py](/docs/assets/img/api/dialog-api-msgprint-py.png)
*frappe.throw*
