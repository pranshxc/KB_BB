---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '330135'
original_report_id: '330135'
title: S3 bucket unnecessarily discloses permissions
weakness: Improper Access Control - Generic
team_handle: udemy
created_at: '2018-03-27T02:41:38.028Z'
disclosed_at: '2019-04-26T13:10:58.399Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
tags:
- hackerone
- improper-access-control-generic
---

# S3 bucket unnecessarily discloses permissions

## Metadata

- HackerOne Report ID: 330135
- Weakness: Improper Access Control - Generic
- Program: udemy
- Disclosed At: 2019-04-26T13:10:58.399Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The 'udemy-images' bucket allows the 'AllUsers' group to list ACLs that are applied to the bucket. By navigating to: [https://udemy-images.udemy.com](https://udemy-images.udemy.com) or by using the `aws-cli` tool an attacker can see which users have `READ`, `WRITE`, `READ_ACP`, and `WRITE_ACP` rights. Doing this now we can see one user who has these rights (see attached screenshot). We can see their ID and DisplayName (hi [@caglaroktay!](https://twitter.com/caglaroktay))

## Impact

While this doesn't give public users write access to the bucket, a motivated attacker can gather a lot of information from this. If one were targeting the Udemy AWS infrastructure, this information would give them all they need to know to start gathering intel on an authorized user (like @caglaroktay). An easy way to do this would be  to look for breached passwords belonging to the authorized user to try logging into their AWS console with.

This public permission is unnecessary as it is not needed for the site to run properly and should be removed immediately.

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
