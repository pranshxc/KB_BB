---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-29_sensitive-data-leak-using-idor-in-integration-service.md
original_filename: 2020-12-29_sensitive-data-leak-using-idor-in-integration-service.md
title: Sensitive data leak using IDOR in integration service
category: documents
detected_topics:
- idor
- access-control
- command-injection
- rate-limit
- automation-abuse
- business-logic
tags:
- imported
- documents
- idor
- access-control
- command-injection
- rate-limit
- automation-abuse
- business-logic
language: en
raw_sha256: 4447a273aa4663da8135de1318ec25ca051d3a8be29c75a3c037ca127bcb4fb6
text_sha256: c1123607d8b367937d258d38527c39df25f2b0896f78f4e602f954a4822655e9
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Sensitive data leak using IDOR in integration service

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-29_sensitive-data-leak-using-idor-in-integration-service.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, rate-limit, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `4447a273aa4663da8135de1318ec25ca051d3a8be29c75a3c037ca127bcb4fb6`
- Text SHA256: `c1123607d8b367937d258d38527c39df25f2b0896f78f4e602f954a4822655e9`


## Content

---
title: "Sensitive data leak using IDOR in integration service"
url: "https://ronak-9889.medium.com/sensitive-data-leak-using-idor-in-integration-service-d9301be9c91e"
authors: ["Ronak Patel (@ronak_9889)"]
bugs: ["IDOR"]
publication_date: "2020-12-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4042
scraped_via: "browseros"
---

# Sensitive data leak using IDOR in integration service

Sensitive data leak using IDOR in integration service
Ronak Patel
Follow
4 min read
·
Dec 29, 2020

289

2

Hello Guys! Hope you are doing well in this pandemic.

This write up is about Bug, Which I found in private program before six months and resolved before two months. As I mentioned in my previous blog posts, I go by functionality to hunt for Bugs. I loved this bug due to how simple IDOR could create a Huge impact if linked with the existing functionality.

As this bug was reported to private program, I won’t be able to disclose program name. I would mention it as Redacted.com throughout this blog post. For better understanding, I would just mention that it is an app to generate forms for surveys, quiz and more, collect responses from those forms as well as integrate with other services.

Mostly I look for Business logic, IDORs and server-side bugs while hunting. I don’t follow any predefined or fixed methodology but just go with some basic recon, Try to understand normal flow of application and then go for hunting.

This bug was in the integration functionality. First I would describe basic flow of this functionality and then I would go step by step how I found this bug. There was a section to connect form’s responses to different platforms like Google analytics, Facebook Pixels and more. Owner could integrate his/her form to one of this apps using this functionality and he could receive form responses in integrated app.

While I was going through all the platforms available to integrate, I came across with the option to integrate with Zendesk sell. Zendesk sell is the application to analyze sales data like leads, contacts and more. So the flow of this functionality was like once started integration process it takes the form id and transfers the request flow to the third party application where you would asked to configure your Zendesk sell account, grant authorization and map form’s questions with the fields in the Zendesk sell. Once this has been done successfully, Form’s responses would be mapped to the Zendesk sell’s fields.

Upon observing request flow, I found that First GET request to initiate integration was getting generated, then requests to third party to configure authentication and mapping and lastly PATCH request to enable the integration. Both GET and PATCH requests were vulnerable to IDOR in form_id parameter.

I had two accounts created to test application, one as an attacker and another as a victim. As per below screenshot, I have started the integration, intercepted GET request and replaced form id to the victim’s form id.

Press enter or click to view image in full size
Victim form_id

After replacing form id to victim’s ID, I turned off interception and got landed to authentication and mapping page.

Get Ronak Patel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I have configured Zendesk sell account as an attacker and granted authorization. As per below screenshot it fetched victim form’s questions to map with attacker’s Zendesk sell account fields.

Press enter or click to view image in full size
Zendesk sell authorization
Press enter or click to view image in full size
Mapping victim form’s questions to attacker’s Zendesk sell fields

After finishing this configuration, I have intercepted next request which was PATCH request to enable integration and replaced form id with victim’s form id .

Press enter or click to view image in full size
Enable integration

After finishing this integration process on attacker’s account. To check whether it worked or not, I logged in to the victim’s account and I found integration got enabled.

To test further, I filled up form as a visitor, checked response received in victim’s account and attacker’s Zendesk sell account. As per below screenshots attacker received form response in his Zendesk sell account.

Press enter or click to view image in full size
Contact has been created with victim form’s received response to attacker’s Zendesk sell account

The question is how to enumerate form ids to integrate forms with our Zendesk account. Enumeration was very simple task as Link for sharing this form contained form_id value which we can use to integrate with our Zendesk account and simply receive all sensitive data being filled to those forms.

As per below screenshot, Simple google dork reveled form ids.

Press enter or click to view image in full size
Form id enumeration using google dork

Summing up, Using IDOR in this integration process, Attacker could integrate his Zendesk sell account with any form without any kind of user interaction and could fetch all Sensitive data received as a form response.

I hope this article was informative to you guys. Thanks for reading. Stay blessed Stay safe…..!!!!!!!!!!!!!!!!!!!
