---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '76733'
original_report_id: '76733'
title: Using GET method for account login with CSRF token leaking to external sites
  Via Referer.
weakness: Information Disclosure
team_handle: zaption
created_at: '2015-07-19T10:35:01.586Z'
disclosed_at: '2016-05-02T19:08:58.195Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Using GET method for account login with CSRF token leaking to external sites Via Referer.

## Metadata

- HackerOne Report ID: 76733
- Weakness: Information Disclosure
- Program: zaption
- Disclosed At: 2016-05-02T19:08:58.195Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

HI

At the time of login, the values are present in URL along with the CSRF token.  Also this URL is leaking to external sites in HTTP REFRERER. 

Here are some of those sites:
dxzc9stvaxhhy.cloudfront.net
bam.nr-data.net
ssl.google-analytics.com
usage.trackjs.com
api.mixpanel.com

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
