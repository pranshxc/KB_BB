---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-14_my-weirdest-bug-bounty-getting-pii-from-o365.md
original_filename: 2020-03-14_my-weirdest-bug-bounty-getting-pii-from-o365.md
title: My Weirdest Bug Bounty — Getting PII from O365.
category: documents
detected_topics:
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: d648208d8f99e64cc165fb5cfe7c949f20e97bd7ab27df6edfaca0db60d5dcea
text_sha256: fb97c8ee718950b79204c0a291f4f05ca908d55f766d1edead603dcce3ab6022
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# My Weirdest Bug Bounty — Getting PII from O365.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-14_my-weirdest-bug-bounty-getting-pii-from-o365.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `d648208d8f99e64cc165fb5cfe7c949f20e97bd7ab27df6edfaca0db60d5dcea`
- Text SHA256: `fb97c8ee718950b79204c0a291f4f05ca908d55f766d1edead603dcce3ab6022`


## Content

---
title: "My Weirdest Bug Bounty — Getting PII from O365."
url: "https://medium.com/@omaidfaizyar/my-weirdest-bug-bounty-getting-pii-from-o365-b4477f4739e"
authors: ["Omaid Faizyar (@rulesofthetrade)"]
programs: ["Microsoft"]
bugs: ["Subdomain takeover"]
bounty: "1,000"
publication_date: "2020-03-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4710
scraped_via: "browseros"
---

# My Weirdest Bug Bounty — Getting PII from O365.

1

·

Top highlight

My Weirdest Bug Bounty — Getting PII from O365.
Omaid Faizyar
Follow
2 min read
·
Mar 14, 2020

207

3

Press enter or click to view image in full size
TLDR; My boss quit. I registered a domain and found the weirdest vulnerability in my entire career.
My boss quit.

I looked at his account on Microsoft Teams and noticed something odd..his email was set to unknown@af4716f4–406e-409b-acc1-b8bf9efe83fa.com.

Before he quit, it was john@[company].com

I recognized af4716f4–406e-409b-acc1-b8bf9efe83fa as a sort of ResourceID or TenantID in Azure.

For some reason, when Azure AD Accounts are deactivated, O365 doesn’t set the email to null, but to ‘unknown@af4716f4–406e-409b-acc1-b8bf9efe83fa.com’…O365’s version of null?

The problem.

After looking up ‘af4716f4–406e-409b-acc1-b8bf9efe83fa.com’ I found it wasn’t a registered domain!

I registered the domain, set up a server, forwarded all emails to my personal email and forgot about it.

Things got interesting on Monday

My inbox was flooded with meeting invitations and email chains from Azure customers, including Microsoft themselves.

Get Omaid Faizyar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I assume the process went something like this:

Bob leaves company/gets fired

Bobs email is set to unknown@af4716f4–406e-409b-acc1-b8bf9efe83fa.com

People CC Bob on email out of habit or he’s still in an email list

Press enter or click to view image in full size

This confirmed there wasn’t a misconfiguration or glitch on our Azure Cloud, it was pervasive and every Azure customer was vulnerable to it. Because I was invited to these meetings, I could actually also JOIN these video meetings too(though I didn’t).

Running Responder on a VPS I spun up, I was also able to get NTLM hashes. Although they were now useless because the accounts are inactive.

Press enter or click to view image in full size
Really really really really really bad engineering practices going on.

For my trouble, Microsoft’s Bug Bounty gave me $1,000. Not bad for 10 minutes of work.

Press enter or click to view image in full size

This is definitely the weirdest vulnerability I’ve found in my entire career. To this day I’m still not 100% sure how it works, only theories.
