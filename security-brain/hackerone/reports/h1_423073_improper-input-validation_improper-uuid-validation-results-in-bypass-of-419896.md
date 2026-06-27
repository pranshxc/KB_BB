---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '423073'
original_report_id: '423073'
title: 'Improper UUID validation results in bypass of #419896'
weakness: Improper Input Validation
team_handle: security
created_at: '2018-10-12T19:18:06.645Z'
disclosed_at: '2018-10-25T22:38:41.919Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 78
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-input-validation
---

# Improper UUID validation results in bypass of #419896

## Metadata

- HackerOne Report ID: 423073
- Weakness: Improper Input Validation
- Program: security
- Disclosed At: 2018-10-25T22:38:41.919Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This was found while evaluating the vulnerability and patch identified in #419896.  I determined the deployed patch to be effective.  However, I noticed tracer values could be sent which didn't conform to the UUID specification as characters outside of the a-f and 0-9 ranges could be used.  For example, a value such as "zzzzzzzz-zzzz-zzzz-zzzz-zzzzzzzzzzzzzz" was accepted by the server as valid.  Likely this indicates a problem with a regex filter that needs to be slightly changed.  

Steps
1. Navigate to a program which allows anonymous submissions.
2. Open the report submission form and add an attachment.
3. Observe the request sent to /attachments includes a client side generated UUID in the tracer field.
4. Replay the request from step 3.  Use an invalid UUID (e.g. "zzzzzzzz-zzzz-zzzz-zzzz-zzzzzzzzzzzzzz") for the tracer and observe the server accepts the value.

## Impact

The impact is unknown, but it is believed to have a cascading side effect.  I was asked to submit this by @jobert.

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
