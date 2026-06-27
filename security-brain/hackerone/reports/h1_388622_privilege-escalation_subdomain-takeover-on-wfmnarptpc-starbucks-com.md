---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '388622'
original_report_id: '388622'
title: Subdomain takeover on wfmnarptpc.starbucks.com
weakness: Privilege Escalation
team_handle: starbucks
created_at: '2018-07-30T22:20:33.463Z'
disclosed_at: '2018-08-09T21:09:10.902Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 88
asset_identifier: Other non domain specific items
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Subdomain takeover on wfmnarptpc.starbucks.com

## Metadata

- HackerOne Report ID: 388622
- Weakness: Privilege Escalation
- Program: starbucks
- Disclosed At: 2018-08-09T21:09:10.902Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

this is pretty serious security issue in some context, so please act as fast as possible.

Overview:
One of the starbucks.com subdomains is pointing to Azure, which has unclaimed CNAME record. ANYONE is able to own starbucks.com subdomain at the moment.

This vulnerability is called subdomain takeover. You can read more about it here:

https://0xpatrik.com/subdomain-takeover-basics/

Details:
wfmnarptpc.starbucks.com has CNAME to s00149tmppcrpt.trafficmanager.net. However, s00149tmppcrpt.trafficmanager.net is not registered in Azure cloud anymore and thus can be registered by anyone. After registering the TrafficManager Profile in Azure portal, the person doing so has full control over content on wfmnarptpc.starbucks.com.

PoC:
http://wfmnarptpc.starbucks.com/poc.html

 Mitigation:
Remove the CNAME record from starbucks.com DNS zone completely.
Claim it back in Azure portal after I release it
Regards,

Patrik Hudak

## Impact

Subdomain takeover is abused for several purposes:

Malware distribution
Phishing / Spear phishing
XSS
Authentication bypass
...
List goes on and on. Since some certificate authorities (Let's Encrypt) require only domain verification, SSL certificate can be easily generated.

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
