---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '27846'
original_report_id: '27846'
title: Stored xss
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2014-09-11T22:17:13.781Z'
disclosed_at: '2014-09-27T08:25:07.849Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored xss

## Metadata

- HackerOne Report ID: 27846
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2014-09-27T08:25:07.849Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi!

There's a stored xss on ads.twitter.com under "Add New App" section at https://ads.twitter.com/accounts/18ce53wsl3g/campaigns/new_objective/app_installs. 

There's a option to add android application by Google play app id, so i searched for a app on play store with name " "><img src=x onerror=alert(1)>" " and then i got this app https://play.google.com/store/apps/details?id=com.rssappmaker.athe319.

So to reproduce this copy paste the app id "com.rssappmaker.athe319" in that box and then click on "add app" button. After that this xss will be triggered. See the attached image poc.png

Tested in latest version of chrome.

Thanks

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
