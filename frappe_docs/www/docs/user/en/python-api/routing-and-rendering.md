---
add_breadcrumbs: 1
title: Routing & Rendering
image: /assets/frappe_io/images/frappe-framework-logo-with-padding.png
metatags:
 description: >
  Learn routing and rendering works in Frappe Framework
---

# Request Lifecycle

The user of web application can visit different URLs like `/about`, `/posts`. These URL are handled based on following rules

1. API requests which starts with `/api`.
1. File downloads like backups (`/backups`), public files (`/files`) and private files (`/private/files`).
1. Web page requests like `/about`, `/posts` are handled by website router.

Learn more about [API requests](/docs/user/en/api/rest) and [Static Files](/docs/user/en/basics/static-assets) in detail.

## Request pre-processing

A few things happen before the routing rules are triggered. These include preprocessing the request initializing the recorder and the rate limiter.

## Website Router

```
> Path resolver
	> Redirects
	> Routing rules
		> Endpoint
	> Renderer list
> Renderer
	> building context
	> building response
	> Renderer types
```

## Path Resolver

Once the request reaches to website router from `app.py` it is passed through the path resolver.

Path resolver does following operations:

1. Tries to resolve any possible redirect for an incoming request path. Path resolver gets redirect rules for [`website_redirects` hook](/docs/user/en/python-api/hooks#website-redirects) and `Web Route Redirect` list.
1. Resolves to route to get the final endpoint based on rules from [website_routing_rules hook](http://frappe_docs:8000/docs/user/en/python-api/hooks#website-route-rules) and dynamic route set in documents of DocType with `has_web_view` enabled.
1. Once the final endpoint is obtained it is passed through all available [Page Renderers](#standard-page-renderers) to check which page renderer can render the given path. First page renderer to return `True` for `can_render` request will be used to render the path.


## Standard Page Renderers

- **StaticPage:** This is seldom used but using this you can serve PDFs, images etc., from the `www` folder of any app installed on the site. Any file that is **not** one of the following types `html`, `md`, `js`, `xml`, `css`, `txt` or `py` is considered to be a static file.
The preferred way of serving static files would be to add them to the `public` folder of your frappe app. That way it will be served by NGINX directly leveraging compression and caching while also reducing latency.

- **TemplatePage:** The TemplatePage looks up the `www` folder in all apps, if it is a HTML or markdown file, it is returned, in case it is a folder, the `index.html` or `index.md` file in the folder is returned.

- **WebformPage:** The WebformPage tries to render web form in WebForm list if the request path matches with any of the available Web Form's route.

- **DocumentPage:** The DocumentPage tries to render a document template if available in `/templates` folder of the DocType. The template file name should be same as the DocType name. Example: If you want to add a document template for User doctype, the `templates` folder of User DocType should have `user.html`. The folder structure will look like `doctype/user/templates/user.html`

- **ListPage:** If a DocType has a list template in `/templates` folder of the DocType, the ListPage will render it. Please check [Blog Post templates folder](https://github.com/frappe/frappe/tree/develop/frappe/website/doctype/blog_post/templates) for implementation reference.

- **PrintPage:** The PrintPage renders print view for a document. It uses standard print format unless a different print format is set for a DocType via `default_print_format`.

- **NotFoundPage:** The NotFoundPage renders a standard not found page and responds with `404` status code.

- **NotPermitterPage:** The NotPermittedPage renders a standard permission denied page with `403` status code.

**Example PageRenderer class**:

```py
from frappe.website.page_renderers.base_renderer import BaseRenderer

class PageRenderer(BaseRenderer):
    def can_render(self):
        return True

    def render(self):
        response_html = "<div>Response</div>"
        return self.build_response(response_html)

```

## Adding Custom Page Renderer

A custom page renderer can be added via `page_renderer` [hook]

```py
# in hooks.py of your custom app

page_renderer = path.to.your.custom_page_renderer.CustomPage

```

A Page Render class needs to have two methods i.e., `can_render` and `render`

Path resolver calls `can_render` to check if a renderer instance is able to render a particular path.
Once a renderer returns `True` from can_render, it will be that renderer class's responsibility to render the path.

**Note:** Custom Page Renderer gets priority and it's `can_render` method will be called before [Standard Page Renderers](#standard-page-renderers).

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
