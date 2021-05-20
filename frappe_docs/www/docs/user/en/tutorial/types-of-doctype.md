---
title: Types of DocType - Frappe Framework Tutorial
description: There are different types of DocType available for different use cases
---

# Types of DocType

Let's learn about the different types of doctype in the framework by creating
more doctypes.

## Library Membership

Let's create another doctype: **Library Membership**. It will have the following
fields:

1. Library Member (Link, Mandatory)
2. Full Name (Data, Read Only)
3. From Date (Date)
4. To Date (Date)
5. Paid (Check)

It will have **Is Submittable** enabled. It will have Naming set as
**LMS.#####** and restricted to **Librarian** role. Also, the Title Field should
be set to `full_name` in the View Settings section.

![Library Membership DocType](/assets/frappe_docs/tutorial/library-membership-doctype.gif)

The Link field **Library Member** is similar to a Foreign Key column in other
frameworks. It will let you link the value to a record in another DocType. In
this case, it links to a record of Library Member DocType.

The Full Name field is a Read Only field that will be automatically **fetched
from** from the `full_name` field in the linked record **Library Member**.

Now, go to the Library Membership list and create a new document. You will see
that the Library Member field is a dropdown with existing records shown as
options. Select a Library Member and the Full Name will be fetched
automatically. Pretty cool, right?

### Linked DocTypes

Linked DocTypes are DocTypes that are linked in other doctypes as Link fields.
All doctypes are linkable. We can classify doctypes broadly into Master and
Transactional based on the type of data they store. Article, Library Member are
examples of Master data because they represent an entity (physical or virtual).
Library Membership is an example of doctype which stores transactional data.

### Submittable DocTypes

When you enable **Is Submittable** in a DocType is becomes a Submittable
DocType. A Submittable doctype can have 3 states: **Draft**, **Submitted** and
**Cancelled**. A document in the **Draft** state can be changed like any
document, however once it is in **Submitted** state, the value of any field in
the document cannot be changed. A Submitted document can be **Cancelled**, which
makes the document invalid. If you notice, an extra field was added in our
Library Membership doctype called **Amended From**. This field is used to keep
track of amendments in documents. Once a document is Cancelled, it can only be
amended, which means it can be duplicated and the cancelled document will be
linked to the new amended document via the **Amended From** field.

### Controller Validation for Membership

Now, let's write code that will make sure whenever a Library Membership is
created, there is no active membership for the Member.

**library_membership.py**

```py
from __future__ import unicode_literals

import frappe
from frappe.model.document import Document

class LibraryMembership(Document):
    # check before submitting this document
    def before_submit(self):
        exists = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                # check for submitted documents
                "docstatus": 1,
                # check if the membership's end date is later than this membership's start date
                "to_date": (">", self.from_date),
            },
        )
        if exists:
            frappe.throw("There is an active membership for this member")
```

We wrote our logic in the `before_submit` method which will run before we submit
the document. We used the `frappe.db.exists` method to check if a Library
Membership record exists with our provided filters. If it exists, we used
`frappe.throw` to stop the execution of program with a message that will show up
letting the user know the reason.

Now, try creating a Library Membership with an overlapping period and you should
see an error when you submit the document.

![Library Membership Validation](/assets/frappe_docs/tutorial/library-membership-validation.png)

## Library Transaction

Let's create a DocType to record an Issue or Return of an Article by a Library
Member who has an active membership.

This doctype will be called **Library Transaction** and will have the following
fields:

1. Article - Link to Article
2. Library Member - Link to Library Member
3. Type - Select with 2 options: Issue and Return
4. Date - Date of Transaction

This doctype will also be a Submittable doctype.

![Library Transaction Doctype](/assets/frappe_docs/tutorial/library-transaction-doctype.gif)

### Validation for Transaction

When an Article is issued, we should verify whether the Library Member has an
active membership. We should also check whether the Article is available for
Issue. Let's write the code for these validations.

**library_transaction.py**

