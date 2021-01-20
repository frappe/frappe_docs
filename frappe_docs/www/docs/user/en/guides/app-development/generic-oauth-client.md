> Introduced in Frappe Version 13.

Frappe comes with generic OAuth 2.0 client. This way you can connect to any third party service supporting OAuth 2.0.

## Prerequisites

- [Connected App](/docs/user/en/guides/app-development/connected-app)

    **Connected App** stores the client ID and secret, scopes and endpoints of the platform you're integrating with.

## Getting started

> This example uses Google, but you can use any service supporting OAuth 2.0.

Your integration will most probably need a settings doctype (for example, "Google Settings"). Here you create a link field to **Connected App**. A System Manager can later create a **Connected App**, enter the client credentials and link it to your integration. You will know which **Connected App** belongs to your integration via your settings DocType.

```py
google_settings = frappe.get_single('Google Settings')
connected_app_name = google_settings.get('connected_app')

connected_app = frappe.get_doc('Connected App', connected_app_name)
```

Now you have an instance of your **Connected App**, containing the credentials and endpoint URIs. If a user didn't connect yet, they can open the **Connected App** and click the "Connect to ..." button on the top right. Alternatively, you can get the authorization URI and use it for your own custom button or redirect:

```py
authorization_uri = connected_app.initiate_web_application_flow() # optional
```

Once the user is authorized, you can get an authenticated session like this:

```py
session = connected_app.get_oauth2_session()
```

> If the user is not authenticated at this time, they will be redirected to the authentication page.

Now you can retrieve any allowed resource from the target platform:

```py
session.get('https://www.googleapis.com/oauth2/v2/userinfo')
```

If the access token is expired, the session will automatically try to refresh it.

{next}
