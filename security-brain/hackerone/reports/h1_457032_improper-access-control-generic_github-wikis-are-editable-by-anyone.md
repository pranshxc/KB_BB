---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '457032'
original_report_id: '457032'
title: Github wikis are editable by anyone
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2018-12-06T19:02:24.008Z'
disclosed_at: '2018-12-07T18:11:16.495Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: nextcloud/spreed
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Github wikis are editable by anyone

## Metadata

- HackerOne Report ID: 457032
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2018-12-07T18:11:16.495Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Github wikis on the following projects 

https://github.com/nextcloud/fulltextsearch
https://github.com/nextcloud/nextcloudpi
https://github.com/nextcloud/spreed
https://github.com/nextcloud/ocsms
https://github.com/nextcloud/nextcloud-snap
https://github.com/nextcloud/passman

can be edited by any logged in user in the system. This poses security and reputation risk for the company.

{F386595}

## Impact

As wikis listed above can be edited by any person on the internet, a malicious actor can accurately craft a message or a note which would lead a user to download a malicious component in a natural way.

For example: 
```
Please note that the current version is not stable due to the following line:
informat_note_send.c:4562
To ensure that the program won't crush in production, please consider installing this patch http://notsoevil.com.
In case of any following troubles, drop us an email at support@company.com
```

The user would surely trust the code (of course if he trusts the company itself), so he will extrapolate this trust to the wiki and consider it being safe enough to follow the instructions and downloading himself a malware.

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
