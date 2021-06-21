# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "frappe_docs"
app_title = "Frappe Docs"
app_publisher = "Frappe Technologies"
app_description = "Frappe Framework Documentation"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "developers@frappe.io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappe_docs/css/frappe_docs.css"
# app_include_js = "/assets/frappe_docs/js/frappe_docs.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappe_docs/css/frappe_docs.css"
# web_include_js = "/assets/frappe_docs/js/frappe_docs.js"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "frappe_docs.utils.get_home_page"

look_for_sidebar_json = True

base_template_map = {
	r"docs.*": "templates/doc.html"
}

update_website_context = ["frappe_docs.website_context.get_context"]

website_redirects = [
	{'source': '/docs/user/en', 'target': '/docs/user/en/basics' },
	{'source': '/docs/user/en/report', 'target': '/docs/user/en/desk/report' },
	{'source': '/docs/user/en/printing', 'target': '/docs/user/en/desk/printing'},
	{'source': '/docs/user/en/attachments', 'target': '/docs/user/en/desk/attachments' },
	{'source': '/docs/user/en/apps', 'target': '/docs/user/en/desk/basics/apps' },
	{'source': '/docs/user/en/architecture', 'target': '/docs/user/en/basics/architecture' },
	{'source': '/docs/user/en/directory-structure', 'target': '/docs/user/en/basics/directory-structure' },
	{'source': '/docs/user/en/understanding-doctypes', 'target': '/docs/user/en/basics/doctypes' },
	{'source': '/docs/user/en/sites', 'target': '/docs/user/en/basics/sites' },
	{'source': '/docs/user/en/users-and-permissions', 'target': '/docs/user/en/basics/users-and-permissions' },
	{'source': '/docs/user/en/what-is-frappe', 'target': '/docs/user/en/basics' },
	{'source': '/docs/user/en/why', 'target': '/docs/user/en/basics/why' },
	{'source': '/docs/user/en/guides/bench', 'target': '/docs/user/en/bench' },
	{'source': '/docs/user/en/guides/basics/hooks', 'target': '/docs/user/en/python-api/hooks' },
	{'source': '/docs/user/en/guides/basics/site_config', 'target': '/docs/user/en/basics/site_config' },
	{'source': '/docs/user/en/tutorial/prerequisites', 'target': '/docs/user/en/prerequisites' },
]

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "frappe_docs.install.before_install"
# after_install = "frappe_docs.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappe_docs.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"frappe_docs.tasks.all"
# 	],
# 	"daily": [
# 		"frappe_docs.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappe_docs.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappe_docs.tasks.weekly"
# 	]
# 	"monthly": [
# 		"frappe_docs.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "frappe_docs.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frappe_docs.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "frappe_docs.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]
