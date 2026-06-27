---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '846400'
original_report_id: '846400'
title: .git file accessible on remote.bittorrent.com
weakness: Information Disclosure
team_handle: btfs
created_at: '2020-04-10T12:04:52.839Z'
disclosed_at: '2020-05-11T23:12:54.468Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# .git file accessible on remote.bittorrent.com

## Metadata

- HackerOne Report ID: 846400
- Weakness: Information Disclosure
- Program: btfs
- Disclosed At: 2020-05-11T23:12:54.468Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi team,
i detected your .git file accessible for any unauthorized user.

url : https://remote.bittorrent.com/static/webui/.git/config

HTTP/1.1 200 OK
Set-Cookie: BTURT=talon-i-0837bbfadd509c546-2; path=/; domain=.utorrent.com
Server: TornadoServer/2.1.1git
Connection: keep-alive
Content-Length: 260
Last-Modified: Wed, 18 Mar 2015 19:18:46 GMT
Accept-Ranges: bytes
Content-Type: text/html; charset=UTF-8
Cache-Control: public
Cache-Control: private

[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = git@github.com:bittorrent/webui.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master

## Impact

change perm for this

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
