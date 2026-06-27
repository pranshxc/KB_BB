---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '308156'
original_report_id: '308156'
title: Email Notification should be get while changing password on apps.nextcloud.com
team_handle: nextcloud
created_at: '2018-01-23T12:40:02.773Z'
disclosed_at: '2018-02-28T08:32:26.492Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 7
asset_identifier: apps.nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Email Notification should be get while changing password on apps.nextcloud.com

## Metadata

- HackerOne Report ID: 308156
- Weakness: 
- Program: nextcloud
- Disclosed At: 2018-02-28T08:32:26.492Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

There is an issue with password reset functionality with Nextcloud: user is not receiving notification when he reset password.


Issue: user not always gets a notification about password change. When user change his password then a notification is not send to the user.

It is good to always send email notification for user when a password change.

## Impact

It would be critical issue if user kept his/her account logged-in into PC or cyber cafe, then attacker can change his/her password without knowing to the user.
Please letme know if you have further questions

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
