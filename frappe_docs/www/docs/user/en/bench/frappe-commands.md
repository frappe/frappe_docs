---
title: Bench - Frappe Commands
metatags:
 description: >
  The Bench CLI inherits commands from the bench's Frappe installation.
---

# Frappe Commands

The Bench CLI utilizes the module`frappe.utils.bench_manager` to get the
framework's as well as any other Application's commands present on the current
bench directory.

This page is concerned only with the commands that exist in the Frappe project,
that are a direct part of the CLI tool. These commands are defined under the
[frappe/frappe](https://github.com/frappe/frappe).

> For references of any Bench commands, checkout [Bench
> Commands](/docs/user/en/bench/bench-commands).

There are four major command types in Frappe inherited by Bench during command
executions. They can be broadly grouped into


### Site Commands

Set of commands used for site-specific operations. These are the most frequented
commands to alter the state of your sites. These commands are accessed by using
the `--site` option along with the site name (or "all") if you wish to run the
operation *(if possible)* for all sites on the bench. These commands are defined
under the module `frappe.commands.site`.

#### Site Creation

Create a new Site on your bench. By default, all sites created on your bench
will have only the Frappe Framework installed on them.

```bash
bench new-site {site}
```

For more information and examples, see the [bench
new-site](/docs/user/en/bench/reference/new-site) reference.

#### Site Backups

You can use the Bench CLI to take backups on the sites of your bench. You can
manage the site's database and files backups and have more control over the
operation.

```bash
bench --site {site} backup
```

The Bench CLI also deletes the older backup files from your bench directory. By
default, it deletes backups older than 24 hours from the backups directory.

For more information and examples, see the [bench
backup](/docs/user/en/bench/reference/backup) reference.

#### Site Restores

Bench CLI can be used to restore an existing site to a previous state. Using the
`bench restore` command, a site may be restored with the specific database and
file restores.

```bash
bench --site {site} restore {path/to/database/file}
```

The least requirement for performing a restore operation is having the database
file on your local filesystem. The specified backup file may have the `sql.gz`
of `sql` extension.

For more information and examples, see the [bench
restore](/docs/user/en/bench/reference/restore) reference.

#### Partial Site Restores and Backups

Since Version 13, Frappe has support for taking partial backups and restoring
them. Partial backups can be taken using the `bench backup` command directly. As
for partial restores, the `bench partial-restore` command may be used to restore
the partial backups to an existing site.

For more information and examples, see the [bench
partial-restore](/docs/user/en/bench/reference/partial-restore) and [bench
backup](/docs/user/en/bench/reference/backup) reference.

#### Site App Management

You can install or uninstall Frappe Applications available on your Bench. To add
Apps to your bench using `bench get-app` checkout [the
docs](/docs/user/en/bench/bench-commands#frequently-used).

##### App Installation

The easiest way to install a Frappe Application on your site is through the
Bench CLI. However, the application must be installed on your bench prior to
that.

```bash
bench --site {site} install-app {app}
```

In this operation, Application `meta`, `modules` and `doctypes` of the specified
site are installed on the specified site.

##### App Uninstallation

Uninstall an app installed on site. This is a destructive action and consists of
removing all app-related data from the site. Hence, a backup is taken before
uninstalling said app.

```bash
bench --site {site} uninstall-app {app}
```

> Note: From Version 13, even apps not installed on the Bench can be uninstalled
> from the site.

For more information and examples, see the [bench
uninstall-app](/docs/user/en/bench/reference/uninstall-app) reference.

#### Site Migrations

Run patches, sync schema and rebuild files, translations and indexes on a
particular site. Find out how site migrations work in [the docs](/docs/user/en/database-migrations).

```bash
bench --site {site} migrate
```

For more information and examples, see the [bench
migrate](/docs/user/en/bench/reference/migrate) reference.

#### Site Deletion

Drops the database and moves the site directory from `./sites` to the
`./archived_sites` *(unless specified otherwise)* folder on your Bench.

```bash
bench drop-site {site}
```

For more information and examples, see the [bench
drop-site](/docs/user/en/bench/reference/drop-site) reference.

#### Reset Site Data

Re-install all installed Applications from your specified site. This completely
resets the site.

```bash
bench reinstall {site}
```

For more information and examples, see the [bench
reinstall](/docs/user/en/bench/reference/reinstall) reference.

#### List Installed Apps

List all the Frappe Applications installed on the specified site. The
information shown by the command is fetched from the **Installed Applications**
DocType which tracks the latest version of the apps, the site was migrated to.
The global default `installed_apps` is used as fallback.

```bash
bench --site {site} list-apps
```

Multi-site support has been added in Version 13. To see the summary for all
sites, run the command with site's value as `all`.

For more information and examples, see the [bench
list-apps](/docs/user/en/bench/reference/list-apps) reference.

#### Setting the default site

Sometimes typing `--site [sitename]` for every site command can be tedious. You
can set the default site for the terminal session by setting the `FRAPPE_SITE`
environment variable.

```bash
~/frappe-bench
❯ export FRAPPE_SITE=mysite.localhost

~/frappe-bench
❯ echo $FRAPPE_SITE
mysite.localhost

~/frappe-bench
❯ bench console
Apps in this namespace:
frappe

In [1]: frappe.local.site
Out[1]: 'mysite.localhost'
```

#### Access site in the browser

To access a site in the browser, you have to remember the webserver port on
which bench is running and then type out the full URL. There is a bench command
that does this for you.

Running the following command will open the site url directly in your default
browser.
```bash
# open site.local in the browser
$ bench --site site.local browse

# this also works
$ bench browse site.local
```

You can also login as a user by passing `--user` option.
```bash
$ bench --site site.local browse --user test@example.com

$ bench --site site.local browse --user Administrator
Login URL: http://site.local:8000/app?sid=<generated-sid>
```

> Note that this command:
>
>  - Allows login as any user only when developer_mode is set to 1
>  - Allows login as Administrator regardless of developer_mode
>  - Prints the login URL only when user is Administrator


#### Site Operations, Debugging & Development

Here are some operations you can perform on your site via the Bench CLI to
update your site state. You may never have to use some of these, but they exist
just in case.

 - **add-system-manager**: Add a new system manager to a site.
 - **add-to-hosts**: Add the specified site to the hosts file on your system.
 - **build-search-index**: Builds search index for Websites. Refer to [Full Text
   Search API Docs](/docs/user/en/api/full-text-search) for more information.
 - **disable-user**: Disable user on site.
 - **publish-realtime**: Publish realtime event from bench.
 - **reload-doc**: Reload schema for a particular *Doctype* and refresh the
   specified *Document*
 - **reload-doctype**: Reload schema for a particular *DocType*
 - **remove-from-installed-apps**: Removes the mentioned app from the site
   gloabl value of `installed_applications`.
 - **run-patch**: Run a particular patch via the Frappe Patch Handler.
 - **migrate-to**: Command to migrate your local site to a Frappe Hosting
   Provider's service.
 - **ngrok**: Create a temporary URL and share it with anyone, and they can
   access your local site in their browser. Primarily built for aiding with the
   development of third party services.
 - **set-password**: Set the password for any user.
 - **set-admin-password**: Set the password for the Administrator user.
 - **set-last-active-for-user**: Set users last active date to current datetime.
 - **start-recording**: Starts the Frappe Recorder for the specified sites.
 - **stop-recording**: Terminates the Frappe Recorder for the specified sites.
 - **use**: Sets the default site on the bench. Adds the site entry to the
   `currentsite.txt`.


### Database Maintenance Commands

Set of commands that are related to database management and maintenance. These
commands offer more control to your site's database. You may want to fine-tune
your deployment to fit your site's needs over time.

#### Table Transformations

The `transform-database` command allows you to manage the settings of your
site's tables. At this point, you can switch `engine` and `row_format` settings for
select tables on your site database.

```bash
bench --site {site} transform-database --tables {tables}
```

For more information and examples, see the [bench
transform-database](/docs/user/en/bench/reference/transform-database) reference.

#### Table Trimming

Docfields removed from a particular DocType may not be deleted from their Database
tables. This is by design to prevent premature data loss in Frappe. This won't be
problematic for the most part, however, at some point you may face issues due to this
lingering data.

Some benefits of regular table trimming are:

- Smaller backup sizes
- Reduced time taken to backup sites
- Reduced Site Database Usages
- Optimized queries in case of `SELECT *`
- Database is clean and doesn't have anything hidden or redundant data

```bash
bench trim-tables [OPTIONS]
```

For more information and examples, see the [bench
trim-tables](/docs/user/en/bench/reference/trim-tables) reference.

#### Database Trimming

Deleting DocTypes from the list view may not delete their corresponding tables from
the database. Migrations may leave ghost tables in your Site Database at times. This
 may be done for the sake of redundancy, for recovery in case your data is corrupted
 or lost, or simply, in cases of human error.

```bash
bench trim-database [OPTIONS]
```

For more information and examples, see the [bench
trim-database](/docs/user/en/bench/reference/trim-database) reference.

### Scheduler Commands

Commands to manage and review the scheduler and background jobs' statuses for
the sites on your bench. Defined under module `frappe.commands.schedule`.

 - **disable-scheduler**: Disable scheduler for specified sites.
 - **doctor**: Get diagnostic info about the status of the scheduler for all
   sites (if unspecified) and active workers on bench.
 - **enable-scheduler**: Enables scheduler for specified sites.
 - **purge-jobs**: Purge any pending periodic tasks, if the event option is not
   given, it will purge everything for the site.
 - **ready-for-migration**: Checks if a particular site is ready for migration
   by checking the existence of any pending background jobs.
 - **scheduler**: Change the state of the scheduler for any site from *pause*,
   *resume*, *disable* or *enable* state.
 - **set-maintenance-mode**: Set the value for maintenance mode in the config
   for specified sites.
 - **show-pending-jobs**: Get diagnostic info about background jobs.
 - **schedule**: Start the scheduler process for your bench. This process
   manages scheduler events defined in the `hooks.py` file. You can find this
   command mentioned in the bench config for your process manager too.
 - **worker**: Start worker process on your bench. The process this starts will
   manage all background jobs started on this bench.
 - **trigger-scheduler-event**: Trigger a specific scheduler event for the
   specified sites.


### Frappe Utility Commands

Frappe Utility commands that can be both, site or bench specific. These commands
are defined under the module `frappe.commands.utils`.

#### Displaying Site Config

The applied configuration for your sites gets applied as a combination of the
bench directory's `common_site_config.json` and the site's own
`site_config.json`. You can read more about this,
[here](/docs/user/en/basics/site_config). Bench provides an interface to view
the applied `frappe.conf` values for your sites. You may choose to access this
information in tabular or JSON formats.

```bash
bench --site {site} show-config
```

For more information and examples, see the [bench
show-config](/docs/user/en/bench/reference/show-config) reference.


#### Updating Site Config

Bench provides a wrapper command to insert or update values in the site config
files. You can update values in your site's `site_config.json`, along with the
bench directory's `common_site_config.json` through the same command.

```bash
bench --site {site} set-config KEY VALUE
```

For more information and examples, see the [bench
set-config](/docs/user/en/bench/reference/set-config) reference.

#### Display Version Of Installed Apps

The `version` command displays all installed apps and their versions.

```bash
bench version [OPTIONS]
```

With version 13, the `-f` / `--format` option was introduced. This option allows
you to display additional information about the branch and last commit. For more
information and examples, see the [bench
version](/docs/user/en/bench/reference/bench-version) reference.

#### More Commands

 - **add-to-email-queue**: Add an email to the Email Queue.
 - **build**: Builds assets for the Frappe Applications installed on bench.
 - **bulk-rename**: Rename multiple records via a CSV file. _Example File Format (Without Header)_:

   | Old Name | New Name | Merge |
   | -------- | -------- | ----- |
   | HR-EMP-00001 | EMP0001 | FALSE |
   | HR-EMP-00002 | EMP0002 | FALSE |
   | HR-EMP-00003 | EMP0003 | FALSE |
   | HR-EMP-00004 | EMP0004 | FALSE |
   | HR-EMP-00005 | EMP0005 | FALSE |
   | HR-EMP-00006 | EMP0006 | FALSE |

 - **clear-cache**: Clear cache, doctype cache and defaults.
 - **clear-website-cache**: Clear Website cache.
 - **console**: Starts an IPython console for the site. Use with the `--autoreload` flag to reload changes to code automatically.
 - **data-import**: Import documents in bulk from CSV or XLSX using data import.
 - **destroy-all-sessions**: Clear sessions of all users (logs them out).
 - **execute**: Execute a particular function or method with a given set of
   `args` and `kwargs`.
 - **export-csv**: Export data import template with data for DocType.
 - **export-doc**: Export a single document to CSV.
 - **export-fixtures**: Export records from a site to your Frappe Application, as JSON files. Fixtures are defined in your app's [`hooks.py` file](/docs/user/en/python-api/hooks#fixtures).
 - **export-json**: Export doclist as json to the given path, use '-' as name
   for Singles.
 - **import-csv**: Import from your CSV file using data import.
 - **import-doc**: Import (insert/update) doclist. If the argument is a
   directory, all files ending with `.json` are imported
 - **jupyter**: Starting a Jupyter Notebook server.
 - **make-app**: Creates a boilerplate Frappe Application.
 - **db-console**: Start the interactive DB console for your site. This command is an alias over commands: mariadb, postgres
 - **mariadb**: Start the MySQL interactive console for the mysql site.
 - **postgres**: Start the PostgreSQL interactive console for the postgres site.
 - **rebuild-global-search**: Setup help table in the current site (called after
   migrate).
 - **request**: Make a request as Administrator with Arguements to a Path.
 - **reset-perms**: Reset permissions for all DocTypes to their default
   settings.
 - **run-tests**: Run Python tests on the specified site.
 - **run-parallel-tests**: Run Python tests parallelly on CI.
 - **run-ui-tests**: Run Cypress UI tests.
 - **serve**: Start the webserver for the bench.
 - **watch**: Watch and concatenate JS and CSS files as and when they change.


### Translation Commands

Set of commands to manage translations for your multi-lingual deployments. These
commands are defined under the module `frappe.commands.translate`.

 - **build-message-files**: Build message files for translation.
 - **get-untranslated**: Get untranslated strings for language.
 - **import-translations**: Import translations from file in standard format.
 - **new-language**: Create lang-code.csv for given Frappe Application.
 - **update-translations**: Update translations for set language between files.
