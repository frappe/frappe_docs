<!-- add-breadcrumbs -->
# Making Users and Records

Now that we have created the models, we can directly start making records using Frappe Desk UI. You do not have to create views! Views in Frappe are automatically made based on the DocType properties.

### 4.1 Creating User

To make records, we will first create a User. To create a user, go to:

> Users and Permissions > User > New

Create a new User and set the email and first name. Then, click on edit in full page, go to **CHANGE PASSWORD** section and set a new password.

After the user is created, click on the user in the list view and go to **ROLES** section. Here, give the Librarian and Library Member Roles to this user

<img class="screenshot" alt="Add User Roles" src="/docs/assets/img/add_user_roles.png">

Now logout and login using the new user id and password.

### 4.2 Creating Desk Page

To add the documents and modules, you will have to create a desk page, you can do so from the **Desk Page**, doctype. Each page represents a module and includes the following:

1. A dashboard section for that particular module by default.
1. Shortcuts for commonly visited masters and pages
1. A masters section where all the reports and masters are grouped and listed

For the sake of simplicity, we will just add a single shortcut here. You can add more entries to the desk page if you want.

<img class="screenshot" alt="Desk Page" src="/docs/assets/img/desk-page-library.png">

After saving this, you can go to the desk home and reload the page. After reloading you will see a entry in the sidebar which points to your page as shown below.

<img class="screenshot" alt="Desk Page" src="/docs/assets/img/workspace-library.png">

First let us create a new Article:

<img class="screenshot" alt="New Article" src="/docs/assets/img/new_article_blank.png">

Here you will see that the DocType you had created has been rendered as a form. The validations and other rules will also apply as designed. Let us fill out one Article.

<img class="screenshot" alt="New Article" src="/docs/assets/img/new_article.png">

You can also add an image.

<img class="screenshot" alt="Attach Image" src="/docs/assets/img/attach_image.gif">

Now let us create a new member:

<img class="screenshot" alt="New Library Member" src="/docs/assets/img/new_member.png">

After this, let us create a new membership record for the member.

Here if you remember we had set the values of Member First Name and Member Last Name to be directly fetched from the Member records and as soon as you will select the member id, the names will be updated.

<img class="screenshot" alt="New Library Membership" src="/docs/assets/img/new_lib_membership.png">

As you can see that the date is formatted as year-month-day which is a system format. To set / change date, time and number formats, go to

> Settings > System Settings

You will find system settings under 'Core'. If you don't find system settings, log in through the administrator account.

<img class="screenshot" alt="System Settings" src="/docs/assets/img/system_settings.png">

{next}
