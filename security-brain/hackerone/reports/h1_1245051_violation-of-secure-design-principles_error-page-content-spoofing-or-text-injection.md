---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1245051'
original_report_id: '1245051'
title: Error Page Content Spoofing or Text Injection
weakness: Violation of Secure Design Principles
team_handle: basecamp
created_at: '2021-06-26T11:38:32.276Z'
disclosed_at: '2021-07-14T12:21:01.122Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 31
asset_identifier: '*.hey.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Error Page Content Spoofing or Text Injection

## Metadata

- HackerOne Report ID: 1245051
- Weakness: Violation of Secure Design Principles
- Program: basecamp
- Disclosed At: 2021-07-14T12:21:01.122Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Target:  https://gopher.hey.com/

Description:  Content spoofing, also referred to as content injection, "arbitrary text injection" or virtual defacement, is an attack targeting a user made possible by an injection vulnerability in a web application. When an application does not properly handle user-supplied data, an attacker can supply content to a web application, typically via a parameter value, that is reflected back to the user. This presents the user with a modified page under the context of the trusted domain.


Steps to Reproduce:
1. Go to https://gopher.hey.com/
2.  Type any thing after slash, it will be reflected on the page.

Reference: https://hackerone.com/reports/498562
                           https://hackerone.com/reports/327671

## Impact

This attack is typically used as, or in conjunction with, social engineering because the attack is exploiting a code-based vulnerability and a user's trust. As a side note, this attack is widely misunderstood as a kind of bug that brings no impact.

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
