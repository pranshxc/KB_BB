---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1329792'
original_report_id: '1329792'
title: AWS subdomain takeover of www.███████
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2021-09-03T17:41:46.480Z'
disclosed_at: '2021-10-28T20:18:39.302Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- improper-access-control-generic
---

# AWS subdomain takeover of www.███████

## Metadata

- HackerOne Report ID: 1329792
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2021-10-28T20:18:39.302Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
The AWS bucket hosted on `www.████████` was vulnerable to a subdomain takeover. It has a DNS record pointing to an unclaimed bucket that I was able to register and serve a PoC on. 

## References
Output of `dig`:
```
;; QUESTION SECTION:
;www.███████.		IN	A

;; ANSWER SECTION:
www.████.	1833	IN	CNAME	██████████.
███. 60 IN	A	███████
█████. 60 IN	A	███
█████████. 60 IN	A	████████
█████. 60 IN	A	███

;; AUTHORITY SECTION:
█████. 1831 IN	NS	████.
███. 1831 IN	NS	█████████.
███████. 1831 IN	NS	██████.
██████. 1831 IN	NS	██████████.

;; ADDITIONAL SECTION:
█████████.	151098	IN	A	████
████.	153636	IN	A	████████
█████.	132552	IN	A	█████
███████. 6009	IN	A	███
████.	56631	IN	AAAA	███

```

## Impact

The impact for a subdomain takeover can be varied and wide: potentially steal cookies, bypass CSP and CORS policies, bypass domain whitelisting for SSRF, spy on legitimate requests sent to that domain, phising vector, etc.

## System Host(s)
www.█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Go to https://www.███████/█████████████████ which is the PoC I have hosted.

## Suggested Mitigation/Remediation Actions
Please remove all dangling DNS records if they are not needed, or claim the buckets if they are.

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
