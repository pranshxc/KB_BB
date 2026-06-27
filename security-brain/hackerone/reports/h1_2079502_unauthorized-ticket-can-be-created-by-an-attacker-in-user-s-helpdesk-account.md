---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2079502'
original_report_id: '2079502'
title: Unauthorized Ticket can be created by an Attacker in user's Helpdesk account
team_handle: security
created_at: '2023-07-21T22:41:25.023Z'
disclosed_at: '2023-09-08T09:29:52.808Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: support.hackerone.com
asset_type: URL
max_severity: none
tags:
- hackerone
---

# Unauthorized Ticket can be created by an Attacker in user's Helpdesk account

## Metadata

- HackerOne Report ID: 2079502
- Weakness: 
- Program: security
- Disclosed At: 2023-09-08T09:29:52.808Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey Team! 

I was able to create a ticket in any user's Support.hackerone.com account without authorization, and can write whatever I wanted in that ticket. Normally, in order to get help, users are required to log in and create a ticket. However, due to this flaw, I could create tickets on behalf of any user without their permission or knowledge. 


### Steps To Reproduce

1. Go to https://emkei.cz/ and enter victim's email as the sender, and support@hackerone.com as the receiver. Fill out other necessary details.

2. Solve the captcha and send the email.

3. Check your helpdesk account at support.hackerone.com and you will see new ticket.


### Optional: Supporting Material/References (Screenshots)

https://medium.com/@khaled.hassan/hacking-thousands-of-companies-through-their-helpdesk-8f180a8595ef

POC :
████

## Impact

Unauthorized user can create  tickets in any user's help desk account!

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
