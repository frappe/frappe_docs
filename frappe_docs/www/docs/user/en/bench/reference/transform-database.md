---
title: Bench - bench transform-database
metatags:
 description: >
  Change tables' internal settings changing engine and row formats
---

# bench transform-database

> This command is added in **Version 14**, and supports only **MariaDB**

## Usage

```bash
bench transform-database [OPTIONS] table
```

## Description

The `transform-database` command allows you to manage the settings of your site's tables. At this point, you can switch engines and row_format settings for select tables on your site database.

> MariaDB 10.6 deprecated the COMPRESSED ROW_FORMAT which was Frappe's default option for a very long time. This command was added to handle upgrades to later versions of MariaDB. For more information on this, refer to the [PR](https://github.com/frappe/frappe/pull/13954).


## Options

 - `--table` Comma separated name of tables to convert. To convert all tables, pass 'all' **[required]**
 - `--engine` Choice of storage engine for said table(s). Options available are *InnoDB* and *MyISAM*.
 - `--row_format` Set *ROW_FORMAT* parameter for said table(s). Options available are *DYNAMIC*, *COMPACT*, *REDUNDANT*, *COMPRESSED*.

## Flags

 - `failfast` Exit on first failure occurred

### Examples

1. Consider a scenario where you'd want to change the engine of a table *"tabAccess Record"* to `MyISAM`. You may want to do this if it's a log table that's dealing with huge volumes of writes and very little reads.

    ```bash
    bench --site {site} transform-database --table 'tabAccess Record' --engine 'MyISAM'
    ```

1. You've upgraded MariaDB on your current server from 10.3 to 10.7. You're going to have to convert all the tables that used the COMPRESSED row_format to the new default, ie `DYNAMIC`. You'd want to run the following command.

    ```bash
    bench --site {site} transform-database --table 'all' --row_format 'DYNAMIC'
    ```