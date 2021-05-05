---
title: Bench - bench show-config
metatags:
 description: >
  The Bench CLI has a show-config command to show the applied site config for your Frappe sites.
---

# bench show-config

## Usage

```bash
bench show-config [OPTIONS]
```

## Description

The applied configuration for your sites gets applied as a combination of the
bench directory's `common_site_config.json` and the site's own
`site_config.json`. Bench provides an interface to view the applied
`frappe.conf` values for your sites. You may choose to access this information
in tabular or JSON formats.

To read more about site configuration and understanding key precedence, refer to
the docs [here](/docs/user/en/basics/site_config).

## Flags

 - `-f`, `--format` Choose the format for listing apps installed on the
   specified site, options being "text" and "json". Default is "json".

## Examples

1. Show site config for all sites in JSON format.

   ```bash
   bench --site all show-config -f json
   ```

1. Show the site config in tabular form.

    ```bash
    bench --site {site} show-config --format text
    ```

    ```bash
    bench --site {site} show-config -f text
    ```

    ```bash
    bench --site {site} show-config
    ```
