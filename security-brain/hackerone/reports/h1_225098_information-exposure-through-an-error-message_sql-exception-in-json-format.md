---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '225098'
original_report_id: '225098'
title: SQL exception in JSON format
weakness: Information Exposure Through an Error Message
team_handle: nextcloud
created_at: '2017-04-30T11:18:15.867Z'
disclosed_at: '2020-01-31T14:12:15.122Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- information-exposure-through-an-error-message
---

# SQL exception in JSON format

## Metadata

- HackerOne Report ID: 225098
- Weakness: Information Exposure Through an Error Message
- Program: nextcloud
- Disclosed At: 2020-01-31T14:12:15.122Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi, I know this is not critical, just a design issue,
but it will be better if it will not show up to the user as an error, maybe in log files readable to the www-user or to the root user in order to debug.

PoC:
----------------------
1. Create a user and confirm the password
2. Capture the packet
3. Replay the packet with a username bigger than 64 words in length two times in order to duplicate the user.
4. Receiving error.

This is working only when the input for the username is bigger than 64 words. (65 needed.)

### Example:
***Request*** -
POST http://172.16.1.68/nextcloud/index.php/settings/users/users HTTP/1.1
DATA: username=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&password=test123A

***Response*** -
```
{"message":"An exception occurred while executing 'INSERT INTO `oc_users` ( `uid`, `password` ) VALUES( ?, ? )' with params [\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\", \"1|$2y$10$gwzH19jqn8HveRpCb2haNurF7rycqsZeYYS7b1zPENnUInUyP35J2\"]:\n\nSQLSTATE[23000]: Integrity constraint violation: 1062 Duplicate entry 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' for key 'PRIMARY'"}
```

### Example:
***Request*** -
POST http://172.16.1.68/nextcloud/index.php/settings/users/users HTTP/1.1
DATA: username=aaaaaaa&password=test123A

***Response*** -
```
{"message":"A user with that name already exists."}
```

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
