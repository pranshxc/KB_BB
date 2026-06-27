---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '138622'
original_report_id: '138622'
title: Self-XSS on partners.uber.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-05-13T13:12:00.206Z'
disclosed_at: '2016-07-26T00:35:43.594Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Self-XSS on partners.uber.com

## Metadata

- HackerOne Report ID: 138622
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-07-26T00:35:43.594Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

I found a reflected XSS vulnerability in password reset page https://partners.uber.com/reset-password. 
I have tested this vulnerability in the latest Chrome and Firefox browsers.

Reproduction Steps:
1- Go to https://login.uber.com/forgot-password and reset password. Then, Click password reset link on your mailbox.
2- Paste  "><img src=x onerror=prompt(document.domain)>   as your new password and submit.
3- Wait and see XSS payload fired.

Also I added screenshots.

Thanks,

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
