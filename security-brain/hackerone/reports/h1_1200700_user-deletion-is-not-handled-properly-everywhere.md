---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1200700'
original_report_id: '1200700'
title: User deletion is not handled properly everywhere
team_handle: nextcloud
created_at: '2021-05-18T09:00:54.288Z'
disclosed_at: '2021-07-15T19:12:16.497Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 76
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# User deletion is not handled properly everywhere

## Metadata

- HackerOne Report ID: 1200700
- Weakness: 
- Program: nextcloud
- Disclosed At: 2021-07-15T19:12:16.497Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

So I came across this when going over https://nextcloud.com/compare/

And noticed the section: "BUILT IN DATA-REQUEST/ACCOUNT DELETION"

However looking at this it seems this is not handled properly everywhere in Nextcloud. I understand that the GDPR etc do consider shared data differently. For example a conversation two people have is shared data often and does not always have to be deleted.

In anycase let me describe what I found.

1. userA has an account on server
2. userB has an account on server
3. userA and userB do a lot of chatting via talk
4. At some point userB leaves the server and their account is deleted
5. Now a new user comes along that gets assigned the id userB (or registers it or whatever)
6. If the new userB now opens the chat to userA they will see all the messages exchanged between userA and the old userB

## Impact

New users might get access to data of other users that left the system. This should not happen.

I would suggest (to make your own life easier) to keep a blocklist of ids for users. So that these things can't happen.
You still have to make sure all required data is removed. But of you miss something at least it won't possibly get leaked to new users.

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
