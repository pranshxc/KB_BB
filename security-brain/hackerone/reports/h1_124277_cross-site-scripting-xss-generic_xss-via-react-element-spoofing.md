---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '124277'
original_report_id: '124277'
title: XSS via React element spoofing
weakness: Cross-site Scripting (XSS) - Generic
team_handle: imgur
created_at: '2016-03-18T15:20:28.897Z'
disclosed_at: '2016-03-23T23:11:47.844Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS via React element spoofing

## Metadata

- HackerOne Report ID: 124277
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: imgur
- Disclosed At: 2016-03-23T23:11:47.844Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello, I noticed an XSS on imgur. Proof of concept: visit the URL

http://imgur.com/vidgif/ticket/aaaaaaaa?error[props][dangerouslySetInnerHTML][__html]=%3Cimg%20src=a%20onerror=%22alert(%27XSS%20on%20%27%2bdocument.domain)%22%3E&error[_isReactElement]=true&error[type]=body

It's not the simplest case as it requires some React magic. There is a good explanation of this type of vulnerabilities at http://danlec.com/blog/xss-via-a-spoofed-react-element . Corresponding H1 report: https://hackerone.com/reports/49652 .

The impact is as usual. The attacker could execute operations on behalf of the victim who visits a malicious link, or access e.g. the session cookie (IMGURSESSION).

I haven't yet checked if this the only such occurrence on Imgur.

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
