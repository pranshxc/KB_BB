---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2109382'
original_report_id: '2109382'
title: 'Support Tickets can be created on behalf of other users using spoofed email
  | Bypass of #2001913'
weakness: Incorrect Authorization
team_handle: security
created_at: '2023-08-14T17:47:05.770Z'
disclosed_at: '2023-09-08T08:14:56.088Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: support.hackerone.com
asset_type: URL
max_severity: none
tags:
- hackerone
- incorrect-authorization
---

# Support Tickets can be created on behalf of other users using spoofed email | Bypass of #2001913

## Metadata

- HackerOne Report ID: 2109382
- Weakness: Incorrect Authorization
- Program: security
- Disclosed At: 2023-09-08T08:14:56.088Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hi team,
Hope you are doing well.I came across a disclosed report by hackerone (#2001913) wherein a researcher was able to create a support ticket on behalf of other users by sending fake email to support@hackerone.com. The issue was fixed by hackerone and sending email to support@hackerone.com does not create support tickets anymore.But,there is a bypass to this fix.
**Description:**
Hackerone uses freshdesk as their third party service provider to handle support tickets .In freshdesk if a email is sent to support@domain.freshdesk.com it would create support tickets on behalf of the user.Similarly,if an email is sent to support@hackerone.freshdesk.com using a fake mailer like https://emkei.cz then a support ticket is  created by an attacker for the victim.

### Steps To Reproduce
1. Visit https://emkei.cz or any other fake mailer website.
2. Put the victim email in from field and support@hackerone.freshdesk.com in the to field.
3. Fill in the body with any message like account deletion and support ticket would be created in the behalf of victim and the support team will take it as legitimate request and process the request .

### Mitigation:
1.Freshdesk has a fix to the issue such that only emails sent to particular email address will only create tickets.The feature is called **Prevent Wildcard Ticket Create**.More deatils at https://support.freshdesk.com/en/support/solutions/articles/50000000652-receiving-spam-emails-to-support-domain-freshdesk-com-please-help-


### Optional: Supporting Material/References (Screenshots)

 * Screenshot attached.██████
* Check ticket **471406** created by me on a test account of mine.

## Impact

1.It is possible to perform sensitive action on behalf of victim .
2.Ability to spam the support inbox thus increasing the wait time and leading to inconvenience for legitimate users.

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
