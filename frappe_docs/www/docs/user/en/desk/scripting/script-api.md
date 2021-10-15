---
add_breadcrumbs: 1
title: Frappe Framwork Script API
metatags:
 description: >
  List of restricted commands that can be called in Frappe Framework Server Script, Print Formats and Script Reports
---

# Script API

List of restricted commands that be called in Frappe Framework Server Script, Print Formats and Script Reports

**Note:** This is only applicable for in-app scripting. If you want more features, you will have to create an "Application" and write the event handlers inside Python Modules


### 1. Python Modules

Following python modules are available

#### `json`

Python standard module `json`

### 2. Formatting

#### _(Translate)

Translate a string

Example: `_("This is translatable")`

#### frappe.format

Format a value based on its datatype

Example: `frappe.format_value(value, dict(fieldtype='Currency'))`

#### frappe.date_format

Format as default date format

#### frappe.format_date

Returns date as "1st September 2019"

### 3. Session

#### frappe.form_dict

Form / request parameters

Example: Request parameter `/page?name="test"` can be accesssed as `frappe.form_dict.name`

#### frappe.request

Request object

#### frappe.response

Response object

#### frappe.session.user

Current user

#### frappe.session.csrf_token

CSRF token of the current session

#### frappe.user

Current user

#### frappe.get_fullname

Returns fullname of the current user

#### frappe.get_gravatar

Gets the user display image from `frappe.utils.get_gravatar_url`

#### frappe.full_name

Fullname of the current user

### 4. Documents (ORM)

Document access and editing

#### frappe.get_meta

Get metadata object

#### frappe.get_doc

Get Document. You can also save or execute any method exposed by the document.

Example: `frappe.get_doc("User", frappe.session.user)`

#### frappe.get_cached_doc

Get Document (or cached)

#### frappe.get_system_settings

Get system default settings

### 5. Database

Database access API

#### frappe.db.get_list

Get list of record filtered by current user's permissions

Example: `frappe.db.get_list("Customer")` will return list of customers

#### frappe.db.get_all

Get list of all records

#### frappe.db.sql

Run a SELECT query

Example: `frappe.db.sql("select name from Customer where name like 'm%'")`

#### frappe.db.get_value

Get a value from a record

Example: `frappe.db.get_value("User", frappe.session.user, "first_name")`

#### frappe.db.get_single_value

Get value from a single type document

Example: `frappe.db.get_single_value("System Settings", "default_currency")`

#### frappe.db.get_default

Get default value

#### frappe.db.escape

Sanitize value for database queries to prevent SQL injection

#### frappe.db.set_value

Set a value

### 6. Utilities

Utility methods and functions

#### run_script

Run a server script (return values in `frappe.flags`)

#### frappe.msgprint

Show a modal on the server side after as a part of the response.

Example: `frappe.msgprint("Hello")`

#### frappe.get_hooks

Get application hooks

#### frappe.utils

Methods in frappe.utils

#### frappe.render_template

Render a Jinja template

#### frappe.get_url

Get url of the current site via `frappe.utils.get_url`

#### socketio_port

Port for socketio

#### style.border_color

Returns '#d1d8dd'

#### guess_mimetype

Returns mimetypes.guess_type

#### html2text

Encode HTML as text (markdown)

#### dev_server

True if in developer mode

#### frappe.log_error

Generate Error Log with a traceback

#### FrappeClient

Connect to a Frappe site using a requests session

#### frappe.enqueue

Enqueue a script / whitelisted method into a background queue

Examples:

```py
frappe.enqueue("path.to.whitelisted.method", queue="long", param_one: True)
frappe.enqueue("my_server_script_api", queue="long", param_one: True)
```