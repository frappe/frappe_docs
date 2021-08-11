---
add_breadcrumbs: 1
title: Customizing DocTypes
metatags:
 description: >
  Frappe allows additional customization for DocTypes on top of standard settings. These customizations can be different for each site (tenant).
---

# Customizing DocTypes

If you are using the same application for multiple site (tenants), each site may want specific customization on top of the DocType. For example if you have a "Customer" DocType each user may want addition Custom Fields or naming or other configuration that would be specific to them.

To allow for site-specific customization, Frappe Framework has multiple approaches

1. Custom Field: A DocType that keeps track of site-specific fields.
1. Property Setter: This keeps track of specific properties that are overridden in DocType and its children.
1. Customize Form: A view that helps you easily customize DocTypes
1. [Client Script](/docs/user/en/desk/scripting/client-script): Additional client-side event handlers.
1. [Server Script](/docs/user/en/desk/scripting/server-script): Additional server-side business logic.
1. Custom DocPerm: Additional Permission (handled via Role Permission Manager)

## Customize Form

Customize Form is a view that helps you override properties of a DocType and add Custom Fields via a single view.

![Customize Form](/docs/assets/img/doctypes/customize-form.png)

When you change any properties of the DocType via Customize Form, it will not change the underlying DocType but add new custom objects to override those properties. This is done in a seamless manner.

#### Adding Custom Links and Actions

> Added in Version 13

You can also add / edit Links and Actions via Customize Form. These changes are saved in the same DocTypes (`DocType Link` and `DocType Action`) but with a `custom` property checked.

These addtional (custom) configurations are automatically applied when metadata is fetched via `frappe.get_meta`.