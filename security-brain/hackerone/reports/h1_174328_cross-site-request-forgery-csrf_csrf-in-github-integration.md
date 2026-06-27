---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '174328'
original_report_id: '174328'
title: CSRF in github integration
weakness: Cross-Site Request Forgery (CSRF)
team_handle: slack
created_at: '2016-10-06T11:34:47.622Z'
disclosed_at: '2016-11-18T04:24:01.420Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF in github integration

## Metadata

- HackerOne Report ID: 174328
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: slack
- Disclosed At: 2016-11-18T04:24:01.420Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There is a CSRF in the github integration in the case of "Only pre-approved apps can be installed by team members: (slack1.png)
Github is not one of those pre approved application. So a normal user cannot install it (slack2)
Now lets assume the channel administrator is adding this integration to one common channel e.g. #random (slack3.png).
Now the other non admin users receive a notification "added an integration to this channel: github" (slack4.png) but if they try to click the link they will have a page saying "added an integration to this channel: github" (slack5.png). The problem is that they still have the uri of the integration, that is something like https://vecchiowerther.slack.com/services/CODE E.g. https://vecchiowerther.slack.com/services/B2L476P3P

This can be used to make the admin of the channel to  "switch to unauthed mode".
For the attacker is enough to forge a an html page as

<html>
<img src="https://vecchiowerther.slack.com/services/88143227125?no_auth_mode=1">
</html>

e.g. in http://asanso.github.io/csrf.html (or in any website). 
If the admin will visit this website he will loose the github integration and switch to the unauthed mode (slack6.png)

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
