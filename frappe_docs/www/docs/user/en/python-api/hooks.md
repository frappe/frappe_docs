---
title: Hooks
image: /assets/frappe_io/images/frappe-framework-logo-with-padding.png
metatags:
 description: >
  Hooks allow you to "hook" into functionality and events of core parts of the Frappe Framework.
---

# Hooks

Hooks allow you to "hook" into functionality and events of core parts of the
Frappe Framework. This page documents all of the hooks provided by the framework.

## App Meta Data

These are automatically generated when you create a new app. Most of the time you
don't need to change anything here.

1. `app_name` - slugified name of the app
2. `app_title` - presentable app name
3. `app_publisher`
4. `app_description`
5. `app_version`
6. `app_icon`
7. `app_color`

## Javascript / CSS Assets

The following hooks allow you to inject static JS and CSS assets in various
 parts of your site.

### Desk

These hooks allow you to inject JS / CSS in `desk.html` which renders the
[Desk](/docs/user/en/desk).

```py
# injected in desk.html
app_include_js = "assets/js/app.min.js"
app_include_css = "assets/js/app.min.css"

# All of the above support a list of paths too
app_include_js = ["assets/js/app1.min.js", "assets/js/app2.min.js"]
```

### Portal

These hooks allow you to inject JS / CSS in `web.html` which renders the
[Portal](/docs/user/en/portal-pages).

```py
# injected in the web.html
web_include_js = "assets/js/app-web.min.js"
web_include_css = "assets/js/app-web.min.css"
# All of the above support a list of paths too
web_include_js = ["assets/js/web1.min.js", "assets/js/web2.min.js"]
```

### Web Form

These hooks allow you to add inject static JS and CSS assets in `web_form.html`
which is used to render Web Forms. These will work only for Standard Web Forms.

```py
webform_include_js = {"ToDo": "public/js/custom_todo.js"}
webform_include_css = {"ToDo": "public/css/custom_todo.css"}
```

> For user created Web Forms, you can directly write the script in the form
> itself.

### Page

These hooks allow you to inject JS assets in Standard Desk Pages.

```py
page_js = {"page_name" : "public/js/file.js"}
```

For e.g., Background Jobs is a standard page that is part of Core module in
Frappe Framework. To add custom behaviour in that page you can add a JS file in
your custom app `custom_app/public/js/custom_background_jobs.js` and add the
following line in your hooks file.

**custom_app/hooks.py**
```py
page_js = {"background_jobs": "public/js/custom_background_jobs.js"}
```

## Install Events

