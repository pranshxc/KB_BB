---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '283460'
original_report_id: '283460'
title: Open Redirect Protection Bypass
weakness: Open Redirect
team_handle: x
created_at: '2017-10-27T09:07:11.514Z'
disclosed_at: '2017-12-23T07:48:36.407Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open Redirect Protection Bypass

## Metadata

- HackerOne Report ID: 283460
- Weakness: Open Redirect
- Program: x
- Disclosed At: 2017-12-23T07:48:36.407Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi

Report #281538 is fixed but Attacker can Bypass this Open Redirect Protection.

Give this link ``` https://twitter.com/teams/authorize?target_screen_name=&authorize_callback=//www.facebook.com``` to authorized victim.Twitter will say him to authorize a different account for create team.After authorization victim will be redirected to ```www.facebook.com```

Vulnerable point ```//www.facebook.com``` (You can use //www.example.com )

Open Redirection Protection Bypassed.

PoC video attached

With Best Regards

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
