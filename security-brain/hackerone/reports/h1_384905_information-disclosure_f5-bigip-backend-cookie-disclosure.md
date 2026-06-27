---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '384905'
original_report_id: '384905'
title: F5 BigIP Backend Cookie Disclosure
weakness: Information Disclosure
team_handle: localtapiola
created_at: '2018-07-21T09:42:24.281Z'
disclosed_at: '2018-09-10T01:21:20.723Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: www.lahitapiolarahoitus.fi
asset_type: URL
max_severity: none
tags:
- hackerone
- information-disclosure
---

# F5 BigIP Backend Cookie Disclosure

## Metadata

- HackerOne Report ID: 384905
- Weakness: Information Disclosure
- Program: localtapiola
- Disclosed At: 2018-09-10T01:21:20.723Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Basic report information
**Summary:** 
The Same issue was reported on www.myynti.lahitapiolarahoitus.fi by another reporter. It was fixed for that. But when I test the same issue on lahitapiolarahoitus.fi. It is also causing leakage of information.

**Description:** 
I just identify F5 BigIP load balancers and leaks backend information (pool name, backend's IP address and port, routed domain) through cookies inserted by the BigIP system.

## Browsers / Apps Verified In:

  * MetaSploit Framework

## Steps To Reproduce:

MetaSploit commands:
1. `use auxiliary/gather/f5_bigip_cookie_disclosure`
2. `SET RHOST lahitapiolarahoitus.fi`
3. `run`

 OUTPUT:
`[*] Starting request /
[+] F5 BigIP load balancing cookie "BIGipServerltr-prod_pool = 224700608.20480.0000" found
[+] Load balancing pool name "ltr-prod_pool" found
[+] Backend 192.168.100.13:80 found
[*] Auxiliary module execution completed`

## Additional material

  * Refer to F322967 for domain lahitapiolarahoitus.fi
  * Refer to F322966 for domain myynti.lahitapiolarahoitus.fi (fixed)

## Related reports, best practices

Related Report: #330716
Refer to F322966 as it is Fixed.

## References:
https://www.rapid7.com/db/modules/auxiliary/gather/f5_bigip_cookie_disclosure
https://support.f5.com/csp/article/K14784%3Fsr%3D45997495
http://www.systemadvise.com/2016/11/f5-big-ip-cookie-remote-information.html

## Impact

Attacker can leaks back-end information (pool name, backend's IP address and port, routed domain) through cookies inserted by the BigIP system.

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
