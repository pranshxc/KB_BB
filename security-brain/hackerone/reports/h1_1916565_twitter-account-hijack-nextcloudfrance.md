---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1916565'
original_report_id: '1916565'
title: Twitter Account hijack @nextcloudfrance
team_handle: nextcloud
created_at: '2023-03-24T08:20:24.864Z'
disclosed_at: '2023-03-30T14:05:03.536Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Twitter Account hijack @nextcloudfrance

## Metadata

- HackerOne Report ID: 1916565
- Weakness: 
- Program: nextcloud
- Disclosed At: 2023-03-30T14:05:03.536Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Broken Link Hijacking (BLH) is a web-based attack where it exploits external links that are no longer valid. The attackers take over this expired, stale, and invalid external links on credible websites or web applications for malicious or fraudulent purposes.

Link Hijacking attacks occur because the website/ web application continues to contain links to expired/ stale resources/pages (loaded using external URLs).

Steps :

1. Go to https://nextcloud.com/fr/

2. Go to last and click on Twitter icon.

3. It redirects you to the
 https://twitter.com/nextcloudfrance

4. It gives 404 at first and i takeover the username for Testing Purpose .

5. If you go to https://nextcloud.com/fr/ and click on Twitter Icon , now it redirect you to Attacker ( My ) Profile .

The best way to prevent Broken Link Hijacking attacks is to proactively identify such stale/ dead links and remove them from the website regularly. 

Ref :
https://hackerone.com/reports/1031321
https://hackerone.com/reports/1607429

## Impact

Since the link can be hijacked so any attacker can claim the link and make fake twitter profile of Nextcloud  and can do scam with them.

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
