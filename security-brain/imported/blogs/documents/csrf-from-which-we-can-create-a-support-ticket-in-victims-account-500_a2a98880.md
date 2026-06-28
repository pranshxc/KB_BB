---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-21_csrf-from-which-we-can-create-a-support-ticket-in-victims-account-500.md
original_filename: 2021-05-21_csrf-from-which-we-can-create-a-support-ticket-in-victims-account-500.md
title: CSRF from which we can create a support ticket in Victim’s Account (500$)
category: documents
detected_topics:
- idor
- command-injection
- otp
- csrf
- supply-chain
tags:
- imported
- documents
- idor
- command-injection
- otp
- csrf
- supply-chain
language: en
raw_sha256: a2a988805f54bd7c692233e0683f1e1d7a4d1a63b137315ad82f36744fa7b067
text_sha256: 52f93e4cd884f20dd286d241c1c3cbc6a0abb190709ee0082747a513025cf26f
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# CSRF from which we can create a support ticket in Victim’s Account (500$)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-21_csrf-from-which-we-can-create-a-support-ticket-in-victims-account-500.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, csrf, supply-chain
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `a2a988805f54bd7c692233e0683f1e1d7a4d1a63b137315ad82f36744fa7b067`
- Text SHA256: `52f93e4cd884f20dd286d241c1c3cbc6a0abb190709ee0082747a513025cf26f`


## Content

---
title: "CSRF from which we can create a support ticket in Victim’s Account (500$)"
url: "https://rohitcoder.medium.com/csrf-from-which-we-can-create-a-support-ticket-in-victims-account-500-c1aa61f99c17"
authors: ["Rohit kumar (@rohitcoder)"]
programs: ["Meta / Facebook"]
bugs: ["CSRF"]
bounty: "500"
publication_date: "2021-05-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3631
scraped_via: "browseros"
---

# CSRF from which we can create a support ticket in Victim’s Account (500$)

CSRF from which we can create a support ticket in Victim’s Account (500$)
Rohit kumar
Follow
2 min read
·
May 20, 2021

10

1

Press enter or click to view image in full size

Complete Details
===

I found a CSRF from which we can create a Support ticket with the exact title “Your payouts have been disabled due to suspected fraud” in the victim’s account which may panic victim, but I wanted to report this issue because I think this may have a bigger impact, So I wanted FB team to investigate it and I also want to mention that while initiating this CSRF attack, it takes a value in parameter payee_id which takes PAGE ID in my case, and I noticed I can supply and PAGE ID there

I don’t know what’s going on FB’s Support Representative Side portal, so if there is any IDOR here in param payee_id then the attacker can use this to Trick FB’s Representative

Impact
===
Create a support ticket in the victim’s account

Get Rohit kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Steps
====

1. Create a test.html page and add this code

<body onload=’window.location.href=”https://business.facebook.com/payments/dcp/payout/support/?payee_id=123&onboarding_type=Dcp&payout_subtype=GTW"'></body>

2. upload it somewhere and send a link to the victim and after opening the link a new report will be created in the victim’s account

3. You can also open this link https://attacker.com/test.html (Step1 performed here), this will also create a report in your account.

This was definitely a low impact issue because we were able to create a support ticket with only specific subject lines, but what about this one? https://rohitcoder.medium.com/victims-anti-csrf-token-could-be-exposed-to-third-party-applications-installed-on-user-s-device-be8e40d511ba i don’t think this also deserves only 500$
