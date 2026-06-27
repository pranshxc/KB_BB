---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '634488'
original_report_id: '634488'
title: Broken Authentication and Session Management Flaw After Change Password and
  Logout
weakness: Violation of Secure Design Principles
team_handle: omise
created_at: '2019-07-03T15:24:20.575Z'
disclosed_at: '2020-11-08T07:36:53.457Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 39
asset_identifier: go.exchange
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Broken Authentication and Session Management Flaw After Change Password and Logout

## Metadata

- HackerOne Report ID: 634488
- Weakness: Violation of Secure Design Principles
- Program: omise
- Disclosed At: 2020-11-08T07:36:53.457Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

####Summary
Usually it's happened that when you change password or sign out from one place (or one browser), automatically someone who is open same account will sign out too from another browser. Basically your session destroyed at server side...
But in your site, it still alive..

####PoC
Detail About Vulnerability and PoC on Attachment File

Noted: You can try these vulnerability in another site. (e.g cryptfolio.com, facebook.com, etc). It's not alive when another has changed password and sign out

For More Information about This Vulnerability You can check OWASP Guide

[https://www.owasp.org/index.php?title=Broken_Authentication_and_Session_Management&setlang=en](https://www.owasp.org/index.php?title=Broken_Authentication_and_Session_Management&setlang=en)

####Attachment Video
[https://gofile.io/?c=Vt4m42](https://gofile.io/?c=Vt4m42)

## Impact

Account profile still can be edited even in another browser the account has signedout and changed password

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
