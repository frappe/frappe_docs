---
title: Installation
metatags:
 description: >
  Guide for installing Frappe Framework pre-requisites and the Bench CLI
add_breadcrumbs: 1
page_toc: 1
---

# Installation

> These steps assume you want to install Bench in developer mode. If you want
> install in production mode, follow the [latest recommended installation methods](https://github.com/frappe/bench#installation).

## System Requirements

This guide assumes you are using a personal computer, VPS or a bare-metal server. You also need to be on a *nix system, so any Linux Distribution and MacOS is supported. However, we officially support only the following distributions.

1. [MacOS `[Intel Processor]`](#macos-intel-processor)
2. [MacOS `[M1]`](#macos-m1)
3. [Debian / Ubuntu](#debian-ubuntu)
4. [Arch Linux](#arch-linux)
5. [Fedora](#fedora)
6. CentOS

> Learn more about the architecture [here](/docs/user/en/architecture).

## Pre-requisites

```
  Python 3.6+
  Node.js 14
  Redis 6                                       (caching and realtime updates)
  MariaDB 10.3.x / Postgres 9.5.x               (to run database driven apps)
  yarn 1.12+                                    (js dependency manager)
  pip 20+                                       (py dependency manager)
  wkhtmltopdf (version 0.12.5 with patched qt)  (for pdf generation)
  cron                                          (bench's scheduled jobs: automated certificate renewal, scheduled backups)
  NGINX                                         (proxying multitenant sites in production)
```

### MacOS `[Intel Processor]`

Install [Homebrew](https://brew.sh/). It makes it easy to install packages on macOS.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```


Now, you can easily install the required packages by running the following command

```bash
brew install python git redis mariadb@10.3
brew install --cask wkhtmltopdf
```

Now, edit the MariaDB configuration file.

```bash
nano /usr/local/etc/my.cnf
```

And add this configuration

```hljs
[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

[mysql]
default-character-set = utf8mb4
```

Now, just restart the mysql service and you are good to go.

```bash
brew services restart mariadb
```

**Install Node**

We recommend installing node using [nvm](https://github.com/nvm-sh/nvm)

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
```

After nvm is installed, you may have to close your terminal and open another one. Now run the following command to install node.

```bash
nvm install 14
```

Verify the installation, by running:

```bash
node -v
# v14.xx.x
```

Finally, install yarn using npm

```bash
npm install -g yarn
```

### MacOS `[M1]`

**Install [Rosetta](https://support.apple.com/en-in/HT211861)**

```bash 
/usr/sbin/softwareupdate --install-rosetta --agree-to-license
```

Make a “Rosetta” version of your terminal:

> Go to your “Applications” folder on Finder → right click Terminal in the “Utilities” folder → Duplicate → rename to “Rosetta Terminal” → Get Info → Open using > Rosetta

Install Homebrew in the Rosetta Terminal:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Install Required Packages**

> All the packages need to be installed in the Rosetta Terminal

```bash
brew install python git redis mariadb
brew install --cask wkhtmltopdf
```

Now, edit the MariaDB configuration file.

```bash 
nano /usr/local/etc/my.cnf
```

And add this configuration

```hljs
[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci
innodb-read-only-compressed=OFF

[mysql]
default-character-set = utf8mb4
```

Now, just restart the mysql service and you are good to go.

```bash
brew services restart mariadb
```

**Install Node**

We recommend installing node using [nvm](https://github.com/nvm-sh/nvm)

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
```

After nvm is installed, you may have to close your terminal and open another one. Now run the following command to install node.

```bash
nvm install 14
```

Verify the installation, by running:

```bash
node -v
# v14.xx.x
```

Finally, install yarn using npm

```bash
npm install -g yarn
```

### Debian / Ubuntu

Install `git`, `python`, and `redis`

```bash
apt install git python-dev redis-server
```

**Install MariaDB**

```bash
apt-get install software-properties-common
```

If you are on Ubuntu version older than 20.04, run this before installing MariaDB:

```bash
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://ftp.ubuntu-tw.org/mirror/mariadb/repo/10.3/ubuntu xenial main'
```

If you are on version Ubuntu 20.04, then MariaDB is available in default repo and you can directly run the below commands to install it:

```bash
apt-get update
apt-get install mariadb-server-10.3
```

During this installation you'll be prompted to set the MySQL root password. If you are not prompted, you'll have to initialize the MySQL server setup yourself. You can do that by running the command:

```bash
mysql_secure_installation
```

> Remember: only run it if you're not prompted the password during setup.

It is really important that you remember this password, since it'll be useful later on. You'll also need the MySQL database development files.

```bash
apt-get install libmysqlclient-dev
```

Now, edit the MariaDB configuration file.

```bash
nano /etc/mysql/my.cnf
```

And add this configuration

```hljs
[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

[mysql]
default-character-set = utf8mb4
```

Now, just restart the mysql service and you are good to go.

```bash
service mysql restart
```

**Install Node**

We recommend installing node using [nvm](https://github.com/creationix/nvm)

```bash
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
```

After nvm is installed, you may have to close your terminal and open another one. Now run the following command to install node.

```bash
nvm install 14
```

Verify the installation, by running:

```bash
node -v
# output
v14.17.2
```

Finally, install `yarn` using `npm`

```bash
npm install -g yarn
```

**Install wkhtmltopdf**

```
apt-get install xvfb libfontconfig wkhtmltopdf
```

### Arch Linux

Install packages using pacman

```bash
pacman -Syu
pacman -S mariadb redis python2-pip wkhtmltopdf git npm cronie nginx openssl
npm install -g yarn
```

Setup MariaDB

```bash
mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
systemctl start mariadb
mysql_secure_installation
```

Edit the MariaDB configuration file

```bash
nano /etc/mysql/my.cnf
```

Add the following configuration

```
[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

[mysql]
default-character-set = utf8mb4
```

Start services

```bash
systemctl start mariadb redis
```

If you don't have cron service enabled you would have to enable it.

```bash
systemctl enable cronie
```

### Fedora
Install required packages using dnf.

```bash
dnf install mariadb mariadb-server yarnpkg nodejs redis cronie
```

Setup MariaDB

```bash
systemctl start mariadb
mysql_secure_installation
```

Open MySQL configuration file

```bash
nano /etc/my.cnf
```
and add the following lines

```bash
[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

[mysql]
default-character-set = utf8mb4
```

Start MariaDB and Redis services

```bash
systemctl start mariadb redis
```

## Install Bench CLI

Install bench via pip3

```bash
pip3 install frappe-bench
```

Confirm the bench installation by checking version

```bash
bench --version

# output
5.2.1
```

Create your first bench folder.

```bash
cd ~
bench init frappe-bench
```

After the frappe-bench folder is created, change your directory to it and run this command

```bash
bench start
```

Congratulations, you have installed bench on to your system.
