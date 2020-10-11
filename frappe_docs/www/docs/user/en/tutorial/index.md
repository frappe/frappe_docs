---
title: Frappe Framework Tutorial
description: Learn how to create a web application from scratch using the Frappe Framework
---

# Frappe Framework Tutorial

In this guide, you will learn how to create a web application from scratch using
the Frappe Framework.

## Who is this for?

This guide is intended for software developers who are familiar with how web
applications are built. Frappe Framework is based on Python and MariaDB (or
Postgres) as the database. Jinja is used as the templating language for Web
Views. So it would be great if you are familiar with all these technologies.

Frappe Framework uses the `git` for version control and automatic updates. It is
also expected that you are familiar with basic git commands.

## What are we building?

We will build a simple **Library Management System** in which the **Librarian**
can log in and manage Articles and Memberships. We will build the following
models:

1. **Article:** A Book or similar item that can be rented.
2. **Library Member:** A user who is subscribed to a membership.
3. **Library Transaction:** An Issue or Return of an article.
4. **Library Membership:** A document that represents an active membership of a
   Library Member.
5. **Library Settings:** Settings that define values like Loan Period and
   maximum number of articles that can be issued at a time.

The Librarian will log in to an interface known as **Desk**, a rich admin
interface that ships with the framework. Desk provides many standard views like
List view, Form view, Report view, etc, and many features like Role-based
Permissions.

We will also create public Web Views which can be accessed by the Library
Members where they can browse available Articles.

## Table of Contents

1. [Prerequisites](/docs/user/en/tutorial/prerequisites)
1. [Install and Setup Bench](/docs/user/en/tutorial/install-and-setup-bench)
1. [Create an App](/docs/user/en/tutorial/create-an-app)
1. [Create a Site](/docs/user/en/tutorial/create-a-site)
1. [Create a DocType](/docs/user/en/tutorial/create-a-doctype)
1. [DocType Features](/docs/user/en/tutorial/doctype-features)
1. [Controller Methods](/docs/user/en/tutorial/controller-methods)
1. [Types of DocType](/docs/user/en/tutorial/types-of-doctype)
1. [Form Scripts](/docs/user/en/tutorial/form-scripts)
1. [Portal Pages](/docs/user/en/tutorial/portal-pages)
1. [What's Next](/docs/user/en/tutorial/whats-next)
