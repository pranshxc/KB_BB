---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-23_finding-hidden-gems-vol-1-forging-oauth-tokens-using-discovered-client-id-and-cl.md
original_filename: 2018-07-23_finding-hidden-gems-vol-1-forging-oauth-tokens-using-discovered-client-id-and-cl.md
title: 'Finding hidden gems vol. 1: forging OAuth tokens using discovered client id
  and client secret'
category: documents
detected_topics:
- oauth
- sso
- jwt
- access-control
- command-injection
- otp
tags:
- imported
- documents
- oauth
- sso
- jwt
- access-control
- command-injection
- otp
language: en
raw_sha256: 04620e9240401f95b70d52e96b1c240d1e35360cef9a80193193d895c01c5ce9
text_sha256: b74d0b6dfd456b5d5502441682dc794e04bb42b35178ccff0f4117388aed8b8b
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Finding hidden gems vol. 1: forging OAuth tokens using discovered client id and client secret

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-23_finding-hidden-gems-vol-1-forging-oauth-tokens-using-discovered-client-id-and-cl.md
- Source Type: markdown
- Detected Topics: oauth, sso, jwt, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `04620e9240401f95b70d52e96b1c240d1e35360cef9a80193193d895c01c5ce9`
- Text SHA256: `b74d0b6dfd456b5d5502441682dc794e04bb42b35178ccff0f4117388aed8b8b`


## Content

---
title: "Finding hidden gems vol. 1: forging OAuth tokens using discovered client id and client secret"
url: "https://medium.com/@mateusz.olejarka/finding-hidden-gems-vol-1-forging-oauth-tokens-using-discovered-client-id-and-client-secret-467f1cd21714"
authors: ["Mateusz Olejarka (@molejarka)"]
bugs: ["Information disclosure"]
bounty: "3,133.7"
publication_date: "2018-07-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5793
scraped_via: "browseros"
---

# Finding hidden gems vol. 1: forging OAuth tokens using discovered client id and client secret

Finding hidden gems vol. 1: forging OAuth tokens using discovered client id and client secret
Mateusz Olejarka
Follow
2 min read
·
Jul 24, 2018

133

4

I
love sensitive information exposure bugs. They are getting more attention at last. Below a short story about leaked Node.js code and OAuth client id and client secret which I found in there.

Recon

One of my bug bounty recon tools discovered a package.json file which looked interesing. The package.json file is a description of a Node.js module. This particular one looked like below:

{
 "name": "[…redacted…]",
 "description": "[…redacted…]",
 "version": "[…redacted…]",
 "private": true,
 […redacted…]
 "engines": {
 "node": ">=6.9.1"
 },
 "scripts": {
 "start": "node server/[…redacted…].js"
 }
}

Setting scripts contained a path to some Node.js code to execute. I was curious what’s in that file, therefore I immediately downloaded the content. It was a huge file, containing Node.js code.

OAuth

I found there four variables which looked very promissing.

const devClientId = '11e7f9d3–9bbf-4a01-a23e-c9c58e3acb1d';
const prodClientId = 'a2ae2727-aa6a-4197–823e-40e6d4e503a7';
const devClientSecret = 'd[…redacted…]=';
const prodClientSecret = 'b[…redacted…]=';

Disclaimer: all values were replaced or redacted.

Get Mateusz Olejarka’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

It ringed a distant bell related to one of the OAuth grant types — the client credentials. To quote the specs:

Client credentials are used as an authorization grant
typically when the client is acting on its own behalf (the client is
also the resource owner) or is requesting access to protected
resources based on an authorization previously arranged with the
authorization server.

From other recon results I knew that this company is built on top of Microsoft Azure therefore I searched for OAuth integration documentation. Now I just wanted to check if prodClientId and prodClientSecret are still valid:

POST /[redacted].onmicrosoft.com/oauth2/v2.0/token HTTP/1.1
Host: login.microsoftonline.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 190
client_id=a2ae2727-aa6a-4197–823e-40e6d4e503a7
&scope=https%3A%2F%2Fgraph.microsoft.com%2F.default
&client_secret=b[…redacted…]%3d
&grant_type=client_credentials
HTTP/1.1 200 OK
[…]
{
 “token_type”:”Bearer”,
 “expires_in”:3600,
 “ext_expires_in”:0,
 “access_token”:”eyJ[…redacted…]”
}

I got back a JWT token and just one thing left — to actually use it and try to get some data. I’ve selected an API call which returns users:

GET /v1.0/users HTTP/1.0
Host: graph.microsoft.com
Authorization: Bearer eyJ[…redacted…]
HTTP/1.1 200 OK
[…]
{
 “id”:”c7f5a5bf-9ba7–4871–8f56-d7584eb95115",
 “businessPhones”:[],”displayName”:”Stuart […redacted…]”,
 “givenName”:”Stuart”,
 “jobTitle”:null,
 “mail”:”[…redacted…]”stuart[…redacted…]”,
 “mobilePhone”:null,
 “officeLocation”:null,
 “preferredLanguage”:null,
 “surname”:”[…redacted…]”,
 “userPrincipalName”:”[…redacted…]
},
{
 “id”:”bd80519d-81e1–4634–9519–4ad9328f3b1d”,
 “businessPhones”:[],
 “displayName”:”Ashley […redacted…],
 “givenName”:”Ashley”,
 “jobTitle”:null,”mail”:”a.[…redacted…],
 “mobilePhone”:null,
 “officeLocation”:”SLC”,
 “preferredLanguage”:null,
 “surname”:”[…redacted…]”,
 “userPrincipalName”:”[…redacted…]”
}
[…]

It worked! This was found in a public program on Bugcrowd and they gave me 3133.7$ for this finding.

Fix

The company fixed it like below — now those variables are taken out of Consul:

class Consul {
 constructor(url) {
 this.consulHost = url;
 }
 getClientId() {
 return this.getConsulValue(‘v1/[redacted]/CLIENT_ID’);
 }
 getClientSecret() {
 return this.getConsulValue(‘v1/[redacted]/APP_KEY’);
 }
 getConsulValue(consulKey) {
 return request({ url: `${this.consulHost}/${consulKey}`, json: true }).promise()
 .then((res) => res[0].Value)
 .then((val) => (new global.Buffer(val, ‘base64’)).toString(‘utf8’));
 }
}
exports.Consul = Consul;

Where consulHost in taken from an environmental variable:

const consulHost = process.env.CONSUL
Lessons learned:
For myself — don’t give up, make a break, return to the problem next day and solve it easily.
Bug hunters — definitely check for package.json files.
Developers — check what is in your package.json file and make sure you don’t leak anything interesing.
