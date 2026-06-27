---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2125346'
original_report_id: '2125346'
title: Twitter account hijack @Costalfy
weakness: Phishing
team_handle: liberapay
created_at: '2023-08-27T16:21:00.183Z'
disclosed_at: '2023-09-27T22:15:01.546Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: '*.liberapay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- phishing
---

# Twitter account hijack @Costalfy

## Metadata

- HackerOne Report ID: 2125346
- Weakness: Phishing
- Program: liberapay
- Disclosed At: 2023-09-27T22:15:01.546Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Summary:
Broken Link Hijacking (BLH) is a web-based attack where it exploits external links that are no longer valid. The attackers take over this expired, stale, and invalid external links on credible websites or web applications for malicious or fraudulent purposes.
Link Hijacking attacks occur because the website/ web application continues to contain links to expired/ stale resources/pages (loaded using external URLs).

So i found a twitter account of one of the members of **liberapay** which is **Andy Costanza** is broken, anyone can claim that account and can scam with it .

{F2642478}
##Steps To Reproduce:

1- Go to ``` https://liberapay.com/Andy_Costanza/ ``` and Click on the twitter button .

{F2642439}
2-now it redirect you to Attacker ( My ) Profile .

{F2642468}

> -  Those interested to get more infomation about **Andy Costanza** at https://liberapay.com/Andy_Costanza/ should be cautious of potential phishing or scam attempts. It is advised to take prompt action to ensure safety and security.

## Impact

Since the links can be hijacked so any attacker can claim the link and make fake Twitter profile of  **Andy Costanza** and can do scam with them.

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
