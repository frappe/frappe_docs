# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe


def get_context(context):
	path = frappe.request.path

	if path.startswith("/"):
		path = path[1:]

	if path.startswith("docs"):
		if context.metatags:
			image = frappe.utils.get_url("/assets/frappe_docs/images/f-logo-square.png")
			for key in ["image", "og:image", "twitter:image"]:
					context.metatags[key] = image
			context.metatags["twitter:card"] = "summary"

		context.update(
			{
				"docs_search_scope": "docs",
				"docs_navbar_items": [
					{"label": "GitHub", "url": "https://github.com/frappe/frappe"},
					{"label": "Discuss", "url": "https://discuss.erpnext.com"},
					{"label": "Twitter", "url": "https://twitter.com/frappetech"},
				],
			}
		)
