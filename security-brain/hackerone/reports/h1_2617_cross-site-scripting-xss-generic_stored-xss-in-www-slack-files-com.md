---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2617'
original_report_id: '2617'
title: Stored XSS in www.slack-files.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2014-03-01T21:29:41.229Z'
disclosed_at: '2014-05-23T22:59:09.590Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in www.slack-files.com

## Metadata

- HackerOne Report ID: 2617
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2014-05-23T22:59:09.590Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

We can create posts under https://subdomain.slack.com/files/create/post

Post will have XSS payload like "><img src=x onerror=alert(10);> in title and body

We save it and hit "Create public link" and once we share the link it will trigger XSS.

Example/POC: https://slack-files.com/T025LLJ2X-F025N8W7W-3a5691

Thanks

Prakhar Prasad

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
