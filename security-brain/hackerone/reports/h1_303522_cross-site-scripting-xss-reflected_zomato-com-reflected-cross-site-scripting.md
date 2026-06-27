---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '303522'
original_report_id: '303522'
title: Zomato.com Reflected Cross Site Scripting
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: zomato
created_at: '2018-01-09T13:17:16.049Z'
disclosed_at: '2018-04-08T12:01:08.363Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Zomato.com Reflected Cross Site Scripting

## Metadata

- HackerOne Report ID: 303522
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: zomato
- Disclosed At: 2018-04-08T12:01:08.363Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

zomato.com/php/liveSuggest.php takes various field input to show customized out put for the users.
The data entered to entity_id field is not santized or html encoded which allows user to add payloads via this parameter which will be reflected to user.

Steps to reproduce :

Please click on below link to check the poc . Also please find attached poc for reference

https://www.zomato.com/php/liveSuggest.php?type=keyword&search_bar=1&q=ad&online_ordering=&search_city_id=5&entity_id=confirm(1)%20%3C%20%22%22%27%22ss%22%20onerror%3E;confirm(1)%3Cvideo%20src=x%3E%3Cvideo%20src=%22&entity_type=%22;%20onerror

## Impact

An attacker can craft a malicious link and send to users , which can then lead to session hijacking , redirecting to malicious or fake websites etc.

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
