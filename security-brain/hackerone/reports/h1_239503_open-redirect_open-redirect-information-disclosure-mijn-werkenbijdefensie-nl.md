---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '239503'
original_report_id: '239503'
title: Open Redirect & Information Disclosure [mijn.werkenbijdefensie.nl]
weakness: Open Redirect
team_handle: radancy
created_at: '2017-06-13T08:14:23.019Z'
disclosed_at: '2017-06-21T14:34:29.495Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 27
tags:
- hackerone
- open-redirect
---

# Open Redirect & Information Disclosure [mijn.werkenbijdefensie.nl]

## Metadata

- HackerOne Report ID: 239503
- Weakness: Open Redirect
- Program: radancy
- Disclosed At: 2017-06-21T14:34:29.495Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,
I've Found an After-Login Open Redirect Vulnerability which can lead to information disclosure like an authentication token and user_id

###Steps To Reproduce:
 1. Go to https://mijn.werkenbijdefensie.nl/login?redirect_url=https://google.com
 2. Login using your valid Email & Password
 3. You will be redirected to :
```
https://www.google.com/?user=████&token=████&channel=mijnwerkenbijdefensie
```

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
