---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '873474'
original_report_id: '873474'
title: Stored XSS on express entries
weakness: Cross-site Scripting (XSS) - Stored
team_handle: concretecms
created_at: '2020-05-13T15:08:57.463Z'
disclosed_at: '2020-07-03T19:51:03.890Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: https://github.com/concrete5/concrete5
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS on express entries

## Metadata

- HackerOne Report ID: 873474
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: concretecms
- Disclosed At: 2020-07-03T19:51:03.890Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

1. Download Concrete5 8.5.2 and install it
2. Log into your Concrete5 instance as admin
3. Go to Dashboard > System settings > Express entities (/index.php/dashboard/system/express/entities) 
4. Сlick on the **Create** button
5. in the field **Name** paste the following text: `</h1><script>alert(1)</script><h1>`
6. Go to tab **View Objects**

## Impact

If the user was added to the group of administrators, then he can create an express object with a payload in the name and give a link to another administrator to view the created object.

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
