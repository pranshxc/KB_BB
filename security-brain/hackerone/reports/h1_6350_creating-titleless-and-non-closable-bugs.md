---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6350'
original_report_id: '6350'
title: creating titleless and non-closable bugs
team_handle: security
created_at: '2014-04-07T21:37:17.452Z'
disclosed_at: '2014-04-17T05:36:56.573Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
---

# creating titleless and non-closable bugs

## Metadata

- HackerOne Report ID: 6350
- Weakness: 
- Program: security
- Disclosed At: 2014-04-17T05:36:56.573Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I just found that it's possible to create titleless and non-closable bugs by prepending values for the 'report[title]'  and 'report[vulnerability_information]' parameters with '%00' characters respectively.

To reproduce:
- Create a baseline request via https://hackerone.com/[program]/reports/new
- Intercept said request to allow tampering using a valid session (i.e. Burp Repeater)
- Prepend the value for 'report[title]' with '%00' (creates titleless report) or;
- Prepend the value for report[vulnerability_information]' with '%00' (create non-closable report)
- View the titleless/non-closable bug reports in the queue for [program]

Regards,

-leander

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
