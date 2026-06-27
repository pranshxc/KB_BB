---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '415139'
original_report_id: '415139'
title: Reflected xss on theacademy.upserve.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: upserve
created_at: '2018-09-27T00:21:31.207Z'
disclosed_at: '2018-09-28T22:14:13.144Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 20
asset_identifier: theacademy.upserve.com
asset_type: URL
max_severity: low
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected xss on theacademy.upserve.com

## Metadata

- HackerOne Report ID: 415139
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: upserve
- Disclosed At: 2018-09-28T22:14:13.144Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Vulnerabilty**
*Reflected xss* in (https://theacademy.upserve.com).

**STEPS TO REPRODUCE**
1. Go to (https://theacademy.upserve.com/playlists/all-videos/).
2. Click on any video to watch from the playlist and capture the request in burp.
3. you have to capture the request to (https://theacademy.upserve.com/wp-admin/admin-ajax.php?action=load_player&video_id=5742677405001&player_id=B14h0D4OM&type=pc&post_id=2712)
4. then replace the video_id with this payload = r"><BODY%20ONLOAD=alert(1)>.
5. Then see the response in browser and the popup will appear.

**NOTE**: *I also attached a video POC*

## Impact

With the help of *xss* a hacker or attacker can perform social engineering on users by redirecting them from real website to fake one. hacker can steal their *cookies* and download a **malware** on their system, and there are many more attacking scenarios a skilled attacker can perform with **xss**.

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
