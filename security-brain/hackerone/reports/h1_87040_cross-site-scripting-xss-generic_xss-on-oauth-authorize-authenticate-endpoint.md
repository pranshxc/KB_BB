---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '87040'
original_report_id: '87040'
title: XSS on OAuth authorize/authenticate endpoint
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2015-09-02T15:24:28.460Z'
disclosed_at: '2015-11-20T18:49:04.664Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS on OAuth authorize/authenticate endpoint

## Metadata

- HackerOne Report ID: 87040
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2015-11-20T18:49:04.664Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I would like to report an issue where certain endpoints on twitter.com and api.twitter.com is vulnerable to XSS.

##Detail
The redirection page after authorization/authentication does not sanitize the *oauth_callback* parameter.

##PoC
1. Go to http://innerht.ml/pocs/twitter-oauth-xss (Please use IE or something that hasn't implemented CSP)
2. Click on Authorize app
3. Alert pops up

Note: it also affects api.twitter.com as they both have the same endpoints

##Repo step
1. Obtain the request token (https://api.twitter.com/oauth/request_token) where parameter *oauth_callback* contains HTML like ```javascript%3A%2F%2F"><script>alert(document.domain)</script>```
2. Redirect the victim to the authorize/authenticate page with the token

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
