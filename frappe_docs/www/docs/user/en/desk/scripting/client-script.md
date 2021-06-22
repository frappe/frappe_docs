---
add_breadcrumbs: 1
title: Client Script
metatags:
  description: >
    Client Scripts allow you to add JavaScript scripts on document events within
    the Desk, without creating Frappe Apps or deploys
---

# Client Script

A Client Script lets you dynamically define a custom Form Script that is
executed on a user's browser. If you choose to utilize non standard tools or
libraries, make sure to test them on different browsers to ensure compatibility
across your userbase.

> In Version 13, **Custom Script** was renamed to **Client Script**


## 1. How to create a Client Script

To create a Client Script

1. To add/edit Client Script, ensure your role is System Manager.
1. Type "New Client Script" in the awesomebar and hit enter to create a new Client Script document.
1. Select the DocType whose form you wish to customize.
1. Update the script using the preset template and save.
1. Head over to the DocType you've customized and see the changes.

## 2. Features

As compared to the restrictive nature of Server Scripts, everything is fair game
in Client Scripts. This is because the frontend APIs are secure by design. You
can utilize all of JavaScript APIs, along with Frappe's and any other JS or CSS
library you might've customized Desk with.

> The validations you add through Client Script will only be applied while using
> the standard form view accessible through the browser. In case you wish for
> those to be applied through API or
> [System Console](/docs/user/en/desk/scripting/system-console) access too, use [Server
> Scripts](/docs/user/en/desk/scripting/server-script).

## 3. Examples

### 3.1 Custom validation

Add additional form validations while creating or updating a document from
Frappe's standard form view.

```javascript
// additional validation on Task dates
frappe.ui.form.on('Task', 'validate', function(frm) {
    if (frm.doc.from_date < get_today()) {
        msgprint('You can not select past date in From Date');
    }
});
```

### 3.2 Fetching values on field updates

Fetch `local_tax_no` on changing value of the `customer` field.

```javascript
cur_frm.add_fetch('customer', 'local_tax_no', 'local_tax_no');
```

### 3.3 Customize field properties

Make a field `ibsn` read only after creating the document.

```javascript
// make a field read-only after saving
frappe.ui.form.on('Task',  {
    refresh: function(frm) {
        frm.set_df_property('ibsn', 'read_only', !frm.is_new());
    }
});
```

### 3.4 Customize field properties

Calculate incentives on a Sales Invoice form on save.

```javascript
// calculate sales incentive
frappe.ui.form.on('Sales Invoice',  {
    validate: function(frm) {
        // calculate incentives for each person on the deal
        total_incentive = 0
        $.each(frm.doc.sales_team,  function(i,  d) {
            // calculate incentive
            let incentive_percent = 2;
            if(frm.doc.base_grand_total > 400) incentive_percent = 4;
            // actual incentive
            d.incentives = flt(frm.doc.base_grand_total) * incentive_percent / 100;
            total_incentive += flt(d.incentives)
        });
        frm.doc.total_incentive = total_incentive;
    }
});
```