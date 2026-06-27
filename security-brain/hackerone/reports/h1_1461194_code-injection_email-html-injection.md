---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1461194'
original_report_id: '1461194'
title: Email html Injection
weakness: Code Injection
team_handle: slack
created_at: '2022-01-27T04:42:26.193Z'
disclosed_at: '2022-05-19T13:03:58.271Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
asset_identifier: app.slack.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- code-injection
---

# Email html Injection

## Metadata

- HackerOne Report ID: 1461194
- Weakness: Code Injection
- Program: slack
- Disclosed At: 2022-05-19T13:03:58.271Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This bug is Email html Injection present in name of workspace while creating

## Impact

The input is unsanitized and vulnerable which led to html injection which may lead to phishing. when 2fa is applied it send mail with injected html

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
