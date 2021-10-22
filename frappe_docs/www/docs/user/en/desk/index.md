---
add_breadcrumbs: 1
title: Desk
metatags:
 description: >
  Frappe Framework comes with a rich admin interface called the Desk. It reads
  meta-data from DocTypes and automatically builds list views, form views and
  report views
---

# Desk

Frappe Framework comes with a rich admin interface called the Desk. It reads meta-data
from DocTypes and automatically builds list views, form views, report views, etc
for your DocTypes. Desk is to be used by users of the type "System User".

In this section we will discuss what views are provided by Desk and how to configure them.

- [Workspace](#workspace)
- [Awesomebar](#awesomebar)
- [List View](#list-view)
- [Form View](#form-view)
- [Grid View](#grid-view)
- [Report Builder](#report-builder)
- [Tree View](#tree-view)
- [Calendar View](#calendar-view)
- [Gantt View](#gantt-view)
- [Kanban View](#kanban-view)

## Workspace

When you login, you're presented with the Desk, it features a persistent sidebar which can be sorted based on user's access.
Each sidebar item links to a page called Workspace.

A workspace represents a page which has combination of different blocks like `Shortcuts`, `Cards` & `Charts` etc. These blocks are fully customizable.

A workspace includes the following features:

<details>
<summary>Add New Page</summary>

![New Page](/docs/assets/img/desk/wspace-new-page.gif)

</details>

<details>
<summary>Create Child Page</summary>

![New Child Page](/docs/assets/img/desk/wspace-new-child-page.gif)

</details>

<details>
<summary>Add new blocks like `Header`, `Paragraph`, `Shortcuts`, `Cards`, `Charts`, `Spacer` etc</summary>

![Add New Blocks](/docs/assets/img/desk/wspace-add-new-blocks.gif)

</details>

<details>
<summary>Customize Blocks like Resize, Sort, Delete blocks</summary>

![Customize Blocks](/docs/assets/img/desk/wspace-customize-blocks.gif)

</details>

<details>
<summary>Sort the Sidebar Navigations</summary>

![Sort Sidebar](/docs/assets/img/desk/wspace-sort-sidebar.gif)

</details>

<details>
<summary>Public & Private Pages</summary>

![Public Private](/docs/assets/img/desk/wspace-public-private-pages.gif)

</details>

These features can be customized for each user directly from Desk.

## Awesomebar

Awesomebar helps you to navigate anywhere in the system, create new records, search in documents
and even perform math operations.

![Awesomebar](/docs/assets/img/desk/awesomebar.png)
*Navigating ToDo using Awesomebar*

## List View

List View is generated for all DocTypes except which are Child Tables and Singles.

The List view is packed with features. Some of them are:

1. Filters
1. Sorting
1. Paging
1. Filter by tags
1. Switch view to Report, Calendar, Gantt, Kanban, etc.

> Learn more about the [List API](/docs/user/en/api/list).

## Form View

Form view is used to view the records in a Form Layout. This view has a lot of
things going on. But the primary purpose of it is to view and edit records.
A document can be assigned to or shared with other users and it can have arbitrary
attachments and tags, all of which can be seen in the form sidebar.

![Form View](/docs/assets/img/doctypes/form-view.png)
*Form View*

When you scroll down to the bottom of the form, you will see the form timeline.
The form timeline shows emails, comments, edits and other events in a reverse
chronological order.

![Form View](/docs/assets/img/desk/form-timeline.png)
*Form Timeline*

> Learn more about the [Form API](/docs/user/en/api/form).

## Grid View

Grid view is used as a table in the form view to insert multiple records.
User can configure the columns of the grid view from the form.

![Grid View](/docs/assets/img/desk/configure_grid_columns.gif)


## Report Builder

Report Builder is a generic tool to customize and build tabular data from a DocType.
You can select columns to show, filters to apply, sort order and save this configuration
by giving your report a name. You can also show Child Table data and also filter
documents by their child records. You can also apply *Group By* on a column with
aggregation methods like Count, Sum and Average.

![Report Builder](/docs/assets/img/desk/report-builder.gif)
*Report Builder Features*

## Tree View

Frappe also supports tree structured records using the [Nested set model](https://en.wikipedia.org/wiki/Nested_set_model).
If a doctype is configured to be a tree structure, it can be viewed in the Tree view.

![Tree View](/docs/assets/img/desk/tree-view.png)
*Tree View*

## Calendar View

Calendar view can be configured for DocTypes with a start date and end date.

![Calendar View](/docs/assets/img/desk/calendar-view.png)
*Calendar View*

The configuration file should be named `{doctype}_calendar.js` and should exist in the
doctype directory.

Here is an example configuration file for calendar view for Event doctype, which must be set in the `event_calendar.js` file.

```js
frappe.views.calendar['Event'] = {
	field_map: {
		start: 'starts_on',
		end: 'ends_on',
		id: 'name',
		allDay: 'all_day',
		title: 'subject',
		status: 'event_type',
		color: 'color'
	},
	style_map: {
		Public: 'success',
		Private: 'info'
	},
	order_by: 'ends_on',
	get_events_method: 'frappe.desk.doctype.event.event.get_events'
}
```

## Gantt View

Gantt view uses the same configuration file as calendar, so every DocType that has a Calendar view has a Gantt view too.

In case certain settings need to be overridden for the Event DocType's Gantt view (for example the `order_by` field) the configuration can be set in the `event_calendar.js` file with the following content.

```js
frappe.views.calendar['Event'] = {
	field_map: {
		start: 'starts_on',
		end: 'ends_on',
		id: 'name',
		allDay: 'all_day',
		title: 'subject',
		status: 'event_type',
		color: 'color'
	},
	gantt: { // The values set here will override the values set in the object just for Gantt View
		order_by: 'starts_on',
	}
	style_map: {
		Public: 'success',
		Private: 'info'
	},
	order_by: 'starts_on',
	get_events_method: 'frappe.desk.doctype.event.event.get_events'
}
```

![Gantt View](/docs/assets/img/desk/gantt-view.png)
*Gantt View*

## Kanban View

Kanban view can be created for any DocType that has a Select field with options.
These options become the column names for the Kanban Board.

![Kanban View](/docs/assets/img/desk/kanban-view.png)
