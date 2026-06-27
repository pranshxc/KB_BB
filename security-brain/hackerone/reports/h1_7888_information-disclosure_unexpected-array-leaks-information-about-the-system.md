---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7888'
original_report_id: '7888'
title: Unexpected array leaks information about the system
weakness: Information Disclosure
team_handle: localize
created_at: '2014-04-17T19:10:01.613Z'
disclosed_at: '2014-04-18T08:37:05.772Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Unexpected array leaks information about the system

## Metadata

- HackerOne Report ID: 7888
- Weakness: Information Disclosure
- Program: localize
- Disclosed At: 2014-04-18T08:37:05.772Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

By changing a string parameter on the `/pages/settings` page to an array (see example.png) and submitting the form, the page shows an error message leaking information about the server and functions used (see error.png). This works on multiple POST parameters.

    Warning: trim() expects parameter 1 to be string, array given in /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/index.php on line 85

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
