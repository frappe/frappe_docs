---
title: Bench - bench partial-restore
metatags:
 description: >
  The Bench CLI has a command to restore partial backups onto your Frappe sites.
---

# bench partial-restore

## Usage

```bash
bench partial-restore [OPTIONS] SQL_FILE_PATH
```

## Description

You may want to restore only specific tables you've backed up to a site. You have
likely taken partial backups using the `--only`, `--exclude` options in `bench backup`.

The `partial-restore` command may be used to restore sites using partial backups. The
partial backup files may be gzip compressed or plain SQL files. In essence, you can
restore anything from SQL files using this command.

## Arguments

 - `SQL_FILE_PATH` Path to the database source file. The path may be relative from
the bench directory root, or the sites folder. It may also be an absolute path.

> To learn more about relative and absolute paths, on Wikipedia click [here](https://en.wikipedia.org/wiki/Path_(computing)#Absolute_and_relative_paths).

## Flags

 - `-v`, `--verbose` Add verbosity

## Examples

1. Restore with partial backups on a site.

    ```bash
    bench --site {site} partial-restore -v {/path/to/sql/file}
    ```