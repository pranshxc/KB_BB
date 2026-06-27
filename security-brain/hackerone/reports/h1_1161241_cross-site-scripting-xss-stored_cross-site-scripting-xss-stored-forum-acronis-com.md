---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1161241'
original_report_id: '1161241'
title: Cross-site Scripting (XSS) - Stored | forum.acronis.com
weakness: Cross-site Scripting (XSS) - Stored
team_handle: acronis
created_at: '2021-04-12T10:11:01.702Z'
disclosed_at: '2022-02-08T13:52:00.761Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 20
asset_identifier: '*.acronis.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Cross-site Scripting (XSS) - Stored | forum.acronis.com

## Metadata

- HackerOne Report ID: 1161241
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: acronis
- Disclosed At: 2022-02-08T13:52:00.761Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary

There is an XSS vulnerability in the search function of the forum (forum.acronis.com).

## Steps To Reproduce

  1. Modify your own forum Nickname, add the following payload after the original nickname:

```
<script>alert(0)</script>
```

  2. Fill in your nickname in the Author form of the search function and wait for the search, it will automatically trigger a pop-up.

{F1262581}

## Recommendations

Add special character filtering to the nickname modification function of the forum.

## Impact

You can add any keywords that users may use when searching for authors to your nickname to attack the corresponding users. It is possible to execute any Javascript.

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
