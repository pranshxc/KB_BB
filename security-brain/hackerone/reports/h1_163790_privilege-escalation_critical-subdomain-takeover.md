---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '163790'
original_report_id: '163790'
title: '[Critical] Subdomain Takeover'
weakness: Privilege Escalation
team_handle: instacart
created_at: '2016-08-27T10:36:24.309Z'
disclosed_at: '2016-09-20T22:46:35.352Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 12
tags:
- hackerone
- privilege-escalation
---

# [Critical] Subdomain Takeover

## Metadata

- HackerOne Report ID: 163790
- Weakness: Privilege Escalation
- Program: instacart
- Disclosed At: 2016-09-20T22:46:35.352Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Your Subdomains are pointing to unconfigured heroku app.
You should immediately remove the DNS-entry. Any One Can Claim That Domain , Please
Read The Advisory Below.


::: Nslookup of Subdomains Not Claimed :::::
i)  0x00hack3r@pirateking:~ % nslookup bugs.instacart.com
Server:		192.168.1.11
Address:	192.168.1.11#53

Non-authoritative answer:
bugs.instacart.com	canonical name = akita-7862.herokussl.com.
akita-7862.herokussl.com	canonical name = elb070827-1683851829.us-east-1.elb.amazonaws.com.
Name:	elb070827-1683851829.us-east-1.elb.amazonaws.com
Address: 50.17.211.105
Name:	elb070827-1683851829.us-east-1.elb.amazonaws.com
Address: 54.225.201.77
Name:	elb070827-1683851829.us-east-1.elb.amazonaws.com
Address: 23.23.106.52

ii) 0x00hack3r@pirateking:~ % nslookup atlas.instacart.com
Server:		192.168.1.11
Address:	192.168.1.11#53

Non-authoritative answer:
atlas.instacart.com	canonical name = tochigi-6557.herokussl.com.
tochigi-6557.herokussl.com	canonical name = elb070826-1853155728.us-east-1.elb.amazonaws.com.
Name:	elb070826-1853155728.us-east-1.elb.amazonaws.com
Address: 54.204.29.82
Name:	elb070826-1853155728.us-east-1.elb.amazonaws.com
Address: 107.20.229.78
Name:	elb070826-1853155728.us-east-1.elb.amazonaws.com
Address: 54.235.189.162


Subdomain pointing to a non-existing Heroku app showing: there is no app configured at that hostname


I have attached screenshots : For the impacts, vuln see : https://labs.detectify.com/2014/10/21/hostile-subdomain-takeover-using-herokugithubdesk-more/

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
