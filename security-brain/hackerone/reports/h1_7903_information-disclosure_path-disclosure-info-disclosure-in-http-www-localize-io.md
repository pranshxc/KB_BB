---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7903'
original_report_id: '7903'
title: Path Disclosure (Info Disclosure) in  http://www.localize.io
weakness: Information Disclosure
team_handle: localize
created_at: '2014-04-17T19:50:16.902Z'
disclosed_at: '2014-04-18T05:38:29.474Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Path Disclosure (Info Disclosure) in  http://www.localize.io

## Metadata

- HackerOne Report ID: 7903
- Weakness: Information Disclosure
- Program: localize
- Disclosed At: 2014-04-18T05:38:29.474Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,
I found a information disclosure vulnerability.
How to reproduce:
GET : http://www.localize.io/
POST : sign_in[username][]=test&sign_in[password][]=test

The info from page is
Warning: trim() expects parameter 1 to be string, array given in /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/index.php on line 732
Is disclosed the path of the site.
Regards,
    Florin

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
