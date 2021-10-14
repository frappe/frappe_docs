---
title: Bench - bench trim-tables
metatags:
  description: >
    Trim ghost columns in your DocType's tables
---

# bench trim-tables

## Usage

```bash
bench trim-tables [OPTIONS]
```

## Description

Docfields removed from a particular DocType may not be deleted from their
Database tables. This is by design to prevent premature data loss in Frappe.
This won't be problematic for the most part, however, at some point you may face
issues due to this lingering data.

Some benefits of regular table trimming are:

- Smaller backup sizes
- Reduced time taken to backup sites
- Reduced Site Database Usages
- Optimized queries in case of `SELECT *`
- Database is clean and doesn't have anything hidden or redundant data

This command modifies the schema of tables in your site's database. It will by default,
take a full backup of your entire database before modifying them. In case, these tables
 were modified errenously, you can restore your site to it's original state using
the [`restore`](/docs/user/en/bench/reference/restore) command.

## Options

 - `--format`, `-f` Set output format. Available options are JSON and TEXT.
   Defaults to TEXT.

## Flags

 - `--dry-run` Show what would be deleted
 - `--no-backup` Do not backup the site. This is not recommended since this is a
   destructive operation.

### Examples

1. There maybe a lot of lingering columns taking up the space. Perhaps you figured this out
    when you got an error that row size limit has reached while customizing your DocType. To
    be sure that there aren't any ghost columns, or old hidden fields taking up the space, you
    can be sure by running

    ```bash
    bench --site {site} trim-tables --dry-run
    ```
