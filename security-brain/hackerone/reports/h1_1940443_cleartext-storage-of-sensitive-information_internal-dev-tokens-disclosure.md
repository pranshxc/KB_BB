---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1940443'
original_report_id: '1940443'
title: internal dev tokens disclosure
weakness: Cleartext Storage of Sensitive Information
team_handle: snapchat
created_at: '2023-04-10T08:51:07.984Z'
disclosed_at: '2023-06-14T10:27:08.739Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 88
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# internal dev tokens disclosure

## Metadata

- HackerOne Report ID: 1940443
- Weakness: Cleartext Storage of Sensitive Information
- Program: snapchat
- Disclosed At: 2023-06-14T10:27:08.739Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

snapchat has made Keydb as opensource but its development repo on github is leaking too much internal sensitive data in commits history which should not be a good idea to be revealed in open source project.
such as https://github.com/Snapchat/KeyDB/commit/157b32109854f947843366f66215ccf90809e766
```
[Dockerfile](https://github.sc-corp.net/Snapchat/keydb-internal/github-action-runner-docker/Dockerfile). 
3. Take the token from that script. Should be in "Configure" section: 
    ``` 
    ./config.sh --url https://github.com/EQ-Alpha/KeyDB --token ████
```
██████

## Impact

internal dev sensitive information disclosed publicaly
for example PAT token i pasted above

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
