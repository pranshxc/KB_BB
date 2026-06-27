---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '361054'
original_report_id: '361054'
title: Phishing by Navigating Browser Tabs
team_handle: liberapay
created_at: '2018-06-02T10:32:42.556Z'
disclosed_at: '2018-06-04T11:52:22.418Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: https://github.com/liberapay/liberapay.com
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Phishing by Navigating Browser Tabs

## Metadata

- HackerOne Report ID: 361054
- Weakness: 
- Program: liberapay
- Disclosed At: 2018-06-04T11:52:22.418Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi team,

I was create a PR on github https://github.com/liberapay/liberapay.com/pull/1127

### Details

Opened windows through normal hrefs with target="_blank" can modify window.opener.location and replace the parent webpage with something else, even on a different origin.

While this doesn't allow script execution, it does allow phishing attacks that silently replace the parent tab.

Hope you will not close it as `N/A` Thinking about resolve.Approve the PR.

Thanks,
@4w3

## Impact

If the links lack of rel="noopener noreferrer" attribute, third party site can change the URL of source tab using window.opener.location.assign and trick the user as if he is still in a trusted page and lead him to enter his secret information or credentials to this malicious copy.

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
