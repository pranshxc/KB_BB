---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-25_part-ii-trusted-contacts.md
original_filename: 2022-02-25_part-ii-trusted-contacts.md
title: Part II - Trusted Contacts
category: documents
detected_topics:
- command-injection
- business-logic
tags:
- imported
- documents
- command-injection
- business-logic
language: en
raw_sha256: 3e5e489827f317d25d0e66c6c83eef8de8124757af6d03ea07584b646288cd89
text_sha256: 33766a220fd91fad8c2d9e39a576c868bb96376a70025d6c5b54496b2a5f9cea
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Part II - Trusted Contacts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-25_part-ii-trusted-contacts.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `3e5e489827f317d25d0e66c6c83eef8de8124757af6d03ea07584b646288cd89`
- Text SHA256: `33766a220fd91fad8c2d9e39a576c868bb96376a70025d6c5b54496b2a5f9cea`


## Content

---
title: "Part II - Trusted Contacts"
page_title: "Bypassing default visibility for newly-added email in Facebook(Part II - Trusted Contacts) | by Kent Jarold Abulag | Medium"
url: "https://medium.com/@Kntjrld/bypassing-default-visibility-for-newly-added-email-in-facebook-part-ii-trusted-contacts-36176eeb103"
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

# Part II - Trusted Contacts

Bypassing default visibility for newly-added email in Facebook(Part II - Trusted Contacts)
Kent Jarold Abulag
Follow
2 min read
·
Feb 25, 2022

53

Press enter or click to view image in full size
Meta BBP

How I managed to bypassed again the default visibility for newly-added email in Facebook. Here is the link of my first write-up related to issue:

Bypassing default visibility for newly-added email in Facebook(Part I - Submitting I.D)
This bug is first announced at Facebook Bug Bounty page where they called it Visibility Setting Bug and thanks to…

medium.com

Steps to reproduce:

Get Kent Jarold Abulag’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1. Go to Facebook Settings > Password and Security > Setting up extra security and choose 3 trusted contacts.
2. Go to facebook.com/login/identify and find your Facebook account.
3. Click "No longer have access to these?" and provide valid email address.
4. Get all recovery code from your 3 trusted contacts and follow the instruction provided to create a successful recovery.
5. Check the visibility of new added email using own account or other account.

Press enter or click to view image in full size
Timeline:

21 January 2022 - Initial Report
25 January 2022 - Provided some details
26 January 2022 - Triage
24 February 2022 - Fixed and awarded $xxx
