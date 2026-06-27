---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '309058'
original_report_id: '309058'
title: Open Redirect on the nl.wordpress.net
weakness: Open Redirect
team_handle: wordpress
created_at: '2018-01-25T17:33:02.479Z'
disclosed_at: '2018-02-22T22:53:16.427Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: '*.wordpress.net'
asset_type: WILDCARD
max_severity: low
tags:
- hackerone
- open-redirect
---

# Open Redirect on the nl.wordpress.net

## Metadata

- HackerOne Report ID: 309058
- Weakness: Open Redirect
- Program: wordpress
- Disclosed At: 2018-02-22T22:53:16.427Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Description
Hello. I discovered an Open redirect vulnerability on the `nl.wordpress.org`.

##Root cause
The 301 Redirect contains full hostname, followed with `@` without trailing slash, when using:
```
GET /@google.com HTTP/1.1
Host: nl.wordpress.net
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1

```
```
HTTP/1.1 301 Moved Permanently
Date: Thu, 25 Jan 2018 17:26:07 GMT
Server: Apache
Location: http://nl.wordpress.org@google.com
Content-Length: 242
Keep-Alive: timeout=2, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=iso-8859-1

```

##POC (Google Chrome)
http://nl.wordpress.net/@google.com

##Suggested fix
Appending the trailing slash after location hostname should fix the issue.
e.g.
```
Location: http://nl.wordpress.org@google.com
```
=>
```
Location: http://nl.wordpress.org/@google.com
```

## Impact

The attacker can redirect the victim to the malicious site using legit *.wordpress.net subdomain name, which can be the copy of the real site, asking for the user credentials.

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
