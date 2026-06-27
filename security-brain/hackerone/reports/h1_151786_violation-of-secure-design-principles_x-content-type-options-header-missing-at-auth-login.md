---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '151786'
original_report_id: '151786'
title: X-Content-Type-Options header missing at Auth Login
weakness: Violation of Secure Design Principles
team_handle: gocd
created_at: '2016-07-16T16:25:52.299Z'
disclosed_at: '2016-08-18T08:43:38.406Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- violation-of-secure-design-principles
---

# X-Content-Type-Options header missing at Auth Login

## Metadata

- HackerOne Report ID: 151786
- Weakness: Violation of Secure Design Principles
- Program: gocd
- Disclosed At: 2016-08-18T08:43:38.406Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Again,

The doesn't have a header settings for X-Content-Type Options which means it is vulnerable to MIME sniffing. The only defined value, "nosniff", prevents Internet Explorer and Google Chrome from MIME-sniffing a response away from the declared content-type. This also applies to Google Chrome when downloading extensions. This reduces exposure to drive-by download attacks and sites serving user uploaded content that by clever naming could be treated by MSIE as executable or dynamic HTML files.

URL :- http://arbaz:8153/go/auth/login

Thanks!

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
