---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '265775'
original_report_id: '265775'
title: Password reset token issue
weakness: Improper Authentication - Generic
team_handle: legalrobot
created_at: '2017-09-04T12:02:42.475Z'
disclosed_at: '2017-09-05T00:23:31.684Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: app.legalrobot.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Password reset token issue

## Metadata

- HackerOne Report ID: 265775
- Weakness: Improper Authentication - Generic
- Program: legalrobot
- Disclosed At: 2017-09-05T00:23:31.684Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Summary
Can still change password without token

##Step to Reproduce

- Request for password reset link.
- Go to email and click on password reset link https://app.legalrobot.com/password-reset/token?v=uWe_yFJS0-N9fIk0nG0b0NZ70lkwNNi7RdUZu0KhiaX
- Now remove the token and use the link https://app.legalrobot.com/password-reset

Observe that able to reset the password without the token.

##Fix :
Always password reset link should work with a valid token.

##Reference :
https://hackerone.com/reports/253934

Thanks,
tell me if you need video. i'll create one.

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
