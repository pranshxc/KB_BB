---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '268228'
original_report_id: '268228'
title: A manager of a determinate group of users still might have access to any user
  account from any group that he doesn't administrate anymore.
weakness: Client-Side Enforcement of Server-Side Security
team_handle: mailru
created_at: '2017-09-14T04:36:46.613Z'
disclosed_at: '2017-12-27T14:26:13.865Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: biz.mail.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
- client-side-enforcement-of-server-side-security
---

# A manager of a determinate group of users still might have access to any user account from any group that he doesn't administrate anymore.

## Metadata

- HackerOne Report ID: 268228
- Weakness: Client-Side Enforcement of Server-Side Security
- Program: mailru
- Disclosed At: 2017-12-27T14:26:13.865Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Domain, site, application: biz.mail.ru

Testing environment: Lastest Chrome

Steps to reproduce:

Ok, this one is pretty much depending on scenario, so lets assume that there is the Evil Manager exists with network knowledge on higher than medium level.
At first lets say that there is such role as "Group administrator" which is granted to us by Superadministrator. Same with this permission there are defined groups of users that this particular administrator able to administrate. 
Lets assume that the Evil Manager got invite from our superviser to administrate group "Cats" and group "Doggies". There are users in each group with Id written directly in html-page (example in attachments below), so we can collect all the id's of all users from page code. Then after some time he got demoted and can not administrate group "Doggies" anymore. All users of "Doggies" group changed their passwords so the Evil Manager can not login with password that he set up for them when he was adding them to group as Group administrator. But the Evil Manager can still get access to user accounts from group "Doggies" by completing following steps:
1. Go to Users 
2. Choose any user you can administrate
3. Change his password via e-mail link, in "email" type your own mailbox.
4. Modify POST request: in URI change userId(7-digit number goes after /users/) to userId from group that you do not administrate anymore;
In body Delete everything but "id" and "email", set "Id" to userId from step 4, set "email" to your own mailbox, send it to server.

Actual results
--
On your own mailbox you will get link to choose new password for user that you dont have access to administrate. 

Expected results, security impact description and recommendations
--
I expected some error like "Not Allowed" which happens when you trying to edit data of Domain administrator when you are just a Group administrator.

PoC, exploit code, screenshots, video, references, additional resources
--
there is a large .gif in attachments that shows everything (little delay between sending a request and receiving a message to email box, sorry for that)

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
