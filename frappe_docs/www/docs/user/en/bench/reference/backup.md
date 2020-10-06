# bench backup

## Usage

    bench backup [OPTIONS]

## Description

Backup sites specified. Executing the vanilla command will create a database
dump, compress it and save the data under the default backup location
`./sites/{site}/private/backups`.

In case a current site is set, simply running `bench backup` command will backup
that site.

## Options

  - `--backup-path` Set path for saving all the files in this operation
  - `--backup-path-db` Set path for saving database file
  - `--backup-path-conf` Set path for saving config file
  - `--backup-path-files` Set path for saving public file
  - `--backup-path-private-files` Set path for saving private file

## Flags

  - `--with-files` Take backup with private and public files
  - `--compress` Compress private and public files
  - `--verbose` Add verbosity


## Examples

1. Backing up with the site's private and public files.

   ```bash
   bench --site {site} backup --with-files
   ```

1. Compress the public and private files (if required). This saves the file
   under a `tgz` format instead of the default `tar` format.

   ```bash
   bench --site {site} backup --with-files --compress
   ```

1. Change the path where the files backed up will be saved.

    ```bash
   bench --site {site} backup --backup-path {backup_path}
    ```

1. Change the path for a specific backup file. For each unspecified option, the
   respective file will be saved in the default location.

   ```bash
   bench --site {site} backup --with-files
      --backup-path-conf {conf_path}
      --backup-path-db {db_path}
      --backup-path-files {files_path}
      --backup-path-private-files {private_path}
   ```

4. Add verbosity for the various stages managed internally via the Bench CLI.

    ```bash
   bench --site {site} backup --verbose
    ```