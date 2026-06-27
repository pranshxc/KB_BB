---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '221298'
original_report_id: '221298'
title: GIT Detected
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2017-04-15T21:22:26.114Z'
disclosed_at: '2017-04-20T09:58:38.332Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- information-disclosure
---

# GIT Detected

## Metadata

- HackerOne Report ID: 221298
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2017-04-20T09:58:38.332Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello team,
While i was testing nextcloud.com, I've detected GIT repository files. GIT repository files can disclose GIT repository usernames and file lists. While disclosures of this type do not provide direct attack vectors, they can be useful for an attacker when combined with other vulnerabilities discovered within the application. 

URL:  https://nextcloud.com/wp-content/themes/next/.git/config

Page is showing:
[core] repositoryformatversion = 0 filemode = true bare = false logallrefupdates = true [remote "origin"] url = https://github.com/nextcloud/nextcloud.com.git fetch = +refs/heads/*:refs/remotes/origin/* [branch "master"] remote = origin merge = refs/heads/master [branch "pricing"] remote = origin merge = refs/heads/pricing [branch "orderform"] remote = origin merge = refs/heads/orderform

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
