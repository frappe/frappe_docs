---
title: Bench - bench list-apps
metatags:
  description: >
    The Bench CLI has a list-apps command to list the apps installed on specific Frappe sites.
---

# bench list-apps

## Usage

```bash
bench list-apps [OPTIONS]
```

## Description

List all the Frappe Applications installed on the specified site. The
information shown by the command is fetched from the **Installed Applications**
DocType which tracks the latest version of the apps, the site was migrated to.
The global default `installed_apps` is used as fallback.

Multi-site support has been added in Version 13. To see the summary for all
sites, run the command with site's value as `all`.

## Options

  - `--format`, `-f` Choose the format for listing apps installed on the
    specified site, options being "text" and "json". Default is "json".

### Examples

1. List apps installed on all sites.

    ```bash
    bench --site all list-apps
    ```

1. List apps installed on all sites in parsable JSON format.

    ```bash
    bench --site all list-apps --format json
    ```

1. List apps installed on a specific site in text format.

    ```bash
    bench --site {site} list-apps --format text
    ```

    ```bash
    bench --site {site} list-apps -f text
    ```

    ```bash
    bench --site {site} list-apps
    ```
