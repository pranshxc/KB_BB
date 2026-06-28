---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-20_privilege-escalation-leads-to-making-authenticated-actions-payment-processing-cr.md
original_filename: 2022-09-20_privilege-escalation-leads-to-making-authenticated-actions-payment-processing-cr.md
title: Privilege Escalation Leads to making authenticated actions (payment processing,
  creating invoices.. etc)
category: documents
detected_topics:
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
language: en
raw_sha256: 2dad73c7bed1c0ef7177dcb274b7472fa510e9e768c8587a21caed92b79d3d33
text_sha256: 9b77806d12270a06b5e8ef36b037f8542c30c6e0286e56236be5077165293a75
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Privilege Escalation Leads to making authenticated actions (payment processing, creating invoices.. etc)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-20_privilege-escalation-leads-to-making-authenticated-actions-payment-processing-cr.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `2dad73c7bed1c0ef7177dcb274b7472fa510e9e768c8587a21caed92b79d3d33`
- Text SHA256: `9b77806d12270a06b5e8ef36b037f8542c30c6e0286e56236be5077165293a75`


## Content

---
title: "Privilege Escalation Leads to making authenticated actions (payment processing, creating invoices.. etc)"
page_title: "Introduction. Introduction | by X-Vector | Medium"
url: "https://x-vector.medium.com/privilege-escalation-leads-to-making-authenticated-actions-payment-processing-creating-invoices-2cf808d517ed"
authors: ["X-Vector (@XVector11)"]
bugs: ["Privilege escalation", "Broken authorization"]
publication_date: "2022-09-20"
added_date: "2022-09-22"
source: "pentester.land/writeups.json"
original_index: 2149
scraped_via: "browseros"
---

# Privilege Escalation Leads to making authenticated actions (payment processing, creating invoices.. etc)

X-Vector
Follow
3 min read
·
Sep 20, 2022

49

Privilege Escalation Leads to making authenticated actions (payment processing, creating invoices.. etc)
Introduction

Today, I’m going to show how unauthenticated users can make (payment processing, creating invoices.. etc)!

First of all, This was a public program, but the vulnerability is not fixed yet so I will refer to it with target.com.

This domain is sandbox but they said

We have ensured the sandbox has the same functionality needed for testing

Summary

When a user creates a new account he must wait for the acceptance period (2–3 days) during this period he should not be able to make authenticated actions e.g (payment processing, creating invoices.. etc) since he’s not accepted yet. however this case it’s not applied to the API keys acquired from commerce/account/apiKeys?

Proof Of Concept

When a user registers a new account on `target.com/commerce`, he waits a few days for approval or rejection. When this user tries to log in to their account, he redirects to

Get X-Vector’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

target.com/commerce/login/auth -> target.com/commerce/login/dashboard -> target.com/commerce/login/denied

Press enter or click to view image in full size

I tried to log in again and stop at `target.com/commerce/login/dashboard` then I found the user can access his dashboard and can have the authorized to see his account, customer, payment, Settings … etc and he can’t make any action. it’s just view pages.

Press enter or click to view image in full size
Press enter or click to view image in full size

But if we see the requests sent in burp, we will find API key endpoint `commerce/apiKeys?appkey=false&source=Ecomerce` which is related to the user’s account

Press enter or click to view image in full size

Although he cannot access the API without logging in (as it was not approved or rejected)

Press enter or click to view image in full size

After getting API keys I went to their API documentation and see how I can [create, list, update, delete & find] The [payment, plan, invoices …. etc] all and all of these functions worked with me :”D this is the result

Press enter or click to view image in full size
Press enter or click to view image in full size

Bug Submitted in Apr 2021 and is not fixed until now :”D
