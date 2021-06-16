---
add_breadcrumbs: 1
title: Routing & Rendering
image: /assets/frappe_io/images/frappe-framework-logo-with-padding.png
metatags:
 description: >
  Navigating the Frappe Router and Renderer
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
			response = frappe.website.serve.get_response()

		else:
			raise NotFound

	except HTTPException as e:
		return e

	# Some More Code
```

From the above code snippet it's evident what those rules are.

1. `/api` is handled by `frappe.handler`
1. `/backups` and `/private/files` are served based on permissions
1. Any other request of type `GET`, `HEAD` or `POST` is handled by the website router.

The next sections cover each of these in detail

A few things happen before these routing rules are triggered. These include preprocessing the request initializing the recorder and the rate limiter.

## Path Resolver

Once the request reaches to website router from `app.py` it is passed through a Path Resolver.

Path Resolver gets the incoming request path and passes it through all available [Page Renderers](#standard-page-renderers) to check which page renderer can render the given path. First page renderer to return `True` for `can_render` request will be used to render the path in the next step.

### Standard Page Renderers

- **StaticPage:** This is seldom used, but using this you can serve PDFs, images etc., from the `www` folder of any app installed on the site. Any file that is **not** one of the following types `html`, `md`, `js`, `xml`, `css`, `txt` or `py` is considered to be a static file.
The preferred way of serving static files would be to add them to the `public` folder of your frappe app. That way it will be served by NGINX directly leveraging compression and caching while also reducing latency

- **TemplatePage:**
- WebformPage
- DocumentPage
- ListPage
- PrintPage

### Adding Custom Page Renderer

A custom page renderer can be added via `page_renderer` [hook]

```py
# in hooks.py of your custom app

page_renderer = path.to.your.custom_page_renderer.CustomPage

```

A Page Render class needs to have two methods i.e., `can_render` and `render`

Path resolver calls `can_render` to check if a renderer instance is able to render a particular path.
Once a renderer returns `True` from can_render, it will be that renderer classes responsibility to render the path.

**Note:** Custom Page Renderer gets priority and it's `can_render` method will be called before [Standard Page Renderers](#standard-page-renderers).

**Example:**
```py

from frappe.website.utils import build_response

def CustomPage():
    def __init__(self, path):
        self.path = path
        self.http_status_code = 200

    def can_render(self):
        return True

    def render(self):
        response_html = "<div>Custom Response</div>"
        return build_response(self.path, response_html, self.http_status_code)

```
**Note:** You can also extend Standard Page Renderers to override or to use some standard functionalities.

