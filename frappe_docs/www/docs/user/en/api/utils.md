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

## pretty_date

## format_duration

## comma_and and comma_or

## money_in_words

## validate_json_string

## getdate, today

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

## validate_email_address and validate_phone

## frappe.cache()

## frappe.sendmail()

