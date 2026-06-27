---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1663363'
original_report_id: '1663363'
title: Wordpress Users Disclosure (/wp-json/wp/v2/users/)
weakness: Information Disclosure
team_handle: top_echelon_software
created_at: '2022-08-08T23:11:05.356Z'
disclosed_at: '2022-08-11T20:46:19.020Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: www.topechelon.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Wordpress Users Disclosure (/wp-json/wp/v2/users/)

## Metadata

- HackerOne Report ID: 1663363
- Weakness: Information Disclosure
- Program: top_echelon_software
- Disclosed At: 2022-08-11T20:46:19.020Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team @top_echelon_software
Information:
Using REST API, we can see all the WordPress users/author with some of their information.  

Step To Reproduce:
You can get user info by entering below url in your browser:
https://www.topechelon.com/wp-json/wp/v2/users/ 
███████

## Impact

Authors : LTR , LTREditor can be created scenario of doing bruteforce attacks to this users

Malicious counterpart could collect the usernames disclosed (and the admin user) and be focused throughout BF attack (as the usernames are now known)

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
