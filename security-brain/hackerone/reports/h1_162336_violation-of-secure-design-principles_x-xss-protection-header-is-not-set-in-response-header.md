---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '162336'
original_report_id: '162336'
title: x-xss protection header is not set in response header
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2016-08-23T08:05:55.552Z'
disclosed_at: '2017-07-10T10:01:10.078Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- violation-of-secure-design-principles
---

# x-xss protection header is not set in response header

## Metadata

- HackerOne Report ID: 162336
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2017-07-10T10:01:10.078Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

URL : http://inside.gratipay.com/

Description : 
This header enables the Cross-site scripting (XSS) filter built into most recent web browsers. It's usually enabled by default anyway, so the role of this header is to re-enable the filter for this particular website if it was disabled by the user. This header is supported in IE 8+, and in Chrome (not sure which versions). The anti-XSS filter was added in Chrome 4. Its unknown if that version honored this header.

Solution : Need to set X-XSS-Protection: 1; mode=block in response header

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
