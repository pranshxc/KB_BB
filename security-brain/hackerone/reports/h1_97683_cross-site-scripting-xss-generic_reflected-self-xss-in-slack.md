---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '97683'
original_report_id: '97683'
title: Reflected Self-XSS in Slack
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2015-11-04T12:39:02.780Z'
disclosed_at: '2015-11-10T18:32:15.422Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected Self-XSS in Slack

## Metadata

- HackerOne Report ID: 97683
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2015-11-10T18:32:15.422Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. Go to https://(domainname).slack.com/services/new
2. In the searchbar, type an XSS payload (I used <img src=x onerror=alert(document.domain)>)
3. Hit Enter
4. XSS pop-up

Thanks!

I have provided POCs

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
