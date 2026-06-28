---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-20_i-obtained-admin-access-via-the-account-activation-link-in-30-seconds.md
original_filename: 2022-05-20_i-obtained-admin-access-via-the-account-activation-link-in-30-seconds.md
title: I Obtained ADMIN access via the Account Activation link [In 30 seconds]
category: documents
detected_topics:
- access-control
- command-injection
- cloud-security
tags:
- imported
- documents
- access-control
- command-injection
- cloud-security
language: en
raw_sha256: e8f11e0aa77cee7e2723be5dd0fe5a89484ceeeadf872bfb3007b74b670b3995
text_sha256: 25db0916454714752739b891b379d542ea98857c1176a485dc04ce769c2dbe22
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# I Obtained ADMIN access via the Account Activation link [In 30 seconds]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-20_i-obtained-admin-access-via-the-account-activation-link-in-30-seconds.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `e8f11e0aa77cee7e2723be5dd0fe5a89484ceeeadf872bfb3007b74b670b3995`
- Text SHA256: `25db0916454714752739b891b379d542ea98857c1176a485dc04ce769c2dbe22`


## Content

---
title: "I Obtained ADMIN access via the Account Activation link [In 30 seconds]"
url: "https://systemweakness.com/i-obtained-admin-access-via-account-activation-link-in-30-seconds-dd7f115ae1d2"
authors: ["popalltheshells"]
bugs: ["Privilege escalation", "Amazon cognito misconfiguration"]
publication_date: "2022-05-20"
added_date: "2023-02-09"
source: "pentester.land/writeups.json"
original_index: 2623
scraped_via: "browseros"
---

# I Obtained ADMIN access via the Account Activation link [In 30 seconds]

Member-only story

I Obtained ADMIN access via the Account Activation link [In 30 seconds]
popalltheshells
Follow
2 min read
·
May 20, 2022

33

1

Folks, for those of you who didn’t know, I absolutely have a blast every time I have to perform web app testing; because the way to exploit insecure designs are always different from one client to another.

I recently wrapped up a testing engagement and was able to discover a high-risk vulnerability that allows a regular user to escalate their privileges to a “admin” user via an account activation link.

Without giving too much information about a client; the web application I was testing is responsible for creating and managing alerts of a [confidentiality] building. As an admin you are able to set alerts, change alerts, manage users, etc. which is crucial for the day-to-day operations of the business. I’m talking may cause severe death or illness to [entity] should these configurations are tampered with.

When a new regular user is created, a link is sent to the user’s e-mail to activate its account

Following the process will call an AWS Cognito end-point API. Sometimes, these requests take form in multiple HTTP requests, in my case there were about 7 requests being submitted (username, passwd, etc.) before the affected request shows up, so be patient and make sure you analyze each request before giving up and turning “intercept” off.
