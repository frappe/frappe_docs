---
title: Install and Setup Bench - Frappe Framework Tutorial
description: Bench is the command line tool to manage Frappe apps and sites
---

# Install and Setup Bench

Bench is the command line tool to manage Frappe apps and sites.

---

## Installation

If you haven't installed Bench, follow the
[Installation](/docs/user/en/installation) guide.
After installation, you should be able to run commands that start with `bench`.

Run the following command to test your installation:

```bash
$ bench --version
5.1.0
```

## Create the frappe-bench directory

Let's create our project folder which will contain our apps and sites. Run the
following command:

```bash
bench init frappe-bench
```

This will create a directory named `frappe-bench` in your current working
directory. It will do the following:

1. Create a python virtual environment under `env` directory.
2. Fetch and install the `frappe` app as a python package.
3. Install node modules of `frappe`.
4. Build static assets.

## Directory Structure

```bash
.
├── Procfile
├── apps
│   └── frappe
├── config
│   ├── pids
│   ├── redis_cache.conf
│   ├── redis_queue.conf
│   └── redis_socketio.conf
├── env
│   ├── bin
│   ├── include
│   ├── lib
│   └── share
├── logs
│   ├── backup.log
│   └── bench.log
└── sites
    ├── apps.txt
    ├── assets
    └── common_site_config.json
```

- **env**: Python virtual environment
- **config**: Config files for Redis and Nginx
- **logs**: Log files for every process (web, worker)
- **sites:** Sites directory
    - **assets:** Static assets that served via Nginx in production
    - **apps.txt:** List of installed frappe apps
    - **common_site_config.json:** Site config that is available in all sites
- **apps:** Apps directory
    - **frappe:** The Frappe app directory
- **Procfile:** List of processes that run in development

## Start the Bench Server

Now that we have created our `frappe-bench` directory, we can start the Frappe
web server by running the following command:

