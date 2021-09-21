---
add_breadcrumbs: 1
title: Field Types
metatags:
  description: >
    A Field type is a type of field you can give to a DocField.
---

# Field Types

There are variety of fieldtypes available in Frappe Framework. Each one has its own use case and can be used to input and store different types of data in a document. Fieldtypes are used to render components in desk as well as web forms.

<img alt="Field Types Dropdown Menu" class="screenshot" src="{{docs_base_url}}/assets/img/doctypes/fieldtypes.png">

#### Data

The data field will be a **simple text field**. It allows you to enter a value of up to 140 characters, making this the most generic field type.

You can enable validations for the following types of data:

1. Name
2. Email
3. Phone
4. URL

by setting the options to "Name", "Email", "Phone" or "URL" respectively.

<img alt="Data field types" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/data-field-1.png">

#### Link

Link field is connected to another master from where it fetches data. For example, in the Quotation master, the Customer is a Link field. To know more, [click here](https://erpnext.com/docs/user/manual/en/customize-erpnext/articles/creating-custom-link-field).

#### Dynamic Link

Dynamic Link field is one which can search and hold value of any document/doctype. [Click here](https://erpnext.com/docs/user/manual/en/customize-erpnext/articles/dynamic-link-fields) to learn how Dynamic Link Field functions.

#### Check

This will enable you to have a checkbox here. You can set the `Default` value to 1 and it will be checked by default.

<img alt="Check Field Preview" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/check-field-2.png">
<img alt="Check Field Edit" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/check-field-1.png">

#### Select

Select will be a drop-down field. You can add multiple results in the Option field, with each option on a new line.

<img alt="Check Field Edit" class="screenshot w-100" src="{{docs_base_url}}/assets/img/fieldtypes/select-field-2.png">
<img alt="Check Field Edit" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/select-field-1.png">

#### Table

A table will be a kind of Link field which renders another DocType within the current form. The DocType linked to this type of table field must be of type `Child Table`.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/child_table.png">

#### Attach

Attach field allows you to browse a field from the File Manager and attach the same herein.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/attach_fieldtype.png">


#### Attach Image

Attach Image is a field wherein you will be allowed to attach Images of the format jpeg, png, etc. This becomes the Image representing that particular DocType. For e.g., you would want the image of an Item in its DocType, you can choose your field to be an Attach Image Field.

#### Text Editor

Text Editor is a text field and renders a **WYSIWYG** editor for input. It has various text-formatting options.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/text_editor_field.png">


#### Date

This field will enable you to enter the Date in this field.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/date_fieldtype.png">


#### Date and Time

This field will give you a date and time picker. The current date and time (as provided by your computer) are set by default.

#### Barcode

In this field, you can specify the field as Barcode which will allow you to enter a Barcode number. Once you do that, the Barcode would automatically get generated against the number.

#### Button

This field lets you place a button in a document. This can be used to perform specific actions like publishing a blog post, triggering an action etc.

#### Code

This fieldtype can be used to take `code` as input. A code editor is rendered in the document form. Optionally, you can provide a langauge in the fieldtype options to enable syntax highlighting. For example, below is a `Code` type field with options set to `Python`:

You can enable basic syntax validations for following languages by setting "Option".

1. Python (for scripts)
2. PythonExpression (for simple one-line expressions that must evaluate to a value) E.g. Assignment Rule condition

Example of differences between `Python` and `PythonExpression`:

* `variable = 42` is a valid `Python` code but not a valid `PythonExpression` since the assignment doesn't evaluate to any value.
* `variable == 42` is both valid `Python` code and valid `PythonExpression` as the expresion can evaluate to some value.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/code_fieldtype.png">


#### Color

This will let the user input a color via a rendered color picker or directly input a hexadecimal color.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/color_fieldtype.png">


#### Column Break

This is a `'meta'` fieldtype that does not store any input data but can be used to indicate a column break in the document view or form.

For example,

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/column_break_fieldtype_1.png">


will result into:


<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/column_break_fieldtype_2.png">


#### Currency

Currency field holds numeric value, like Item Price, Amount, etc. Currency field can have value up to six decimal places. Also, you can have a currency symbol being shown for the currency field.

#### Float

Float field carries numeric value, up to nine decimal places.

#### Geolocation

Use Geolocation field to store GeoJSON <a href="https://tools.ietf.org/html/rfc7946#section-3.3">feature_collection</a>. Stores polygons, lines, and points. Internally it uses the following custom properties for identifying a circle.

#### HTML

This will render the content entered in `Options` as HTML in the document form or view page. Here is an example:


<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/html_fieldtype_1.png">

will result into:


<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/html_fieldtype_2.png">

#### Image

Image field will render an image file selected in another attach field.

For the Image field, under Option (in Doctype), a field name should be provided where the image file is attached. By referring to the value in that field, the image will be a reference in the Image field.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/image_fieldtype_1.png">

will result into:

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/image_fieldtype_2.png">

#### Int (Integer)

The integer field holds numeric value, without decimal place.

#### Small Text

Small Text field carries text content and has more character limit than the Data field.

#### Long Text

You can define your field to a Long Text Field when you would want to enter data with an unlimited character limit.

#### Text

This field type would allow you to add text in the field. The character limit in Small text, Long text and Text fields shall be determined based on the Relational Database Management System.

#### Markdown Editor

This field will allow you to add the text in markdown. This fieldtype also provides a `Preview` view of rendered HTML:

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/md_fieldtype_1.png">

when preview is clicked:


<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/md_fieldtype_2.png">

#### Password

The password field will have decoded value in it. This type of field can be used to store sensitive data like passwords, pass phrases, secret keys etc.

#### Percent

You can define the field as a Percentage field which in the background will be calculated as a percentage.

#### Rating

This field can be used to display an interactive star rating input. The user can give from 0 to 5 stars.

<img alt="Check Field Edit" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/rating-field.png">

#### Read Only

Read Only field will carry data fetched from another form which will be non-editable. You should set Read Only as field type if its source for value is predetermined.

#### Section Break

Section Break is used to divide the form into multiple sections. Any fields that follow (and before any other `Section Break`) a `Section Break` field will be part of this new section.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/section_break_fieldtype.png">

### Tab Break

Tab Break is used to divide the form into multiple tabs. Any field that follow till the next `Tab Break` will be the part of this new tab.

<img alt="Tabs" class="screenshot" src="{{docs_base_url}}/assets/img/fieldtypes/tabs.png">

**Note:** If the `fields` table of a DocType is not started with a Tab Break, a default Tab Break named `Details` will be used. This happens only if a DocType has atleast one `Tab Break` in the `fields` table.

#### Signature

You can define the field to be a Signature field wherein you can add the Digital Signature in this field. Read documentation for [Signature Field](https://erpnext.com/docs/user/manual/en/customize-erpnext/articles/signature-field) to know more.

#### Table MultiSelect

This is a combination of 'Link' type and 'Table' type fields. Instead of a child table with 'Add Row' button, in one field multiple values can be selected.

#### Time

This is a Time field where you can define the Time in the field.

#### Duration

You can use the Duration field if you want to define a timespan.

If you don't want to track duration in terms of days or seconds, you can enable "Hide Days" and "Hide Seconds" options respectively in your Form.

{next}
