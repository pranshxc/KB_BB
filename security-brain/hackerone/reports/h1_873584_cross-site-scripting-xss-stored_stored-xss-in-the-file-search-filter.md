---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '873584'
original_report_id: '873584'
title: Stored XSS in the file search filter
weakness: Cross-site Scripting (XSS) - Stored
team_handle: concretecms
created_at: '2020-05-13T18:05:58.255Z'
disclosed_at: '2020-07-03T19:51:36.848Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: https://github.com/concrete5/concrete5
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in the file search filter

## Metadata

- HackerOne Report ID: 873584
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: concretecms
- Disclosed At: 2020-07-03T19:51:36.848Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

1. Download Concrete5 8.5.2 and install it
2. Log into your Concrete5 instance as admin
3. Go to Dashboard >Files > Search
4. In the file search bar, click **Advanced**
5. In the window that appears, enter a phrase and click the save button, paste the following payload: `<img src=1 onerror=alert(1)>` and click the save button
6.  In the filter search bar, click **Edit** and wait for the malicious code to execute

## Impact

If a user has been added to the administrators group, then he can create a malicious filter and wait for someone else to change this filter

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
