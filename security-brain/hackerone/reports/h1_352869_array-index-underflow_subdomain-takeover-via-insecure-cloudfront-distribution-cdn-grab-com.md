---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '352869'
original_report_id: '352869'
title: Subdomain Takeover Via Insecure CloudFront Distribution cdn.grab.com
weakness: Array Index Underflow
team_handle: grab
created_at: '2018-05-16T13:40:17.516Z'
disclosed_at: '2021-02-24T01:52:42.853Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 127
asset_identifier: '*.grab.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- array-index-underflow
---

# Subdomain Takeover Via Insecure CloudFront Distribution cdn.grab.com

## Metadata

- HackerOne Report ID: 352869
- Weakness: Array Index Underflow
- Program: grab
- Disclosed At: 2021-02-24T01:52:42.853Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Good day, I truly hope it treats you awesomely on your side of the screen :)


I have found that your website cdn.grab.com is pointed via a cname to a cloudfront instance

cdn.grab.com => *.cloudfront.net

This was not registered on Amazon Aws Cloudfront.

I was able to take over the domain:

See my POC (Pug of Concept)
http://cdn.grab.com/index.html



Options How to fix:

1) Remove the Cname record on cdn.grab.com to not point to cloudfront.net

2) Ask me to remove my registered cdn.grab.com on cloudfront, and you can re register yours :)

May you be well on your side of the screen :)

-Eric

## Impact

Impact:

Cyber attackers can launch a phishing campaign leveraging your established (soon to be impacted) brand reputation.

The victim has no way of telling, whether the content is served by the domain owner or the cyber attacker.

Attackers can also chain higher severity attacks to this. Many applications expose session cookies to a wildcard domain (*.example.com),
so any subdomain can access them. An attacker can take a forgotten subdomain, trick the user to visit it, and extract cookies 
(even those with secure flag). This can be seen as an advanced version of XSS.

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
