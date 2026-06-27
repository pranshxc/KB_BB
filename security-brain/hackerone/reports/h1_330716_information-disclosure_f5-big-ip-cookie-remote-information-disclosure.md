---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '330716'
original_report_id: '330716'
title: F5 BIG-IP Cookie Remote Information Disclosure
weakness: Information Disclosure
team_handle: localtapiola
created_at: '2018-03-28T09:44:30.271Z'
disclosed_at: '2018-06-21T11:24:16.526Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: myynti.lahitapiolarahoitus.fi
asset_type: URL
max_severity: none
tags:
- hackerone
- information-disclosure
---

# F5 BIG-IP Cookie Remote Information Disclosure

## Metadata

- HackerOne Report ID: 330716
- Weakness: Information Disclosure
- Program: localtapiola
- Disclosed At: 2018-06-21T11:24:16.526Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Basic report information
**Summary:** 
The remote host for myynti.lahitapiolarahoitus.fi is appears to be an F5 BIG-IP load balancer(or behind load balancer) and the unencrypted cookie may disclose BigIP pool name, backend's IP address and port, routed domain.

**Description:** 
The remote host appears to be an F5 BIG-IP load balancer. The load balancer encodes the IP address of the actual web server that it is acting on behalf of within a cookie. Additionally, information after 'BIGipServer' is configured by the user and may be the logical name of the device. These values may disclose sensitive information, such as internal IP addresses and names.

As you can see, when i'm testing with curl, it will show like this
```
< Set-Cookie: BIGipServermy██████████oitus-fi_pool=2079████████6.0000; path=/
< Set-Cookie: TS013d0012=0147052ac538e5a096f03ce792d4dfca4fa7aa1446dea5089d1317f68b65cec609e178c83e1b5a758b8525b5d28fa72da9dc462362; Path=/
```

**Impact:**
Attacker can leaks backend information (pool name, backend's IP address and port, routed domain) through cookies inserted by the BigIP system.

## Browsers / Apps Verified In:

  * Metasploit

## Steps To Reproduce:

  For this case, you can use metasploit auxilary module to scan vuln:
```
use auxiliary/gather/f5_bigip_cookie_disclosure
set RHOST myynti.lahitapiolarahoitus.fi
run
```

## Additional material

  * I've attaching screenshot in this report

```
msf auxiliary(gather/f5_bigip_cookie_disclosure) > run

[*] Starting request /
[+] F5 BigIP load balancing cookie "BIGipServermy█████oitus-fi_pool = 2079██████████6.0000" found
[+] Load balancing pool name "my██████oitus-fi_pool" found
[+] Backend 19█████████2:81 found
```

## Remediations

  * Encrypting the cookies from BigIP : http://www.systemadvise.com/2016/11/f5-big-ip-cookie-remote-information.html

## Related reports, best practices

  * https://support.f5.com/csp/article/K14784?sr=45997495
  * http://www.systemadvise.com/2016/11/f5-big-ip-cookie-remote-information.html
  * https://www.rapid7.com/db/modules/auxiliary/gather/f5_bigip_cookie_disclosure

## Impact

Attacker can leaks backend information (pool name, backend's IP address and port, routed domain) through cookies inserted by the BigIP system.

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
