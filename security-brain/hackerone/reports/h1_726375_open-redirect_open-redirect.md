---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '726375'
original_report_id: '726375'
title: Open Redirect
weakness: Open Redirect
team_handle: mailru
created_at: '2019-10-31T13:41:47.435Z'
disclosed_at: '2020-02-18T11:30:13.336Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
asset_identifier: Ext. B Scope
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open Redirect

## Metadata

- HackerOne Report ID: 726375
- Weakness: Open Redirect
- Program: mailru
- Disclosed At: 2020-02-18T11:30:13.336Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team Mail.ru

Open Redirect on http://aw.mail.ru/

There is an Open Redirect on http://aw.mail.ru/dynamic/auth/?forum_reg= due to the application not checking the value passed by the user to the "forum_reg" parameter.

User can be redirect to malicious site

PoC: Open Redirect
http://aw.mail.ru/dynamic/auth/?forum_reg=http://evil.com/

I hope you know the impact of open redirect and more info refer

Reference:

https://www.owasp.org/index.php/Unvalidated_Redirects_and_Forwards_Cheat_Sheet

## Impact

Attacker can trick users to visit malicious websites.
Attackers may be able to use this to execute believable phishing attacks, bypass authentication, or (in rare circumstances) violate CSRF mitigations.

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
