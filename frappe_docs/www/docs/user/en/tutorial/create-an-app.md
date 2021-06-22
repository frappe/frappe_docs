---
title: Create an App - Frappe Framework Tutorial
description: Create a frappe app scaffold using the bench CLI
---

# Create an App

Create a frappe app scaffold using the bench CLI.

## Create app

Before we start, make sure you're in a bench directory. To confirm, run `bench find .`:

```bash
$ bench find .
/home/frappe/frappe-bench is a bench directory!
```

To create our Library Management app, run the `new-app` command:

```bash
$ bench new-app library_management
App Title (default: Library Management):
App Description: Library Management System
App Publisher: Faris Ansari
App Email: faris@example.com
App Icon (default 'octicon octicon-file-directory'):
App Color (default 'grey'):
App License (default 'MIT'):
'library_management' created at /home/frappe/frappe-bench/apps/library_management

Installing library_management
$ ./env/bin/pip install -q -U -e ./apps/library_management
$ bench build --app library_management
yarn run v1.22.4
$ FRAPPE_ENV=production node rollup/build.js --app library_management
Production mode
✔ Built js/moment-bundle.min.js
✔ Built js/libs.min.js
✨  Done in 1.95s.
```

You will be prompted with details of your app, fill them up and an app named
`library_management` will be created in the `apps` folder.

## App directory structure

Your app directory structure should look something like this:

```bash
apps/library_management
├── MANIFEST.in
├── README.md
├── library_management
│   ├── hooks.py
│   ├── library_management
│   │   └── __init__.py
│   ├── modules.txt
│   ├── patches.txt
│   ├── public
│   │   ├── css
│   │   └── js
│   ├── templates
│   │   ├── __init__.py
│   │   ├── includes
│   │   └── pages
│   │       └── __init__.py
│   └── www
├── requirements.txt
└── setup.py
```

- **library_management:** This directory will contain all the source code for your app
    - **public**: Store static files that will be served from Nginx in production
    - **templates**: Jinja templates used to render web views
    - **www**: Web pages that are served based on their directory path
    - **library\_management:** Default Module bootstrapped with app
    - **modules.txt:** List of modules defined in the app
    - **patches.txt**: Patch entries for database migrations
    - **hooks.py**: Hooks used to extend or intercept standard functionality provided by the framework
    - **requirements.txt:** List of Python packages that will be installed when you install this app

Next: [Create a Site](/docs/user/en/tutorial/create-a-site)
