---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '399165'
original_report_id: '399165'
title: Possible Subdomain Takeover
team_handle: khanacademy
created_at: '2018-08-24T22:43:21.485Z'
disclosed_at: '2018-08-31T15:27:45.184Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
---

# Possible Subdomain Takeover

## Metadata

- HackerOne Report ID: 399165
- Weakness: 
- Program: khanacademy
- Disclosed At: 2018-08-31T15:27:45.184Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

None of the weakness categories really fit this so I apologize for that.

The subdomain learnstormindia.khanacademy.org  points to 52.203.185.84 a webflow.io proxy server (proxy-ssl.webflow.com). The CNAME entry in the subdomain is pointing to an external page service (learnstormindia.khanacademy.org. 299 IN CNAME proxy-ssl.webflow.com)Because it 404s, this leads me to believe that a subdomain takeover is possible through the webflow service as whatever this is pointing to is unused.
IF it is possible to TAKEOVER 
therefore,by these steps the attacker should takeover this subdomian
1>Creat an account at webflow.io 
2>Creat a webpage(fake login page) to host and add you custom domian learnstormindia.khanacademy.org (for adding custom subdomian you need a paid account of webflow.io someabout $15)

## Impact

Subdomain takeover can be used for several purposes:
1>Malware
2>Phishing / Spear phishing
3>XSS
4>Authentication bypass

ex:-
An attacker can utilize this domain learnstormindia.khanacademy.org for targeting the organization by fake login khanacademy forms, or steal sensitive information of teams (credentials, credit card information, etc)

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
