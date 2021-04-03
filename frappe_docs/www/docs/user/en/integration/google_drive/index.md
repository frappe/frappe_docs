---
add_breadcrumbs: 1
title: Google Drive
image: /docs/assets/img/integration/google_drive/google_drive_picker_attach_file.png
metatags:
 description: Use the file picker to attach files from Google Drive to any DocType.
---

# Google Drive

Google Drive is a file storage and synchronization service developed by Google. It allows users to store, synchronize and share files. Google Drive is a key component of Google Workspace, Google's monthly subscription offering for businesses.

You can use Frappe Framework's file picker to select any file from Google Drive and attach it to the current DocType. For example, you can attach the invoice PDF stored in Google Drive to a Sales Invoice record in your Frappe app.

## Setup

### Google Cloud Console

First we need to get some credentials that will allow us to access Google Drive. You can [use the setup tool](https://console.cloud.google.com/flows/enableapi?apiid=picker&credential=client_key), which guides you through creating a project in the Google Cloud Console, enabling the API, and creating credentials.

If you haven't done so already, create your application's API key by clicking **Create credentials > API key**. Next, look for your API key in the **API keys** section. You can open the API Key and restrict it.

1. Under **Application restrictions** choose "HTTP referrers", 
2. under  **Website restrictions** add your frappe instance's hostname and
3. under **API restrictions** choose "Restrict key" and select the "Google Picker API". 

![API Key configuration](/docs/assets/img/integration/google_drive/google_drive_picker_api_key.png)

If you haven't done so already, create your OAuth 2.0 credentials by clicking **Create credentials > OAuth client ID**.

1. Under **Application type** choose "Web application" and 
2. under **Authorized JavaScript origins** add your frappe instance's hostname.

![OAuth Client configuration](/docs/assets/img/integration/google_drive/google_drive_picker_oauth_client.png)

After you've created the credentials, you can see your client ID on the [Credentials page](https://console.cloud.google.com/apis/credentials).

Last but not least you need to configure the [OAuth Consent Screen](https://console.cloud.google.com/apis/credentials/consent). This is the page that users will see when they are using the Google Drive Picker for the first time. It asks them to grant access to their Google Drive. You can configure this as you like, just take care to add the scope `https://www.googleapis.com/auth/drive.readonly` on the **Scopes** page.

You will also need your App ID at hand. This is your project number which you can find under **IAM & Admin > Settings**.

> Portions of this section are modifications based on work created and [shared by Google](https://developers.google.com/picker/docs) and used according to terms described in the [Creative Commons 4.0 Attribution License](https://creativecommons.org/licenses/by/4.0/).

### Frappe instance

Now that the Google Picker API is enabled and we have the necessary credentials we can go ahead and configure the **Google Settings** in you Frappe instance.

1. Open **Google Settings**.
2. Check the "Enable" checkbox.
3. In the **Google Drive Picker** section, check the "Google Drive Picker Enabled" checkbox.
4. Enter your App ID, Client ID and API Key.
5. Save the **Google Settings** and reload your browser window.

![Google Settings](/docs/assets/img/integration/google_drive/google_drive_picker_settings.png)

Now when you click "Attach file" in the sidebar you should see the Google Drive icon.

![Attach File Dialog](/docs/assets/img/integration/google_drive/google_drive_picker_attach_file.png)

If you click on it the first time you have to authorize the Frappe app to access your Google Drive files. 

![Google Sign In](/docs/assets/img/integration/google_drive/google_drive_picker_signin.png)

Then the Google Drive Picker opens where you can choose a file.

![Google Drive Picker](/docs/assets/img/integration/google_drive/google_drive_picker_select.png)

Click the blue button on the bottom left to attach a link to this file to the current DocType.

![File Attached to DocType](/docs/assets/img/integration/google_drive/google_drive_picker_attached.png)

> In case you're looking for technical details, Google Drive was introduced in [Pull Request #12715](https://github.com/frappe/frappe/pull/12715).
