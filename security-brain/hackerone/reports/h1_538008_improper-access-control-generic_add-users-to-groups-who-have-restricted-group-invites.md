---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '538008'
original_report_id: '538008'
title: Add users to groups who have restricted group invites
weakness: Improper Access Control - Generic
team_handle: wordpress
created_at: '2019-04-14T13:20:39.998Z'
disclosed_at: '2019-07-27T09:22:18.600Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 30
asset_identifier: BuddyPress Core
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Add users to groups who have restricted group invites

## Metadata

- HackerOne Report ID: 538008
- Weakness: Improper Access Control - Generic
- Program: wordpress
- Disclosed At: 2019-07-27T09:22:18.600Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#Description:

WordPress version: 5.2
BuddyPress version: 4.2.0

Through this vulnerability, an attacker could add users to groups who have set :
   `I want to restrict Group invites to my friends only.`

There is no proper validation of the personal settings of the user and thus the users with such privacy settings selected could be added.

#Steps to Reproduce:

Make 2 accounts A and B, make sure they are not friends.

  1. From account of user A, enable the setting `I want to restrict Group invites to my friends only.` from the following URL http://bbwordpress.esy.es/members/yuvraj/settings/invites/.
  2. From account of user B, make a POST request to : 

      `POST : http://bbwordpress.esy.es/wp-admin/admin-ajax.php`
       `BODY : message=&nonce=21f500cbfd&group_id=1&action=groups_send_group_invites&_wpnonce=7264177f51&users%5B%5D=3`

  3. Replace the value of users with the victims user id , i.e id of user A.
  4. Victim (user A) would receive an invitation from Attacker (user B) even though the privacy setting to restrict group invites has been enabled.

## Impact

An attacker who is not a friend of the victim can send him a group invite even though the victim has selected to restrict group invites from friends only.

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
