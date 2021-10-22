<!-- add-breadcrumbs -->


# How to Enable Backup Encryption
Files created during the backup process can be encrypted using an **Auto-generated key** by checking the **Encrypt Backup** option and the data can be saved under the default or provided location.

## System Requirements

For MacOS, ensure that [gnupg](https://formulae.brew.sh/formula/gnupg) is installed in the system. Use the following command to install gnupg:

```bash

brew install gnupg
```
Most Linux distributions already have GnuPG installed, and the current version will likely use GnuPG 2.0 by default.
## Encrypt Backup option

1. Under Settings tab go to `System settings`.

1. Inside the `Backups` section check the `Encrypt Backup` checkbox.

<img class="screenshot" alt="Encrypt Backup option(Enabled)" src="/docs/assets/img/encrypt-backup.png">

The system uses an auto-generated key supplied by the **Site config**. If no such key is found, **a new key is generated**. Any Administrator can later look it from the `https://{site}/app/backups` page.

It encrypts the  public and private files as well as the partial backup files.

## Backup Encryption Status

1. Encrypted backups are stored at the same location as the general backups `./sites/{site}/private/backups`.

1. Encrypted backups can be downloaded from the `https://{site}/app/backups`

1. Encrypted backups are differentiated using the `key icon`.

<img class="screenshot" alt="Encrypt Backup option(Enabled)" src="/docs/assets/img/backup-page.png">

## Backup Encryption Key

1. To get the backup encryption key go to the `./sites/{site}/private/backups`.

1. Click on the `Get Encrpytion key` and verify your password.

<img class="screenshot" alt="Encrypt Backup option(Enabled)" src="/docs/assets/img/backup-encryption-key.png">

Copy the key to restore the encrypted backup files.

## Restoring the Encrypted backup files

1. The `bench restore SQL_FILE_PATH` can be used to restore the files without `--backup-encryption-key` as it is automatically picked from the Site Config.

1. In case of an unsuccessful restoration due to a wrong key `--backup-encryption-key` can be used to provide the key to restore the files.

1. Usage:
	- For full backup files
	```bash
	bench --site {site} restore --backup-encryption-key {key} [OPTIONS]
	```
	- For partial backup files
	```bash
	bench --site {site} partial-restore --backup-encryption-key {key} [OPTIONS]
	```

<!-- markdown -->
