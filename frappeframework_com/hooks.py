# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "frappeframework_com"
app_title = "Frappe Framework Website"
app_publisher = "Frappe Technologies"
app_description = "Website and Documentation for Frappe Framework"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "developers@frappe.io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappeframework_com/css/frappeframework_com.css"
# app_include_js = "/assets/frappeframework_com/js/frappeframework_com.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappeframework_com/css/frappeframework_com.css"
# web_include_js = "/assets/frappeframework_com/js/frappeframework_com.js"

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
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "frappeframework_com.utils.get_home_page"

base_template_map = {
	r"docs.*": "templates/doc.html"
}

doc_layout = {
	'navbar_items': [
		{'label': 'GitHub', 'url': 'https://github.com/frappe/frappe' },
		{'label': 'Discuss', 'url': 'https://discuss.erpnext.com' },
		{'label': 'Twitter', 'url': 'https://twitter.com/frappe' },
	]
}

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "frappeframework_com.install.before_install"
# after_install = "frappeframework_com.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappeframework_com.notifications.get_notification_config"

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
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"frappeframework_com.tasks.all"
# 	],
# 	"daily": [
# 		"frappeframework_com.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappeframework_com.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappeframework_com.tasks.weekly"
# 	]
# 	"monthly": [
# 		"frappeframework_com.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "frappeframework_com.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frappeframework_com.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "frappeframework_com.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

