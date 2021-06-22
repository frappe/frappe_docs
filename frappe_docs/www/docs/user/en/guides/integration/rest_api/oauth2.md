<!-- add-breadcrumbs -->

Base URL: https://{your frappe instance}

Example: https://demo.erpnext.com

# OAuth 2

Use the header `Authorization: Bearer <access_token>` to perform authenticated requests. You can receive a [bearer token](https://tools.ietf.org/html/rfc6750) by combining the following two requests.

## GET /api/method/frappe.integrations.oauth2.authorize

Get an authorization code from the user to access ERPNext on his behalf.

Params (in query):

* client_id (string)

	ID of your OAuth2 application

* state (string)

	Arbitrary value used by your client application to maintain state between the request and callback. The authorization server includes this value when redirecting the user-agent back to the client. The parameter should be used for preventing [cross-site request forgery](https://tools.ietf.org/html/rfc6749#section-10.12).

* response_type (string)

	"code"

* scope (string)

	The scope of access that should be granted to your application.

* redirect_uri (string)

	Callback URI that the user will be redirected to, after the application is authorized. The authorization code can then be extracted from the params.

* code_challenge_method (string)

	(OPTIONAL) Can be one from `s256` or `plain`.

* code_challenge (string)

	(OPTIONAL) Can be `base64encode(sha256(random_string))` in case `code_challenge_method=s256` or `random_string` in case `code_challenge_method=plain`. Refer https://tools.ietf.org/html/rfc7636#appendix-A

Example:

```bash
curl -X POST https://{your frappe instance}/api/method/frappe.integrations.oauth2.authorize \
	 --data-urlencode 'client_id=511cb2ac2d' \
	 --data-urlencode 'state=444' \
	 # base64encode(sha256('420')) => 21XaP8MJjpxCMRxgEzBP82sZ73PRLqkyBUta1R309J0
	 # --data-urlencode 'code_verifier=21XaP8MJjpxCMRxgEzBP82sZ73PRLqkyBUta1R309J0' \
	 --data-urlencode 'response_type=code'
	 --data-urlencode 'scope=openid%20all' \
	 --data-urlencode 'redirect_uri=https://app.getpostman.com/oauth2/callback'
```

Returns:

* HTTP Code: 200
* text/html

	This will open the authorize page which then redirects you to the `redirect_uri`.

If the user clicks 'Allow', the redirect URI will be called with an authorization code in the query parameters:

`https://{redirect uri}?code=plkj2mqDLwaLJAgDBAkyR1W8Co08Ud&state=444`

If user clicks 'Deny' you will receive an error:

`https://{redirect uri}?error=access_denied`


## Token Exchange for Authorization Code Grant with ID Token

```
POST /api/method/frappe.integrations.oauth2.get_token
Header Content-Type: application/x-www-form-urlencoded
```

Trade the authorization code (obtained above) for an access token.

Params (in body):

* grant_type (string)

	"authorization_code"

* code (string)

	Authorization code received in redirect URI.

* client_id (string)

	ID of your OAuth2 application

* redirect_uri (string)

	Registered redirect URI of client app

Example:

```bash
curl -X POST https://{your frappe instance}/api/method/frappe.integrations.oauth2.get_token \
	 -H 'Content-Type: application/x-www-form-urlencoded' \
	 -H 'Accept: application/json' \
	 -d 'grant_type=authorization_code&code=wa1YuQMff2ZXEAu2ZBHLpJRQXcGZdr
		 &redirect_uri=https%3A%2F%2Fapp.getpostman.com%2Foauth2%2Fcallback&client_id=af615c2d3a'
```
For **testing purposes** you can also pass the parameters in the URL like this (and open it in the browser):

`https://{your frappe instance}/api/method/frappe.integrations.oauth2.get_token?grant_type=authorization_code&code=A1KBRoYAN1uxrLAcdGLmvPKsRQLvzj&client_id=511cb2ac2d&redirect_uri=https%3A%2F%2Fapp.getpostman.com%2Foauth2%2Fcallback`

Returns:

```json
	{
		"access_token": "pNO2DpTMHTcFHYUXwzs74k6idQBmnI",
		"token_type": "Bearer",
		"expires_in": 3600,
		"refresh_token": "cp74cxbbDgaxFuUZ8Usc7egYlhKbH1",
		"scope": "openid all",
		"id_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.XbPfbIHMI6arZ3Y922BhjWgQzWXcXNrz0ogtVhfEd2o"
	}
```

## Token Exchange for Authorization Code Grant with ID Token (PKCE)

```
POST /api/method/frappe.integrations.oauth2.get_token
Header Content-Type: application/x-www-form-urlencoded
```

Trade the authorization code (obtained above) for an access token.

Params (in body):

* grant_type (string)

	"authorization_code"

* code (string)

	Authorization code received in redirect URI.

* client_id (string)

	ID of your OAuth2 application

* redirect_uri (string)

	Registered redirect URI of client app

* code_verifier (string)

	`random_string` used during `Authorization Request` with `code_challenge_method` and `code_challenge`.


Content-Type: application/x-www-form-urlencoded

Example:

```bash
curl -X POST https://{your frappe instance}/api/method/frappe.integrations.oauth2.get_token \
	 -H 'Content-Type: application/x-www-form-urlencoded' \
	 -H 'Accept: application/json' \
	 -d 'grant_type=authorization_code&code=wa1YuQMff2ZXEAu2ZBHLpJRQXcGZdr
		 &redirect_uri=https%3A%2F%2Fapp.getpostman.com%2Foauth2%2Fcallback&client_id=af615c2d3a&code_verifier=420'
```
For **testing purposes** you can also pass the parameters in the URL like this (and open it in the browser):

`https://{your frappe instance}/api/method/frappe.integrations.oauth2.get_token?grant_type=authorization_code&code=A1KBRoYAN1uxrLAcdGLmvPKsRQLvzj&client_id=511cb2ac2d&redirect_uri=https%3A%2F%2Fapp.getpostman.com%2Foauth2%2Fcallback&code_verifier=420`

Returns:

```json
{
	"access_token": "pNO2DpTMHTcFHYUXwzs74k6idQBmnI",
	"token_type": "Bearer",
	"expires_in": 3600,
	"refresh_token": "cp74cxbbDgaxFuUZ8Usc7egYlhKbH1",
	"scope": "openid all",
	"id_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.XbPfbIHMI6arZ3Y922BhjWgQzWXcXNrz0ogtVhfEd2o"
}
```

## Revoke Token Endpoint

```
POST /api/method/frappe.integrations.oauth2.revoke_token
Header: Content-Type: application/x-www-form-urlencoded
```

Revoke token endpoint.

Params:

* token

	Access token to be revoked.

Returns:

Always returns empty response with HTTP status code 200.

```json
	{}
```

## Open ID Connect id_token

ID Token is a JWT.

- `aud` claim has registered `client_id`.
- `iss` claim has frappe server url.
- `sub` claim has Frappe User's userid.
- `roles` claim has user roles.
- `exp` claim has expiration time.
- `iat` claim has issued at time.

Example: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkouIERvZSIsImVtYWlsIjoiakBkb2UuY29tIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE1MTYyNDIwMjIsImF1ZCI6ImNsaWVudF9pZCJ9.ZEdnrHjLbArahVTN19b4zoRFoBO5a2BakRkR82O1VU8`

Verify and extract it with PyJWT.

```python
import jwt

id_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkouIERvZSIsImVtYWlsIjoiakBkb2UuY29tIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE1MTYyNDIwMjIsImF1ZCI6ImNsaWVudF9pZCIsInJvbGVzIjpbIlN5c3RlbSBNYW5hZ2VyIiwiU2FsZXMgTWFuYWdlciJdLCJub25jZSI6Ijc4OTEyMyIsImlzcyI6Imh0dHBzOi8vZXJwLmV4YW1wbGUuY29tIn0.F8Wbh5dtD1loZPltJLj_sqF9DZNeBvEbo-ITtf3UPqk"

client_id = 'client_id'
client_secret = 'client_secret'

payload = jwt.decode(
	id_token,
	audience=client_id,
	key=client_secret,
	algorithm="HS256",
	options={"verify_exp": False}, # Enabled by default to verify expiration time
)

print(payload)
# Output

{'sub': '1234567890', 'name': 'J. Doe', 'email': 'j@doe.com', 'iat': 1516239022, 'exp': 1516242022, 'aud': 'client_id', 'roles': ['System Manager', 'Sales Manager'], 'nonce': '789123', 'iss': 'https://erp.example.com'}
```

## OpenID User Info Endpoint

Request

```
GET /api/method/frappe.integrations.oauth2.openid_profile
Header: Authorization: Bearer valid_access_token
```

Response

```json
{
	"sub": "1234567890",
	"name": "J. Doe",
	"given_name": "J",
	"family_name": "Doe",
	"iss": "https://erp.example.com",
	"picture": "https://erp.example.com/files/jdoe.jpg",
	"email": "j@doe.com",
	"iat": 1516239022,
	"exp": 1516242022,
	"aud": "client_id",
	"roles": ["System Manager", "Sales Manager"]
}
```

## Introspect Token Endpoint

```
POST /api/method/frappe.integrations.oauth2.introspect_token
Header: Content-Type: application/x-www-form-urlencoded
```

Revoke token endpoint.

Params:

* token_type_hint

	`access_token` or `refresh_token`, defaults to `access_token` if nothing is provided

* token

	Access token or Refresh Token to be introspected. Depends on token_type_hint

Returns:

```json
{
	"client_id": "511cb2ac2d",
	"trusted_client": 1,
	"active": true,
	"exp": 1619523326,
	"scope": "openid all",
	"sub": "1234567890",
	"name": "J. Doe",
	"given_name": "J",
	"family_name": "Doe",
	"iss": "https://erp.example.com",
	"picture": "https://erp.example.com/files/jdoe.jpg",
	"email": "j@doe.com",
	"iat": 1516239022,
	"exp": 1516242022,
	"aud": "511cb2ac2d",
	"roles": ["System Manager", "Sales Manager"]
}
```

OR

```json
{
	"active": false,
	"_server_messages": "..."
}
```

## Further Reading

Please check `Guides / Integration / How To Set Up Oauth` to see how to create a new OAuth 2 client.

* [Content-Type Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type),
* [Authorization Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization),
* [OAuth 2 Specification](https://tools.ietf.org/html/rfc6749),
* [Bearer token](https://tools.ietf.org/html/rfc6750).

Authors:

	- Raffael Meyer (raffael@alyf.de)
	- Revant Nandgaonkar (revant@castlecraft.in)

{next}
