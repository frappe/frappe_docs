<!-- add-breadcrumbs -->
# Frappe Commands

The Bench CLI utilizes the module`frappe.utils.bench_manager` to get the framework's as well as any other Application's commands present on the current bench directory.

This page is concerned only with the commands that exist in the Frappe project, that are a direct part of the CLI tool. These commands are defined under the [frappe/frappe](https://github.com/frappe/frappe).

> For references of any Bench commands, checkout [Bench Commands](/docs/user/en/bench/bench-commands).


## Commands

There are four major command types in Frappe inherited by Bench during command executions. They can be broadly grouped into

 - **[Scheduler Commands](#scheduler-commands)**

Commands to manage and review the scheduler and background jobs' statuses for the sites on your bench. Defined under mdule `frappe.commands.schedule`.

 - **[Site Commands](#site-commands)**

Set of commands used for site-specific operations. These are the most frequented commands to alter the state of your sites. These commands are accessed by using the `--site` option along with the site name (or "all") if you wish to run the operation *(if possible)* for all sites on the bench. These commands are defined under the module `frappe.commands.site`.

 - **[Frappe Util Commands](#frappe-util-commands)**

Frappe Utility commands that can be both, site or bench specific. These commands are defined under the module `frappe.commands.utils`.

 - **[Translation Commands](#translation-commands)**

Set of commands to manage translations for your multi-lingual deployments. These commands are defined under the module `frappe.commands.translate`.


### Scheduler Commands

 - **disable-scheduler**: Disable scheduler for specified sites.
 - **doctor**: Get diagnostic info about the status of the scheduler for all sites (if unspecified) and active workers on bench.
 - **enable-scheduler**: Enables scheduler for specified sites.
 - **purge-jobs**: Purge any pending periodic tasks, if the event option is not given, it will purge everything for the site.
 - **ready-for-migration**: Checks if a particular site is ready for migration by checking the existence of any pending background jobs.
 - **scheduler**: Change the state of the scheduler for any site from *pause*, *resume*, *disable* or *enable* state.
 - **set-maintenance-mode**: Set the value for maintenance mode in the config for specified sites.
 - **show-pending-jobs**: Get diagnostic info about background jobs.
 - **schedule**: Start the scheduler process for your bench. This process manages scheduler events defined in the `hooks.py` file. You can find this command mentioned in the bench config for your process manager too.
 - **worker**: Start worker process on your bench. The process this starts will manage all background jobs started on this bench.
 - **trigger-scheduler-event**: Trigger a specific scheduler event for the specified sites.

### Site Commands

 - **add-system-manager**: Add a new system manager to a site.
 - **add-to-hosts**: Add the specified site to the hosts file on your system.
 - **backup**: Take a backup of the specified sites.
 - **browse**: Opens the specified site on the browser if available.
 - **build-search-index**: Builds search index for Websites. Refer to [Full Text Search API Docs](/docs/user/en/api/full-text-search) for more information.
 - **disable-user**: Disable specified user on the site.
 - **drop-site**: Drop a particular site from the existing bench.
 - **install-app**: Install a particular Frappe Application to the site.
 - **list-apps**: List all the Frappe Applications installed on the specified site.
 - **migrate**: Run patches, sync schema and rebuild files, translations and indexes on a particular site.
 - **migrate-to**: Command to migrate your local site to a Frappe Hosting Provider's service.
 - **new-site**: Create a new site on the bench.
 - **ngrok**: Create a temporary URL and share it with anyone, and they can access your local site in their browser. Primarily built for aiding with the development of third party services.
 - **publish-realtime**: Publish realtime event from bench.
 - **reinstall**: Re-install all installed Applications from your specified site. This completely resets the site.
 - **reload-doc**: Reload schema for a particular *Doctype* and refresh the specified *Document*
 - **reload-doctype**: Reload schema for a particular *DocType*
 - **remove-from-installed-apps**: Removes the mentioned site from the site gloabl value of `installed_applications`.
 - **restore**: Restores the specified site with the specified restore files. The least requirement for performing a restore operation is the database file.
 - **run-patch**: Run a particular patch via the Frappe Patch Handler.
 - **set-admin-password**: Set the password for the Administrator user.
 - **set-last-active-for-user**: Set users last active date to current datetime.
 - **start-recording**: Starts the Frappe Recorder for the specified sites.
 - **stop-recording**: Terminates the Frappe Recorder for the specified sites.
 - **uninstall-app**: Uninstalls a particular Frappe Application from the site.
 - **use**: Sets the default site on the bench. Adds the site entry to the `currentsite.txt`.

### Frappe Util Commands

 - **add-to-email-queue**
 - **build**
 - **bulk-rename**
 - **clear-cache**
 - **clear-website-cache**
 - **console**
 - **data-import**
 - **destroy-all-sessions**
 - **execute**
 - **export-csv**
 - **export-doc**
 - **export-fixtures**
 - **export-json**
 - **import-csv**
 - **import-doc**
 - **jupyter**
 - **make-app**
 - **mariadb**
 - **postgres**
 - **rebuild-global-search**
 - **request**
 - **reset-perms**
 - **run-tests**
 - **run-ui-tests**
 - **serve**
 - **set-config**
 - **show-config**
 - **version**
 - **watch**

### Translation Commands

 - **build-message-files**: Build message files for translation.
 - **get-untranslated**: Get untranslated strings for language.
 - **import-translations**: Import translations from file in standard format.
 - **new-language**: Create lang-code.csv for given Frappe Application.
 - **update-translations**: Update translations for set language between files.
