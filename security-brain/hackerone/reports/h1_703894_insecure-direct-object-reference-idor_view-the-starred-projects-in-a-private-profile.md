---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '703894'
original_report_id: '703894'
title: View the Starred Projects in a Private Profile
weakness: Insecure Direct Object Reference (IDOR)
team_handle: gitlab
created_at: '2019-09-29T18:09:48.881Z'
disclosed_at: '2021-02-02T14:07:50.702Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 44
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# View the Starred Projects in a Private Profile

## Metadata

- HackerOne Report ID: 703894
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: gitlab
- Disclosed At: 2021-02-02T14:07:50.702Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Summary

It is possible to view the  starred Projects in a private profile. Consider my profile for instance, https://gitlab.com/maruthi-adithya . This is a private profile and none of my account-related information should be leaked. However, https://gitlab.com/users/maruthi-adithya/starred.json exposes Starred Projects.

### Steps to reproduce

1. Login to Gitlab. Go to Settings.
2. Check "Don't display activity-related personal information on your profiles".
3. Save the Profile.
4. Now, open your profile from a private window. It will say this is a private profile. However, the above mentioned API exposes the starred projects information.

## Impact

According to the docs, https://gitlab.com/help/user/profile/index.md#private-profile, starred projects should be hidden. However, due to this API, it is getting exposed. Using this, an attacker could steal sensitive data from a private profile.

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
