---
add_breadcrumbs: 1
title: Virtual DocTypes
metatags:
 description: >
  Frappe allows additional DocTypes feature with custom data sources and DocType controller.
---

# Virtual DocTypes

Virtual DocType is a feature-extension for DocType which allows developers to create DocTypes with custom data sources and DocType controller. The purpose is to define custom DocTypes in the system without creating a table in the database, while utilizing the frontend, resource APIs, and roles and permissions from the framework.

These Virtual DocTypes function exactly like normal DocTypes in the frontend and are indistinguishable for the end-user, but gives more control to the developer over the DocType's data source. With this, the data source for a Virtual DocType can be anything: an external API, a secondary database, JSON or CSV files, etc. This enables the developers to plug-in database backends other than MariaDB and Postgres, and makes the Frappe Framework even more powerful!


## Creating a Virtual DocType

To create a Virtual DocType, just select the Virtual DocType checkbox while creating the DocType:

![Virtual DocType](/docs/assets/img/virtual_doctype.png)


#### Creating a Custom Controller
As an example, the following controller code uses a JSON file as the DocType datasource:

```python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class test_virtual(Document):
	def db_insert(self):
		d = self.get_valid_dict(convert_dates_to_str=True)
		with open("data_file.json", "w+") as read_file:
			json.dump(d, read_file)
	def db_update(self):
		d = self.get_valid_dict(convert_dates_to_str=True)
		with open("data_file.json", "w+") as read_file:
			json.dump(d, read_file)

	def get_list(self, args):
		with open("data_file.json", "r") as read_file:
			return [json.load(read_file)]

```
To integrate other datasources with the Virtual DocType, you will need to add controller methods defining the database access.


#### Outcome

The frontend for Virtual DocTypes remain unchanged

![Virtual DocType Form](/docs/assets/img/virtual_doctype_form.png)

All the /api/resource methods defined by the framework are compatible with Virtual DocTypes.

> Added in Version 13

