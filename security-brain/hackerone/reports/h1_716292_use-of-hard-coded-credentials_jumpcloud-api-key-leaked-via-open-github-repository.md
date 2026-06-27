---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '716292'
original_report_id: '716292'
title: JumpCloud API Key leaked via Open Github Repository.
weakness: Use of Hard-coded Credentials
team_handle: starbucks
created_at: '2019-10-17T11:14:33.624Z'
disclosed_at: '2019-12-30T15:40:29.038Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 715
asset_identifier: Other non domain specific items
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- use-of-hard-coded-credentials
---

# JumpCloud API Key leaked via Open Github Repository.

## Metadata

- HackerOne Report ID: 716292
- Weakness: Use of Hard-coded Credentials
- Program: starbucks
- Disclosed At: 2019-12-30T15:40:29.038Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** Open Github Repo Leaking Starbucks JumbCloud API Key

**Description:** 
Team,

While going through Github search I discovered a public repository which contains Jumbcloud API Key of Starbucks. 

Repo:  [https://github.com/██████████/Project](https://github.com/██████████/Project).
File: [https://github.com/████/Project/blob/0d56bb910923da2fbee95971778923f734a25f68/getSystemUsers.go](https://github.com/████/Project/blob/0d56bb910923da2fbee95971778923f734a25f68/getSystemUsers.go)

```
req.Header.Add("x-api-key", "████████")
```

**POC**
* List systems ```
curl -H "x-api-key: ████████" "https://console.jumpcloud.com/api/systems"
``` There are multiple AWS instances present

* ```
curl -H "x-api-key: █████" "https://console.jumpcloud.com/api/systemusers"
```
* SSO Applications ```curl -H "x-api-key: ██████" "https://console.jumpcloud.com/api/applications"
``` AWS login SAM config is presents. This would leads to AWS account takeover

## Impact

This issue impact is critical as through this API anyone could 
* Execute commands on systems [https://docs.jumpcloud.com/1.0/commands/create-a-command](https://docs.jumpcloud.com/1.0/commands/create-a-command)
* Add/Remove users which has access to internal systems
* AWS Account Takeover

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
