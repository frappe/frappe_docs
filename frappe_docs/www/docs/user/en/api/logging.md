---
add_breadcrumbs: 1
title: Frappe Logging - API
metatags:
  description: >
    API method for creating and accessing logging objects in Frappe
---

# Logging

Logging is a means of tracking events that happen when some software runs. Under the bench architecture, with multitenancy, it might get really complicated really fast to track down and eliminate any uncertainties. You may wan't to log events along with circumstantial, variable data.

Frappe implements Python's [logging module](https://docs.python.org/3/howto/logging.html) to maintain bench and site wise logs. `Version 13` uses Log Rotation to maintain the last 20 files along with the current running of _100kB_ each for the _out of the box_ log files.

## frappe.log_level

Maintains the log level of Frappe processes. To learn more about logging levels, you can check out Python's [documentation](https://docs.python.org/dev/library/logging.html#logging.Logger.setLevel).

## frappe.utils.logger.set\_log\_level

`frappe.utils.logger.set_log_level(level)` can be used to set the log level and regenerate the loggers dynamically.

## frappe.loggers

`frappe.loggers` maintains a `dict` of active loggers in your process. The key is the name of the logger, typically "{module}-{site}" and the value holds the Logger instance.

A web worker may have `frappe.loggers` such as the following if [docs.erpnext.com](https://docs.erpnext.com/), [frappeframework.com](https://frappeframework.com) and [getanerp.com](https://getanerp.com) are the sites on the bench.

```python
{
    "frappe.web-docs.erpnext.com": <Logger frappe.web-docs.erpnext.com (DEBUG)>,
    "frappe.web-frappeframework.com": <Logger frappe.web-frappeframework.com (DEBUG)>,
    "frappe.web-getanerp.com": <Logger frappe.web-getanerp.com (DEBUG)>
}
```

## frappe.logger

`frappe.logger(module, with_more_info, allow_site, filter, max_size, file_count)`

Returns a `logging.Logger` object with Site and Bench level logging capabilities. If logger doesn't already exist, creates and updates`frappe.loggers`.

Arguments:

- **module**: Name of your logger and consequently your log file.
- **with_more_info**: Will log the `Form Dict` as additional information, typically useful for requests.
- **allow_site**: Pass site name to explicitly log under it's logs. If `True` and unspecified, guesses which site the logs would be saved under.
- **filter**: Add a filter function for your logger.
- **max_size**: Max file size of each log file in bytes.
- **file_count**: Max count of log files to be retained via Log Rotation.

### Usage

```python
frappe.logger("frappe.web").debug({
    "site": "frappeframework.com",
    "remote_addr": "192.148.1.7",
    "base_url": "https://frappeframework.com/docs/user/en/api/logging",
    "full_path": "/docs/user/en/api/logging",
    "method": "POST",
    "scheme": "https",
    "http_status_code": 200
})
```

```log
2020-07-31 16:06:55,067 DEBUG frappe.web {'site': 'frappeframework.com', 'remote_addr': '192.148.1.7', 'base_url': 'https://frappeframework.com/docs/user/en/api/logging', 'full_path': '/docs/user/en/api/logging', 'method': 'POST', 'scheme': 'https', 'http_status_code': 200}
```

The above entry would be logged under `./logs/frappe.web.log` and `./sites/frappeframework.com/logs/frappe.web.log` files.

> Usage specified as implemented in [app.py#L102-L110](https://github.com/frappe/frappe/blob/fe22595e854e3fb3fa4dbcbd6d9dacdf94e73462/frappe/app.py#L102-L110)

### Example

Consider a scenario where you've written an API for updating a counter with the value sent by the user and return the updated value. Now you want to log information in the API, to make sure it's working as expected. So, you create a logger `api` to track events for the same.

```python
frappe.utils.logger.set_log_level("DEBUG")
logger = frappe.logger("api", allow_site=True, file_count=50)


@frappe.whitelist()
def update(value):
    user = frappe.session.user
    logger.info(f"{user} accessed counter_app.update with value={value}")

    current_value = frappe.get_single_value("Value", "counter")
    updated_value = current_value + value
    logger.debug(f"{current_value} + {value} = {updated_value}")
    frappe.db.set_value("Value", "Value", "counter", updated_value)
    logger.info(f"{user} updated value to {value}")

    return updated_value

```

API calls made to this endpoint will now start getting logged in your `api.log` as follows

```log
2020-07-31 16:06:55,067 INFO api gavin@frappe.io accessed counter_app.update with value 100
2020-07-31 16:06:55,067 DEBUG api 1000 + 100 = 1100
2020-07-31 16:06:55,068 INFO api gavin@frappe.io updated value to 1100
```

> Learn more about Logging in Frappe [here](/docs/user/en/logging)
