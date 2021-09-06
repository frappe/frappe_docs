<!-- add-breadcrumbs -->
# Packages

> New in [Version 14](https://github.com/frappe/frappe/pull/14123)

Packages are light weight apps that you can directly build from the Framework UI. A Package is very much like an app and a collection of Module Defs.

You can make apps directly from the Framework UI (without using the command-line) using DocTypes, Server Scripts, Web Page etc. High quality apps can be build from the Framework directly. These apps can be bundled in a "Package" and then imported to other sites.

To add a module to a package, you have to set its "Package" property. This is available for "Custom" Module Defs

### Creating a Package

You can create a new Package by creating a Package object. You can set a README and a LICENSE. A Package is designed in a way that it can be pushed to a git repository.

Once you have created a package, you can add your custom Module Defs to that package.

![Package](/docs/assets/img/deployment/package.png)

### Making a Package Release

A **Package Release** will export all the package modules in the `[bench]/sites/[site]/packages` folder like an app, and then bundle the folder in a gzipped tarfile `[package]-[version].tar.gz`

You can then download the package release and import it in another site

![Package Release](/docs/assets/img/deployment/package-release.png)

### Importing a Package

You can create a **Package Import** and attach the exported package on a new site. If you check "Activate", the package will be extracted into the `[bench]/sites/[sitename]/packages` folder (existing files will be overwritten).

The system will then *migrate* this package to the database similar to how an app migration works. Files that have not been changed will be skipped unless the "Force" check is applied.

A log is created with the output.

![Package Import](/docs/assets/img/deployment/package-import.png)


