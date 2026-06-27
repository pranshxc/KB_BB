---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '28632'
original_report_id: '28632'
title: Email field filtering problem.
weakness: Improper Authentication - Generic
team_handle: mavenlink
created_at: '2014-09-19T19:11:47.764Z'
disclosed_at: '2014-11-17T14:30:52.473Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Email field filtering problem.

## Metadata

- HackerOne Report ID: 28632
- Weakness: Improper Authentication - Generic
- Program: mavenlink
- Disclosed At: 2014-11-17T14:30:52.473Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

From the page: **https://app.mavenlink.com/settings/email**
When I tried to update the email address, I noticed that the database field was allocating 255 characters there.And if the input was more than 255 character that field was truncating.
For example:
``` text
haxorsistz+axorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxoailrsistzhaxoaaaaaaaa@gmail.com
```
This is a **265** character address.Though as per  RFC the maximum length allowed for an email address is 255 characters.
But when I submitted that info,that was truncated and stored first 255 characters to the database.So the email address which was stored into database was:
```text
haxorsistz+axorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxorsistzhaxoailrsistzhaxoaaaaaaaa
```
Which is an invalid email address,without any @ and trailing domain name.

So,I suggest mavenlink to check the submitted character length and the validity of that email address before storing it to database to prevent further errors.

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
