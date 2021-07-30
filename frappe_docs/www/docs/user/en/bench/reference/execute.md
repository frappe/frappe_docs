---
title: Bench - bench execute
metatags:
 description: >
  Execute a method inside any app.
---

# bench execute

## Usage

```bash
bench execute [METHOD]
bench --site [SITE_NAME] execute [METHOD] --args [ARGS]
```

## Description

Executes given method.

## Options

 - `--args` Arguments for the method. Ex: --args "{'ITEM_A', 'WAREHOUSE_B'}"
 - `--site` Site to execute the given method
 
## Examples

1. Executes the enqueue_scheduler_events method

   ```bash
   bench execute frappe.utils.scheduler.enqueue_scheduler_events
   ```

1. Executes the method for the site

   ```bash
   bench --site {site} frappe.utils.scheduler.enqueue_scheduler_events
   ```

1. Executes the method with arguments (Parameters)

   ```bash
   bench --site site1.local execute erpnext.stock.stock_balance.repost_stock --args "{'ITEM_A', 'WAREHOUSE_B'}
   ```
