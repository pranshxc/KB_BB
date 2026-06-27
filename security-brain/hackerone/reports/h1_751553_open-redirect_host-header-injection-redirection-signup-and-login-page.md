---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '751553'
original_report_id: '751553'
title: Host header injection/redirection | signup and login page
weakness: Open Redirect
team_handle: nordsecurity
created_at: '2019-12-14T06:19:36.707Z'
disclosed_at: '2020-02-21T11:27:12.055Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 8
asset_identifier: '*.nordvpn.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Host header injection/redirection | signup and login page

## Metadata

- HackerOne Report ID: 751553
- Weakness: Open Redirect
- Program: nordsecurity
- Disclosed At: 2020-02-21T11:27:12.055Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hey Team.

There's a host header injection vulnerability in  signup and login page.

If possible, the application should avoid incorporating user-controllable data into redirection targets. In many cases, this behavior can be avoided in two ways:
Remove the redirection function from the application, and replace links to it with direct links to the relevant target URLs.
Maintain a server-side list of all URLs that are permitted for redirection. Instead of passing the target URL as a parameter to the redirector, pass an index into this list.

Vulnerable URL:
https://affiliates.nordvpn.com/signup

Payload: " Host: constitutionclub.in"

How to reproduce this vulnerability:

1.Open this URL "https://affiliates.nordvpn.com/signup" 
2.Send it to the repeater in burp suite add the payload to the header request and forward the request.
3.It will directly redirect to constitutionclub.in

## Impact

Whenever a user visits this URL, it will redirect them to site.com. It is used in phishing attacks.

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
