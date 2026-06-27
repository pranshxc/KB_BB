---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1560717'
original_report_id: '1560717'
title: Possible to make restricted files public on Phabricator via Diffusion
weakness: Improper Access Control - Generic
team_handle: phabricator
created_at: '2022-05-05T23:54:40.958Z'
disclosed_at: '2022-07-29T22:37:58.052Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- improper-access-control-generic
---

# Possible to make restricted files public on Phabricator via Diffusion

## Metadata

- HackerOne Report ID: 1560717
- Weakness: Improper Access Control - Generic
- Program: phabricator
- Disclosed At: 2022-07-29T22:37:58.052Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Files on Phabricator are always viewable to a user if they are attached to an object that they can view. It seems Phabricator does check if you can view a file before allowing you to a attach it. If you don't have access to the file, it will just look like this {F99999999999} in plaintext. It seems Phabricator does not do this check when creating commits in Differential repositories. This means you make a restricted file public simply by including the syntax to attach the file in the commit message which will then by synced to Phabricator, causing the file to be made public regardless of whether you had access in the first place. It is possible to find a restricted file simply by enumeration.

File "Can View" is set to Administrator:
F1718695
However the file is in the commit and viewable:
F1718696
User is not an Administrator:
F1718697

## Impact

Gain access to restricted file objects.

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
