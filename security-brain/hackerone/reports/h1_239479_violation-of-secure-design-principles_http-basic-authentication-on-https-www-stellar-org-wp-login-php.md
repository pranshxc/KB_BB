---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '239479'
original_report_id: '239479'
title: HTTP - Basic Authentication on https://www.stellar.org/wp-login.php
weakness: Violation of Secure Design Principles
team_handle: stellar
created_at: '2017-06-13T06:25:16.168Z'
disclosed_at: '2017-06-13T14:00:12.958Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 6
tags:
- hackerone
- violation-of-secure-design-principles
---

# HTTP - Basic Authentication on https://www.stellar.org/wp-login.php

## Metadata

- HackerOne Report ID: 239479
- Weakness: Violation of Secure Design Principles
- Program: stellar
- Disclosed At: 2017-06-13T14:00:12.958Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Greetings, noticed https://www.stellar.org/wp-login.php using basic authentication.

#PoC:
YWRtaW46YWRtaW4= is base64 encode of admin:admin
#Impact:

Vulnerable to client side attacks.
Vulnerable to MITM attack.
Vulenrable to Eavesdropping attack.
Vulnerable to Brute force attacks.

#Fix:
HTTP-Basic Authentication should be changed for HTTP-Digest Authentication.

Let me know if any further info is required.

Regards,
Mr.R3boot.

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
