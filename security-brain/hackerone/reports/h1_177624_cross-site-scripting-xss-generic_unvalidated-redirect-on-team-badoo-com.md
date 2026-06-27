---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '177624'
original_report_id: '177624'
title: Unvalidated redirect on team.badoo.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: bumble
created_at: '2016-10-23T09:13:56.683Z'
disclosed_at: '2016-12-03T12:22:31.916Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Unvalidated redirect on team.badoo.com

## Metadata

- HackerOne Report ID: 177624
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: bumble
- Disclosed At: 2016-12-03T12:22:31.916Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#Domain affected: 
https://team.badoo.com/  (corp.badoo.com)

#PoC (Tested on Firefox): 
https://team.badoo.com/%0d%0adata:text/html;text,%3Csvg%2fonload%3Dprompt%281%29%3E
{F129735}

#Describe:
team.badoo.com may vulnerable to CRLF injection, when we inject %0d%0a into url, the Location header, entire content after %0d%0a and '/' will appear in Response header:
{F129733}

Since your server is configured pretty good that i can't do attack like HTTP response splitting or redirect to external url, i decided to test XSS on it.

Using Data URI scheme which is a uniform resource identifier (URI) scheme that provides a way to include data in-line in web pages as if they were external resources can bypass it and triggered XSS:
{F129734}

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
