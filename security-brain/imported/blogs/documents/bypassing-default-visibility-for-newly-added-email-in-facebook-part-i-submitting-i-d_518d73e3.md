---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-25_bypassing-default-visibility-for-newly-added-email-in-facebookpart-i-submitting-.md
original_filename: 2022-02-25_bypassing-default-visibility-for-newly-added-email-in-facebookpart-i-submitting-.md
title: Bypassing default visibility for newly-added email in Facebook(Part I - Submitting
  I.D)
category: documents
detected_topics:
- command-injection
- password-reset
- business-logic
- cloud-security
tags:
- imported
- documents
- command-injection
- password-reset
- business-logic
- cloud-security
language: en
raw_sha256: 518d73e30eb66ea649c77da5e657c134409e550eddc9a78eea00472fdeaf0c9c
text_sha256: dd6f7477c655c5c6e28a2acbf723d8fe78b7130af8cb7132146cce3219e116fc
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing default visibility for newly-added email in Facebook(Part I - Submitting I.D)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-25_bypassing-default-visibility-for-newly-added-email-in-facebookpart-i-submitting-.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, business-logic, cloud-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `518d73e30eb66ea649c77da5e657c134409e550eddc9a78eea00472fdeaf0c9c`
- Text SHA256: `dd6f7477c655c5c6e28a2acbf723d8fe78b7130af8cb7132146cce3219e116fc`


## Content

---
title: "Bypassing default visibility for newly-added email in Facebook(Part I - Submitting I.D)"
url: "https://medium.com/@Kntjrld/bypassing-default-visibility-for-newly-added-email-in-facebook-part-i-submitting-i-d-da78142f032d"
authors: ["Kent Jarold Abulag (@wkemenhehehegsg)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
bounty: "1,500"
publication_date: "2022-02-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2870
scraped_via: "browseros"
---

# Bypassing default visibility for newly-added email in Facebook(Part I - Submitting I.D)

Bypassing default visibility for newly-added email in Facebook(Part I - Submitting I.D)
Kent Jarold Abulag
Follow
3 min read
·
Feb 25, 2022

109

1

Press enter or click to view image in full size
Meta BBP

This bug is first announced at Facebook Bug Bounty page where they called it Visibility Setting Bug and thanks to 
Saugat Pokharel
 for sharing his findings. First, the default visibility for newly-added contact in Facebook is always set to "Only Me". However through Facebook account recovery, I noticed that the email address that added to account is in unexpected privacy.

Press enter or click to view image in full size
Facebook Email after confirming user identity
Steps to reproduce

1. Go to facebook.com/login/identify and find your Facebook account.
2. Click "No longer have access to these?" and choose "I cannot access my Email".
3. Enter a new email address and upload supported documents.
4. When you receive the email of Facebook about confirming your identity, login your account and check the visibility setting of the new added email address to your account.

In this case, Facebook Security added the new email address with visibility that set to "Friends".

Get Kent Jarold Abulag’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This report got two requested review because they don’t consider it as valid. I tried to clarify my report until I received this reply.

Press enter or click to view image in full size
Closed as Informative

So I understand why they don’t consider it as valid, But after 5 days I received this reply.

Press enter or click to view image in full size
Tagged as valid report

This is the link of my part II write-up related to this issue:

Bypassing default visibility for newly-added email in Facebook(Part II - Trusted Contacts)
After 3 months, I manage to bypassed again the default visibility for newly-added email in Facebook. This is my first…

medium.com

To understand more this issue here’s the first security researcher write-up regarding to this issue:

A Facebook bug that exposes email/phone number to your friends
Hi, I am Saugat from Kathmandu, Nepal. This is a writeup about a bug which I found recently on Facebook.

iamsaugat.medium.com

Timeline:

06 -SEP-2021 - Initial Report
08-SEP-2021 - Closed my report
08-SEP-2021 - Requested a review
10-SEP- 2021 - Closed my report
10-SEP- 2021 - Requested a review again
14-SEP-2021 - Closed my report again
19-SEP-2021 - Considered my report as eligible
05-OCT-2021 - Rewarded $x,xxx but fix is still pending
13-OCT-2021 - Fixed
