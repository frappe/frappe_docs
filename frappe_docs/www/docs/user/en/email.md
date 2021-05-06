---
add_breadcrumbs: 1
title: Email
image: /assets/frappe_io/images/frappe-framework-logo-with-padding.png
metatags:
 description: >
  Learn how optionally multiple IMAP folders in `Email Account` can be sycned
---

# Email Accounts
Frappe has the ability to check the emails of a email account and append them to a DocType.
With the opportunity to use the IMAP function, Frappe can check the mails of multiple IMAP
folder of the given mail account.

## Set Up
### IMAP
To set up multiple IMAP folder, it's required to check the `Enable Incoming`
and `Use IMAP`, then a table will appear with the pre-filled INBOX. The `Use IMAP`
flag can also be set up in the `Email Domain` which can be selected in the `Domain` field.

![Print Format Builder](/docs/assets/img/imap_setup.gif)
*IMAP example*

Each folder has its own option for the `append_to` so that this can be selected
separately for each folder. The `UIDVALIDITY` and the `UIDNEXT` are handled separately 
for each IMAP folder to mark the Mails correctly on the email server. 

### POP3
If you don't set up a IMAP mail account, then you'll see the `append_to` field in the
incoming settings. There you can select, where the mails should be imported.

![Print Format Builder](/docs/assets/img/pop_setup.gif)
*POP3 example*
