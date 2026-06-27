---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '296632'
original_report_id: '296632'
title: Audit log validation
weakness: Improper Neutralization of HTTP Headers for Scripting Syntax
team_handle: weblate
created_at: '2017-12-10T04:08:59.173Z'
disclosed_at: '2018-08-28T08:07:11.549Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: https://github.com/WeblateOrg/docker
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-neutralization-of-http-headers-for-scripting-syntax
---

# Audit log validation

## Metadata

- HackerOne Report ID: 296632
- Weakness: Improper Neutralization of HTTP Headers for Scripting Syntax
- Program: weblate
- Disclosed At: 2018-08-28T08:07:11.549Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Issue ##
For the docker image (git clone https://github.com/WeblateOrg/docker.git weblate-docker), the IP address in the audit log (in the user's profile, and in the administration console) can be forged using the `X-Forwarded-For` header during the login process.

This does not affect http://demo.weblate.org/.

For http://demo.weblate.org/, `User-Agent: '"<b>test` was accepted. This will not lead to XSS issues, but could potentially be an issue if the input is used elsewhere, such as a database query.

## Impact

## Consequence ##
When using the docker image, it may be possible to spoof audit log entries. If an account were compromised, it may be more difficult to determine this from the audit log entries.

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