```bash
$ cd frappe-bench
$ bench start
18:16:36 system           | redis_cache.1 started (pid=11231)
18:16:36 system           | redis_socketio.1 started (pid=11233)
18:16:36 system           | redis_queue.1 started (pid=11234)
18:16:36 system           | socketio.1 started (pid=11236)
18:16:36 system           | web.1 started (pid=11237)
18:16:36 system           | watch.1 started (pid=11240)
18:16:36 system           | schedule.1 started (pid=11241)
18:16:36 system           | worker_short.1 started (pid=11242)
18:16:36 redis_queue.1    | 11234:C 10 Jul 2020 18:16:36.320 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
18:16:36 redis_queue.1    | 11234:C 10 Jul 2020 18:16:36.320 # Redis version=6.0.5, bits=64, commit=00000000, modified=0, pid=11234, just started
18:16:36 redis_queue.1    | 11234:C 10 Jul 2020 18:16:36.320 # Configuration loaded
18:16:36 system           | worker_long.1 started (pid=11244)
18:16:36 redis_cache.1    | 11231:C 10 Jul 2020 18:16:36.318 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
18:16:36 redis_cache.1    | 11231:C 10 Jul 2020 18:16:36.318 # Redis version=6.0.5, bits=64, commit=00000000, modified=0, pid=11231, just started
18:16:36 redis_cache.1    | 11231:C 10 Jul 2020 18:16:36.318 # Configuration loaded
18:16:36 redis_cache.1    | 11231:M 10 Jul 2020 18:16:36.320 * Increased maximum number of open files to 10032 (it was originally set to 256).
18:16:36 redis_queue.1    | 11234:M 10 Jul 2020 18:16:36.325 * Increased maximum number of open files to 10032 (it was originally set to 256).
18:16:36 system           | worker_default.1 started (pid=11245)
18:16:36 redis_cache.1    | 11231:M 10 Jul 2020 18:16:36.337 * Running mode=standalone, port=13000.
18:16:36 redis_cache.1    | 11231:M 10 Jul 2020 18:16:36.337 # Server initialized
18:16:36 redis_cache.1    | 11231:M 10 Jul 2020 18:16:36.337 * Ready to accept connections
18:16:36 redis_queue.1    | 11234:M 10 Jul 2020 18:16:36.367 * Running mode=standalone, port=11000.
18:16:36 redis_queue.1    | 11234:M 10 Jul 2020 18:16:36.367 # Server initialized
18:16:36 redis_queue.1    | 11234:M 10 Jul 2020 18:16:36.367 * Ready to accept connections
18:16:36 redis_socketio.1 | 11233:C 10 Jul 2020 18:16:36.359 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
18:16:36 redis_socketio.1 | 11233:C 10 Jul 2020 18:16:36.359 # Redis version=6.0.5, bits=64, commit=00000000, modified=0, pid=11233, just started
18:16:36 redis_socketio.1 | 11233:C 10 Jul 2020 18:16:36.359 # Configuration loaded
18:16:36 redis_socketio.1 | 11233:M 10 Jul 2020 18:16:36.374 * Increased maximum number of open files to 10032 (it was originally set to 256).
18:16:36 redis_socketio.1 | 11233:M 10 Jul 2020 18:16:36.417 * Running mode=standalone, port=12000.
18:16:36 redis_socketio.1 | 11233:M 10 Jul 2020 18:16:36.418 # Server initialized
18:16:36 redis_socketio.1 | 11233:M 10 Jul 2020 18:16:36.418 * Ready to accept connections
18:16:37 socketio.1       | listening on *: 9000
18:16:41 web.1            |  * Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
18:16:41 web.1            |  * Restarting with fsevents reloader
18:16:41 watch.1          | yarn run v1.22.4
18:16:41 watch.1          | $ node rollup/watch.js
18:16:42 watch.1          |
18:16:42 watch.1          | Rollup Watcher Started
18:16:42 watch.1          |
18:16:42 watch.1          | Watching...
18:16:42 web.1            |  * Debugger is active!
18:16:42 web.1            |  * Debugger PIN: 100-672-925
18:16:43 watch.1          | Rebuilding frappe-web-b4.css
18:16:44 watch.1          | Rebuilding frappe-chat-web.css
18:16:44 watch.1          | Rebuilding chat.js
18:16:45 watch.1          | Rebuilding frappe-recorder.min.js
18:16:48 watch.1          | Rebuilding checkout.min.js
18:16:48 watch.1          | Rebuilding frappe-web.min.js
18:16:51 watch.1          | Rebuilding bootstrap-4-web.min.js
18:16:52 watch.1          | Rebuilding control.min.js
18:16:54 watch.1          | Rebuilding dialog.min.js
18:16:57 watch.1          | Rebuilding desk.min.css
18:16:57 watch.1          | Rebuilding frappe-rtl.css
18:16:58 watch.1          | Rebuilding printview.css
18:16:58 watch.1          | Rebuilding desk.min.js
18:17:04 watch.1          | Rebuilding form.min.css
18:17:04 watch.1          | Rebuilding form.min.js
18:17:07 watch.1          | Rebuilding list.min.css
18:17:07 watch.1          | Rebuilding list.min.js
18:17:09 watch.1          | Rebuilding report.min.css
18:17:09 watch.1          | Rebuilding report.min.js
18:17:12 watch.1          | Rebuilding web_form.min.js
18:17:12 watch.1          | Rebuilding web_form.css
18:17:13 watch.1          | Rebuilding email.css
18:17:13 watch.1          | Rebuilding social.min.js
18:17:13 watch.1          | Rebuilding barcode_scanner.min.js
18:17:15 watch.1          | Rebuilding data_import_tools.min.js
```

This will start several processes including a Python web server based on
Gunicorn, redis servers for caching, job queuing and socketio pub-sub,
background workers, node server for socketio and a node server for compiling
JS/CSS files.

The web server will start listening on the port `8000` but we don't have any
sites yet to serve. Our next step is to create our app and create a site that
will have this app installed.

Make sure not to close the terminal where `bench start` is running. To run bench
commands, create another terminal and cd into the `frappe-bench` directory.

Good job on following the tutorial so far!

Next: [Create an App](/docs/user/en/tutorial/create-an-app)
