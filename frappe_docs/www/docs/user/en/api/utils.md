---
add_breadcrumbs: 1
title: Utils
image: /assets/frappe_io/images/frappe-framework-logo-with-padding.png
metatags:
 description: >
  Utility functions available in Frappe Framework
---

# Utility Functions

There are many different **utility functions** available in Frappe Framework that you can use to carry out many common operations like date formating, PDF generation and much more. 

This utility methods (`utils`) can be imported from the `frappe` module (or nested modules like `frappe.utils` and `frappe.utils.data`) in any Python file of your Frappe app. This list is not at all exhaustive, you can take a peek at the Framework codebase to see what's available.

## now, getdate, today

## add_to_date

## pretty_date

Function Signature: `pretty_date(iso_datetime)`

Takes an ISO time and returns a string representing how long ago the date represents. Very common in communication applications like instant messangers.

Example usage:

```py
from frappe.utils import pretty_date, now, add_to_date

pretty_date(now()) # 'just now'

# Some example outputs:

# 1 hour ago
# 20 minutes ago
# 1 week ago
# 5 years ago
```

## format_duration

Function Signature: `format_duration(seconds, hide_days=False)`

Converts the given duration value in seconds (float) to duration format.

Example Usage:
```py
from frappe.utils import format_duration

format_duration(50) # '50s'
format_duration(10000) # '2h 46m 40s'
format_duration(1000000) # '11d 13h 46m 40s'

# Convert days to hours
format_duration(1000000, hide_days=True) # '277h 46m 40s'
```

## comma_and and comma_or

## money_in_words

## validate_json_string

## random_string

## unique

## get_pdf

Function Signature: `get_pdf(html, options=None, output=None)`

`html`: HTML string to render

`options`: An optional `dict` for configuration

`output`: A optional `PdfFileWriter` object.

This function uses `pdfkit` and `pyPDF2` modules to generate PDF files from HTML. If `output` is provided, appends the generated pages to this object and returns it, otherwise returns a `byte` stream of the PDF.

Example usage, generating and returning a PDF as response:

```py
import frappe
from frappe.utils.pdf import get_pdf

@frappe.whitelist(allow_guest=True)
def generate_invoice():
	cart = [{
		'Samsung Galaxy S20': 10,
		'iPhone 13': 80
	}]

	html = "<h1>Invoice from Star Electronics e-Store!</h1>"

	# Add items to PDF HTML
	html += "<ol>"
	for item, qty in cart.items():
		html += f"<li>{item} - {qty}</li>"
	html += "</ol>"

	# Attaching PDF to response
	frappe.local.response.filename = "invoice.pdf"
	frappe.local.response.filecontent = get_pdf(html)
	frappe.local.response.type = "pdf"
```

## validate_url

Function Signature: `validate_url(txt, throw=False, valid_schemes=None)`

`txt`: A string to check validity

`throw`: Weather to throw an exception if `txt` does not represent a valid URL, `False` by default

`valid_schemes`: A string or an iterable (list, tuple or set). If provided, checks the given URL's scheme against this.

This utility function can be used to check if a string represents a valid URL address.

Example Usage:

```py
from frappe.utils import validate_url

validate_url('google') # False
validate_url('https://google.com') # True
validate_url('https://google.com', throw=True) # throws ValidationError
```

## validate_email_address and validate_phone

## frappe.cache()

## frappe.sendmail()