These hooks allow you to run code before and after installation of your app. For
example, [ERPNext](https://github.com/frappe/erpnext) has these
[defined](https://github.com/frappe/erpnext/blob/develop/erpnext/hooks.py#L37-L38).

```py
# python module path
before_install = "app.setup.install.before_install"
after_install = "app.setup.install.after_install"
```

**app/setup/install.py**
```py
def after_install():
	# run code after app installation
	pass
```

## Boot Session

After a successful login, the Desk is injected with a dictionary of global
values called `bootinfo`. The `bootinfo` is available as a global object in
Javascript as `frappe.boot`.

The `bootinfo` dict contains a lot of values including:

- System defaults
- Notification status
- Permissions
- User settings
- Language and timezone info

You can add global values that makes sense for your app via the `boot_session`
hook.

```py
# python module path
boot_session = "app.boot.boot_session"
```

The method is called with one argument `bootinfo`, on which you can directly
add/update values.

**app/boot.py**

```py
def boot_session(bootinfo):
	bootinfo.my_global_key = 'my_global_value'
```

Now, you can access the value anywhere in your client side code.
```js
console.log(frappe.boot.my_global_key)
```

## Website Context

When a Portal Page is rendered, a dictionary is built with all of the possible
variables that the page might need to render. This dict is also known as
`context`. To add or modify values in this dict, you can use the
`update_website_context` hook.

**app/hooks.py**
```py
update_website_context = 'app.overrides.website_context`
```

The method is called with one argument, which is the `context` dict. You can
either modify the context directly by mutating it or return a dict that will be
merged with `context`.

**app/overrides.py**
```py
def website_context(context):
	context.my_key = 'my_value'
```

## Session Creation

When a User logs in to the site successfully, a session creation hook is
triggered. You can respond to this event by using the `on_session_creation` hook.

**app/hooks.py**

```py
on_session_creation = 'app.overrides.allocate_free_credits'
```

The method is called with one argument `login_manager`.

**app/overrides.py**
```py
def allocate_free_credits(login_manager):
	# allocate free credits to frappe.session.user
	pass
```

## Website Clear Cache

Frappe Framework caches a lot of static web pages for fast subsequent rendering.
If you have created web pages that use cached values, and you want to invalidate
the cache, this hook is place to do it.

**app/hooks.py**

```py
website_clear_cache = 'app.overrides.clear_website_cache'
```

The method is called with one argument `path`. `path` is set when cache is being
cleared for one route, and is `None` when cache is cleared for all routes. You
need to handle this case if your cache is page specific.

**app/overrides.py**
```py
def clear_website_cache(path=None):
	if path:
		# clear page related cache
	else:
		# clear all cache
```

## Document Hooks

### Modify List Query

You can customize how list of records are queried for a DocType by adding custom
match conditions using the `permission_query_conditions` hook. This match
condition must be a valid WHERE clause fragment for an SQL query.

**app/hooks.py**
```py
permission_query_conditions = {
	"ToDo": "app.permissions.todo_query",
}
```
The method is called with a single argument `user` which can be `None`. The
method should return a string that is a valid SQL WHERE clause.

**app/permissions.py**
```py
def todo_query(user):
	if not user:
		user = frappe.session.user
	# todos that belong to user or assigned by user
	return "(`tabToDo`.owner = {user} or `tabToDo`.assigned_by = {user})".format(user=frappe.db.escape(user))
```

Now, if you use the `frappe.db.get_list` method, your WHERE clause will be
appended to the query.
```py
todos = frappe.db.get_list('ToDo', debug=1)

# output
'''
select `tabToDo`.`name`
from `tabToDo`
where ((`tabToDo`.owner = 'john@doe.com' or `tabToDo`.assigned_by = 'john@doe.com'))
order by `tabToDo`.`modified` DESC
'''
```

> This hook will only affect the result of `frappe.db.get_list` method and not
> `frappe.db.get_all`.

### Document Permissions

You can modify the behaviour of `doc.has_permission` document method for any
DocType and add custom permission checking logic using the `has_permission`
hook.

**app/hooks.py**
```py
has_permission = {
	"Event": "app.permissions.event_has_permission",
}
```

The method will be passed the `doc`, `user` and `permission_type` as arguments.
It should return `True` or a `False` value. If `None` is returned, it will
fallback to default behaviour.

**app/permissions.py**
```py
def event_has_permission(doc, user=None, permission_type=None):
	# when reading a document allow if event is Public
	if permission_type == "read" and doc.event_type == "Public":
		return True

	# when writing a document allow if event owned by user
	if permission_type == "write" and doc.owner == user:
		return True

	return False
```

### Override DocType Class

You can override/extend the class for standard doctypes by using the
`override_doctype_class` hook.

**app/hooks.py**
```py
override_doctype_class = {
	'ToDo': 'app.overrides.todo.CustomToDo'
}
```

**app/overrides/todo.py**
```py
from frappe.desk.doctype.todo.todo import ToDo

class CustomToDo(ToDo):
	def on_update(self):
		self.my_custom_code()
		super(ToDo, self).on_update()

	def my_custom_code(self):
		pass
```

> It is recommended that you extend the standard class of the doctype, otherwise
> you will have to implement all of the core functionality.

### CRUD Events

You can hook into various CRUD events of any doctype using the `doc_events`
hook.

**app/hooks.py**
```py
doc_events = {
	"*": {
		# will run after any DocType record is inserted into database
		"after_insert": "app.crud_events.after_insert_all"
	},
	"ToDo": {
		# will run before a ToDo record is inserted into database
		"before_insert": "app.crud_events.before_insert_todo",
	}
}
```

The method will be passed the doc and the method name as arguments.

**app/crud_events.py**
```py
def after_insert_all(doc, method=None):
	pass

def before_insert_todo(doc, method=None):
	pass
```

> See [Controller Hooks](/docs/user/en/basics/doctypes/controllers#controller-hooks)
> for a list of all available hooks.

### Override Whitelisted Methods

Whitelisted Methods are python methods that are accessible on a REST endpoint
and consumed by a client. You can override standard whitelisted methods that are
part of the core framework using the `override_whitelisted_methods` hook.

**app/hooks.py**
```py
override_whitelisted_methods = {
	"frappe.client.get_count": "app.whitelisted.custom_get_count"
}
```

The method should have the same signature as the original method.

**app/whitelisted.py**
```py
def custom_get_count(doctype, filters=None, debug=False, cache=False):
    # your custom implementation of the standard get_count method provided by frappe
    pass
```

### Form Timeline

The timeline section of [form view](/docs/user/en/desk#form-view) of a document
shows an audit trail of actions performed on that document like views, value
changes, comments and related communications, etc.

Apart from these standard actions, there might arise a situation where you need
to add your own custom actions. You can do this via
`additional_timeline_content` hook.

```py
additional_timeline_content: {
	# show in each document's timeline
	'*': ['app.timeline.all_timeline']
	# only show in ToDo's timeline
	'ToDo': ['app.timeline.todo_timeline']
}
```

The method will be passed the doctype and docname as arguments. You can perform
queries and return actions related to that document as a list of dicts as shown
in the example. Each dict in the list must have a `creation` value which will be
used to sort the item in the timeline.

```py
def todo_timeline(doctype, docname):
	# this method should return a list of dicts
	return [
		{
			 # this will be used to sort the content in the timeline
			'creation': '22-05-2020 18:00:00'
			# this JS template will be rendered in the timeline
			'template': 'custom_timeline_template'
			# this data will be passed to the template.
			'template_data': {'key': 'value'}
		},
		...
	]
```

## Scheduler Hooks

You can use Scheduler Hooks for running tasks periodically in the background.

**app/hooks.py**
```py
scheduler_events = {
	"hourly": [
		# will run hourly
		"app.scheduled_tasks.update_database_usage"
	],
}
```

**app/scheduled_tasks.py**
```py
def update_database_usage():
	pass
```

### Available Events

- `hourly`, `daily`, `weekly`, `monthly`

  These events will trigger every hour, day, week and month respectively.

- `hourly_long`, `daily_long`, `weekly_long`, `monthly_long`

  Same as above but these jobs are run in the [long
  worker](/docs/user/en/basics/directory-structure#worker_long) suitable for
  long running jobs.

- `all`

  The `all` event is triggered every 60 seconds. This can be configured
  via the `scheduler_tick_interval` key in
  [`common_site_config.json`](/docs/user/en/basics/sites#scheduler_tick_interval)

- `cron`

  A valid cron string that can be parsed by [croniter](https://pypi.org/project/croniter/).

Usage Examples:

```py
scheduler_events = {
	"daily": [
		"app.scheduled_tasks.manage_recurring_invoices"
	],
	"daily_long": [
		"app.scheduled_tasks..take_backups_daily"
	],
	"cron": {
		"15 18 * * *": [
			"app.scheduled_tasks..delete_all_barcodes_for_users"
		],
		"*/6 * * * *": [
			"app.scheduled_tasks..collect_error_snapshots"
		],
		"annual": [
			"app.scheduled_tasks.collect_error_snapshots"
		]
	}
}
```

## Jinja Customization

Frappe provides a list of [global utility methods](/docs/user/en/api/jinja) in
Jinja templates. To add your own methods and filters you can use the `jenv` hook.

**app/hooks.py**
```py
jenv = {
	"methods": [
		"get_fullname:app.jinja.get_fullname"
	],
	"filters": [
		"format_currency:app.jinja.currency_filter"
	]
}
```

**app/jinja.py**

```py
def get_fullname(user):
	first_name, last_name = frappe.db.get_value('User', user, ['first_name', 'last_name'])
	return first_name + ' ' + last_name

def format_currency(value, currency):
	return currency + ' ' + str(value)
```

Now, you can use these utilities in your Jinja templates like so:

{% raw %}
```html
<h1>Hi, {{ get_fullname(frappe.session.user) }}</h1>
<p>Your account balance is {{ account_balance | format_currency('INR') }}</p>
```
{% endraw %}

## Prevent Auto Cancellation of Linked Documents

To prevent documents of a specific DocType from being automatically cancelled on
the cancellation of any linked documents you can use the
`auto_cancel_exempted_doctypes` hook.

**app/hooks.py**
```py
auto_cancel_exempted_doctypes = ["Payment Entry"]
```

In the above example, if any document (for e.g Sales Invoice) that is linked
with Payment Entry is cancelled, it will skip the auto-cancellation of the
linked Payment Entry document.


## Notification configurations

The notification configuration hook is used to customize the items shown in the
Notification dropdown in Desk. It can be configured by the `notification_config`
hook.

**app/hooks.py**
```py
notification_config = 'app.notification.get_config'
```

The method is called without any arguments.

**app/notification.py**
```py
def get_config():
	return {
		"for_doctype": {
			"Issue": {"status":"Open"},
			"Issue": {"status":"Open"},
		},
		"for_module_doctypes": {
			"ToDo": "To Do",
			"Event": "Calendar",
			"Comment": "Messages"
		},
		"for_module": {
			"To Do": "frappe.core.notifications.get_things_todo",
			"Calendar": "frappe.core.notifications.get_todays_events",
			"Messages": "frappe.core.notifications.get_unread_messages"
		}
	}
```

The above configuration has three parts:

1. `for_doctype` part of the above configuration marks any "Issue"
	or "Customer Issue" as unread if its status is Open
2. `for_module_doctypes` maps doctypes to module's unread count.
3. `for_module` maps modules to functions to obtain its unread count. The
   functions are called without any argument.
