---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '708123'
original_report_id: '708123'
title: Stored cross-site scripting in dataset owner.
weakness: Cross-site Scripting (XSS) - Stored
team_handle: quantopian
created_at: '2019-10-05T09:23:46.300Z'
disclosed_at: '2022-12-21T20:13:33.471Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: www.quantopian.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored cross-site scripting in dataset owner.

## Metadata

- HackerOne Report ID: 708123
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: quantopian
- Disclosed At: 2022-12-21T20:13:33.471Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi again. Another XSS this time.
**Summary:** Unescaped chars in 'dataset owner' could be abused to store arbitrary javascript.

**Description:** There is a 'dataset owner' field in new 'custom dataset dashboard' which contains unsanitized output. If attacker would modify his name, like first name '<img src=x' and last name 
'onerror=alert(1)>', the field would hold a script. While for most users this is a case of self-xss, for enterprise users (for which, as i understand. this field was introduced in the first place), it can lead to executing arbitrary javascript.

**Steps To Reproduce:**

  1. Put the payload in name and/or surname
 *(first name '<img src=x' and last name 
'onerror=alert(1)>')*
  2. Navigate to custom datasets. 


**Test account information**

tvburis+hackerone@gmail.com

## Impact

Executing arbitrary javascript, stealing other users' algos as demonstrated in previous reports with XSS on quantopian domain.

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
