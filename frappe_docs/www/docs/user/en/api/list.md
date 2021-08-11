---
add_breadcrumbs: 1
title: List - API
metatags:
 description: >
  Everything you need to know about customizing List views and available API methods.
---

# List

The List View is generated for all DocTypes except Child Tables and Single DocTypes.

The List view is packed with features. Some of them are:

- Filters
- Sorting
- Paging
- Filter by tags
- Switch view to Report, Calendar, Gantt, Kanban, etc.

![List View](/docs/assets/img/list-view.png)
*List View*

## Standard List JS

To customize the List View you must have a `{doctype}_list.js` file in the doctype directory.
Below are all the options that can be customized.

For instance, if you want to customize the Note DocType, you'll have to create a file `note_list.js` with the following contents.

```js
frappe.listview_settings['Note'] = {
	// add fields to fetch
	add_fields: ['title', 'public'],
	// set default filters
	filters: [
		['public', '=', 1]
	],
	hide_name_column: true, // hide the last column which shows the `name`
	onload(listview) {
		// triggers once before the list is loaded
	},
	before_render() {
		// triggers before every render of list records
	},
	get_indicator(doc) {
		// customize indicator color
		if (doc.public) {
			return [__("Public"), "green", "public,=,Yes"];
		} else {
			return [__("Private"), "darkgrey", "public,=,No"];
		}
	},
	primary_action() {
		// triggers when the primary action is clicked
	},
	get_form_link(doc) {
		// override the form route for this doc
	},
	// add a custom button for each row
	button: {
		show(doc) {
			return doc.reference_name;
		},
		get_label() {
			return 'View';
		},
		get_description(doc) {
			return __('View {0}', [`${doc.reference_type} ${doc.reference_name}`])
		},
		action(doc) {
			frappe.set_route('Form', doc.reference_type, doc.reference_name);
		}
	},
	// format how a field value is shown
	formatters: {
		title(val) {
			return val.bold();
		},
		public(val) {
			return val ? 'Yes' : 'No';
		}
	}
}
```

## Custom List JS

You can also customize the list view by creating **Client Script** in the
system. You should write Client Scripts if the logic is specific to your site.
If you want to share List view customization across sites, you must include them
via Apps.

To create a new Client Script, go to

**Home > Customization > Client Script > New**

![New Client Script](/docs/assets/img/client-script-list.png)
*New Client Script for List*

The above customization will result in a list view that looks like this:

![List View Customized](/docs/assets/img/list-view-customized.png)
*List View Customized*
