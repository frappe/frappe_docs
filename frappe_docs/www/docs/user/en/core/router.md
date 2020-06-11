---
add_breadcrumbs: 1
title: Routing - API
image: /assets/frappe_io/images/frappe-framework-logo-with-padding.png
metatags:
 description: >
  Navigating the Frappe Router
---

# Request Lifecycle

Each request begins at `application` in [`app.py`](https://github.com/frappe/frappe/blob/develop/frappe/app.py). Here based on top level routing rules the request is served.

```python
@Request.application
def application(request):
	response = None

	try:
		# Some Code

		if frappe.local.form_dict.cmd:
			response = frappe.handler.handle()

		elif frappe.request.path.startswith("/api/"):
			response = frappe.api.handle()

		elif frappe.request.path.startswith('/backups'):
			response = frappe.utils.response.download_backup(request.path)

		elif frappe.request.path.startswith('/private/files/'):
			response = frappe.utils.response.download_private_file(request.path)

		elif frappe.local.request.method in ('GET', 'HEAD', 'POST'):
			response = frappe.website.render.render()

		else:
			raise NotFound

	except HTTPException as e:
		return e

	# Some More Code
```

From the above code snippet it's evident what those rules are.

1. `/api` is handled by `frappe.handler`
1. `/backups` and `/private/files` are served based on permissions
1. Any other request of type `GET`, `HEAD` or `POST` is handled by the website router

The next sections cover each of these in detail

A few things happen before these routing rules are triggered. These include preprocessing the request initializing the recorder and the rate limiter.

## Website Router

The request reaches router from `app.py` the render function looks like this

```python
def render(path=None, http_status_code=None):
	"""render html page"""
	if not path:
		path = frappe.local.request.path

	try:
		# Do all the fancy pre processing
		# Resolve the route
		# Render error page if required
		# Inject CSRF token
		# Redirect anywhere if required

	except frappe.Redirect:
		# return a 301 redirect reponse

	return build_response(path, data, http_status_code or 200)
```

Once render is initialized, we first need to cleanup the route, resolve it against any doctype map, check for static file and redirects.
Next step is resoling the route, this piece of the code checks whether the route requested is of a standard type, they can be
one of the following:

1. Static File
1. Web Form
1. Web Page
1. DocType View
	1. List
	1. Item
1. Print View

The precedence is as sequenced in the list above.

### Serving Static File

This is seldom used, but using this you can serve PDFs, images etc from the `www` folder of any app installed on the site. Any file that is **not** one of the following types `html`, `md`, `js`, `xml`, `css`, `txt` or `py` is considered to be a static file.

The preferred way of serving static files would be to add them to the `public` folder of your frappe app. That way it will be served by NGINX directly leveraging compression and caching while also reducing latency

### Web Forms

Web Forms exist in a database, as you might have guessed it, Web Form is a *DocType* that allows you to host forms like contact, surveys, quotations on your website and collect responses.

Each Web Form document has a route it is published from. In the case the path requested matches one of the routes in Web Form, it is served.

The above two are pretty straight forward.

### Serving Web Pages

Web Pages can be from one of the following

1. HTML file in `wwww/`
1. Portal View of a DocType
1. Website Generator Pages

```python
try:
	# Try to resolve path
	data = render_page_by_language(path)
except frappe.DoesNotExistError:
	doctype, name = get_doctype_from_path(path)
	if doctype and name:
		# PRINT VIEW
	elif doctype:
		# LIST VIEW
	else:
		# 404

	render_page(path)

except frappe.PermissionError as e:
	data, http_status_code = render_403(e, path)

except frappe.Redirect as e:
	raise e

except Exception:
	path = "error"
	data = render_page(path)
	http_status_code = 500
```

The way this works is that we first try to resolve the route as is using the `render_page_by_language` method. This can also be called the *Web Page Router* for the sake of reference.

In case the route is not resolved, a `DoesNotExistError` is raised. After this, the **DocType** and the **docame** is guessed using `get_doctype_from_path`. If both are present, the printview of the document is shown, else a generic list view is rendered.

In case neither is found, a 404 is thrown.

> This 404 is also cached and checked for at the beginning of the `render` function.


## Rendering and Context

The `render_page_by_language` calls the `render_page` function which either serves a page from the cache if found, otherwise the page is built (from `build_page`), cached if required and served.

The `render_page` is a generic function that generates the pages by calling the `build_page`

> This function is used in `render_page_by_language` as well as used when rendering printview, and list view mentioned before.


```python
def build_page(path):
	context = get_context(path)

	if context.source:
		html = frappe.render_template(context.source, context)
	elif context.template:
		# Initalize jinja2 loader if path.endswith('min.js')
		html = frappe.get_template(context.template).render(context)

	# Cache if required

	return html
```

This is a two step process:

1. Build `context`, these are the variables that will be available in the context of the template.
1. Render the template. If a template file is specified it is used. In case the context has source set, the source is used as the template (this is similar to `render_template_string` in flask).

The context is built by initializing the context from the router and then setting some standard variables before returning it back to `build_page`

The function `frappe.website.router.get_page_context` builds the context from the `path` provided if it is unable to build it, a `DoesNotExistError` exception is raised.


> In case the route is not resolved, a `DoesNotExistError` is raised. After this, the DocType and the docname is guessed using get_doctype_from_path. If both are present, the printview of the document is shown, else a generic list view is rendered.
>
> from [Serving Web Pages](#serving-web-pages)

### Path Context

The `get_page_context` is a caching function which calls `make_page_context` in case of a cache miss.

```python
def make_page_context(path):
	context = resolve_route(path)
	if not context:
		raise frappe.DoesNotExistError
	# Setting standard variables from context
	return context
```

The `resolve_route` function returns the page route object based on searching in pages and generators.

> The `www` folder is also a part of generator **Web Page**. The only exceptions are `/about` and `/contact` these will be searched in Web Pages first before checking the standard pages.

```python
def resolve_route(path):
	context = get_page_info_from_template(path)
	if context:
		return context
	return get_page_context_from_doctype(path)
```

#### From Template

The `get_page_info_from_template` function looks up the `www` folder in all apps, if it is a html or markdown file, it is returned, in case it is a folder, the `index.html` or `index.md` file in the folder is returned

#### From DocType

The `get_page_context_from_doctype` looks up all the doctypes with web views enabled, If a document matching the path is found, and if it is marked as published explicitly, the page info is built and returned


### Post Process
The other variables that are set later are

1. Website Settings
1. Meta Tags
1. Breadcrumbs
1. Sidebar Data
1. Additional context from hooks
1. Base Template (if not set already)
