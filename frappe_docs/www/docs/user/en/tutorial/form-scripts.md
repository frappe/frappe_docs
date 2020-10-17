---
title: Form Scripts - Frappe Framework Tutorial
description: Form Scripts are client-side javascript code that enhances the UX of your Forms
---

# Form Scripts

Form Scripts are client-side javascript code that enhances the UX of your Forms.

Let's say you want to create a membership for a member. To do this, you have to
go to the Library Membership list, create a new form, select the member and
other fields and then save.

Similarly, when you want to create a transaction against a member, you have to
make a new Library Transaction form.

We can make this process easier. Write the following code in **library_member.js**

```js
frappe.ui.form.on('Library Member', {
    refresh: function(frm) {
        frm.add_custom_button('Create Membership', () => {
            frappe.new_doc('Library Membership', {
                library_member: frm.doc.name
            })
        })
        frm.add_custom_button('Create Transaction', () => {
            frappe.new_doc('Library Transaction', {
                library_member: frm.doc.name
            })
        })
    }
});
```

Now, refresh your page and go to the Library Member form. You should see two buttons
on the top right. Click on them to try them out. They will automatically set the
Library Member in each of those documents making the process easier.

![Library Member Form Actions](/assets/frappe_docs/tutorial/library-member-form-actions.png)

We have only scratched the surface here. You can do a lot more with Form
Scripts. Learn more about the API at [Form Scripts
API](/docs/user/en/api/form).

Next: [Portal Pages](/docs/user/en/tutorial/portal-pages)
