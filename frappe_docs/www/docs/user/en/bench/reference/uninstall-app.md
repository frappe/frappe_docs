---
title: Bench - bench uninstall-app
metatags:
 description: >
  The Bench CLI has an uninstall-app command to remove apps from your Frappe sites.
---

# bench uninstall-app

## Usage

```bash
bench uninstall-app [OPTIONS] APP
```

## Description

Remove Application and linked doctypes, modules from the site. Executing the
vanilla command will check if the app exists on site before attempting to delete
its modules and doctypes. The application may not be necessarily installed on
the bench to run the `uninstall-app` command.

## Flags

 - `-y`, `--yes` To bypass confirmation prompt for uninstalling the app
 - `--dry-run` List all doctypes that will be deleted
 - `--no-backup` Do not backup the site
 - `--force` Force remove the app from site

## Examples

1. Perform a dry run to see what would happen on running it on a particular
   site.

   ```bash
   bench --site {site} uninstall-app {app} --dry-run
   ```

1. Don't take a backup before the application uninstall operation.

   ```bash
   bench --site {site} uninstall-app {app} --no-backup
   ```

1. Use force to uninstall application from site.

   ```bash
   bench --site {site} uninstall-app {app} --force
   ```

2. Skip the interactive prompt for confirmation of uninstall.

   ```bash
   bench --site {site} uninstall-app {app} --yes
   ```