```py
from __future__ import unicode_literals

import frappe
from frappe.model.document import Document

class LibraryTransaction(Document):
    def before_submit(self):
        if self.type == "Issue":
            self.validate_issue()
            # set the article status to be Issued
            article = frappe.get_doc("Article", self.article)
            article.status = "Issued"
            article.save()

        elif self.type == "Return":
            self.validate_return()
            # set the article status to be Available
            article = frappe.get_doc("Article", self.article)
            article.status = "Available"
            article.save()

    def validate_issue(self):
        self.validate_membership()
        article = frappe.get_doc("Article", self.article)
        # article cannot be issued if it is already issued
        if article.status == "Issued":
            frappe.throw("Article is already issued by another member")

    def validate_return(self):
        article = frappe.get_doc("Article", self.article)
        # article cannot be returned if it is not issued first
        if article.status == "Available":
            frappe.throw("Article cannot be returned without being issued first")

    def validate_membership(self):
        # check if a valid membership exist for this library member
        valid_membership = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": 1,
                "from_date": ("<", self.date),
                "to_date": (">", self.date),
            },
        )
        if not valid_membership:
            frappe.throw("The member does not have a valid membership")
```

There is a lot of code here but it should be self explanatory. There are inline
code comments for more explanation.

## Library Settings

Let's create the last doctype for our app: **Library Settings**. It will have
the following fields:

1. Loan Period - Will define the loan period in number of days
2. Maximum Number of Issued Articles - Restrict the maximum number of articles that can be issued by a single member

Since we don't need to have multiple records for these settings, we will enable
**Is Single** for this doctype.

![Library Settings Doctype](/assets/frappe_docs/tutorial/library-settings-doctype.gif)

After creating the doctype, click on **Go to Library Settings**, to go to the
form and set the values for **Loan Period** and **Maximum Number of Issued
Articles**.

### Single DocTypes

When a DocType has **Is Single** enabled, it will become a Single DocType. A
single doctype is similar to singleton records in other frameworks. It does not
create a new database table. Instead all single values are stored in a single
table called `tabSingles`. It is used usually for storing global settings.

### Validation for Library Settings

Let's make the change in Library Membership such that, the To Date automatically
computed based on the Loan Period and the From Date.

**library_membership.py**

```py
from __future__ import unicode_literals

import frappe
from frappe.model.document import Document

class LibraryMembership(Document):
    # check before submitting this document
    def before_submit(self):
        exists = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                # check for submitted documents
                "docstatus": 1,
                # check if the membership's end date is later than this membership's start date
                "to_date": (">", self.from_date),
            },
        )
        if exists:
            frappe.throw("There is an active membership for this member")

        # get loan period and compute to_date by adding loan_period to from_date
        loan_period = frappe.db.get_single_value("Library Settings", "loan_period")
        self.to_date = frappe.utils.add_days(self.from_date, loan_period or 30)
```

We have used `frappe.db.get_single_value` method to get the value of
`loan_period` from the Library Settings doctype.

Now, let's make the change in Library Transaction such that when an Article is
Issued, it checks whether the maximum limit is reached.

**library_transaction.py**

```py
from __future__ import unicode_literals

import frappe
from frappe.model.document import Document

class LibraryTransaction(Document):
    def before_submit(self):
        if self.type == "Issue":
            self.validate_issue()
            self.validate_maximum_limit()
            # set the article status to be Issued
            article = frappe.get_doc("Article", self.article)
            article.status = "Issued"
            article.save()

        elif self.type == "Return":
            self.validate_return()
            # set the article status to be Available
            article = frappe.get_doc("Article", self.article)
            article.status = "Available"
            article.save()

    def validate_issue(self):
        self.validate_membership()
        article = frappe.get_doc("Article", self.article)
        # article cannot be issued if it is already issued
        if article.status == "Issued":
            frappe.throw("Article is already issued by another member")

    def validate_return(self):
        article = frappe.get_doc("Article", self.article)
        # article cannot be returned if it is not issued first
        if article.status == "Available":
            frappe.throw("Article cannot be returned without being issued first")

    def validate_maximum_limit(self):
        max_articles = frappe.db.get_single_value("Library Settings", "max_articles")
        count = frappe.db.count(
            "Library Transaction",
            {"library_member": self.library_member, "type": "Issue", "docstatus": 1},
        )
        if count >= max_articles:
            frappe.throw("Maximum limit reached for issuing articles")

    def validate_membership(self):
        # check if a valid membership exist for this library member
        valid_membership = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": 1,
                "from_date": ("<", self.date),
                "to_date": (">", self.date),
            },
        )
        if not valid_membership:
            frappe.throw("The member does not have a valid membership")
```

We added a `validate_maximum_limit` method and used `frappe.db.count` to count
the number of transactions made by the member.

With that, we have covered the basics of doctype creation and types of doctype.
We also wrote business logic for various doctypes.

Good job making it this far. Let's keep going.

Next: [Form Scripts](/docs/user/en/tutorial/form-scripts)
