---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '226418'
original_report_id: '226418'
title: HackerOne reports escalation to JIRA is CSRF vulnerable
weakness: Cross-Site Request Forgery (CSRF)
team_handle: security
created_at: '2017-05-05T20:39:02.926Z'
disclosed_at: '2017-08-30T09:33:31.440Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 34
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# HackerOne reports escalation to JIRA is CSRF vulnerable

## Metadata

- HackerOne Report ID: 226418
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: security
- Disclosed At: 2017-08-30T09:33:31.440Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

HackerOne reports escalation to JIRA is CSRF vulnerable

**Description (Include Impact):**

An attacker can steal private reports details through a CSRF in HackerOne report escalation to JIRA implementation.

### CSRF

GET https://hackerone.com/reports/[REPORT_NUMBER]/escalate

### Optional: Supporting Material/References (Screenshots)

 * https://youtu.be/N6JSGA_RIV4

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
