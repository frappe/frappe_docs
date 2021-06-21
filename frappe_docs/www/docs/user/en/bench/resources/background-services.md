<!-- add-breadcrumbs -->
# Background Services

Running an active Frappe environment requires the running of various system
level services and some Frappe processes.

The system level services, apart from your choice of database solutions and
Redis will depend on your deployment architecture and strategy. As for the
Frappe services, they are defined in the
[Procfile](/docs/user/en/bench/resources/bench-procfile) for development benches
and config/supervisor.conf for production benches.

System Processes
-----------------

These processes are handled at a system level and may have configs setup via
bench or some other Frappe deployment management tool.

    * MariaDB/PostgreSQL (Database)
    * Redis (Queues for background workers, and Caching)
    * NGINX (Reverse Proxy for production deployment)
    * Supervisor (Process Management for bench's non containerized production deployment)

Frappe Processes
----------------

These processes may be triggered manually or via a process manager. However,
they are defined in Frappe's codebase and are managed by the same.

* WSGI Server

The WSGI server is responsible for responding to the HTTP requests to frappe. In
a development scenario, `bench serve` or `bench start` start the Werkzeug server.
For production setups, Bench uses Gunicorn (automatically configured in supervisor).

* Redis Worker Processes

The worker processes execute background jobs in the Frappe system.

These processes are automatically started when `bench start` is run and for production
are configured in supervisor configuration.

* Scheduler Process

The Scheduler process schedules enqeueing of scheduled jobs in the Frappe
system. This process is automatically started when `bench start` is run and for
production are configured in supervisor configuration.
