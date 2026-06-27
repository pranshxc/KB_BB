---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '111676'
original_report_id: '111676'
title: attack in not an authorized user
weakness: Uncontrolled Resource Consumption
team_handle: security
created_at: '2016-01-19T19:39:58.556Z'
disclosed_at: '2016-02-16T20:00:32.973Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- uncontrolled-resource-consumption
---

# attack in not an authorized user

## Metadata

- HackerOne Report ID: 111676
- Weakness: Uncontrolled Resource Consumption
- Program: security
- Disclosed At: 2016-02-16T20:00:32.973Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

example (exit account) go to http://myfuneral.ru/hackerone.php your location https://hackerone.com/users/sign_in and Error 502 Ray ID: ***************** • 2016-01-19 19:31:49 UTC
Bad gateway

I think this was due to the fact that enrolled in the cookie with an invalid redirection ssesiyami
(after authorization of the user was redirected to the link which is in hackerone.php, but this site does not do)

короче все в сессию записалась трудная ссылка , которую hackerone.com не может нормально воспринимать , чтобы после авторизации направить  пользователя по пути редикта

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
