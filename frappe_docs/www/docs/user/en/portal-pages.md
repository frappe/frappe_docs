---
add_breadcrumbs: 1
title: Portal Pages
metatags:
 description: >
  Frappe Framework allows you to host server rendered web pages which are great
  for SEO. You can also create public portals for external users.
safe_render: false
---

# Portal Pages

Frappe Framework not only provides a rich admin interface via the
[Desk](/docs/user/en/desk) which is an SPA but also static server rendered web
pages. These pages are generally built for your website visitors. They can be
public or can require login.

## Adding pages

Every frappe app including frappe comes with a `www` folder which directly maps
to website urls. Here is what the directory structure looks like:

```bash
frappe/www
├── about.html
├── about.py
├── contact.html
├── contact.py
├── desk.html
├── desk.py
├── login.html
├── login.py
├── me.html
└── me.py
```

This structure enables the routes `/about`, `/contact`, `/desk`, `/login` and
`/me`.

To add your own page, just add an HTML file in the `www` folder of your app.
There are multiple ways to organize these portal pages. For example,

```bash
custom_app/www
├── custom_page.html
└── custom_page.py
```
Will be rendered on the route `/custom_page`.

To add subpages you can convert your main page into a folder and add its content
in an index file. For example,

```bash
custom_app/www
└── custom_page
	├── index.html
	├── index.py
	├── subpage.html
	└── subpage.py

```
Will still be rendered on the route `/custom_page` and `/custom_page/subpage`
will also be available.

> You can write `.md` files instead of `.html` for simple static pages like
> documentation. This documentation you are reading is written as a markdown file.

### Overriding standard pages

Frappe also allows you to override standard pages through your custom app. For
example, to override the standard `/about` provided by frappe, just add a file
named `about.html` in the `www` folder of your app and it will take precedence.

### Templating

You can add dynamic content to Portal Pages using Jinja templates. All of the
portal pages extend from the base template `frappe/templates/web.html` which
itself extends from `frappe/templates/base.html`.

Here is what a sample page might look like:

{% raw %}
```html
<!-- about.html -->
{%  extends "templates/web.html" %}

{% block title %}{{ _("About Us") }}{% endblock %}

{% block page_content %}
<h1>{{ _("About Us") }}</h1>
<div class="row">
    <div class="col-sm-6">
		We believe that great companies are driven by excellence,
		and add value to both its customers and society.
		You will find our team embibes these values.
    </div>
</div>
{% endblock %}
```
{% endraw %}

You can also omit the `extend` and `block` if you want to the use the default
base template.

{% raw %}
```html
<!-- about.html -->
<h1>{{ _("About Us") }}</h1>
<div class="row">
    <div class="col-sm-6">
		We believe that great companies are driven by excellence,
		and add value to both its customers and society.
		You will find our team embibes these values.
    </div>
</div>
```
{% endraw %}

### Context

Every portal page can have a python controller which will build `context` for
the page. The controller should have the same name as the `.html` or `.md` file
with a `.py` extension.

```bash
custom_app/www
├── custom_page.html
└── custom_page.py
```

The controller should have a `get_context` method which takes a `context` dict,
adds any data to it and then returns it. Here is what a sample page controller
might look like:

```py
# about.py
import frappe

def get_context(context):
	context.about_us_settings = frappe.get_doc('About Us Settings')
	return context
```

Usage in template

{% raw %}
```html
<!-- about.html -->
<h1>{{ _("About Us") }}</h1>
<div class="row">
    <div class="col-sm-6">
		We believe that great companies are driven by excellence,
		and add value to both its customers and society.
		You will find our team embibes these values.
	</div>

	{% if about_us_settings.show_contact_us %}
	<a href="/contact" class="btn btn-primary">Contact Us</a>
	{% endif %}
</div>
```
{% endraw %}

> Since Portal Pages are built using Jinja, frappe provides a standard
> [API](/docs/user/en/api/jinja) to use in jinja templates.

#### List of standard context keys

Here is a list of all the standard keys that can be set in `context` and their
functionalities.

| Context Key           | Functionality                            |
| --------------------- | ---------------------------------------- |
| `add_breadcrumbs`     | Add breadcrumbs to page                  |
| `no_breadcrumbs`      | Remove breadcrumbs from page             |
| `show_sidebar`        | Show web sidebar                         |
| `safe_render`         | Toggle [safe_render](#safe_render)       |
| `no_header`           | Hide header                              |
| `no_cache`            | Disable caching for this page            |
| `sitemap`             | Include/exclude page in sitemap          |
| `add_next_prev_links` | Add Next and Previous navigation buttons |
| `title`               | Set the page title                       |

##### safe_render

`frappe.render_template` does not render a template which contains the string
`.__` to prevent running any illegal python expressions. You may want to disable
this behaviour if you are sure that the content is safe. To do this, you need to
turn off safe render by setting the value of `safe_render` key to `False` in
context.

#### Set context via frontmatter

You can also set values in context using a frontmatter block. Frontmatter blocks
can be used to set static values specific to a page like meta tags.

Take a look at the following example:
```bash
---
title: Introduction
metatags:
  description: This is description for the introduction page
---

# Introduction
This is an introduction page
```

The above frontmatter block will update the `context` dict with the following values:
```py
{
	'title': 'Introduction',
	'metatags': {
		'description': 'This is description for the introduction page'
	}
}
```

#### Set context via comments

You can also set some values in context by adding html comments in your pages.

For example by adding `<!-- add-breadcrumbs -->` to your `.html` or `.md` file,
`context.add_breadcrumbs` will be set to `True` and it will automatically generate
breadcrumbs based on folder structure.

{% raw %}
```html
<!-- add-breadcrumbs -->

<h1>{{ _("About Us") }}</h1>
<div class="row">
    <div class="col-sm-6">
		We believe that great companies are driven by excellence,
		and add value to both its customers and society.
		You will find our team embibes these values.
	</div>

	{% if about_us_settings.show_contact_us %}
	<a href="/contact" class="btn btn-primary">Contact Us</a>
	{% endif %}
</div>
```
{% endraw %}

Here is a list of keys that you can set and their context values:

| Comment                                                       | Context Value                                           |
| ------------------------------------------------------------- | ------------------------------------------------------- |
| `<!-- add-breadcrumbs -->`                                    | `add_breadcrumbs = 1`                                   |
| `<!-- no-breadcrumbs -->`                                     | `no_breadcrumbs = 1`                                    |
| `<!-- show-sidebar -->`                                       | `show_sidebar = 1`                                      |
| `<!-- no-header -->`                                          | `no_header = 1`                                         |
| `<!-- no-cache -->`                                           | `no_cache = 1`                                          |
| `<!-- no-sitemap -->`                                         | `sitemap = 0`                                           |
| `<!-- sitemap -->`                                            | `sitemap = 1`                                           |
| `<!-- add-next-prev-links -->`                                | `add_next_prev_links = 1`                               |
| `<!-- title: Custom Title -->`                                | `title = 'Custom Title'`                                |
| `<!-- base_template: custom_app/path/to/custom_base.html -->` | `base_template = 'custom_app/path/to/custom_base.html'` |

### Custom CSS and JS

You can add custom CSS and JS for your pages by dropping a `.css` or `.js` file
of the same name.

```bash
custom_app/www
├── custom_page.html
├── custom_page.css
├── custom_page.js
└── custom_page.py
```

### Home Page

The home page for your portal can be defined in

1. Role
1. Portal Settings (this will be for logged in users)
1. Via Hook `get_website_user_home_page`
1. Website Settings (this will be for non logged in users as well - i.e. Guest)
