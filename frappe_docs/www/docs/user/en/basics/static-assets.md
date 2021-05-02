---
add_breadcrumbs: 1
title: Static Assets
metatags:
 description: A guide to understanding how static assets are served in Frappe Framework.
---

# Static Assets

A guide to understanding how static assets are served in Frappe Framework.

## The `assets` folder

Static files are served from the `frappe-bench/sites/assets` folder. When you
set up frappe for production deployment, nginx serves this folder directly. All
static file URLs always start with `/assets`. A file at the location
`frappe-bench/sites/assets/hero.png` is accessible publicly via the URL
`/assets/hero.png`.

## The `public` folder

Every app has its own `public` folder which can be used to serve static assets.
This folder is symlinked to `frappe-bench/sites/assets/[appname]`. Here is the
output of `tree` command on the assets folder.

```sh
~/frappe-bench
$ tree sites/assets -L 1
sites/assets
├── erpnext -> ~/frappe-bench/apps/erpnext/erpnext/public
└── frappe -> ~/frappe-bench/apps/frappe/frappe/public
```

This means if there is file at `[appname]/public/images/favicon.png`, then it
also exists as a symlink at `assets/[appname]/images/favicon.png` and is
accessible publicly via the URL `/assets/[appname]/images/favicon.png`.

### Bundled Assets

[Bundled Assets](/docs/user/en/basics/asset-bundling) are generated at
`assets/[appname]/dist/js` and `assets/[appname]/dist/css`. Hence, they are
accessible via the URL `/assets/[appname]/dist/js/main.bundle.[hash].js`.

## Site Assets
<!-- ## /files and /private/files and /private/backups -->

In addition to static files provided by apps, each site can have its own static
files that might come from user uploads or site backups.

### User uploads

Files uploaded by user that are public are stored at
`frappe-bench/sites/[sitename]/public/files`. A file stored at
`frappe-bench/sites/[sitename]/public/files/profile.png` is accessible publicly
via the URL `/files/profile.png`

Files uploaded by user that are private are stored at
`frappe-bench/sites/[sitename]/private/files`. A file stored at
`frappe-bench/sites/[sitename]/private/files/profile.png` is accessible via the
URL `/private/files/profile.png`. Private files are accessible only when the
user is authorized to view them.

### Backups

Any local backups that are generated for the site are stored as
`frappe-bench/sites/[sitename]/private/backups/20210502_182223-[sitename]-database.sql.gz`.
It is accessible via the URL
`/backups/20210502_182223-[sitename]-database.sql.gz` and only when the user is
authorized to download them.

Here is the output of the `ls` command:

```sh
~/frappe-bench
$ ls -l sites/site1.test/private/backups
total 6160
-rw-r--r--  1 farisansari  staff  2429268 May  2 18:22 20210502_182223-site1_test-database.sql.gz
-rw-r--r--  1 farisansari  staff      278 May  2 18:22 20210502_182223-site1_test-site_config_backup.json
```
