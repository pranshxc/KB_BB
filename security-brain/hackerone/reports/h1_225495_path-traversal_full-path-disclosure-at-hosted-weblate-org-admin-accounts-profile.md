---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '225495'
original_report_id: '225495'
title: full path disclosure at hosted.weblate.org/admin/accounts/profile/
weakness: Path Traversal
team_handle: weblate
created_at: '2017-05-02T08:38:53.634Z'
disclosed_at: '2017-05-17T14:07:42.355Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- path-traversal
---

# full path disclosure at hosted.weblate.org/admin/accounts/profile/

## Metadata

- HackerOne Report ID: 225495
- Weakness: Path Traversal
- Program: weblate
- Disclosed At: 2017-05-17T14:07:42.355Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Browsing this link https://hosted.weblate.org/admin/accounts/profile/  will ask for admin username and password as asked  when browsing https://hosted.weblate.org/admin/accounts/ or https://hosted.weblate.org/admin/ hence disclosing the directory path of forbidden area.
screenshot : path.png

also it is found that there is no rate limiting enforced at https://hosted.weblate.org/admin/login/?next=/admin/  hence attacker can break into staffs account by brute forcing. 
screenshot : login.png

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
