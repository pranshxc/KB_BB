---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-04_add-new-user-with-admin-permission-and-takeover-the-organization.md
original_filename: 2019-09-04_add-new-user-with-admin-permission-and-takeover-the-organization.md
title: Add new user with Admin permission and takeover the organization
category: documents
detected_topics:
- access-control
- command-injection
- file-upload
- rate-limit
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- file-upload
- rate-limit
- api-security
language: en
raw_sha256: 8e2171df27c9f351e94965c4be7cc76ffc2497a686c92a7f647f1b630f25dc42
text_sha256: 4ad59a4ae26c6a3a98cdf6d30de402f81616c1261eeb187f0fc3e29f3972020f
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Add new user with Admin permission and takeover the organization

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-04_add-new-user-with-admin-permission-and-takeover-the-organization.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, file-upload, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `8e2171df27c9f351e94965c4be7cc76ffc2497a686c92a7f647f1b630f25dc42`
- Text SHA256: `4ad59a4ae26c6a3a98cdf6d30de402f81616c1261eeb187f0fc3e29f3972020f`


## Content

---
title: "Add new user with Admin permission and takeover the organization"
url: "https://medium.com/@tarekmohamed_20773/add-new-user-with-admin-permission-and-takeover-the-organization-6318ee10154a"
authors: ["Tarek Mohamed (@Conan0x3)"]
bugs: ["Broken authorization", "Privilege escalation"]
publication_date: "2019-09-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5051
scraped_via: "browseros"
---

# Add new user with Admin permission and takeover the organization

Add new user with Admin permission and takeover the organization
Tarek Mohamed
Follow
4 min read
·
Sep 5, 2019

359

7

Target : redacted.com

Recently i joined a private program and i asked them for two testing accounts ( Admin — user )
Next day i received an invite to redacted.com and they told me they can’t provide an account with admin permission , i’m only allowed to test with a low user account.

So i go to the website and login to the application but i didn’t find anything interesting
the low user can only view pages and no functions to test except a file upload function which only accept PDF formats.

Now i need to test the Authorization functions but i don’t have admin account, also their is no API documentation so i can figure out what is the admin endpoints.

The rule is “ if there is an admin user so for sure there is an admin endpoints”

Without admin account and without API documentation available The only way here is to guess the admin endpoints
and from my previous experience i know that there is a lot of endpoints that can belong to the admin but the most popular one is the one which disclose the user information

This endpoint can be in the following formats :

/api/v2/member/
/api/v2/members/
/api/v2/users/
/api/v2/user/

So i quickly go to burp suite to get any API request so i can play with it

Press enter or click to view image in full size

i changed the endpoint from /api/v2/search/suggestion/counterparty/ to /api/v2/members/ == 404

Press enter or click to view image in full size

api/v2/users== 404

Press enter or click to view image in full size

api/v2/user == 405

Press enter or click to view image in full size

So when sending a GET request to non-existing endpoint it give 404 but when requesting an existing endpoint we got a different response. (405 the method is not allowed )
Now i changed the the request method from GET to POST

Press enter or click to view image in full size

The server tell us that he missing some parameters in body request

Get Tarek Mohamed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As you know , because we play with API’s endpoints so the data will be in JSON format
So i changed the content type to JSON and insert the parameters which is missing as shown below

Press enter or click to view image in full size

well there is another missing parameter “client” for the first time i thought this parameter controlling the user permission, so i entered a test value and it give me an error

Press enter or click to view image in full size

i change the value from string to integer

Press enter or click to view image in full size

Great, the user has been created
i opened another browser and trying to reset password for the new account but i didn’t receive the reset password email

after some time i found that the “client” parameter was controlling where to create this user
So i send the request to burp intruder and then i configure it to brute force the client param from 1 to 100
and the result as follows

so the request succeeded in the above id’s so i go again to the browser and send a reset password request to my new account and i got the reset password email after 1 min and then i logged in to the application

“Let’s takeover the organization”

i told myself to be quit and don’t submit this now, what if i can add new user with admin permission ?
may be there is a parameter that can control the user permission

For my luck , all what i did is add new parameter to the request which is “role” with “admin” value ( “role”=”admin” )
and guess what ? the request succeeded and when i login with the new account i found myself has admin permission on the organization

i hope you find anything useful after reading this :)

https://twitter.com/Conan0x3

https://hackerone.com/co0nan
