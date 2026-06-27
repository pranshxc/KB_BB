---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '380317'
original_report_id: '380317'
title: Team object exposes amount of participants in a private program to non-invited
  users
weakness: Information Disclosure
team_handle: security
created_at: '2018-07-10T22:13:56.389Z'
disclosed_at: '2018-07-20T17:44:07.836Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 57
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Team object exposes amount of participants in a private program to non-invited users

## Metadata

- HackerOne Report ID: 380317
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2018-07-20T17:44:07.836Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hello.

Similar to other reports, suddenly after the update with ordering users, the GraphQL API is exposing the amount of participants in a private program to non-invited users. This allows an attacker to retrieve the amount of participants in a private program, as well as their details.

**Description:**
Steps To Reproduce

Query, for example, ██████ via the GraphQL API. ██████ is known to have a private program running on HackerOne, and they do exist in the external directory.
```
query {
    team(handle: "█████") {
     participants { total_count  }
     about

}
}
```
You'll get the amount of participants, as well as their details if you query them. 
```
...
{ "data": { "team": {participants": { "total_count": 268 }, "about": "████" } } }
...
```

**Impact**

This leads to information disclosure. An attacker can expose the existence of a private program under the external program directory.

## Impact

This will eventually lead to information disclosure.

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
