<!-- add-breadcrumbs -->
# Site Config

Settings for `sites/{site}/site_config.json`

`site_config.json` stores global settings for a particular site and is present
in the site directory. Here is a list of properties you can set in
`site_config.json`.

Example:

    {
     "db_name": "test_frappe",
     "db_password": "test_frappe",
     "admin_password": "admin",
    }

### Mandatory Settings

- `db_type`: Database Type. Optionas include "mariadb" and "postgres".
- `db_name`: Database Name.
- `db_password`: Database password.
- `encryption_key`: encryption_key for stored non user passwords.

### Optional Settings

- `admin_password`: Default Password for "Administrator".
- `deny_multiple_logins`: Stop users from having more than one active session.
- `deny_multiple_sessions`: Deny Multiple Sessions.
- `disable_website_cache`: Disable Website Cache.
- `disable_session_cache`: Disable Session Cache.
- `disable_global_search`: Disable Global Search.
- `disable_error_snapshot`: Disable Error Snapshot.
- `encryption_key`: Key used to encrypt Passwords. This password is created
  automatically on a fresh site. Upon site restore, this key will have to be
  restored as well to be able to use existing passwords.
- `error_report_email`: Set the default Error Report Email.
- `ignore_csrf`: Ignore CSRF.
- `host_name`: Host Name
- `http_port`: Change the HTTP port for your Frappe Setup.
- `max_file_size`: Max file size allowed for uploads.
- `max_reports_per_user`: Maximum number of Auto Email Reports which can be
  created by a user, default is 3.
- `monitor`: If set, logs all requests and saves under `./logs/monitor.json.log`
- `mute_emails`: Stops email sending if true.
- `root_login`: Database root username.
- `root_password`: Database root password.
- `server_script_enabled`: Enable Server Script.
- `skip_setup_wizard`: Skip Setup Wizard.
- `socketio_port`: Specify Socket.IO.
- `webserver_port`: Generally used as fallback for conf key `http_port`.

### Remote Database Host Settings
- `db_host`: Database host if not `localhost`.

To connect to a remote database server using *SSL*, you must first configure the
database host to accept SSL connections. An example of how to do this is
available at [this tutorial by Digital
Ocean](https://www.digitalocean.com/community/tutorials/how-to-configure-ssl-tls-for-mysql-on-ubuntu-16-04).
After you do the configuration, set the following three options. All options
must be set for Frappe to attempt to connect using SSL.

- `db_port`: Specify port for your database.
- `db_ssl_ca`: Full path to the ca.pem file used for connecting to a database
  host using ssl. Example value is `"/etc/mysql/ssl/ca.pem"`.
- `db_ssl_cert`: Full path to the cert.pem file used for connecting to a
  database host using ssl. Example value is `"/etc/mysql/ssl/client-cert.pem"`.
- `db_ssl_key`: Full path to the key.pem file used for connecting to a database
  host using ssl. Example value is `"/etc/mysql/ssl/client-key.pem"`.
- `rds_db`: Grant certain privileges instead of all, while setting up a Site's
  database. Used in `db_manager.py`.



### Default Outgoing Email Settings

- `auto_email_id`: If set, this will be the default email for outgoing mails.
  `mail_login` is used as the second preference and "notifications@example.com"
  is used as fallback.
- `always_use_account_email_id_as_sender`: Use Account Email ID As Sender.
- `always_use_account_name_as_sender_name`  Use Account Name as Sender Name
- `email_sender_name`: Email Sender Name.
- `mail_server`: SMTP server hostname.
- `mail_port`: STMP port.
- `mail_login`: Login id for SMTP server.
- `mail_password`: Password for SMTP server.
- `pop_timeout`: POP Timeout.
- `use_ssl`: Connect via SSL.
- `use_tls`: Connect via TLS.

### Developer Settings

- `allow_tests`: Setting this allows tests to be run on this site.
- `developer_mode`: If developer mode is set, DocType changes are automatically
  updated in files.
- `disable_website_cache`: Don't cache website pages.
- `logging`: Utilise frappe.debug_log via frappe.log to enable different levels
  of logging. At level 2, shows queries and results run at every action.
- `disable_async`: Disables socket.io client; the client stops polling the
  socket.io server.
- `maintenance_mode`: Enable maintenance mode.

### Integrations

#### Sandbox

- `sandbox_api_key`: Sandbox API Key
- `sandbox_api_secret`: Sandbox API Secret
- `sandbox_api_password`: Sandbox API Password
- `sandbox_api_username`: Sandbox API Username
- `sandbox_publishable_key`: Sandbox Publishable Key
- `sandbox_signature`: Sandbox Signature

#### DropBox

- `dropbox_access_key`: Dropbox Access Key
- `dropbox_broker_site`: Dropbox Broker Site
- `dropbox_secret_key`: Dropbox Secret Key

#### PayPal

- `paypal_username`: Paypal Username
- `paypal_password`: PayPal Password
- `paypal_signature`: Paypal Signature

#### Others

- `google_analytics_id`: Google Analytics ID
- `mixpanel_id`: Mixpanel ID for MixPanel analytics on desk
- `converted_rupee_to_paisa`: Converted Rupee To Paisa for RazorPay Settings

### Others

- `robots_txt`: Path to robots.txt file to be rendered when going to
  frappe-site.com/robots.txt
- `pause_scheduler`: Pause Scheduler
- `disable_scheduler`: Disable Scheduler


- `local_infile`: Set Flag to allow Data from local infile for MySQL
  connections.

- `rate_limit`: Specify Rate Limits using `frappe.rate_limiter`.
- `data_import_batch_size`: Batch Size for Data Import

- `keep_backups_for_hours`: Utilized in `frappe.utils.new_backup` to pass
  through `frappe.utils.delete_temp_backups`. Retains the backup files depending
  on their age in hours.
- `install_apps`: Mention the list of apps to install at site `restore`,
  `reinstall` and on `new` creations.

- `restart_supervisor_on_update`
- `restart_systemd_on_update`
