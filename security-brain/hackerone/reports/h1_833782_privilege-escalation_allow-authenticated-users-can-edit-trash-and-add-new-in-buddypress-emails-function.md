---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '833782'
original_report_id: '833782'
title: Allow authenticated users can edit, trash,and add new in BuddyPress Emails
  function
weakness: Privilege Escalation
team_handle: wordpress
created_at: '2020-03-29T08:52:13.199Z'
disclosed_at: '2020-05-22T00:33:04.676Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: BuddyPress Core
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Allow authenticated users can edit, trash,and add new in BuddyPress Emails function

## Metadata

- HackerOne Report ID: 833782
- Weakness: Privilege Escalation
- Program: wordpress
- Disclosed At: 2020-05-22T00:33:04.676Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Description:

Allow author can edit, trash,and add new your posts in BuddyPress Emails function
And editor can edit,trash, add new any posts in BuddyPress Emails default.
## Steps To Reproduce:

Step 1 : Create two accounts: Admin and Author
Step 2: Login with admin account. In admin account, give author to admin account.
Step 4: Login with author within dashboard
Access link:
*domain/wp-admin/edit.php?post_type=bp-email*
Step 5: Revoke author to author privilege in admin account
Step 6: Within author dashboard, author can edit, trash,and add new
PoC by video:
https://bit.ly/2UH7iLz
## Recommendations
Valid user current session access.

## Impact

Author can edit, trash,and add new in BuddyPress Emails.
And editor can edit,trash, add new any posts in BuddyPress Emails default.

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
