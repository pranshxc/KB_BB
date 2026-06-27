---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1752146'
original_report_id: '1752146'
title: POST following PUT confusion
weakness: Information Disclosure
team_handle: ibb
created_at: '2022-10-26T14:34:05.583Z'
disclosed_at: '2022-12-02T21:03:59.407Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# POST following PUT confusion

## Metadata

- HackerOne Report ID: 1752146
- Weakness: Information Disclosure
- Program: ibb
- Disclosed At: 2022-12-02T21:03:59.407Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The bug I submitted at https://github.com/curl/curl/issues/9507 can have at least a few unintended security issues:

Information Disclosure: this bug causes an HTTP PUT to occur when the user intends for an HTTP POST to occur. The user, who intended an HTTP POST, expects the POSTed information to come from CURLOPT_POSTFIELDS. However, as an HTTP PUT is performed instead, the data that is PUT comes from a buffer specified in CURLOPT_READDATA, which may be sensitive information intended for an entirely different host (host1.com below). If CURLOPT_READDATA is not specified, this data could come from stdin!
Use after free: using the description above, if the user had already freed the data specified in CURLOPT_READDATA, then the unintended HTTP PUT (which was intended to be an HTTP POST) would attempt to read the freed data specified in CURLOPT_READDATA.

## Impact

An attacker could potentially inject data, either from stdin or from an unintended buffer. Further, without even an active attacker, this could lead to segfaults or sensitive information being exposed to an unintended recipient.

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
