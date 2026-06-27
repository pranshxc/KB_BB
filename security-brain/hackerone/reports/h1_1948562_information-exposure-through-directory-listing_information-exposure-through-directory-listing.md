---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1948562'
original_report_id: '1948562'
title: Information Exposure Through Directory Listing
weakness: Information Exposure Through Directory Listing
team_handle: mars
created_at: '2023-04-15T18:35:12.331Z'
disclosed_at: '2023-06-23T14:57:45.264Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: '*.individualis.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-exposure-through-directory-listing
---

# Information Exposure Through Directory Listing

## Metadata

- HackerOne Report ID: 1948562
- Weakness: Information Exposure Through Directory Listing
- Program: mars
- Disclosed At: 2023-06-23T14:57:45.264Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Directory listing is a web server function that displays the directory contents when there is no index file in a specific website directory. It is dangerous to leave this function turned on for the web server because it leads to information disclosure.

## Steps To Reproduce:

Go to this URL:  http://35.156.91.137/grafana/logs/
You can see logs files
http://35.156.91.137/grafana/logs/error.log
http://35.156.91.137/grafana/logs/access.log

## PoC:
```
88.244.90.152 - - [31/Jan/2022:11:53:19 +0000] "GET /api/live/ws HTTP/1.1" 400 3325 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
165.225.95.75 - - [31/Jan/2022:11:53:20 +0000] "GET /api/live/ws HTTP/1.1" 400 3325 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
88.244.90.152 - - [31/Jan/2022:11:53:21 +0000] "GET /api/live/ws HTTP/1.1" 400 872 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
```
```
[Sat Feb 05 01:49:35.862611 2022] [core:error] [pid 8186:tid 140028348987136] [client 161.35.86.181:47058] AH00126: Invalid URI in request GET /cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/hosts HTTP/1.1
[Sat Feb 05 01:49:36.316927 2022] [authz_core:error] [pid 8186:tid 140027803723520] [client 161.35.86.181:47426] AH01630: client denied by server configuration: proxy:http://127.0.0.1:3000/server-status
[Thu Feb 10 23:55:47.412015 2022] [ssl:error] [pid 11243:tid 140029020075776] [client 54.205.194.131:42490] AH02042: rejecting client initiated renegotiation
[Fri Feb 11 06:50:00.503097 2022] [proxy:error] [pid 4547:tid 140029011683072] (111)Connection refused: AH00957: HTTP: attempt to connect to 127.0.0.1:3000 (127.0.0.1) failed
```

## Impact

Information Disclosure

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
