---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2286764'
original_report_id: '2286764'
title: Avatar URL is exposed in patron export for secret donations
weakness: Privacy Violation
team_handle: liberapay
created_at: '2023-12-14T19:14:15.339Z'
disclosed_at: '2023-12-15T14:37:10.269Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 47
asset_identifier: '*.liberapay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- privacy-violation
---

# Avatar URL is exposed in patron export for secret donations

## Metadata

- HackerOne Report ID: 2286764
- Weakness: Privacy Violation
- Program: liberapay
- Disclosed At: 2023-12-15T14:37:10.269Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

When user sets their donation Privacy level to "Secret" they are indicating that they don't want to be identified by the donation recipient.

By exporting the `patron_avatar_url`, in `https://liberapay.com/<account_name>/patrons/export.csv`, the user might be exposed just by doing a reverse image search for such avatar.

## Impact

I would hope that there is no gain in trying to deanonymise their donors, but including the avatar should not be needed and I hope it should be an easy fix. 


I do not wish to be compensated in any way, the reason for using HackerOne is just that I don't want to disclose the issue on Github. Thank you for your great service! :)

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
