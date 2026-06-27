---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '185914'
original_report_id: '185914'
title: constant cache_page_secret in regolith
team_handle: iandunn-projects
created_at: '2016-11-28T02:07:28.040Z'
disclosed_at: '2016-12-30T04:48:13.103Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
---

# constant cache_page_secret in regolith

## Metadata

- HackerOne Report ID: 185914
- Weakness: 
- Program: iandunn-projects
- Disclosed At: 2016-12-30T04:48:13.103Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

in:
https://github.com/iandunn/regolith/blob/master/config/plugins/wp-super-cache.php#L28
```
$cache_page_secret             = 'ad270361c39c428c9465313363b02559';
```
there usage of static $cache_page_secret, as regolith is installation template. it's better to generate the secret for each installation instead of using static known value.
knowledge of $cache_page_secret value can be used to send requests which will not pass though the caching:
https://github.com/Automattic/wp-super-cache/blob/ea592c1d2796d0bc5c343322923c5f8bb40a0066/wp-cache-phase1.php#L32
thus enable more effective DOS (denial of service) attacks as the caching mechanism is disabled.

fix:
generate the $cache_page_secret in safe way once per installation & store the value in needed configuration file.

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
