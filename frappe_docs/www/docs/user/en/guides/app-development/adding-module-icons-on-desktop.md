<!-- add-breadcrumbs -->
# Adding Module Icons On Desktop

> For Frappe version 12 

To create a module icon for top level Module, you will have to edit the `config/desktop.py` file in your app.

In this file you will have to write the `get_data` method that will return a dict object with the module icon parameters

To create a dropdown list of action available on this module and actions available on page when you click on this module, you have to create a file `config/app_name.py` where `app_name` is replace by your application name  

### Example 1: Module Icon

	def get_data():
	return \
		[
			# Library Management
			{
				"module_name": "Library Management",
				"category": "Modules",
				"label": _("Library Management"),
				"color": "#589494",
				"reverse": 1,
				"icon": "octicon octicon-book",
				"type": "module",
				"description": "Library management"
			},
		]

### Example 2: List Icon and link into `config/app_name.py` (eg. `config/library_management.py`)

    def get_data():
        return [
            {
                "label": _("Library Management"),
                "icon": "octicon octicon-book",
                "items": [
                    {
                        "type": "doctype",
                        "name": "Article",
                        "label": _("Article"),
                        "description": _("Manage Books"),
                        "onboard": 1,
                    },
                    {
                        "type": "doctype",
                        "name": "Library Member",
                        "label": _("Library Member"),
                        "description": _("Manage Members"),
                        # Not displayed on dropdown list action but on page after click on module
                        "onboard": 0,
                    },
       			]
            },
        ]


Note: Module views are visible based on permissions.

<!-- markdown -->
