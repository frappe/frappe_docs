---
title: Portal Pages - Frappe Framework Tutorial
description: Portal pages are server rendered pages for your website visitors
---

# Portal Pages

Portal pages are server rendered pages for your website visitors.

We have been exclusively working with the Desk which is the admin interface
accessible by System Users. Usually you will want to give limited access to your
customers. In our case, we want Library Members to be able to view available
Articles that they can issue from our website. Portal Pages can help us achieve
that.

Go to Article doctype, and scroll down to the Web View section.

1. Enable **Has Web View** and **Allow Guest to View**
2. Enter **articles** in the Route field
3. Add a field named **Route** in the fields table
4. Click on Save

![Article Web View](/assets/frappe_docs/tutorial//article-web-view.gif)

We have now enabled web views for Article doctype. This means you can now view
details of an Article on your website without logging into Desk. Let's test this
out by creating a new Article. You should see **See on Website** at the top left
of your form. Click on it to view the web view of the Article.

![Article Web Page](/assets/frappe_docs/tutorial//article-web-page.gif)

## Customize Web View Template

The default web view that is generated is pretty barebones and serves only as a
starting point for us to customize it. When we made Article a web view, two HTML
files were created namely: `article.html` and `article_row.html`

Let's edit **article.html** first. Frappe uses Bootstrap 4 by default for it's
web views. So, you can use any valid Bootstrap 4 markup to style your pages. Add
the following HTML to **article.html**.

{% raw %}
```html
{%  extends "templates/web.html" %}

{% block page_content %}
<div class="py-20 row">
    <div class="col-sm-2">
        <img src="{{ image }}" alt="{{ title }}">
    </div>
    <div class="col">
        <h1>{{ title }}</h1>
        <p class="lead">By {{ author }}</p>
        <div>
            {%- if status == 'Available' -%}
            <span class="badge badge-success">Available</span>
            {%- elif status == 'Issued' -%}
            <span class="badge badge-primary">Issued</span>
            {%- endif -%}
        </div>
        <div class="mt-4">
            <div>Publisher: <strong>{{ publisher }}</strong></div>
            <div>ISBN: <strong>{{ isbn }}</strong></div>
        </div>
        <p>{{ description }}</p>
    </div>
</div>
{% endblock %}
```
{% endraw %}

Now, go to any Article and click on **See on Website**. If you have filled in
all fields of your Article, you should see a page like this:

![Article Portal Page](/assets/frappe_docs/tutorial/article-portal-page.png)

Now, open
[http://library.test:8000/articles](http://library.test:8000/articles). This
should show the list of articles, but it is also pretty barebones. Let's
customize the HTML.

Edit the **article_row.html** and add the following HTML:

{% raw %}
```html
<div class="py-8 row">
	<div class="col-sm-1">
		<img src="{{ doc.image }}" alt="{{ doc.name }}">
	</div>
	<div class="col">
		<a class="font-size-lg" href="{{ doc.route }}">{{ doc.name }}</a>
		<p class="text-muted">By {{ doc.author }}</p>
	</div>
</div>
```
{% endraw %}

Now, the articles list should look prettier. You can click on any article to
view it's details.

![Articles Portal Page](/assets/frappe_docs/tutorial/articles-portal-page.png)

Good job on following the tutorial so far.

Next: [What's Next](/docs/user/en/tutorial/whats-next)
