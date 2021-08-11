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

### Form Tour

1. **Is Standard**: To make a standard Form Tour which will be stored as JSON. Can only be set while developer mode is on.
1. **Save on Completion**: If checked, the last step of the Form Tour will prompt the user to save the document.

### Form Tour Steps

1. **Field**: A field from the selected doctype. This will be highlighted with a Title & Description.
1. **Title** & **Description**: To describe the field for its use, impact, and other hidden wirings of the field. 
1. **Position**: The position of the highlighting popover is decided by this field. There are multiple options to choose depending upon the position of the highlighted field. 
1. **Next Condition**: A code field which expects a valid JS condition which applies on the document. For eg., for a Task DocType Tour, we can check if task priority is set before going to the next condition by setting next condition as follows:

    ```js
    eval: doc.priority != ""
    ```
1. **Is Table Field**: To be checked if the field to be highlighted is under a child table.
1. **Parent Field**: Table field from the selected doctype. Only visible if **Is Table Field** is checked. Allows user to select a child table field.

## Triggering the Tours

Once you are done describing the Form & its fields, you are now ready to trigger the tour by using Form API. You just have to initialize the tour with appropriate `tour_name` and then simply start the tour with `frm.tour.start()`. 

```js
frappe.ui.form.on('Workflow', 'onload', () => {
  const tour_name = 'Setting up a Workflow';
  frm.tour
    .init({ tour_name })
    .then(() => frm.tour.start());
});
```
