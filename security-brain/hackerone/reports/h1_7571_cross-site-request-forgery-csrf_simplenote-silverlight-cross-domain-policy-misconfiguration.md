---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7571'
original_report_id: '7571'
title: Simplenote Silverlight cross-domain policy misconfiguration
weakness: Cross-Site Request Forgery (CSRF)
team_handle: automattic
created_at: '2014-04-14T15:29:06.951Z'
disclosed_at: '2014-05-17T19:01:03.094Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Simplenote Silverlight cross-domain policy misconfiguration

## Metadata

- HackerOne Report ID: 7571
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: automattic
- Disclosed At: 2014-05-17T19:01:03.094Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The Simplenote application publishes a [Silverlight cross-domain policy](https://app.simplenote.com/clientaccesspolicy.xml) which allows access from any domain.  

    <allow-from http-request-headers="*">
      <domain uri="http://*"/>
      <domain uri="https://*"/>
    </allow-from>

Allowing access from all domains means that any domain can perform two-way interaction with this application. This policy is likely to present a significant security risk.

If a user is logged in to the application, and visits a domain allowed by the policy (any domain, in this case), then any malicious content running on that domain can potentially gain full access to the application within the security context of the logged in user.

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
