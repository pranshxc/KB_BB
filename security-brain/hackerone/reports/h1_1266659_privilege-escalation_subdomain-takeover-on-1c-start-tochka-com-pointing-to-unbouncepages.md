---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1266659'
original_report_id: '1266659'
title: Subdomain Takeover on 1c-start.tochka.com pointing to unbouncepages
weakness: Privilege Escalation
team_handle: qiwi
created_at: '2021-07-17T06:38:12.465Z'
disclosed_at: '2021-09-07T17:02:55.595Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: '*.tochka.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Subdomain Takeover on 1c-start.tochka.com pointing to unbouncepages

## Metadata

- HackerOne Report ID: 1266659
- Weakness: Privilege Escalation
- Program: qiwi
- Disclosed At: 2021-09-07T17:02:55.595Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Actuall this report is same as of this one:- https://hackerone.com/reports/38007  

Subdomain takeover vulnerabilities occur when a subdomain (subdomain.example.com) is pointing to a service (e.g. GitHub pages, Heroku, etc.) that has been removed or deleted. This allows an attacker to set up a page on the service that was being used and point their page to that subdomain. For example, if subdomain.example.com was pointing to a GitHub page and the user decided to delete their GitHub page, an attacker can now create a GitHub page, add a CNAME file containing subdomain.example.com, and claim subdomain.example.com.

Here there is a greenhouse domain (1c-start.tochka.com) which is pointing towards unbounce pages so this domain can be taken over can can be used to do any type of attacks mostly i can make a fake login page on your behalf and spoof your users, this is a critical vulnerability and needs to be fixed .

Vulnerable url : 1c-start.tochka.com

PoC
Snapshot of the vulnerable page(actually for taking over from unbounce i need to take a paid subscription hich is of higher cost neraly 150-200$ i cannot afford that so as a poc i m showing you a vulnerable page hoping this should work )
cname: unbouncepages.com
Name: 1c-start.tochka.com
Type: CNAME

Remediation
Remove the cname entry or claim the subdomain demo.greenhouse.io on unbounce.com
See also
https://github.com/EdOverflow/can-i-take-over-xyz#unbounce
https://labs.detectify.com/2014/10/21/hostile-subdomain-takeover-using-herokugithubdesk-more/
https://0xpatrik.com/subdomain-takeover/
https://medium.com/@ajdumanhug/subdomain-takeover-through-external-services-f0f7ee2b93bd
http://yassineaboukir.com/blog/neglected-dns-records-exploited-to-takeover-subdomains/

## Impact

Impact
Risk
fake website
malicious code injection
users tricking
company impersonation
This issue can have really huge impact on the companies reputation someone could post malicious content on the compromised site and then your users will think it's official but it's not.

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
