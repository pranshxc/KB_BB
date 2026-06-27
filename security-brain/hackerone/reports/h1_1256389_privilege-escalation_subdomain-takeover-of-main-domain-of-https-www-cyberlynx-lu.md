---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1256389'
original_report_id: '1256389'
title: Subdomain takeover of main domain of https://www.cyberlynx.lu/
weakness: Privilege Escalation
team_handle: acronis
created_at: '2021-07-09T20:59:39.026Z'
disclosed_at: '2021-10-12T09:15:47.619Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 63
asset_identifier: Other Acronis Domains
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- privilege-escalation
---

# Subdomain takeover of main domain of https://www.cyberlynx.lu/

## Metadata

- HackerOne Report ID: 1256389
- Weakness: Privilege Escalation
- Program: acronis
- Disclosed At: 2021-10-12T09:15:47.619Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary
Hi Acronis Security Team , Hope you well.
I found one of your subdomains which is `www.cyberlynx.lu` (One of your Acquisition)  is pointing towards

`
www.cyberlynx.lu	canonical name = www118.wixdns.net.
www118.wixdns.net	canonical name = balancer.wixdns.net.
balancer.wixdns.net	canonical name = f7a0737a-balancer.wixdns.net.
f7a0737a-balancer.wixdns.net	canonical name = td-balancer-dc11-60-102.wixdns.net.
`
see the following:-

{F1371299}

{F1371300}

And it is unclaimed

##Steps To Reproduce:
    1. Go to http://site.therealreal.com , Gives 404
    2. the domain pointing towards to WIX cdn
    3. Anyone can claim this subdomain
 
##Similar report at H1:-
- https://hackerone.com/reports/1183296

Please let me know if need more info , OR need for poc video
Best Regards.
@doosec101

## Impact

An attacker can claim this subdomain by requesting a process of registering this abandoned subdomain to his name.
And attacker can fully take over this subdomain and do whatever he wants. this can cause huge damage to the website's main domain as well as to the company.

**I Recommend removing  the Cname and DNS connecting to it.**

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
