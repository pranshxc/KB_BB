---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '123849'
original_report_id: '123849'
title: Cookie Does Not Contain The "secure" Attribute
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2016-03-17T05:53:38.636Z'
disclosed_at: '2016-04-02T05:01:51.629Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Cookie Does Not Contain The "secure" Attribute

## Metadata

- HackerOne Report ID: 123849
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2016-04-02T05:01:51.629Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Poc :

https://gratipay.com/ -- optimizelyBuckets=%7B%7D; expires=Sat Mar 14 21:28:25 2026; path=/; domain=.gratipay.com; max-age=315359448,https://gratipay.com/ -- optimizelyEndUserId=oeu1458188905178r0.282567850779742; expires=Sat Mar 14 21:28:25 2026; path=/; domain=.gratipay.com; max-age=315359448,https://gratipay.com/ -- optimizelySegments=%7B%7D; expires=Sat Mar 14 21:28:25 2026; path=/; domain=.gratipay.com; max-age=315359448,https://gratipay.com/ -- optimizelyPendingLogEvents=%5B%5D; expires=Wed Mar 16 21:28:40 2016; path=/; domain=.gratipay.com


Impact:
Cookies with the "secure" attribute are only permitted to be sent via HTTPS. Session cookies sent via HTTP expose an unsuspecting user to sniffing attacks that could lead to user impersonation or compromise of the application account.

Solution:
If the associated risk of a compromised account is high, apply the "secure" attribute to cookies and force all sensitive requests to be sent via HTTPS.

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
