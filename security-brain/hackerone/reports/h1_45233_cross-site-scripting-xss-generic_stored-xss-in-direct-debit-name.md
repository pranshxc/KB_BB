---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '45233'
original_report_id: '45233'
title: Stored XSS in Direct debit name
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mobilevikings
created_at: '2015-01-26T17:48:27.727Z'
disclosed_at: '2015-03-04T14:19:37.770Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in Direct debit name

## Metadata

- HackerOne Report ID: 45233
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mobilevikings
- Disclosed At: 2015-03-04T14:19:37.770Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

1. Make new or edit old Direct debit (for example https://mobilevikings.be/en/account/easypay/correct-direct-debit-mandate/111366/)
2. Fill owners name with payload asdf'"><script>alert(document.cookie)</script>
3. Save form. 
We got Stored XSS in pages:
https://mobilevikings.be/en/account/easypay/
https://mobilevikings.be/en/account/easypay/history/111366/
https://mobilevikings.be/en/account/easypay/auto-sms-topup/?req_subscription=1030418
And admin area pages may be affected.

The really interesting thing is if we press https://mobilevikings.be/en/account/easypay/287740/suspend/ link we got this cookie setted:
Set-Cookie	messages="e052df5f3af892c7a61d74d0d9a6ab14c7f1631c$[[\"__json_message\"\0540\05425\054\"Successfully suspended asdf'\\\"><script>alert(document.cookie)</script> <span>BE61310126985517</span>\"]]"; Path=/

So we have a properly signed cookie with XSS payload. And if we found some way to setup it (it may be some xss on mobilevikings.be subdomain or CRLF issue in some data which used in header) we can use this xss vector too.

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
