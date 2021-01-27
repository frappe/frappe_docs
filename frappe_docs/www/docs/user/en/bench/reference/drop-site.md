---
title: Bench - bench drop-site
metatags:
 description: >
  The Bench CLI has a drop-site command to archive Frappe sites from an existing bench.
---

# bench drop-site

## Usage

```bash
bench drop-site [OPTIONS] SITE
```

## Description

Drop an existing site. In this operation, the database is dropped and the
respective site's folder is moved from `./sites` to `./archived_sites` *(unless
specified otherwise)* on your Bench. A full site backup is taken prior to this.

## Options

 - `--root-login` Username for a DBMS user with drop database privileges.
   Defaults to *root*
 - `--root-password` Password for the DBMS user
 - `--archived-sites-path` Specify the path to move the site's folder in

## Flags

 - `--no-backup` Skip backup prior to site drop
 - `--force` Force drop-site even if an error is encountered

### Examples

1. Skip the interactive prompt by passing the root password.

    ```bash
    bench drop-site {site} --root-password {db-root-pass}
    ```

1. Skip taking a backup before site deletion.

    ```bash
    bench drop-site {site} --no-backup
    ```

1. Move the site's folder in a different folder instead of the standard
   `./archived_sites`.

    ```bash
    bench drop-site {site} --archived-sites-path {path/to/archive}
    ```
