---
title: Bench - Bench Commands
metatags:
 description: >
  The Bench CLI has a set of commands to manage all Frappe Deployments.
---

# Bench Commands

This page is concerned only with the commands that exist in the bench project,
that are a direct part of the CLI tool. These commands are defined under the
[frappe/bench](https://github.com/frappe/bench).

> For references of any Framework commands, checkout [Frappe
> Commands](/docs/user/en/bench/frappe-commands).


## Using the bench CLI

```zsh
➜ bench
Usage: bench [OPTIONS] COMMAND [ARGS]...

  Bench manager for Frappe

Options:
  --version
  --help     Show this message and exit.

Commands:
  backup                   Backup single site
  backup-all-sites         Backup all sites in current bench
  config                   Change bench configuration
  disable-production       Disables production environment for the bench.
  download-translations    Download latest translations
  exclude-app              Exclude app from updating
  find                     Finds benches recursively from location
  get-app                  Clone an app from the internet or filesystem and...
```

Similarly, all available flags and options can be checked for commands
individually by executing them with the `--help` flag. The `init` command for
instance:

```zsh
➜ bench init --help
Usage: bench init [OPTIONS] PATH

  Initialize a new bench instance in the specified path

Options:
  --python TEXT                   Path to Python Executable.
  --ignore-exist                  Ignore if Bench instance exists.
  --apps_path TEXT                path to json files with apps to install
                                  after init
```


## Commands

Under Click's structure, `bench` is the main command group, under which there
are three main groups of commands in bench currently, namely


### General Commands

A set of commands that don't classify broadly in the other commands. Commands
such as `init`, `get-app`, `find` come under this category. These commands
belong directly to the bench group so they can be invoked directly prefixing
each with `bench` in your shell. Therefore, the usage for these commands is as

```zsh
➜ bench COMMAND [ARGS]...
```

#### Frequently Used

 - **init**: Initialize a new bench instance in the specified path. This sets up
   a complete bench folder with an `apps` folder which contains all the Frappe
   apps available in the current bench, `sites` folder that stores all site data
   separated by individual site folders, `config` folder that contains your
   redis, NGINX and supervisor configuration files. The `env` folder consists of
   all python dependencies of the current bench and installed Frappe
   applications have.
 - **restart**: Restart web, supervisor, systemd processes units. Used in the
   production setup.
 - **update**: If executed in a bench directory, without any flags will backup,
   pull, setup requirements, build, run patches and restart bench. Using
   specific flags will only do certain tasks instead of all.
 - **migrate-env**: Migrate Virtual Environment to desired Python version. This
   regenerates the `env` folder with the specified Python version.
 - **retry-upgrade**: Retry a failed upgrade
 - **disable-production**: Disables production environment for the bench.
 - **renew-lets-encrypt**: Renew Let's Encrypt certificate for site SSL.
 - **backup**: Backup single site data. Can be used to backup files as well.
 - **backup-all-sites**: Backup all sites in the current bench.

 - **get-app**: Download an app from the internet or filesystem and set it up in
   your bench. This clones the git repo of the Frappe project and installs it in
   the bench environment.
 - **remove-app**: Completely remove the specified Frappe App from the current
   bench and re-build assets if not installed on any site.
 - **exclude-app**: Exclude app from updating during a `bench update`
 - **include-app**: Include app for updating. All Frappe applications are
   included by default when installed.
 - **remote-set-url**: Set app remote url
 - **remote-reset-url**: Reset app remote url to frappe official
 - **remote-urls**: Show apps remote url
 - **switch-to-branch**: Switch all apps to specified branch, or specify apps
   separated by space
 - **switch-to-develop**: Switch Frappe and ERPNext to develop branch

#### Advanced Setup-based

 - **set-nginx-port**: Set NGINX port for site
 - **set-ssl-certificate**: Set SSL certificate path for site
 - **set-ssl-key**: Set SSL certificate private key path for site
 - **set-url-root**: Set URL root for site
 - **set-mariadb-host**: Set MariaDB host for bench
 - **set-redis-cache-host**: Set Redis cache host for bench
 - **set-redis-queue-host**: Set Redis queue host for bench
 - **set-redis-socketio-host**: Set Redis socketio host for bench
 - **use**: Set default site for bench
 - **download-translations**: Download latest translations

#### Development

 - **start**: Start Frappe development processes. Uses the Procfile to start the
   Frappe development environment.
 - **src**: Prints bench source folder path, which can be used to cd into the
   bench installation repository by `cd $(bench src)`.
 - **find**: Finds benches recursively from location or specified path.
 - **pip**: Use the current bench's pip to manage Python packages. For help
   about pip usage: `bench pip help [COMMAND]` or `bench pip [COMMAND] -h`.
 - **new-app**: Create a new Frappe application under apps folder.

#### Release bench
 - **release**: Create a release of a Frappe application
 - **prepare-beta-release**: Prepare major beta release from develop branch


### Setup Commands

This command group consists of commands used to manipulate the requirements and
the environment required by your Frappe environment. The setup commands used for
setting up the Frappe environment in the context of the current bench need to be
executed using `bench setup` as the prefix. So, the general usage of these
commands is as

```zsh
➜ bench setup COMMAND [ARGS]...
```

 - **sudoers**: Add commands to sudoers list for allowing bench commands
   execution without root password

 - **env**: Setup Python's virtual environment for your bench. This sets up a
   `env` folder under the root of the bench directory.
 - **redis**: Generates configuration for Redis
 - **fonts**: Add Frappe fonts to system
 - **config**: Generate or over-write `sites/common_site_config.json`
 - **backups**: Add cronjob for bench backups
 - **socketio**: Setup node dependencies for socketio server
 - **requirements**: Setup Python and Node dependencies

 - **manager**: Setup `bench-manager.local` site with the [Bench
   Manager](https://github.com/frappe/bench_manager) app, a GUI for bench
   installed on it.

 - **procfile**: Generate Procfile for bench start

 - **production**: Setup a Frappe production environment for the specified user.
   This installs ansible, NGINX, supervisor, fail2ban and generates the
   respective configuration files.
 - **nginx**: Generate configuration files for NGINX
 - **fail2ban**: Setup fail2ban, an intrusion prevention software framework that
   protects computer servers from brute-force attacks
 - **systemd**: Generate configuration for systemd
 - **firewall**: Setup firewall for system
 - **ssh-port**: Set SSH Port for system
 - **reload-nginx**: Checks NGINX config file and reloads service
 - **supervisor**: Generate configuration for supervisor
 - **lets-encrypt**: Setup lets-encrypt SSL for site
 - **wildcard-ssl**: Setup wildcard SSL certificate for multi-tenant bench

 - **add-domain**: Add a custom domain to a particular site
 - **remove-domain**: Remove a custom domain from a site
 - **sync-domains**: Check if there is a change in domains. If yes, updates the
   domains list.

 - **role**: Install dependencies via ansible roles


### Config Commands

The config command group deals with making changes in the current bench (not the
CLI tool) configuration. The config group commands are used for manipulating
configurations in the current bench context. The usage for these commands is as

```zsh
➜ bench config COMMAND [ARGS]...
```
 - **set-common-config**: Set value in common config with parameters -c, configs
   or --config
 - **remove-common-config**: Remove specific keys from current bench's common
   config
 - **update\_bench\_on\_update**: Enable/Disable bench updates on running bench
   update
 - **restart\_supervisor\_on\_update**: Enable/Disable auto restart of
   supervisor processes
 - **restart\_systemd\_on\_update**: Enable/Disable auto restart of systemd
   units
 - **dns\_multitenant**: Enable/Disable bench multitenancy on running bench
   update
 - **serve\_default\_site**: Configure nginx to serve the default site on port
   80
 - **http\_timeout**: Set HTTP timeout


### Install Commands

The install command group deals with commands used to install system
dependencies for setting up a Frappe environment. The usage for these commands
is as

```zsh
    bench install COMMAND [ARGS]...
```

 - **prerequisites**: Installs pre-requisite libraries, essential tools like
   b2zip, htop, screen, vim, x11-fonts, python libs, cups and Redis
 - **nodejs**: Installs Node.js v8
 - **nginx**: Installs NGINX. If user is specified, sudoers is setup for that
   user
 - **packer**: Installs Oracle virtualbox and packer 1.2.1
 - **psutil**: Installs psutil via pip
 - **mariadb**: Install and setup MariaDB of specified version and root password
 - **wkhtmltopdf**: Installs wkhtmltopdf v0.12.3 for linux
 - **supervisor**: Installs supervisor. If user is specified, sudoers is setup
   for that user
 - **fail2ban**: Install fail2ban, an intrusion prevention software framework
   that protects computer servers from brute-force attacks
 - **virtualbox**: Installs virtualbox.



## General Usage

This section covers the general usage of the Bench CLI, enough to get you
familiar with the basic usage.

### Create a new bench

  The init command will create a bench directory with the frappe framework
  installed. It will be setup for periodic backups.

```zsh
➜ bench init frappe-bench && cd frappe-bench
```

### Add a site

  Frappe apps are run by frappe sites and you will have to create at least one
  site. The new-site command allows you to do that.

```zsh
➜ bench new-site site1.local
```

### Add apps

  The get-app command gets remote frappe apps from a remote git repository and
  installs them. Example: [erpnext](https://github.com/frappe/erpnext)

```zsh
➜ bench get-app erpnext https://github.com/frappe/erpnext
```

### Install apps

  To install an app on your new site, use the bench `install-app` command.

```zsh
➜ bench --site site1.local install-app erpnext
```

### Start bench

  To start using the bench, use the `bench start` command

```zsh
➜ bench start
```

  To login to Frappe / ERPNext, open your browser and go to
  `[your-external-ip]:8000`, probably `localhost:8000`

  The default username is "Administrator" and password is what you set when you
  created the new site.

### Update bench

  Update all apps and sites from your bench directory. This operation performs
  backups, sets up requirements, build asstes, runs migrations and restarts your
  process manager for you.

```zsh
➜ bench update
```

### Update Bench config

  To update the common site config for your bench, you can use the
  `set-common-config` and `remove-common-config` commands under the config
  command group. To learn more about Frappe Site configurations available,
  checkout the Site and Bench Config
  [docs](/docs/user/en/guides/basics/site_config).

  To add or update an existing config key, you can run something like

```zsh
➜ bench config set-common-config -c enable_frappe_logger true
```

  To remove an existing config key, you can run something like

```zsh
➜ bench config remove-common-config enable_frappe_logger
```

## Bench Manager

For a UI based approach to managing your deployments, checkout [Bench
Manager](https://github.com/frappe/bench_manager).

```zsh
➜ bench setup manager
```

You can set it up easily on any existing bench by running the above command.


### What this does?

1. Create a new site `bench-manager.local`
1. Get the `bench_manager` app
1. Install the `Bench Manager` app on the site `bench-manager.local`

You can use this site to manage your bench operations through
*bench-manager.local*'s `/desk` view.
