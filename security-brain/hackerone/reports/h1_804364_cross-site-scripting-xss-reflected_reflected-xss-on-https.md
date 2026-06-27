---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '804364'
original_report_id: '804364'
title: Reflected XSS on https://███████/
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2020-02-25T10:49:54.642Z'
disclosed_at: '2020-07-30T17:53:19.370Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on https://███████/

## Metadata

- HackerOne Report ID: 804364
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2020-07-30T17:53:19.370Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

Hey Team,

There is reflected xss on https://█████/kinetic/ when certain action results in 404 error.

**Description:**

I am using some random strings paths after kinetic in https://███████/kinetic/ if that path is not exist then it says 404 not found. Strings is not sanitized after kinetic/ due to which any one can able to use Java Script code after kinetic/ and it executed successfully leads to reflected xss.

## Impact

The attacker can able to execute JS code.

## Step-by-step Reproduction Instructions

1. open this  https://████████/kinetic/1%3C!--%3E%3CSvg%20OnLoad=(confirm)(document.domain)--%3E/ in firefox
2. You will get alert pop up.

## Product, Version, and Configuration (If applicable)

## Suggested Mitigation/Remediation Actions

Sanitize string

## Impact

The attacker can able to execute JS code.

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
