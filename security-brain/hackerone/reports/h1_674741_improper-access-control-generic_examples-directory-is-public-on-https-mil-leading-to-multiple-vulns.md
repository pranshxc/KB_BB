---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '674741'
original_report_id: '674741'
title: Examples directory is PUBLIC on https://████████mil, leading to multiple vulns
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2019-08-15T22:24:37.289Z'
disclosed_at: '2019-10-10T19:11:41.367Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 22
tags:
- hackerone
- improper-access-control-generic
---

# Examples directory is PUBLIC on https://████████mil, leading to multiple vulns

## Metadata

- HackerOne Report ID: 674741
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2019-10-10T19:11:41.367Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
Hello, 

In an effort to consolidate reporting. I have located 4 issues with having the Examples Directory open(my require just 1 solution to mitigate) The following URLs that show concern are the following:

1. https://█████mil/examples/servlets/servlet/SessionExample <--Will lead to Session Manipulation and potential Account Takeover

2. https://██████mil/examples/servlets/servlet/RequestHeaderExample <---Internal IP disclosure

3. https://██████████mil/examples/servlets/ <---Source Code Disclosure and an "Execute" option(did not press Execute button so I am not sure the impact of it.

4. https://████mil/examples/servlets/servlet/CookieExample <----Insecure Cookie Handling



## Step-by-step Reproduction Instructions

1. Please visit the above links
2.
3.


## Suggested Mitigation/Remediation Actions

Disable public access to the examples directory as soon as possible!

## Impact

Ordered by Highest Impact:

1. https://██████mil/examples/servlets/servlet/SessionExample <--Will lead to Session Manipulation and potential Account Takeover. Because the session is global this servlet poses a big security risk as an attacker can potentially become an administrator by manipulating its session.

2. https://██████████mil/examples/servlets/servlet/CookieExample <----Insecure Cookie Handling

3. https://███████mil/examples/servlets/ <---Source Code Disclosure and an "Execute" option

4. https://██████mil/examples/servlets/servlet/RequestHeaderExample <---Internal IP disclosure

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
