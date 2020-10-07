# bench restore

## Usage

    bench restore [OPTIONS] SQL_FILE_PATH

## Description

Bench CLI can be used to restore an existing site to a previous state. Using the
`bench restore` command, a site may be restored with the specific database and
file restores. Downgrades aren't supported for Frappe Sites; when a downgrade is
detected, an interactive prompt will pop up before the site restore begins.

The least requirement for performing a restore operation is having the database
file on your local filesystem. The specified path may be relative to the bench
or sites folder, although absolute paths often work best.

The specified database backup file may have the `sql.gz` or `sql` extension. For
public and private file backup archives, the default is `tar`, but since **Version
13**, compressed archives with the extension `tgz` are also supported.

> Note: As of this point, there's no way to restore only files using this
> command.

## Options

 - `--mariadb-root-username` Root username for MariaDB
 - `--mariadb-root-password` Root password for MariaDB
 - `--db-name` Database name for site in case it is a new one
 - `--admin-password` Administrator password for new site
 - `--install-app` Install app after installation
 - `--with-public-files` Restores the public files of the site, given path to
   its archive file
 - `--with-private-files` Restores the private files of the site, given path to
   its archive file

## Flags

 - `--force` Ignore the site downgrade warning, if applicable. This is **not
   recommended** unless you're fully aware of the consequences


## Examples

1. Restore a site with files

   ```bash
    bench --site {site} restore {path/to/database/file}
        --with-public-files {path/to/public/archive}
        --with-private-files {path/to/private/archive}
   ```

1. Bypass DBMS root interactive prompt by passing values in options

    ```bash
    bench --site {site} restore {path/to/database/file}
       --mariadb-root-username {db-user}
       --mariadb-root-password {db-pass}
    ```

1. Specify new app to install after site restore

    ```bash
    bench --site {site} restore {path/to/database/file}
       --install-app {app}
    ```

1. Specify custom database name for the restored site

    ```bash
    bench --site {site} restore {path/to/database/file}
       --db-name {custom-db-name}
    ```

1. Reset the admin password for the restored site

    ```bash
    bench --site {site} restore {path/to/database/file}
       --admin-password {admin-pass}
    ```
