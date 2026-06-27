---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '266908'
original_report_id: '266908'
title: Impersonation attack via Broken Link in Resellers Page
weakness: Violation of Secure Design Principles
team_handle: gitlab
created_at: '2017-09-08T05:45:55.821Z'
disclosed_at: '2017-09-08T21:42:12.394Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- violation-of-secure-design-principles
---

# Impersonation attack via Broken Link in Resellers Page

## Metadata

- HackerOne Report ID: 266908
- Weakness: Violation of Secure Design Principles
- Program: gitlab
- Disclosed At: 2017-09-08T21:42:12.394Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary
A link on `https://about.gitlab.com/resellers/` was broken and could've allowed a user to impersonate a reseller and attack / scam your customers.

## Proof of Concept
1.) Visit https://about.gitlab.com/resellers/
2.) Hit `Ctrl+F` and find "intenso"
 {F219301}
3.) Now click the Facebook link and you'll see the Facebook page I've "hijacked"
(https://www.facebook.com/InTENSO.IT.Enterprise.Solutions)

This happened because this reseller either deleted their Facebook page or changed their username. Not much you could do about that, but I thought I'd report it because it could be used to attack / scam your customers.

## References
 This post by edoverflow => https://gist.github.com/EdOverflow/24e0bb929169eb948bb7f3d0a2d5528f


Sorry for the lower quality of this report, but decided to report it as it could actually be used to scam users.
Thanks,
Corben Douglas (@sxcurity)

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
