---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '329862'
original_report_id: '329862'
title: Stored xss in shop name @ lp.reverb.com
weakness: Cross-site Scripting (XSS) - Stored
team_handle: reverb
created_at: '2018-03-26T04:04:28.168Z'
disclosed_at: '2018-10-01T12:47:19.119Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored xss in shop name @ lp.reverb.com

## Metadata

- HackerOne Report ID: 329862
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: reverb
- Disclosed At: 2018-10-01T12:47:19.119Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

hello team,

There is a stored xss in lp.reverb.com.
Attacker can inject malicious script into server while adding shop name as `lll"></script><script>alert('xss');</script>`.
Exploit: https://lp.reverb.com/shops/faniyos-boutique/listings

Steps to reproduce:
1. Navogate to https://reverb.com/my/lp_shop/edit
2. Change your lp shop name to this: lll"></script><script>alert('xss')</script>
3. Save the changes.
4. View your lp shop.

Fix:
Sanitise the given input in the backend and encode the special characters.

Thanks,
Sandeep

## Impact

Attack can save malicious script directly into the server. Malicious script can be used to gain users session.

The hacker selected the **Cross-site Scripting (XSS) - Stored** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://lp.reverb.com/shops/faniyos-boutique/listings

**Verified**
Yes

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
