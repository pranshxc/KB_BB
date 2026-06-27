---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '826176'
original_report_id: '826176'
title: program_analytics_benchmarks query shows information not visible in public
weakness: Information Disclosure
team_handle: security
created_at: '2020-03-22T00:26:00.520Z'
disclosed_at: '2020-03-27T16:25:42.270Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# program_analytics_benchmarks query shows information not visible in public

## Metadata

- HackerOne Report ID: 826176
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2020-03-27T16:25:42.270Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
`program_analytics_benchmarks` is displaying information i don't see yet in public profile of a program.

**Description:**
I tried querying program_analytics_benchmarks for the program security and ██████ and it showing information i cannot find in public profile especially in ███████ 
### Steps To Reproduce
Please try the graphql for the the program security and ████████
```
{
  program_analytics_benchmarks(teams:"security" select:p50_time_to_bounty, from:response_targets, where:{severity:{is_null:true}},group:week_bounty_awarded_at, 
    start_date:"2019-10-01T00:00:00.000Z",end_date:"2020-10-01T00:00:00.000Z%00")
    {
      id
      x
      y
      
    }
}
```
Please see the attached file for the actual response



### Optional: Supporting Material/References (Screenshots)
███
███
 * 

I saved this graphql query and been trying to run this for a month now and i just noticed now that it's returning some information.

## Impact

Information disclosure

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
