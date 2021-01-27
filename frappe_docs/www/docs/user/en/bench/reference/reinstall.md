---
title: Bench - bench reinstall
metatags:
 description: >
  The Bench CLI has a reinstall command to reset the state of a Frappe site.
---

# bench reinstall

## Usage

```bash
bench reinstall [OPTIONS]
```

## Description

Reinstall a site with the current apps. This will wipe all site data and start
afresh. This is considered a destructive operation, hence, contains an
interactive confirmation prompt by default.

> Note: This feature only exists for **MariaDB** sites currently. In the future,
> they may be extended for **PostgreSQL** support as well.

## Options

 - `--admin-password` Administrator Password for reinstalled site
 - `--mariadb-root-username` Root username for MariaDB
 - `--mariadb-root-password` Root password for MariaDB

## Flags

 - `--yes` Skip confirmation for reinstall


## Examples

1. Reinstall a site skipping the prompts for:
   - Confirmation for operation
   - MariaDB Root Password
   - Administrator Password

   ```bash
    bench reinstall {site} --yes
        --mariadb-root-password {db-pass}
        --admin-password {admin-pass}
   ```

1. Reinstall a site using an alternative user with *DBMS SUPER* privileges.

    ```bash
    bench reinstall
        --mariadb-root-username {db-user}
        --mariadb-root-password {db-pass}
    ```
