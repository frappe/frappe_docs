---
add_breadcrumbs: 1
title: Frappe ORM
metatags:
 description: >
  Data manipulation using the Frappe ORM
---

# ORM

There are a few ways to interact with the Database in Frappe. `Query Builder`, `DatabaseQuery`, `Database` and `Document` are the major ways.

Some of the available interfaces in the Frappe ORM are:

  1. [Document](#document)
  1. [DatabaseQuery](#database-query)
  1. [Query Builder](#query-builder)

## Document

> TODO: Add introductory content

Read more in the [Document](/docs/user/en/api/document) reference.

## Database Query

> TODO: Add introductory content

Read more in the [DatabaseQuery](/docs/user/en/api/database-query) reference.

## Query Builder

> TODO: Add introductory content

Read more in the [Query Builder](/docs/user/en/api/query-builder) reference.

## Database transaction model

Frappe's database abstractions implement a sane transaction model by default. So in most cases, you won't have to deal with SQL transactions manually. A broad description of this model is described below:

### Web requests

- While performing `POST` or `PUT`, if any writes were made to the database, they are committed at end of the successful request.
- AJAX calls made using `frappe.call` are `POST` by default unless changed.
- `GET` requests do not cause an implicit commit.
- Any **uncaught** exception during handling of request will rollback the transaction.

### Jobs

> These include Background and Scheduled jobs

- Calling a function as background or scheduled job will commit the transaction after successful completion.
- Any **uncaught** exception will cause rollback of the transaction.

### Patches

- Successful completion of the patch's `execute` function will commit the transaction automatically.
- Any **uncaught** exception will cause rollback of the transaction.

### Unit tests

- Transaction is committed after running one test module. Test module means any python test file like `test_core.py`.
- Transaction is also committed after finishing all tests.
- Any **uncaught** exception will exit the test runner, hence won't commit.

> Note: If you're catching exceptions anywhere, then database abstraction does not know that something has gone wrong hence you're responsible for the correct rollback of the transaction.
