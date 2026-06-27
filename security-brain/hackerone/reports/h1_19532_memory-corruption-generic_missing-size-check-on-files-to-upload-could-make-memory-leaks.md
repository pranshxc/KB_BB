---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '19532'
original_report_id: '19532'
title: Missing "size check" on files to upload could make memory leaks.
weakness: Memory Corruption - Generic
team_handle: uzbey
created_at: '2014-07-09T19:59:37.006Z'
disclosed_at: '2014-08-22T03:19:03.559Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- memory-corruption-generic
---

# Missing "size check" on files to upload could make memory leaks.

## Metadata

- HackerOne Report ID: 19532
- Weakness: Memory Corruption - Generic
- Program: uzbey
- Disclosed At: 2014-08-22T03:19:03.559Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I noticed that there isn't any "size check" when someone tries to upload a flie through the "upload picture" option, this could generate a memory leak or also a kind of DoS and is deangerous with bigger and bigger files. So i first tried to upload a file of about 2,52 GB (see the pic) and no warning messaege about the size wasn't displayed (such as a 413 error message), and the site was unable to charge the page, it generated an huge solwdown of the connection to https://staging.uzbey.com. 

------Risks------

Someone interested could exploit that to make a designed wepay dosser software to take the website down and that colud also make a dangerous memory leak or exploitable overflows .

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
