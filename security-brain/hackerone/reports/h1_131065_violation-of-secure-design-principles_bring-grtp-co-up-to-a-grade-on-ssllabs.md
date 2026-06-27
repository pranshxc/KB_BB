---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '131065'
original_report_id: '131065'
title: bring grtp.co up to A grade on SSLLabs
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2016-04-15T11:45:34.151Z'
disclosed_at: '2016-08-13T22:03:09.890Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# bring grtp.co up to A grade on SSLLabs

## Metadata

- HackerOne Report ID: 131065
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2016-08-13T22:03:09.890Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Issues at https://grtp.co/
reference for Weak SSL Ciphers:https://www.owasp.org/index.php/Testing_for_Weak_SSL/TLS_Ciphers,_Insufficient_Transport_Layer_Protection_(OTG-CRYPST-001)
Weak SSL Ciphers supported at port 443:
TLS 1.0:
 TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA (ec 256) - C
 TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA (dh 1024) - D
 TLS_RSA_WITH_3DES_EDE_CBC_SHA (rsa 4096) - C
TLSv1.2: 
TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA (ec 256) - C
TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA (dh 1024) - D
TLS_RSA_WITH_3DES_EDE_CBC_SHA (rsa 4096) - C
Evidence of Weak SSL ciphers is attached in figure 1

Weak SSH Ciphers supported at port 22:
Reference :https://www.tenable.com/plugins/index.php?view=single&id=70658
Supported CBC ciphers
aes128-cbc
3des-cbc
blowfish-cbc
cast128-cbc
aes192-cbc
aes256-cbc

Evidence related to supported CBC ciphers is attached in figure 2

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
