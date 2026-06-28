---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-07_workplace-by-facebook-unauthorized-access-to-companies-environment-275k.md
original_filename: 2021-05-07_workplace-by-facebook-unauthorized-access-to-companies-environment-275k.md
title: Workplace by Facebook | Unauthorized access to companies environment — $27,5k
category: documents
detected_topics:
- idor
- access-control
- command-injection
- otp
- rate-limit
- business-logic
tags:
- imported
- documents
- idor
- access-control
- command-injection
- otp
- rate-limit
- business-logic
language: en
raw_sha256: 2d18460921dc73fb33ba3334f573c32290e62a0ee29f642ac8d60e2ab295bbc0
text_sha256: 13707dae8c850b61908a095b8efcaea5828d0622e90944eb797ed0239363cc62
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Workplace by Facebook | Unauthorized access to companies environment — $27,5k

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-07_workplace-by-facebook-unauthorized-access-to-companies-environment-275k.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, otp, rate-limit, business-logic
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `2d18460921dc73fb33ba3334f573c32290e62a0ee29f642ac8d60e2ab295bbc0`
- Text SHA256: `13707dae8c850b61908a095b8efcaea5828d0622e90944eb797ed0239363cc62`


## Content

---
title: "Workplace by Facebook | Unauthorized access to companies environment — $27,5k"
page_title: "Workplace from Facebook | Unauthorized access to companies environment | by Marcos Ferreira | Medium"
url: "https://mvinni.medium.com/workplace-by-facebook-unauthorized-access-to-companies-environment-27-5k-a593a57092f1"
authors: ["Marcos Ferreira (@mvinni_)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Logic flaw", "IDOR"]
bounty: "27,500"
publication_date: "2021-05-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3669
scraped_via: "browseros"
---

# Workplace by Facebook | Unauthorized access to companies environment — $27,5k

Workplace from Facebook | Unauthorized access to companies environment
Marcos Ferreira
Follow
2 min read
·
May 7, 2021

247

2

Hello Everyone,

In this article, I will be describing a serious vulnerability I found in Workplace, an enterprise social network from Facebook.

Description:

In Workplace, the administrators can choose to activate an option called “self-invite”, which allows anyone to enter without having a verified email address by the admin.

Info: https://www.workplace.com/help/work/336227380906523

Although, the server wasn’t correctly verifying the email used on registration, allowing the creation of accounts through an email that wasn’t verified by the administrator.

This could have allowed a malicious user to access a company’s Workplace environment. But, this was only possible if the company enabled the self-invite feature.

Details:

I was able to find this issue by analyzing network traffic on the “Workplace from Facebook” Android application.

==

After registering a new account in my Workplace and revising Burp Suite history tab, I came across the following request:
Press enter or click to view image in full size

After some tests with this endpoint, I concluded that was possible to create accounts in other Workplaces just by modifying “community_id”

Get Marcos Ferreira’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Using a personal email account (@gmail.com), it was already possible to execute the vulnerability.

Reproduction Steps:
Requesting Activation Code:
POST /at_work/accounts_send_notification HTTP/1.1
Host: graph.workplace.com
identifier=test@gmail.com
pre_login_flow_type=SIGNUP
access_token=*****

Activation code successfully received.

2. Create a Facebook Workplace account:

POST /at_work/accounts_self_invite HTTP/1.1
Host: graph.workplace.com
identifier=test@gmail.com
nonce=998236
community_id=86381-----------
form_data={"name":"Test","password":"Test1234@"}
access_token=*****
nonce : activation code from first step.
community_id : Target company’s community ID.

==

Boom! The account has been successfully created, and now the attacker has free access to the files, photos, groups, emails and other data from the target company.

Without counting employees exposure…

==

However…

The attacker had to have the ID from the target company’s community. This was possible to get through brute force, or with some ex-employee from the company.
Some days after I received the bounty, I was able to find an endpoint which gives the community_id from any company in Workplace.
Timeline:

January 11, 2021 — Initial Report
January 25, 2021 — Triaged
February 9, 2021 — Bug Fixed
February 23, 2021 — Bounty awarded (27,5k)

Thank you for taking the time to read my article

My Twitter profile: https://twitter.com/mvinni_
