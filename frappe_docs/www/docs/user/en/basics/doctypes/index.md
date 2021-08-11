---
add_breadcrumbs: 1
page_toc: 1
title: DocTypes
metatags:
 description: >
  Learn all about the core concept of DocType and how it is used to describe
  almost any kind of logic and behaviour in Frappe.
---

# Understanding DocTypes

1. [Introduction](#doctype)
1. [Modules](doctypes/modules)
1. [DocField](doctypes/docfield)
1. [Naming](doctypes/naming)
1. [Controllers](doctypes/controllers)
    - [Controller Methods](doctypes/controllers#controller-methods)
    - [Controller Hooks](doctypes/controllers#controller-hooks)
1. [Child DocType](doctypes/child-doctype)
1. [Single DocType](doctypes/single-doctype)
1. [Virtual DocType](doctypes/virtual-doctype)
1. [Actions and Links](doctypes/actions-and-links)
1. [Customizing DocTypes](doctypes/customize)

## Introduction

A DocType is the core building block of any application based on the Frappe Framework.
It describes the **Model** and the **View** of your data.
It contains what fields are stored for your data, and how they behave with respect to each other.
It contains information about how your data is named.
It also enables rich **Object Relational Mapper (ORM)** pattern which we will discuss later in this guide.
When you create a DocType, a JSON object is created which in turn creates a database table.

> ORM is just an easy way to read, write and update data in a database without writing explicit SQL statements.

#### Conventions

To enable rapid application development, Frappe Framework follows some standard conventions.

1. DocType is always singular. If you want to store a list of articles in the
database, you should name the doctype **Article**.
1. Table names are prefixed with `tab`. So the table name for **Article** doctype
is `tabArticle`.


The standard way to create a DocType is by typing *new doctype* in the search bar in the **Desk**.

![ToDo DocType](/docs/assets/img/doctypes/todo-doctype.png)
*ToDo DocType*

A DocType not only stores fields, but also other information about how your data
behaves in the system. We call this **Meta**. Since this meta-data is also stored
in a database table, it makes it easy to change meta-data on the fly without writing
much code. Learn more about [Meta](#meta).

> A DocType is also a DocType. This means that we store meta-data as the part of the data.

After creating a DocType, Frappe can provide many features out-of-the-box.
If you go to `/app/todo` you will be routed to the List View in the desk.

![ToDo List](/docs/assets/img/doctypes/list-view.png)
*ToDo List*

Similarly, you get a Form View at the route `/app/todo/000001`.
The Form is used to create new docs and view them.

![ToDo Form](/docs/assets/img/doctypes/form-view.png)
*ToDo Form*
