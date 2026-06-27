---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '14803'
original_report_id: '14803'
title: 'Serving Transitions From: HTTP Protocol (not secure)'
weakness: Information Disclosure
team_handle: automattic
created_at: '2014-06-03T09:24:00.621Z'
disclosed_at: '2014-06-04T12:57:32.154Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Serving Transitions From: HTTP Protocol (not secure)

## Metadata

- HackerOne Report ID: 14803
- Weakness: Information Disclosure
- Program: automattic
- Disclosed At: 2014-06-04T12:57:32.154Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Dear Sir,

I've Noticed from your SourceCode that you are using HTTP Protocol, and that will makes Insecure served for data transition.

we will give the attacker a chance for "MIMT" ( man in the middle attack) as you know that the name of the attack itself explain the steps.

-check the source code of the main page.

Solution: try to use https protocol, to prevent data and information disclosure.

Best,

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
