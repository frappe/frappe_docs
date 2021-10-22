<!-- add-breadcrumbs -->
# How To Enable Social Logins

Use Facebook, Google or GitHub authentication to login to Frappe, and your users will be spared from remembering another password.

The system uses the **Email Address** supplied by these services to **match with an existing user** in Frappe. If no such user is found, **a new user is created** of the default type **Website User**, if Signup is not disabled in Website Settings. Any System Manager can later change the user type from **Website User** to **System User**, so that the user can access the Desktop.

#### Login screen with Social Logins enabled
<img class="screenshot" alt="Login screen with Social Logins enabled" src="/docs/assets/img/social-logins.png">

To enable these signups, you need to have **Client ID** and **Client Secret** from these authentication services for your Frappe site. The Client ID and Client Secret are to be set in **Desktop > Integration > Authentication > Social Login Key > Client ID** and **Desktop > Integration > Authentication > Social Login Key > Client Secret**. Here are the steps to obtain these credentials.

> Use **https://{{ yoursite }}** if your site is HTTPS enabled.

---

### Facebook

1. Go to [https://developers.facebook.com](https://developers.facebook.com)
1. Click on Apps (topbar) > New App, fill in the form.
1. Go to Settings > Basic, set the **Contact Email** and save the changes.
1. Go to Settings > Advanced, find the field **Valid OAuth redirect URIs**, and enter:
    **http://{{ yoursite }}/api/method/frappe.www.login.login\_via\_facebook**
1. Save the changes in Advance tab.
1. Go to Status & Review and switch on "Do you want to make this app and all its live features available to the general public?"
1. Go to Dashboard, click on the show button besides App Secret, and copy the App ID and App Secret into **Desktop > Integration > Authentication > Social Login Key > Client ID** and **Desktop > Integration > Authentication > Social Login Key > Client Secret**

<div class="embed-responsive embed-responsive-16by9">
	<iframe src="https://www.youtube.com/embed/zC6Q6gIfiw8" class="embed-responsive-item" allowfullscreen></iframe>
</div>

---

### Google

1. Go to [https://console.developers.google.com](https://console.developers.google.com)
1. Create a new Project and fill in the form.
1. Click on APIs & Auth > Credentials > Create new Client ID
1. Fill the form with:
    - Web Application
    - Authorized JavaScript origins as **http://{{ yoursite }}**
	- Authorized redirect URI as
	    **http://{{ yoursite }}/api/method/frappe.www.login.login\_via\_google**
1. Go to the section **Client ID for web application** and copy the Client ID and Client Secret into **Desktop > Integration > Authentication > Social Login Key > Client ID**

<div class="embed-responsive embed-responsive-16by9">
  <iframe src="https://www.youtube.com/embed/w_EAttrE9sw" class="embed-responsive-item" allowfullscreen></iframe>
</div>

---

### GitHub

1. Go to [https://github.com/settings/applications](https://github.com/settings/applications)
1. Click on **Register new application**
1. Fill the form with:
    - Homepage URL as **http://{{ yoursite }}**
	- Authorization callback URL as
	    **http://{{ yoursite }}/api/method/frappe.www.login.login\_via\_github**
1. Click on Register application.
1. Copy the generated Client ID and Client Secret into **Desktop > Website > Setup > Social Login Keys** and **Desktop > Integration > Authentication > Social Login Key > Client Secret**

<div class="embed-responsive embed-responsive-16by9">
	<iframe src="https://www.youtube.com/embed/bG71DxxkVjQ" class="embed-responsive-item" allowfullscreen></iframe>
</div>

---

### Office 365

1. Go to [https://portal.azure.com](https://portal.azure.com)
1. Create a new Azure Active Directory > App Registration.
1. Click on New Application Registration
1. Fill the form with:
    - Application Name
    - Select Accounts in any organizational directory (Any Azure AD directory - Multitenant).
    - Application Type - Web app / API
	- Redirect URI as
    		- Homepage URL as **http://{{ yoursite }}**
		- Authorization callback URL as **http://{{ yoursite }}/api/method/frappe.integrations.oauth2_logins.login_via_office365**
1. Click on Register application.
1. Go to the section **Overview** in Azure Portal copy the Application (client) ID into  **Desktop > Integration > Authentication > Social Login Key > Client ID
1. Go to the section **Certificates & secrets** in Azure Portal and create new client secrets copy than copy Client Secret by adding into **Desktop > Integration > Authentication > Social Login Key > Client Secret**
1. Select Office 365 as Social Login Provider
1. Click Enable Social Login and Save
1. Go to the section **Token configuration** click add optional claim
    - Add Token Type > ID > Email	
---
<!-- markdown -->
