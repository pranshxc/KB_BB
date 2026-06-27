---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1386277'
original_report_id: '1386277'
title: Attachment references in markdown don't warn before downloading
weakness: Open Redirect
team_handle: security
created_at: '2021-10-29T22:06:35.254Z'
disclosed_at: '2022-02-25T17:06:07.850Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Attachment references in markdown don't warn before downloading

## Metadata

- HackerOne Report ID: 1386277
- Weakness: Open Redirect
- Program: security
- Disclosed At: 2022-02-25T17:06:07.850Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
By default if any link of report is clicked, There will be a popup to user 
that you're visiting a third-party website please proceed at your own risk etc. 
However, when a user views the report all links are non clickable and file URI is appended. 
I have Found out that I can bypass this functionality by appending a " and ) in the end . 
For example if you view this link  as PDF and click the link it will simply redirect you to the URL. 

there will be a popup,  That you are visited a third party domain etc.
**Description:**

### Steps To Reproduce

1. create a H1 report with the following payload 

(https://example.com") 

2. view the report click export and view as pdf
3. hover the link and click . 
4. observe that you are directly redirected without any warning of going to third party domain. 

### Optional: Your Environment (Browser version, Device, etc)

 * 

### Optional: Supporting Material/References (Screenshots)

 *

## Impact

By using this vulnerability an attacker might be able to get a victims IP address , make them login etc.

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
