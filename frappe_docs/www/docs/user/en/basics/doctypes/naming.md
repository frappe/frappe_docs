---
add_breadcrumbs: 1
title: Naming DocTypes
image: /docs/assets/img/doctypes/naming_field.png
metatags:
 description: >
  The many ways to create names (primary keys) for a DocType in Frappe
---
# Naming

All DocTypes in Frappe have a primary key called `name`. This is the unique id by
which you will be finding records and manipulating them using the ORM.
You can configure how `docs` should be named when a new document is created.
The following are the ways you can setup naming in a DocType.

## DocType `autoname`

You can set the name by the `autoname` property of the DocType.

#### 1. field:[fieldname]

The `doc` name is fetched from the value of the field provided.

<img src="/docs/assets/img/doctypes/naming_field.png" alt="naming by field" class="screenshot" style="width: 50%;">

#### 2. [series]

You can provide a naming pattern which will be incremented automatically. For e.g, if you set it as `PRE.#####`, the first document created will have the `name` as **PRE00001**, and second one will be **PRE00002** and so on.

<img src="/docs/assets/img/doctypes/naming_series_1.png" alt="naming by series" class="screenshot" style="width: 50%;">

#### 3. naming_series:

The naming pattern is derived from a field in the document. For e.g, you have a field `naming_series` in your document and it's value is set as `PRE.#####`, then that will be the pattern used for generating the name. This value can change per document. So the next document can have a different pattern.

> This works only if you have a field called `naming_series` in your DocType.

<img src="/docs/assets/img/doctypes/naming_series_2.png" alt="naming by series by field" class="screenshot" style="width: 50%;">

#### 4. Prompt

If you set it as **Prompt**, the name is required to be filled in manually.

<img src="/docs/assets/img/doctypes/naming-prompt.png" alt="naming by prompt" class="screenshot">

#### 5. Format

This is the most flexible one when it comes to configuring your naming schemes.

Let's say we have

```text
{%- raw -%}
EXAMPLE-{MM}-test-{fieldname1}-{fieldname2}-{#####}
{% endraw -%}
```

<img src="/docs/assets/img/doctypes/naming_format.png" alt="naming by format" class="screenshot" style="width: 50%;">

Everything outside the curly braces are plain text. Keywords inside the curly braces will be evaluated based on what they represent. In this case:

- **MM**: will be replaced by the current month
- **fieldname1**: will be replaced by the value of `fieldname1` in the document
- **#####**: will generate a series, which starts with `00001`

So the final name may look like `EXAMPLE-02-test-value1-value2-00001`.
You can find more information about available placeholders in [Placeholders for Naming Patterns](#placeholders-for-naming-patterns).

## By Controller Method

You can also define a name programatically by declaring an `autoname` method in the controller class. Example

```py
from frappe.model.naming import getseries

class Project(Document):
    def autoname(self):
        # select a project name based on customer
        prefix = `P-{}-`.format(self.customer)
        self.name = getseries(prefix, 3)
```

## By Document Naming Rule

> Introduced in v13

You can also create rules for naming DocTypes by creating **Document Naming Rule**

![Document Naming Rule](/docs/assets/img/doctypes/document-naming-rule.png)

You can create multiple Document Naming Rules for a particular doctype that can be applied selectively based on filters.

To define a Document Naming Rule you have to specify

1. Document Type it is being applied on
1. Priority of the rule (rules with higher priority will be applied first)
1. Conditions to apply the rule
1. Naming Rules

#### Numbering

You can define various numbering prefixes for the rule based on the conditions defined. This is done by setting a prefix and the number of digits for that rule.

For example if you are creating a separate numbering for high priority todos:

1. Prefix: todo-high-
1. Digits: 3

Will lead to numbering like `todo-high-001`, `todo-high-002` and so on.

## Priority of Naming

Naming priority is as follows

1. Document Naming Rule
1. `autoname` controller method.
1. `autoname` DocType property

## Special Rules

1. Child DocTypes do not follow naming rules
1. Amended documents have a suffix (`-1`, `-2` etc) to the original document

## Placeholders for Naming Patterns

Formatting patterns for naming series support the following placeholders:

| Placeholder | Replacement |
| --- | --- |
| `###` | autoincrementing number starting with `1`. The Number of digits equal the number of hashes |
| `fieldname1` | the value of `fieldname1` in the document |
| `DD` | the current day (zero-padded) |
| `MM` | the current month (zero-padded) |
| `YY` | the current year (two digits) |
| `YYYY` | the current year (four digits) |
| `FY` | the current fiscal year |
| `WW` | the current consecutive calendar week (ISO 8601 based but always starting with `00` or `01` at the beginning of a new year) |
| `timestamp` | the full notation of the current date and time (e.g. `2020-03-12 16:23:00`) |
