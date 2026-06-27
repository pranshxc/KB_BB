---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1386547'
original_report_id: '1386547'
title: Disclosure of github access token in config file via nignx off-by-slash
weakness: Path Traversal
team_handle: adobe
created_at: '2021-10-30T15:35:05.117Z'
disclosed_at: '2022-01-13T18:16:19.419Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: '*.marketo.com'
asset_type: URL
max_severity: critical
tags:
- hackerone
- path-traversal
---

# Disclosure of github access token in config file via nignx off-by-slash

## Metadata

- HackerOne Report ID: 1386547
- Weakness: Path Traversal
- Program: adobe
- Disclosed At: 2022-01-13T18:16:19.419Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
`██████████` is vulnerable to Nginx off-by-slash vulnerability that exposes Git configuration.

## Steps To Reproduce:
1. Visit `https://█████████████` to download git config containing username and token.
2. Use it to pull entire source code via `git clone ████████`

Leaked:
```
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = ████
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
[branch "vespa-2021-Q4"]
	remote = origin
	merge = refs/heads/vespa-2021-Q4
```

## Impact

Malicious attacker can mess around using the leaked github token to access and modify or even try to delete github repos that the token has permission to.

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
