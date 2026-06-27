---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1320976'
original_report_id: '1320976'
title: '[3] Bypassing IP Based Rate Limit Blocking leads to rate limit bypass in Courier
  Login Panel'
weakness: Uncontrolled Resource Consumption
team_handle: trycourier
created_at: '2021-08-27T04:05:42.955Z'
disclosed_at: '2021-09-16T17:31:54.078Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: api.trycourier.app
asset_type: URL
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# [3] Bypassing IP Based Rate Limit Blocking leads to rate limit bypass in Courier Login Panel

## Metadata

- HackerOne Report ID: 1320976
- Weakness: Uncontrolled Resource Consumption
- Program: trycourier
- Disclosed At: 2021-09-16T17:31:54.078Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team,
I would like to report rate limit issue based on IP blocking mechanism. Rate-limitation nowadays is not effective anymore to protect against brute-force. There are many botnets out there which can be used to overcome this hurdle, as well as cloud (VPS) services (e.g. Amazon AWS EIPs, Digital Ocean, ...), VPNs, proxies. 

Many VPS providers today offer a whole /64 subnet range of IPv6 addresses (18.446.744.073.709.551.616 unique addresses), such as but not limited to:
RamNode: $15/year (https://www.ramnode.com/vps.php)
Hetzner: $3.9/month (https://www.hetzner.de/us/hosting/produktmatrix_vserver/vserver-produktmatrix)
Vultr: $5/month (https://www.vultr.com/pricing/) and AWS too.

One example of a similar vulnerability that was exploited by Black Hats in the past would be Apple's Celebgate scandal of January 2015, where celebrity passwords were brute-forced through an unprotected Apple authentication endpoint which is on IP based rate limit blocking. But in the case of Courier user can easily rotate the IP's and can cause denial of services to its victim, or can cause notification bombarding after every 5 request. 

#Recommendation: I'm recommending you to implement Captcha Verification to avoid such rate limit issue, or You can add rate limit on the basis of user's email address not IP address.

So make brute force attack on login page and change IP after you get rate limited. I Don't have AWS subscription that why I'm demonstrating this with my free ( RiseupVPN ). Hope you will understand.

{F1426888}


Please let me know if you need any extra information. cheers

## Impact

IP based Rate limit Bypass can cause Dos on courier users.

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
