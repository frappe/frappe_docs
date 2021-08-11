---
add_breadcrumbs: 1
title: Routing & Rendering
metatags:
 description: >
  Learn routing and rendering works in Frappe Framework
---

# Request Lifecycle

The user of a web application can visit different URLs like `/about`, `/posts` or `/api/resources`. Each request is handled based on the following request types.

1. API requests that start with `/api` are handled by [rest API handler](https://github.com/frappe/frappe/blob/develop/frappe/api.py#L16).
1. File downloads like backups (`/backups`), public files (`/files`), and private files (`/private/files`) are handled separately to respond with a downloadable file.
1. Web page requests like `/about`, `/posts` are handled by the website router. This is explained further on this page.

Learn more about [API requests](/docs/user/en/api/rest) and [Static Files](/docs/user/en/basics/static-assets) in detail.

## Request pre-processing

A few things happen before the routing rules are triggered. These include preprocessing the request initializing the recorder and the rate limiter.

## Path Resolver

Once the request reaches to website router from `app.py` it is passed through the path resolver.

Path resolver does the following operations:

### Redirect Resolution

Path resolver tries to resolve any possible redirect for an incoming request path. Path resolver gets redirect rules for [`website_redirects` hook](/docs/user/en/python-api/hooks#website-redirects) and route redirects from website settings.

### Route Resolution

If there are no redirects for incoming requests path resolver tries to resolve the route to get the final endpoint based on rules from [website_routing_rules hook](http://frappe_docs:8000/docs/user/en/python-api/hooks#website-route-rules) and dynamic route set in documents of DocType with `has_web_view` enabled.

### Renderer Selection

Once the final endpoint is obtained it is passed through all available [Page Renderers](#page-renderer) to check which page renderer can render the given path. A first page renderer to return `True` for `can_render` request will be used to render the path.

## Page Renderer

A page renderer takes care of rendering or responding with a page for a given endpoint. A page renderer is implemented using a python class. A page renderer class needs to have two methods i.e., `can_render` and `render`.

Path resolver calls `can_render` to check if a renderer instance can render a particular path.
Once a renderer returns `True` from `can_render`, it will be that renderer class's responsibility to render the path.

### Example page renderer class

```py
from frappe.website.page_renderers.base_renderer import BaseRenderer

class PageRenderer(BaseRenderer):
    def can_render(self):
        return True

    def render(self):
        response_html = "<div>Response</div>"
        return self.build_response(response_html)

```

Following are the standard page renderers which handle all the generic types of web pages.

### StaticPage

Using StaticPage you can serve PDFs, images, etc., from the `www` folder of any app installed on the site. Any file that is **not** one of the following types `html`, `md`, `js`, `xml`, `css`, `txt` or `py` is considered to be a static file.
The preferred way of serving static files would be to add them to the `public` folder of your frappe app. That way it will be served by NGINX directly leveraging compression and caching while also reducing latency.

### TemplatePage

The TemplatePage looks up the `www` folder in all apps, if it is an HTML or markdown file, it is returned, in case it is a folder, the `index.html` or `index.md` file in the folder is returned.

### WebformPage

The WebformPage tries to render web form in the Web Form list if the request path matches with any of the available Web Form's routes.

### DocumentPage

The DocumentPage tries to render a document template if it is available in `/templates` folder of the DocType. The template file name should be the same as the DocType name. Example: If you want to add a document template for User doctype, the `templates` folder of User DocType should have `user.html`. The folder structure will look like `doctype/user/templates/user.html`

### ListPage

If a DocType has a list template in `/templates` folder of the DocType, the ListPage will render it. Please check [Blog Post templates folder](https://github.com/frappe/frappe/tree/develop/frappe/website/doctype/blog_post/templates) for implementation reference.

### PrintPage

The PrintPage renders a print view for a document. It uses [standard print format](https://github.com/frappe/frappe/blob/develop/frappe/templates/print_formats/standard.html) unless a different print format is set for a DocType via `default_print_format`.

### NotFoundPage

The NotFoundPage renders a standard not found page and responds with `404` status code.

### NotPermitterPage

The NotPermittedPage renders standard permission denied page with `403` status code.

## Adding a custom page renderer

If you have any other requirements which are not handled by Standard Page renderers a custom page renderer can be added via `page_renderer` [hook]

```py
# in hooks.py of your custom app

page_renderer = "path.to.your.custom_page_renderer.CustomPage"

```

A Page renderer class needs to have two methods i.e., `can_render` and `render`

Path resolver calls `can_render` to check if a renderer instance can render a particular path.
Once a renderer returns `True` from can_render, it will be that renderer class's responsibility to render the path.

**Note:** Custom page renderers get priority and it's `can_render` method will be called before [Standard Page Renderers](#page-renderer).

**Example:**
```py

from frappe.website.utils import build_response
from frappe.website.page_renderers.base_renderer import BaseRenderer

class CustomPage(BaseRenderer):
    def can_render(self):
        return True

    def render(self):
        response_html = "<div>Custom Response</div>"
        return self.build_response(response_html)

```
**Note:** You can also extend Standard Page Renderers to override or to use some standard functionalities.
