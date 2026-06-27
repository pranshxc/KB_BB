---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1341133'
original_report_id: '1341133'
title: Subdomain takeover [​████████]
weakness: Privilege Escalation
team_handle: deptofdefense
created_at: '2021-09-16T07:36:39.503Z'
disclosed_at: '2021-10-13T22:17:30.087Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- privilege-escalation
---

# Subdomain takeover [​████████]

## Metadata

- HackerOne Report ID: 1341133
- Weakness: Privilege Escalation
- Program: deptofdefense
- Disclosed At: 2021-10-13T22:17:30.087Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The subdomain `███████` was pointing to an Azure Cloud App domain (araz-sp.centralus.cloudapp.azure.com), but that endpoint was not registered.

## Impact

It's extremely vulnerable to attacks as a malicious user could create any web page with any content and host it on the vulnerable domain. This would allow them to post malicious content which would be mistaken for a valid site. 

They could perform several attacks like:
 - Cookie Stealing
 - Phishing campaigns. 
 - Bypass Content-Security Policies and CORS.

 
## Recommendations for fix

* Remove the affected DNS record if not used 
 

### Supporting Material/References:

 - https://0xpatrik.com/subdomain-takeover/
 - https://hackerone.com/reports/661751

## System Host(s)
███████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Just go to 

http://████████ 

You will see a blank page, but checking the source code you will see proof of the take over. 

```
<html>  
<!-- poc by deleite --> 
 </html>
```

## Suggested Mitigation/Remediation Actions

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
