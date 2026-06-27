---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1106652'
original_report_id: '1106652'
title: redirect_to(["string"]) remote code execution
weakness: Information Exposure Through an Error Message
team_handle: rails
created_at: '2021-02-18T16:40:59.146Z'
disclosed_at: '2021-05-07T23:01:09.877Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: https://github.com/rails/rails
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-exposure-through-an-error-message
---

# redirect_to(["string"]) remote code execution

## Metadata

- HackerOne Report ID: 1106652
- Weakness: Information Exposure Through an Error Message
- Program: rails
- Disclosed At: 2021-05-07T23:01:09.877Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

For example, `redirect_to(params[:user_input])`  with a URL of `?user_input[]=something` calls the method `something_url` and tries to redirect the return value of the method. If this call is on an unauthenticated route, it would allow an external user to test if a route name exists by determining if the app 500s  (the method does not exist) or successfully redirects.

## Impact

Any public method defined on a controller ending with `_url` could be remotely executed.

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
