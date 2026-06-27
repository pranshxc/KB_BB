---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '282490'
original_report_id: '282490'
title: Application Vulnerable to CSRF - Remove Invited user
weakness: Cross-Site Request Forgery (CSRF)
team_handle: infogram
created_at: '2017-10-24T13:48:00.594Z'
disclosed_at: '2018-05-08T09:29:30.229Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Application Vulnerable to CSRF - Remove Invited user

## Metadata

- HackerOne Report ID: 282490
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: infogram
- Disclosed At: 2018-05-08T09:29:30.229Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

POC:

1. Login to the application with a business account.
2. Go to Manage teams, where we can send invites to a team member. Send a Invite to a team member
3. After the invite is sent to a user, the admin has option to Remove User.
4. While trying to remove the user, capture the request in burp , do not forward the request, send to repeater and drop the request
5. Now, from repeater , copy the url and put it in a new tab of authenticated admin browser, the user removal is successful

The user removal URL would look like https://infogram.com/api/team/cancel-invitation/c535cc62-9586-4f4b-8306-9381dcdbc815?teamId=16537204&_=1508852073697

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
