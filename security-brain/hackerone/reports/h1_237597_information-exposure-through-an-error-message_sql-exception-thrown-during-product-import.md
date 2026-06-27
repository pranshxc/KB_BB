---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '237597'
original_report_id: '237597'
title: SQL Exception thrown during product import
weakness: Information Exposure Through an Error Message
team_handle: shopify
created_at: '2017-06-07T16:18:36.209Z'
disclosed_at: '2017-07-12T00:44:11.203Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- information-exposure-through-an-error-message
---

# SQL Exception thrown during product import

## Metadata

- HackerOne Report ID: 237597
- Weakness: Information Exposure Through an Error Message
- Program: shopify
- Disclosed At: 2017-07-12T00:44:11.203Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Possible SQL Injection was observed when a descriptive error message was thrown in a mail sent to the user while importing products from csv. Used some special characters in csv to induce the error.

DATABASE FOUND TO BE MYSQL.

{F192274}

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
