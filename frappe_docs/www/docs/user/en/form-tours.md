---
add_breadcrumbs: 1
title: Form Tours
metatags:
 description: >
  Learn how to get your users onboarded to a Form with Form Tours
---

# Form Tours

Frappe provides an easy way to generate form tutorials for your complex doctype with very little configuration. 

![Form Tour](/docs/assets/img/form-tour-display.png)

## Creating a Form Tour

To create a Form Tour, type "new form tour" in awesomebar and hit enter.

1. Enter Title. For eg., 'Setting up a Worflow'
1. Select Reference DocType.
1. Add steps defining each fields.
1. Save the document.

![Workflow Tour](/docs/assets/img/workflow-form-tour.png)
*A Tour to explain Workflows*

## Configuration Options

### Steps

1. **Field**: A field from the selected doctype. This will be highlighted with a Title & Description.
1. **Title** & **Description**: To describe the field for its use, impact, and other hidden wirings of the field. 
1. **Position**: The position of the highlighting popover is decided by this field. There are multiple options to choose depending upon the position of the highlighted field. 
1. **Next Condition**: A code field which expects a valid JS condition which applies on the document. For eg., for a Task DocType Tour, we can check if task priority is set before going to the next condition by setting next condition as follows:

    ```js
    eval: doc.priority != ""
    ```

## Triggering the Tours

Once you are done describing the Form & its fields, you are now ready to trigger the tour by using Form API. You will have to fetch the steps & set it into a global `frappe` object for the Form API to access & drive the steps. 

You just new to get the steps from your Form Tour Record and set those steps into `frappe.tour` object with a `<doctype>` key and simply call `frm.show_tour()`

```js
const form_tour = await frappe.db.get_doc('Form Tour', 'Setting up a Workflow')
frappe.tour['Workflow'] = form_tour.steps;
frm.show_tour();
```
