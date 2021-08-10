---
add_breadcrumbs: 1
title: DocType Actions and Links
image: /docs/assets/img/doctypes/action-link-config.png
metatags:
 description: >
  Actions allow you to add custom action buttons on the DocType, and Links help you to configure the dashboard for linked documents on the DocTye form.
---
## Actions and Links

> Added in Version 12.1

**Actions**

A DocType may also have `DocType Action` that will result in a button creation on the DocType View. Supported actions are:

1. **Server Action**: This will trigger a whitelisted server action.

**Links**

A standard navigation aid to the DocType view is the `Links` section on the dashboard. This helps the viewer identify at a glance which document types are connected to this DocType and can quickly create new related documents.

These links also support adding internal links (links to DocType in child tables) which can be configured as shown in the image below

### Configuration of Actions and Links

![Action and Link Configuration](/docs/assets/img/doctypes/action-link-config.png)

![Action and Link View](/docs/assets/img/doctypes/action-link.png)

![Internal Link](/docs/assets/img/doctypes/internal-link.png)

### Customization of Actions and Links

DocType Actions and Links are extensible via [Customize Form](customize)