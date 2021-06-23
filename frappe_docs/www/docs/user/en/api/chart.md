---
add_breadcrumbs: 1
title: Chart - API
image: /assets/frappe_io/images/frappe-framework-logo-with-padding.png
metatags:
 description: >
  API methods for creating and managing Charts in Frappe
---

# Chart API
Frappe provides easy-to-use and fully configurable SVG charts. You can learn about them in the Frappe Chart's [documentation]('https://frappe.io/charts').

## frappe.ui.RealtimeChart
`new frappe.ui.RealtimeChart(dom_element, event_name, max_label_count, data)`

Creates a new Realtime chart instance that adds real-time data update functionality on top of Frappe chart.

The `max_label_count` is the maximum number of labels allowed on the x-axis.

```js
// Empty data array 
const data = {
	datasets: [
		{
			name: "Some Data",
			values: []
		},
	]
}
// Realtime Chart initialization
let chart = new frappe.ui.RealtimeChart('#chart','test_event', 8, {
	title: 'My Realtime Chart',
	data: data,
	type: 'line',
	height: 250,
	colors: ['#7cd6fd', '#743ee2']
})
```

Here is the sample Python code to emit the data to the specified socket event.

The `label` key in `data` specifies the label to be appended in the Realtime Chart.

The `points` key in `data` specifies the array of points to be plotted on the Realtime Chart.

The number of values in the `points` array depends on the number of datasets.

The following python code can be executed as a cron job using [Hook](https://frappeframework.com/docs/user/en/python-api/hooks) functionality.

```py
data = {
	'label': 1,
	'points': [10]
}
frappe.publish_realtime('test_event', data)
```

Here is how the Realtime Chart would look like.
![RealtimeChart](/docs/assets/img/api/realtime-chart.png)

### frappe.ui.RealtimeChart.start_updating
`frappe.ui.RealtimeChart.start_updating()`

Start listening to the specified socket event and updates the Realtime Chart accordingly with the data received.

```js
frappe.ui.RealtimeChart.start_updating()
```
![RealtimeChart](/docs/assets/img/api/realtime-chart-demo.gif)
*frappe.ui.RealtimeChart.start_updating*

### frappe.ui.RealtimeChart.stop_updating
`frappe.ui.RealtimeChart.stop_updating()`

Stop listening to the socket event which was mentioned while initializing the Realtime Chart.

```js
frappe.ui.RealtimeChart.stop_updating()
```

### frappe.ui.RealtimeChart.update_chart
`frappe.ui.update_chart(label, data)`

Manually updates the Realtime Chart by appending the label and associated data to the end of the chart.

```js
frappe.ui.update_chart(2, [30])
```
