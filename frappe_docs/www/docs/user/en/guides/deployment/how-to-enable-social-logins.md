<!-- add-breadcrumbs -->
# How To Enable Social Logins

Use Facebook, Google or GitHub authentication to login to Frappe, and your users will be spared from remembering another password.

The system uses the **Email Address** supplied by these services to **match with an existing user** in Frappe. If no such user is found, **a new user is created** of the default type **Website User**, if Signup is not disabled in Website Settings. Any System Manager can later change the user type from **Website User** to **System User**, so that the user can access the Desktop.

#### Login screen with Social Logins enabled
<img class="screenshot" alt="Login screen with Social Logins enabled" src="/docs/assets/img/social-logins.png">

To enable these signups, you need to have **Client ID** and **Client Secret** from these authentication services for your Frappe site. The Client ID and Client Secret are to be set in Website > Setup > Social Login Keys. Here are the steps to obtain these credentials.

> Use **https://{{ yoursite }}** if your site is HTTPS enabled.

---

### Facebook

1. Go to [https://developers.facebook.com](https://developers.facebook.com)
2. Click on Apps (topbar) > New App, fill in the form.
3. Go to Settings > Basic, set the **Contact Email** and save the changes.
4. Go to Settings > Advanced, find the field **Valid OAuth redirect URIs**, and enter:
    **http://{{ yoursite }}/api/method/frappe.www.login.login\_via\_facebook**
5. Save the changes in Advance tab.
6. Go to Status & Review and switch on "Do you want to make this app and all its live features available to the general public?"
7. Go to Dashboard, click on the show button besides App Secret, and copy the App ID and App Secret into **Desktop > Website > Setup > Social Login Keys**

<div class="embed-responsive embed-responsive-16by9">
	<iframe src="https://www.youtube.com/embed/zC6Q6gIfiw8" class="embed-responsive-item" allowfullscreen></iframe>
</div>

---

### Google

1. Go to [https://console.developers.google.com](https://console.developers.google.com)
2. Create a new Project and fill in the form.
3. Click on APIs & Auth > Credentials > Create new Client ID
4. Fill the form with:
    - Web Application
    - Authorized JavaScript origins as **http://{{ yoursite }}**
	- Authorized redirect URI as
	    **http://{{ yoursite }}/api/method/frappe.www.login.login\_via\_google**
5. Go to the section **Client ID for web application** and copy the Client ID and Client Secret into **Desktop > Website > Setup > Social Login Keys**

<div class="embed-responsive embed-responsive-16by9">
  <iframe src="https://www.youtube.com/embed/w_EAttrE9sw" class="embed-responsive-item" allowfullscreen></iframe>
</div>

---

### GitHub

1. Go to [https://github.com/settings/applications](https://github.com/settings/applications)
2. Click on **Register new application**
3. Fill the form with:
    - Homepage URL as **http://{{ yoursite }}**
	- Authorization callback URL as
	    **http://{{ yoursite }}/api/method/frappe.www.login.login\_via\_github**
4. Click on Register application.
5. Copy the generated Client ID and Client Secret into **Desktop > Website > Setup > Social Login Keys**

<div class="embed-responsive embed-responsive-16by9">
	<iframe src="https://www.youtube.com/embed/bG71DxxkVjQ" class="embed-responsive-item" allowfullscreen></iframe>
</div>

---

### Office 365

#### Your Server
Note: Microsoft requires **https://** in the redirect URI. In order for the login verification redirect to work, edit the hostname in site_config.json to include http:// like this: 
	**"host_name": "https://yoursitename.com",**

#### Azure AD
1. Go to [https://portal.azure.com](https://portal.azure.com)
2. In the sidebar menu, click **Azure Active Directory > App Registrations.**
3. Click on **New Registration**
	- Application Name: (Anything you want)
	- Application Supported Account Types: **Any Azure AD Directory - Multitenant**
	- Redirect URI: **https://{{yoursitename.com}}/api/method/frappe.integrations.oauth2_logins.login_via_office365**
	- Click **Register**
4. On the Application Overview screen, copy the **Application (client) ID** to a Textedit doc.
5. In the sidebar menu, click **Token Configuration**
	- Click Add Optional Claim: **ID > email**
	- If given the option, **Turn on Microsoft Graph** email permission.
	- Click Add Optional Claim: **Access > email**
6. In the sidebar menu, click **Certificates and secrets**	
	- Click **New client secret**
	- Name: (Anything)
	- Click **Create**
7. **DO NOT CLOSE SECRETS PAGE**
	- Copy the **Client Secret: Value** (NOT Secret ID) to your Textedit doc. This is the only time you will see it!

#### Your Frappe Site
1. Log into your Frappe site and go to **Social Login Keys.**
2. Create **new Social Login Key** using items saved to your Textedit doc.
	- Social Login Provider: Office 365
	- Client ID: **Application (client) ID**
	- Client Secret: **Client Secret: Value**
3. Click **Save**
4. Click **Enable Social Login**, then click **Save** again.
5. Make sure your Frappe user email is same as your Microsoft 365 email you are going to link.
6. Then click Logout, then click **Login with Office 365**
---
<!-- markdown -->
