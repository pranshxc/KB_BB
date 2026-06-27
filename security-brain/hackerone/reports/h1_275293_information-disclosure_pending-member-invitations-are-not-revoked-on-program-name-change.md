---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '275293'
original_report_id: '275293'
title: Pending member invitations are not revoked on program name change
weakness: Information Disclosure
team_handle: security
created_at: '2017-10-07T05:47:43.291Z'
disclosed_at: '2017-11-18T00:53:39.057Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Pending member invitations are not revoked on program name change

## Metadata

- HackerOne Report ID: 275293
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2017-11-18T00:53:39.057Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

**Summary:**
When private program updates the handle of the hackerone program, former **team members** can see the new updated handles using old invitation link.

The invitation link looks like `https://hackerone.com/invitations/<UID>`

This may also be true for participants participating in private programs but i can not confirm this yet. 

**Description (Include Impact):**
Former team members should not see the updated handle. Lets consider the example of `█████` private program which may have invited few team members and later removed them for some reason. The program was later acquired by `█████████` and handle was changed accordingly. But the former team members can still see this updated name as `██████████` using old invitation links. I verified this by changing my demo team handle from test account using hackerone support.

This may be possible for researchers too. when private program invites them, they also get invitation links. if researcher themselves quits the program or program decides to remove them for some reason, they can still use old invitation link which redirects to new updated handle.

### Steps To Reproduce

1. Using a private program, invite any team members to join your team 
2. Team member receives the invitation and he joins the program
3. Remove team member from your program and update the program handle with new name 
4. Now, team member can browse to old invitation link, which will redirect him to new updated handle in url (he will get 404 but still can see the handle in url)

Regards,
Ashish

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
