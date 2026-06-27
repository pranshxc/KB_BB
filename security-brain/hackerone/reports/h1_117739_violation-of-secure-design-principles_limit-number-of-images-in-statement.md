---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '117739'
original_report_id: '117739'
title: limit number of images in statement
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2016-02-20T23:00:19.790Z'
disclosed_at: '2017-06-16T13:55:05.733Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# limit number of images in statement

## Metadata

- HackerOne Report ID: 117739
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2017-06-16T13:55:05.733Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello

The use of the images in the statements 

`![](http://blackdoorsec.net:80/1    "HTTP") `

There appears to be no limit on how many can be inserted.
On my own account "https://gratipay.com/~34534534fsfs/" I placed 100

Gratipay users could unknowingly become part of a DDoS attack against another site.

I would recommend limiting the number of images that can be placed.

Attached is a video of just a traffic counter being triggered by the page load.

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
