---
title: Create a DocType - Frappe Framework Tutorial
description: DocType is analogous to a Model in other frameworks. Apart from defining properties, it also defines the behavior of the Model.
---

# Create a DocType

DocType is analogous to a Model in other frameworks. Apart from defining
properties, it also defines the behavior of the Model.

## Enable Developer Mode

Before we can create DocTypes, we need to enable developer mode on our bench. This
will enable boilerplate creation when we create doctypes and we can track them into
version control with our app.

Go to your terminal and quit the bench server if it's already running then from the `frappe-bench` directory, run the following command:

```bash
$ bench set-config -g developer_mode true
$ bench start
```

## Creating a DocType

While in Desk, navigate to the **DocType List** using the [Awesomebar](/docs/user/en/desk#awesomebar). This list will include DocTypes bundled with the framework, those that are a part of the installed Frappe apps and custom ones, which you can create specific to each site.

The first doctype we will create is **Article**. To create it, click on New.

1. Enter Name as Article
2. Select Library Management in Module
3. Add the following fields in the Fields table:
    1. Article Name (Data)
    1. Image (Attach Image)
    1. Author (Data)
    1. Description (Text Editor)
    1. ISBN (Data)
    1. Status (Select) - Enter two options: Issued and Available (Type Issued, hit enter, then type Available)
    1. Publisher (Data)

Refer the following GIF to check how it should be done:

![Article DocType](/assets/frappe_docs/tutorial/article-doctype.gif)

After adding the fields, click on Save.

You will see a **Go to Article List** button at the top right of the form. Click
on it to go to the Article List. Here you will see a blank list with no records
because the table has no records.

Let's create some records. But before that, we need to clear the Desk cache.
Click on the **Settings** dropdown on the right side of the navbar and click on
**Reload**.

Now, you should see the **New** button. Click on it and you will see the Form
view of the Article doctype. Fill in the form and click on Save. You have
created your first Article document. Go back to the list view and you should see
one record.

![Article New Form](/assets/frappe_docs/tutorial/article-new-form.gif)

### What happened when you created the Article DocType?

**1. Database Table**

A database table with the name `tabArticle` was created with the fields we
specified in the fields table. You can confirm this by checking it from the
MariaDB console

```bash
$ bench --site library.test mariadb
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 2445938
Server version: 10.4.13-MariaDB Homebrew

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [_ad03fa1a016ca1c4]> desc tabArticle;
+--------------+--------------+------+-----+-----------+-------+
| Field        | Type         | Null | Key | Default   | Extra |
+--------------+--------------+------+-----+-----------+-------+
| name         | varchar(140) | NO   | PRI | NULL      |       |
| creation     | datetime(6)  | YES  |     | NULL      |       |
| modified     | datetime(6)  | YES  | MUL | NULL      |       |
| modified_by  | varchar(140) | YES  |     | NULL      |       |
| owner        | varchar(140) | YES  |     | NULL      |       |
| docstatus    | int(1)       | NO   |     | 0         |       |
| parent       | varchar(140) | YES  | MUL | NULL      |       |
| parentfield  | varchar(140) | YES  |     | NULL      |       |
| parenttype   | varchar(140) | YES  |     | NULL      |       |
| idx          | int(8)       | NO   |     | 0         |       |
| article_name | varchar(140) | YES  |     | NULL      |       |
| image        | text         | YES  |     | NULL      |       |
| author       | varchar(140) | YES  |     | NULL      |       |
| description  | longtext     | YES  |     | NULL      |       |
| isbn         | varchar(140) | YES  |     | NULL      |       |
| status       | varchar(140) | YES  |     | Available |       |
| publisher    | varchar(140) | YES  |     | NULL      |       |
| _user_tags   | text         | YES  |     | NULL      |       |
| _comments    | text         | YES  |     | NULL      |       |
| _assign      | text         | YES  |     | NULL      |       |
| _liked_by    | text         | YES  |     | NULL      |       |
+--------------+--------------+------+-----+-----------+-------+
21 rows in set (0.002 sec)

MariaDB [_ad03fa1a016ca1c4]>
```

The fields we specified in Title Case were converted to snake case
automatically, and are used as the column names in the table. For e.g.,
`article_name`, `image`, `author` , and `description`.

However, many other fields were created like `name`, `creation`, `modified`,
`modified_by` . These are standard fields created for all doctypes. `name` is
the primary key column.

If you created a record with the Form, you can also run a standard select query
to get the rows.

```bash
MariaDB [_ad03fa1a016ca1c4]> select * from tabArticle;
+------------+----------------------------+----------------------------+---------------+---------------+-----------+--------+-------------+------------+-----+-----------------------------+--
| name       | creation                   | modified                   | modified_by   | owner         | docstatus | parent | parentfield | parenttype | idx | article_name                | i
+------------+----------------------------+----------------------------+---------------+---------------+-----------+--------+-------------+------------+-----+-----------------------------+--
| bd514646b9 | 2020-10-10 16:24:43.033457 | 2020-10-10 16:24:43.033457 | Administrator | Administrator |         0 | NULL   | NULL        | NULL       |   0 | The Girl with all the Gifts | N
+------------+----------------------------+----------------------------+---------------+---------------+-----------+--------+-------------+------------+-----+-----------------------------+--

MariaDB [_ad03fa1a016ca1c4]>
```

**2. Desk Views**

There are a number of views that were also created for our DocType. The Article
List is the list view that shows the records from the database table. The Form
view is the view that is shown when you want to create a new document or view an
existing one.

**3. Form Layout**

If you notice, the layout of fields in the form is according to how you ordered
them in the Fields table. For e.g., Article Name is the first field followed by
Image which is followed by Author. In later parts of the tutorial we will learn
how to customize this further.

**4. Boilerplate code**

If you look at the changes in your app, you should find a number of files that
were created. Go to your terminal and from the `frappe-bench` directory run the
following commands.

```bash
$ cd apps/library_management
$ git status -u
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	library_management/library_management/doctype/__init__.py
	library_management/library_management/doctype/article/__init__.py
	library_management/library_management/doctype/article/article.js
	library_management/library_management/doctype/article/article.json
	library_management/library_management/doctype/article/article.py
	library_management/library_management/doctype/article/test_article.py

nothing added to commit but untracked files present (use "git add" to track)
```

**article.json** - JSON file that defines the doctype attributes

**article.js** - Client-side controller for the Form view

**article.py** - Python controller for Article

**test_article.py** - Python Unit Test boilerplate for writing tests

As you can see, a DocType describes a lot of things about the model. Not only
does it define the table and column names but also how it will be rendered in
various views in the Desk.

Good job following the tutorial so far. Let's keep going!

Next: [DocType Features](/docs/user/en/tutorial/doctype-features)
