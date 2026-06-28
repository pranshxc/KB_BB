---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-19_api-misconfiguration-no-swag-of-swaggerui.md
original_filename: 2023-01-19_api-misconfiguration-no-swag-of-swaggerui.md
title: API Misconfiguration - No Swag of SwaggerUI
category: documents
detected_topics:
- access-control
- command-injection
- otp
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- otp
- api-security
language: en
raw_sha256: 33bf30518d72a7ed5dfb9cb3b6eab5ad89011e833e7ba938e70bd4a0a65e6962
text_sha256: e275839fa3f370772803d903295673027e1e621191468bac10cfa4d28f8b5bdb
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# API Misconfiguration - No Swag of SwaggerUI

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-19_api-misconfiguration-no-swag-of-swaggerui.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `33bf30518d72a7ed5dfb9cb3b6eab5ad89011e833e7ba938e70bd4a0a65e6962`
- Text SHA256: `e275839fa3f370772803d903295673027e1e621191468bac10cfa4d28f8b5bdb`


## Content

---
title: "API Misconfiguration - No Swag of SwaggerUI"
url: "https://shahjerry33.medium.com/api-misconfiguration-no-swag-of-swaggerui-9b43135346be"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["Security misconfiguration", "Privilege escalation"]
publication_date: "2023-01-19"
added_date: "2023-01-23"
source: "pentester.land/writeups.json"
original_index: 1652
scraped_via: "browseros"
---

# API Misconfiguration - No Swag of SwaggerUI

API Misconfiguration - No Swag of SwaggerUI
Jerry Shah (Jerry)
Follow
4 min read
·
Jan 19, 2023

356

Press enter or click to view image in full size

Summary

API misconfiguration refers to the improper or insecure setup of an application programming interface (API). This can include issues such as weak authentication, lack of input validation, or improper access controls.

API misconfigurations can provide an attacker with unauthorized access to sensitive data or the ability to perform actions on behalf of a user. This can lead to sensitive data leaks, system compromise and other security issues.

Description

I found an API misconfiguration on SwaggerUI endpoint in one of the web application on a private program. It was leaking the authorization token in the local storage of the web application which I used to find the sensitive information of the users on the website. However upon investigating the requests by accessing the SwaggerUI endpoint it gave me an error saying “Unauthorized, Full authentication is required to access” and one thing that caught my eye was WWW-Authenticate header with the starting value Bearer in the response, which means an Authorization request header with starting value Bearer will be used.

I started digging for the token in the requests but did not find any token then I started looking in the cookies, localstorage and sessionstorage for the token and found an authorization token being stored in the localstorage of the application. I copied the token and used it in the request then I changed the {serviceIdentifier} to 1 and I was able to enumerate the userlist which contained employee details like firstname, lastname, employee id, email, department name and phone number.

What is SwaggerUI ?

Swagger UI is a user-friendly interface for displaying and testing the endpoints of a RESTful API that is defined using the OpenAPI specification. It allows developers to easily interact with the API and view the various requests and responses in a simple, intuitive format.

How I found this vulnerability ?

I went to my target endpoint of swaggerUI and intercepted the request > sent it to repeater and clicked on send
Press enter or click to view image in full size
Repeater

2. Then I searched for authorization token into local storage by right clicking > Inspect > Storage > LocalStorage

Press enter or click to view image in full size
Inspect
Press enter or click to view image in full size
Local Storage

3. I copied the authorization token from the local storage and pasted it in a file for using it in a request

Press enter or click to view image in full size
Authorization Token

4. Then I added the Authorization header with the starting value as Bearer followed by authorization token

Press enter or click to view image in full size
Authorization Header and Token

5. I clicked on Send and got users details

Press enter or click to view image in full size
Users Details
Press enter or click to view image in full size
User Details
Press enter or click to view image in full size
User Details

Why this happened ?

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In my opinion,

There were two issues here which led to this vulnerability

Accessible swaggerUI endpoint
Overly permissive authorization token

Impact

Any user will easily be able to access all the user information which he/she should be restricted from accessing it.

Calculated CVSS

Vector String - CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:N/A:L

Score - 7.2 High

Mitigation

There would be two mitigations applicable for this issue

Restricting the swaggerUI endpoint
Granting proper permissions to the generated authorization token

An application should have two types of authorization, one for the normal user and another for the admin user and only admin user token should have the permission to access the details via swaggerUI endpoint.

Press enter or click to view image in full size
