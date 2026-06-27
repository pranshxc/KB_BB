---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '866271'
original_report_id: '866271'
title: Lack of Input sanitization leads to database Character encoding configuration
  Disclosure
weakness: Information Exposure Through an Error Message
team_handle: unikrn
created_at: '2020-05-05T06:59:46.406Z'
disclosed_at: '2020-08-07T08:48:39.733Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: unikrn.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-exposure-through-an-error-message
---

# Lack of Input sanitization leads to database Character encoding configuration Disclosure

## Metadata

- HackerOne Report ID: 866271
- Weakness: Information Exposure Through an Error Message
- Program: unikrn
- Disclosed At: 2020-08-07T08:48:39.733Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary:
Email Input field during Register is not properly sanitized leads to sql error 

 Steps To Reproduce:
   During Register use '💩' character in email field

## Impact

Information Exposure Through an Error Message
███████

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
