---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '243619'
original_report_id: '243619'
title: No Rate Limitation on Regenerate Api Key
team_handle: weblate
created_at: '2017-06-27T13:00:15.458Z'
disclosed_at: '2017-08-21T17:41:05.953Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
---

# No Rate Limitation on Regenerate Api Key

## Metadata

- HackerOne Report ID: 243619
- Weakness: 
- Program: weblate
- Disclosed At: 2017-08-21T17:41:05.953Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I discovered that there is no request throttling or limit on api key regeneration. Though theres a little change while making a total of 30 requests in a few seconds, server error occurred then it continued.

##Screenshot
{F197872}

In the screenshot `685` denotes a processed request and `6052` denotes an error: on the server.

Shuaib

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
