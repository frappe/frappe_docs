
Frappe comes with generic oAuth2 client. This way you can connect to any other platform supporting oAuth2.

## Connected App

The doctype **Connected App** stores the Client ID, Client Secret, Scopes and Endpoint URI of the platform you're integrating with.

Your integration will most probably need a settings doctype (for example, "Google Settings"). Here you should create a link field to **Connected App**. The administrator of a site can later create a new **Connected App**, enter his client credentials and link it here. Via the settings DocType you will know which **Connected App** belongs to your integration.

```py
google_settings = frappe.get_single('Google Settings')
connected_app_name = google_settings.get('connected_app')

connected_app = frappe.get_doc('Connected App', connected_app_name)
```

Now you have an instance of your **Connected App**, containing the credentials and endpoint URIs. Now it's time to authorize the individual users. They can open the **Connected App** and click the 'Init' button on the top right. Alternatively, you can get the authorization URI and display it where you like:

```py
authorization_uri = connected_app.initiate_web_application_flow()
```

Once the user is authorized, you can get an authenticated session:

```py
session = connected_app.get_oauth2_session()
```

> If the user is not authenticated at this time, they will be redirected to the authentication page.

Now you can retrieve any allowed resource from the target platform:

```py
session.get('https://gmail.googleapis.com/gmail/v1/users/{userId}/profile')
```

{next}
