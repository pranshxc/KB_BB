---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-09_privilege-escalation-using-api-endpoint.md
original_filename: 2019-08-09_privilege-escalation-using-api-endpoint.md
title: Privilege Escalation using Api endpoint
category: documents
detected_topics:
- access-control
- command-injection
- webhooks
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- webhooks
- api-security
language: en
raw_sha256: 26e160ed1b9b3d81ad9c11b4ac59b6b9bf6cb73f222ef0c90623861131bd5002
text_sha256: 388794aed667a6bdb978977fe6dfd06b49e2435f556ca7c9be190c670e652c42
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Privilege Escalation using Api endpoint

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-09_privilege-escalation-using-api-endpoint.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, webhooks, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `26e160ed1b9b3d81ad9c11b4ac59b6b9bf6cb73f222ef0c90623861131bd5002`
- Text SHA256: `388794aed667a6bdb978977fe6dfd06b49e2435f556ca7c9be190c670e652c42`


## Content

---
title: "Privilege Escalation using Api endpoint"
url: "https://medium.com/@ronak_9889/privilege-escalation-using-api-endpoint-fce841caaff3"
authors: ["Ronak Patel (@ronak_9889)"]
bugs: ["Privilege escalation"]
publication_date: "2019-08-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5091
scraped_via: "browseros"
---

# Privilege Escalation using Api endpoint

Privilege Escalation using Api endpoint
Ronak Patel
Follow
3 min read
·
Aug 9, 2019

200

1

Hi All,

This article is about bug i found on a private program on which i was invited few months back. I am not allowed to disclose any information about program so i would use program name as example.com.

Upon invitation this program assigns test accounts to the researcher to test application and those test accounts has normal user level permissions assigned. Main functionality of the application was related to provide employee background check service and with the normal user permission you can only create candidate,read reports and manage reports… such basic functionalities. I couldn’t find anything with the basic access i got.

I observed that this application was using the angularjs as a client side javascript framework and hence I decided to open the developer console and read the application js file available to learn more about routing, permissions and endpoints available.

Upon reading the code, i found that application has functionality to create webhooks to receive candidate reports and more notifications as per below screenshot.

Press enter or click to view image in full size
Create Webhook Endpoint

So, Further i decided to check which permission is required to create webhooks and as per code in below screenshot, it required manage_dev_settings permission which is by default assigned to only admin users.

Manage_dev_permission

With this findings, i though as this is the client side check if i can edit the response which contains the user permissions , i can get the UI level access of the developer settings.

Get Ronak Patel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I logged in again and set my Burp proxy to intercept all the response and it has been found that response from the http request to “api.example.com/user” contains user permissions as per below screenshot.

Press enter or click to view image in full size
response with user permission

As highlighted in response, i switched the manage_dev_settings from false to true and forwarded the response. Now i got the UI level access of the developer settings with the normal user test account.

Now,I navigated to the create webhook functionality,created webhook with the requestbin link and created new candidate which generated post request to the endpoint “api.example.com/v1/webhooks”. Luckily, i found that there was no permission validation at server level and webhook was created successfully. I immediately created new candidate and i received webhook log on my requestbin link as below.

Press enter or click to view image in full size
Webhook Log

So, this is how i was able to create webhook and receive notification with the normal user permission by escalating privileges.

You might be thinking that i could have skipped this UI level stuff and directly achieved this by firing request to the api endpoint of webhook found from the Js file directly. Yes, i could have done that but i wanted to learn as much as about the application so i gained first UI level access and then i verified this endpoint.

I submitted this bug to the program and initially it was triaged but one month later, I was informed that this was a duplicate and i didn’t get paid which was little bit disappointing but it is not always about chasing stuffs and being needy, sometimes it brings the inner satisfaction by slowing yourself down,learning new stuffs that you already don’t know,going as deeper as you can and push you limitations which i received as a reward by working with this program and finding this bug.

Thanks for reading this article.
