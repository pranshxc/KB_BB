---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1406335'
original_report_id: '1406335'
title: Subdomain takeover of images.crossinstall.com
weakness: Business Logic Errors
team_handle: x
created_at: '2021-11-21T03:12:47.555Z'
disclosed_at: '2022-01-05T19:58:27.163Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 63
tags:
- hackerone
- business-logic-errors
---

# Subdomain takeover of images.crossinstall.com

## Metadata

- HackerOne Report ID: 1406335
- Weakness: Business Logic Errors
- Program: x
- Disclosed At: 2022-01-05T19:58:27.163Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary
images.crossinstall.com points to an AWS S3 bucket that no longer exists. I was able to take control of this bucket and put my own content onto it. I can now serve content on this domain, obtain a TLS certificate for this domain, etc.

If any customers or servers are pointing to anything within this domain, I could serve them arbitrary/malicious content. I could also use this in case your domain whitelists your own domain for OAuth, or if there are cookies scoped to the entire domain. Usually this can have a high impact.

## PoC
Visit images.crossinstall.com/index.html; an HTML comment with my username is present.

```
% dig images.crossinstall.com +short
assets.crossinstall.com.s3.amazonaws.com.
s3-1-w.amazonaws.com.
s3-w.us-east-1.amazonaws.com.
52.217.103.180

% curl images.crossinstall.com/index.html
<!-- hackerone/ian bugcrowd/iangcarroll -->

% whois crossinstall.com | grep Org
Registrant Organization: Twitter, Inc.
Admin Organization: Twitter, Inc.
Tech Organization: Twitter, Inc.
```

## Impact

Subdomain takeover

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
