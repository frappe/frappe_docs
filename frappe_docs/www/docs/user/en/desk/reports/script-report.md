---
add_breadcrumbs: 1
title: Script Report
image: /docs/assets/img/script-report-example-1.png
metatags:
 description: >
  Anything that can't be achieved using Report Builder or Query Report can be
  achieved using Script Reports. These reports are built using Python scripts.
---

# Script Report

Anything that can't be achieved using Report Builder or Query Report can be
achieved using Script Reports. As the name suggests, these reports are built
using Python scripts. Since these reports give you unrestricted access via
Python scripts, they can only be created by Administrators. These reports are
meant to be written during development and be a part of your app.

> To create Script Reports you must enable Developer Mode.

To create a Script Report, type "new report" in the awesomebar and hit enter.

1. Set Report Type as "Script Report"
1. Set "Is Standard" as "Yes"
1. Select the Module in which you want to add this report
1. In the module folder (for example if it is Accounts in ERPnext the folder
   will be `erpnext/accounts/report/[report-name]`) you will see that templates
   for the report files will be created.
1. Write your python script in the generated `{report-name}.py` file.
1. You can add filters to your report by adding them to `{report-name}.js`

![New Script Report](/docs/assets/img/desk/script-report-example-1.png)
*New Script Report*

### Standard and Custom Reports

> Added in Version 12

Verson 12 onwards, you can make custom Query and Script reports in Frappe Framework. In custom reports, the script can be added directy in the Report itself and you can use the [Script API](/docs/user/en/desk/scripting/script-api) functions of Frappe Framework.

### Columns and Filters

> Added in Version 13

You can configure the columns and filters in the Report document. Here you can set the label, width, format (fieldtype) for the columns and filters.

Filters can be used as formatting variables in the query. For example a filters of type `customer` can be used as `%(customer)s` in the query.

![Standard Columns and Filters](/docs/assets/img/desk/report-columns-filters.png)

### Writing the script

#### Custom Report

In custom reports, you can use the [Script API](/docs/user/en/desk/scripting/script-api) and write the script directly in the Code section.

```python
return frappe.db.get_all('User', ['first_name', 'last_name'], filters = filters)
```

#### Standard Report

The generated `.py` file comes with a boilerplate for your report. There is one method named `execute` which takes `filters` and returns `columns` and `data`. You can use any combination of python modules and SQL queries to generate your report. The `execute` function looks like this

```python
from __future__ import unicode_literals
# import frappe

def execute(filters=None):
	columns, data = [], []
	return columns, data

```

The `execute` function is supposed to return the `columns` and the `data` to be shown in the report by default. A developer can optionally return a few paramters like `message`, `chart`, `report_summary`, `skip_total_rows`.

The following are the parameters that can be returned by the execute function

#### columns

This is a list of dictionaries. This holds all the columns that are to be displayed in the datatable in an order.

**Note:** You only need to return columns if you have not specified them in the Report

Example:
```python
columns = [
		{
			'fieldname': 'account',
			'label': _('Account'),
			'fieldtype': 'Link',
			'options': 'Account'
		},
		{
			'fieldname': 'currency',
			'label': _('Currency'),
			'fieldtype': 'Link',
			'options': 'Currency'
		},
		{
			'fieldname': 'balance',
			'label': _('Balance'),
			'fieldtype': 'Currency',
			'options': 'currency'
		}
	]
```

#### Results

This can be a list of lists or a list of dictionaries. This holds the data to be displayed in the report

Example:
```python
data = [
		{
			'account': 'Application of Funds (Assets)',
			'currency': 'INR',
			'balance': '15182212.738'
		},
		{
			'account': 'Current Assets - GTPL',
			'currency': 'INR',
			'balance': '17117932.738'
		},
		...
	]
```

#### chart

Contains the configuration for the default chart to be shown in the report.

#### report_summary

This is a list of dictionaries that stores the important values in the report and is shown separately in the top section on the UI.

Example:
```python
[{
		"value": profit,
		"indicator": "Green" if profit > 0 else "Red",
		"label": _("Total Profit This Year"),
		"datatype": "Currency",
		"currency": "INR"
}]
```

> Note: These arguments are supposed to be returned in the specific order as follows

Here is a script report from ERPNext: [Balance Sheet](https://github.com/frappe/erpnext/blob/develop/erpnext/accounts/report/balance_sheet/balance_sheet.py)

#### Adding filters

To add filters in your report define the fields and their fieldtypes in the
`{report-name}.js` file. The filter values will be available in the `execute`
method as a dict.

```js
frappe.query_reports['Balance Sheet'] = {
	filters: [
		{
			fieldname: 'company',
			label: __('Company'),
			fieldtype: 'Link',
			options: 'Company',
			default: frappe.defaults.get_user_default('company')
		},
		{
			fieldname: 'periodicity',
			label: __('Periodicity'),
			fieldtype: 'Select',
			options: [
				'Monthly',
				'Quarterly',
				'Half-Yearly',
				'Yearly'
			],
			default: 'Yearly',
			depends_on: 'eval:doc.company=="Gadget Technologies Pvt. Ltd."'
		}
	]
}
```

Similar to the `depends_on` property that controls the display of fields, in
Version 13 we have introduced `depends_on` for Script Report filters. This can
be used to determine whether the filter will be visible based on the value of the
condition in `depends_on`.

![Balance Sheet](/docs/assets/img/desk/script-report-example-2.png)
*Balance Sheet*

> *Protip*: To navigate directly to a Report of any of the above type, type its
> name in the awesomebar and hit enter.
