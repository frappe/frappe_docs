---
add_breadcrumbs: 1
title: Attachments
metatags:
 description: >
  Frappe Framework allows attachment of files to documents by selecting or dragging and dropping a file from your device, choosing an uploaded file, attaching a web link or taking a photo. It also has a File Manager where you can import multiple files using the Import Zip feature.
---

# Attachments

Frappe allows attachment of files to documents. Users with **Read** permissions on a particular document will also be able to access the files attached to it.

![Attachments](/docs/assets/img/file_uploader.png)

## How to Attach a New File

There are several ways to attach a file to a document.

### Select File

![Select File](/docs/assets/img/file_uploader_my_device.gif)

### Drag and Drop

![Drag and Drop](/docs/assets/img/file_uploader_drag_and_drop.gif)

### Uploaded File

Attach a file a that was previously uploaded, to a different document.

![Uploaded File](/docs/assets/img/file_uploader_uploaded.gif)

### Web Link

If you use a separate server for files or use online services like Dropbox or Docs, you can attach a file by providing a link to it.

![Web Link](/docs/assets/img/file_uploader_weblink.gif)

### Camera

Attach Images by taking a photo using your device's camera.

![Camera](/docs/assets/img/file_uploader_camera.gif)

## File Manager

All the attached files are listed in the File Manager. You can access these by navigating here:

**Home > Tools > Files**

![File Manager](/docs/assets/img/file_manager.png)

## Import Zip

You can also bulk import multiple files at once using the Import Zip feature.

1. Go to **File List > Menu > Import Zip**.
1. Upload a zip file.
1. After the zip file is uploaded, it's contents will be extracted and each file
   will be created as a new File record.

![Importing files from zip](/docs/assets/img/import_zip.gif)

> Note: Hidden files (files starting with `.`) are not extracted when importing from a zip file.

## Cropping Images

You can crop `.jpeg` and `.png` images by clicking on the crop icon.

![Cropping images on upload](/docs/assets/img/crop_image.gif)

## Optimizing Images

Images can be optimized to reduce their file size. Currently optimizing an image does the following:

1. Resizes it to fit a max-width of 1920px and a max-height of 1080px, while preserving the aspect ratio
1. Uses optimal encoder settings
1. Reduces the quality to 85%
  
**Toggle optimization during upload**

![Toggle image optimization](/docs/assets/img/toggle_image_optimization.gif)

**Optimize an already uploaded image**

![Optimize saved image](/docs/assets/img/optimize_saved_image.gif)

## Limits

A limit of 10MB is applicable on file size per attachment by default. For self-hosted users, this can be changed by setting `max_file_size` in your site's configuration file.

### Attachments per Document

You can limit how many files can be attached to a specific document.

#### Step 1: Navigate to Customize Form

> Home > Customization > Customize Form

#### Step 2: Select Document Type

Select the document type for which you'd like to set this limit.

![Select Document Type](/docs/assets/img/select_document_type.png)

#### Step 3: Set Limit

Set the value of **Max Attachments** to the maximum number of attachments allowed for this document type.

![Set Limit](/docs/assets/img/set_max_attachments.png)

Once you're satisfied with the changes, click the **Update** button. That's it! The maximum number of attachments per document will now be validated every time a new attachment is added to a document of this type.

<!-- markdown -->