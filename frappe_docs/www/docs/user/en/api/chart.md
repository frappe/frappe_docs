---
add_breadcrumbs: 1
title: Chart - API
metatags:
  description: >
    API methods for creating and managing Charts in Frappe
---

# Chart API

Frappe provides easy-to-use and fully configurable SVG charts. You can learn about them in the Frappe Chart's [documentation](https://frappe.io/charts).

## frappe.ui.RealtimeChart

`new frappe.ui.RealtimeChart(dom_element, event_name, max_label_count, data)`

Creates a new RealtimeChart instance that adds real-time data update functionality on top of the Frappe Chart API.

`dom_element`: HTML Element to be used to render the Chart.
`event_name`: Socket event which will provide the data stream.
`max_label_count`: Maximum number of labels allowed on the x-axis.
`data`: Data for the chart to be initialized with.

```js
// Empty data array
const data = {
  datasets: [
    {
      name: "Some Data",
      values: [],
    },
  ],
};

// Realtime Chart initialization
let chart = new frappe.ui.RealtimeChart("#chart", "test_event", 8, {
  title: "My Realtime Chart",
  data: data,
  type: "line",
  height: 250,
  colors: ["#7cd6fd", "#743ee2"]
});
```

Here is the sample client code to render a chart over the specified socket event.

The following python code can be executed as a cron job using [Hook](https://frappeframework.com/docs/user/en/python-api/hooks) functionality.

```py
data = {
	'label': 1,
	'points': [10]
}
frappe.publish_realtime('test_event', data)
```

The `label` key specifies the label to be appended in the Chart. The `points` key specifies the array of points to be plotted. The number of values in the `points` array depends on the number of datasets.

This would produce a Chart like

![RealtimeChart](/docs/assets/img/api/realtime-chart.png)

### frappe.ui.RealtimeChart.start_updating

`frappe.ui.RealtimeChart.start_updating()`

Start listening to the specified socket event and update the RealtimeChart accordingly.

```js
frappe.ui.RealtimeChart.start_updating();
```

![RealtimeChart](/docs/assets/img/api/realtime-chart-demo.gif)
_frappe.ui.RealtimeChart.start_updating_

### frappe.ui.RealtimeChart.stop_updating

`frappe.ui.RealtimeChart.stop_updating()`

Stop listening to the socket event that RealtimeChart was initialized with.

```js
frappe.ui.RealtimeChart.stop_updating();
```

### frappe.ui.RealtimeChart.update_chart

`frappe.ui.update_chart(label, data)`

Manually updates RealtimeChart by appending the label and associated data to the end of the chart.

```js
frappe.ui.update_chart(2, [30]);
```
