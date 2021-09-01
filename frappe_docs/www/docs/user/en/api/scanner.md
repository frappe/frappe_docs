---
add_breadcrumbs: 1
title: Scanner - API
metatags:
  description: >
    API for enabling scanner inputs in Frappe
---

# Scanner API

Frappe uses the open-source library [Html5-QRCode](https://github.com/mebjas/html5-qrcode) to provide a flexible way to handle inputs like Barcodes, QRCodes, etc. using the device camera.



## frappe.ui.Scanner

```
new frappe.ui.Scanner({ ... })
```

Creates a new Scanner instance that can be used to scan single or multiple barcodes.

Options:

- `container`: Dom element under which video feed from the camera will be shown.
- `dialog`: If set as `true`, will open a dialog to show video feed from the camera.
- `multiple`: If set as `false`, will stop scanning after one successful scan.
- `on_scan`: Callback method to handle the scanned input.

Here is a sample client code to scan one single barcode and log it to the console.

```js
new frappe.ui.Scanner({
  dialog: true, // open camera scanner in a dialog
  multiple: false, // stop after scanning one value
  on_scan(data) {
    console.log(data.decodedText);
  }
});
```

The below code can be used to continously scan and handle the scanned input.

```js
const scanner = new frappe.ui.Scanner({
  dialog: true, // open camera scanner in a dialog
  multiple: true, // stop after scanning one value
  on_scan(data) {
    handle_scanned_barcode(data.decodedText);
  }
});
```

To stop the scanning, you can either close the dialog or use `scanner.stop_scan();`