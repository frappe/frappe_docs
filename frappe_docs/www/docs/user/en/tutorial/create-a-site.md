---
title: Create a Site - Frappe Framework Tutorial
description: A site comes with a database and apps can be installed on it
---

# Create a Site

Each site comes with a database. They may be customized throughsite specific scripting or Apps may be installed on them.

## Create a new site

To create a new site, run the following command from the `frappe-bench`
directory:

```bash
$ bench new-site library.test
MySQL root password:

Installing frappe...
Updating DocTypes for frappe        : [========================================] 100%
Updating country info               : [========================================] 100%
Set Administrator password:
Re-enter Administrator password:
*** Scheduler is disabled ***
Current Site set to library.test
```

This command will create a new database, so you need to enter your MySQL root
password. It will also ask to set the password for the Administrator user, just
set a password that you won't forget. This will be useful later.

Now, you will have a new folder named `library.test` in the `sites` directory.

## Site Directory Structure

The site directory structure will look something like this:

```bash
sites/library.test
├── indexes
│   └── web_routes
├── locks
├── logs
├── private
│   ├── backups
│   └── files
├── public
│   └── files
└── site_config.json

```

The `indexes` folder has indexes generated via [Website
Search](/docs/user/en/python-api/search).

The `locks` folder maintains file based locks over in-site documents as well as
indicators of the state of the site itself.

As you can see, the `private` folder will contain any database backups and
private files. Private files are user uploaded files that need authentication to
be accessible.

The `public` folder will contain files that are accessible without
authentication. This can contain website images that should be accessible
without login.

The `site_config.json` file contains configuration that is specific to this site
which should not be version controlled. This is similar to an environment
variables file. If you look at the contents of the file, it contains the
database configuration values for this site.

```json
{
 "db_name": "_ad03fa1a016ca1c4",
 "db_password": "pz1d2gN5y35ydRO5",
 "db_type": "mariadb"
}
```

## Access site in your browser

Now, that we have created our first site, we can access it on
[http://localhost:8000](http://localhost:8000) in our browser.

![Site Login Page](/assets/frappe_docs/tutorial/site-login-page.png)

However, `bench` allows you to create multiple sites and access them separately in
the browser on the same port. This is what we call multi-tenancy support in
bench.

To achieve that, we must disable the serving of the default site. Go back to
your terminal and delete the file `sites/currentsite.txt` from the
`frappe-bench` directory.

```bash
$ rm sites/currentsite.txt
```

Now, you won't be able to access your site on
[http://localhost:8000](http://localhost:8000).

Frappe will identify which site to serve by matching the hostname of the request
with the site name, so you should be able to access your site on
[http://library.test:8000](http://library.test:8000) but this won't work because
we have to tell our operating system that library.test should point to
localhost. To do that, you can add the following entry to your `/etc/hosts`
file.

```
127.0.0.1 library.test
```

This will map `library.test` to `localhost`. Bench has a convenient command to do
just that.

```bash
$ bench --site library.test add-to-hosts
```

This will ask for your root password and will add an entry to your `/etc/hosts` file.

Great, now you can access your site at
[http://library.test:8000](http://library.test:8000). Congratulations for making
it this far.

## Install app on site

To install our Library Management app on our site, run the following command:

```bash
$ bench --site library.test install-app library_management

Installing library_management...
```

To confirm if the app was installed, run the following command:

```bash
$ bench --site library.test list-apps
frappe
library_management
```

You should see `frappe` and `library_management` as installed apps on your site.

> When you create a new site, the `frappe` app is installed by default.

## Login to Desk

To create DocTypes in our app, we must log in to Desk. Go to
[http://library.test:8000](http://library.test:8000) and it should show you a
login page.

Enter Administrator as the user and password that you set while creating the
site.

![Setup Wizard](/assets/frappe_docs/tutorial/setup-wizard.png)

After successful login, you will see the setup wizard. This is a one-time setup
wizard used to set up localization details for your site. Go ahead, select your
language, and complete the wizard.

You should see the Desk that looks something like this:

![Desk](/assets/frappe_docs/tutorial/desk.png)

Good job making it this far!

## Site commands

We ran a couple of bench commands with the `--site` option. These commands are
called site commands.

Here are some of the useful site commands.

**Python Console**

```bash
# access the python console
$ bench --site library.test console
Apps in this namespace:
frappe, library_management

In [1]:
```

**MariaDB Console**

```bash
# access the mariadb console
$ bench --site library.test mariadb
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 2333498
Server version: 10.4.13-MariaDB Homebrew

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [_ad03fa1a016ca1c4]>
```

**Database Backup**

```bash
$ bench --site library.test backup
Backup Summary for library.test at 2020-10-06 23:21:17.277960
Config  : ./library.test/private/backups/20201006_232116-library_test-site_config_backup.json   94.0B
Database: ./library.test/private/backups/20201006_232116-library_test-database.sql.gz           217.4KiB
Backup for Site library.test has been successfully completed
```

You can see a list of all site commands by running the following command:

```bash
$ bench --site library.test --help
Usage: bench frappe [OPTIONS] COMMAND [ARGS]...

Options:
  --site TEXT
  --profile    Profile
  --verbose    Verbose
  --force      Force
  --help       Show this message and exit.

Commands:
  add-system-manager          Add a new system manager to a site
  add-to-email-queue          Add an email to the Email Queue
  add-to-hosts                Add site to hosts
  backup                      Backup
  browse                      Opens the site on web browser
  build                       Minify + concatenate JS and CSS files, build...
  build-message-files         Build message files for translation
  build-search-index
  bulk-rename                 Rename multiple records via CSV file
  clear-cache                 Clear cache, doctype cache and defaults
  clear-website-cache         Clear website cache
  console                     Start ipython console for a site
  data-import                 Import documents in bulk from CSV or XLSX...
  destroy-all-sessions        Clear sessions of all users (logs them out)
```

Next: [Create a DocType](/docs/user/en/tutorial/create-a-doctype)
