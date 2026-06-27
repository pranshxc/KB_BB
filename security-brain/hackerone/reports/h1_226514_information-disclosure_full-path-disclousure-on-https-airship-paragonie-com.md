---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '226514'
original_report_id: '226514'
title: Full Path Disclousure on https://airship.paragonie.com
weakness: Information Disclosure
team_handle: paragonie
created_at: '2017-05-06T08:17:30.515Z'
disclosed_at: '2017-05-07T01:41:36.811Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Full Path Disclousure on https://airship.paragonie.com

## Metadata

- HackerOne Report ID: 226514
- Weakness: Information Disclosure
- Program: paragonie
- Disclosed At: 2017-05-07T01:41:36.811Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi , i found an full path disclousure vulnerability on https://airship.paragonie.com

For reproduce this vulnerability go to: https://airship.paragonie.com/my/cabins
You will see something like this : Class '\ParagonIE\Airship\Cabins' not found #0 /var/www/paragonie/framework/Router.php(236): ParagonIE\Tuner\Router::passArgs(Array, Array, Array) #1 /var/www/paragonie/framework/Router.php(150): ParagonIE\Tuner\Router::serve(Array, Array, Array) #2 /var/www/paragonie/framework/Router.php(107): ParagonIE\Tuner\Router::site(Array) #3 /var/www/paragonie/public_html/index.php(26): ParagonIE\Tuner\Router::route(Array) #4 {main}

See attached file 
Thanks

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
