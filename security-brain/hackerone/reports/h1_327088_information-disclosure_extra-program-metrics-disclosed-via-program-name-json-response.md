---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '327088'
original_report_id: '327088'
title: Extra program metrics disclosed via /PROGRAM_NAME json response
weakness: Information Disclosure
team_handle: security
created_at: '2018-03-18T16:28:00.128Z'
disclosed_at: '2018-03-28T18:05:03.095Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 51
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Extra program metrics disclosed via /PROGRAM_NAME json response

## Metadata

- HackerOne Report ID: 327088
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2018-03-28T18:05:03.095Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
The response to www.hackerone.com/PROGRAM.json includes `sla_missed_count` `sla_failed_count` and `researcher_count`. 

**Description:**
Viewing the response from a program's json endpoint includes the values for `sla_missed_count`, `sla_failed_count` and `researcher_count`.

With regards to the SLA metrics, these are not included in the UI on the policy page and hovering over a program indicator just reveals a summary of the information, such as >=1 report has failed the SLA. There is no mention of these values being disclosed in the program settings pages and according to the SLA FAQ docs, only a `summarized version of a program’s response efficiency metric performance [will be displayed] on their hacker facing security page` https://support.hackerone.com/hc/en-us/articles/115005927583-Response-SLAs-on-Security-Pages

With regards to the researcher count, I'm including this because the information isn't disclosed in the UI when you have a pending invite to a program and I'm not sure why that might be. Nonetheless, viewing the same JSON response includes the `researcher_count`

### Steps To Reproduce

1. Log in
2. Visit any program and have Burp capture the response
3. Confirm the bottom of the JSON response includes the SLA information

### Supporting Material/References (Screenshots)

{F273408}

## Impact

The program settings page nor documentation indicates that SLA misses/fails will be disclosed. This information should be considered sensitive in nature and programs should opt into disclosing it if this is intentional since it reveals a minimum number of security vulnerabilities a program may be addressing (I say may because the SLA violation could be response / triage).

The researcher count could be considered sensitive in the context of a private invite, revealing how many vulnerabilities have been found by what number of people before having actually accepted an invitation. I recognize this is a stretch but also assume there is a reason this number isn't disclosed before accepting a private invitation.

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
