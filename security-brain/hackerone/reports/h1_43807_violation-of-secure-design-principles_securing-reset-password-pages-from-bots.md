---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '43807'
original_report_id: '43807'
title: Securing "Reset password" pages from bots
weakness: Violation of Secure Design Principles
team_handle: vimeo
created_at: '2015-01-14T22:23:45.125Z'
disclosed_at: '2017-01-31T14:25:30.256Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- violation-of-secure-design-principles
---

# Securing "Reset password" pages from bots

## Metadata

- HackerOne Report ID: 43807
- Weakness: Violation of Secure Design Principles
- Program: vimeo
- Disclosed At: 2017-01-31T14:25:30.256Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I found a security issue on your "Reset password" page

Google botnets are indexing some of your sensitive pages with tokens of accounts.

For this you may like to add:
<meta name="robots" content="noindex,nofollow">

(For pages like "resetting your password" need to have this.)

Vulnerable url:
https://vimeo.com/forgot_password/7173461/x5vozxp0d6aqh5ja

Real Proof:
https://www.google.cl/search?q=site:vimeo.com+inurl:forgot_password/&num=100&safe=off&client=firefox-a&hs=Ehs&rls=org.mozilla:en-US:official&channel=sb&filter=0&biw=1280&bih=672

(Please note that this pages are index by Google already )

This is not a super serious bug I agree.  but still if user don't change the password this link will be active for some longer time it can be access by Google.

PS: it also a good Idea to add /forgot_password/* to http://vimeo.com/robots.txt

Any problems reproducing this bug please let me know.

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
