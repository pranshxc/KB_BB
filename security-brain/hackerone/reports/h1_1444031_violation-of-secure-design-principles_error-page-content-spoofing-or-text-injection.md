---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1444031'
original_report_id: '1444031'
title: Error Page Content Spoofing or Text Injection
weakness: Violation of Secure Design Principles
team_handle: krisp
created_at: '2022-01-08T14:59:59.052Z'
disclosed_at: '2022-03-09T17:57:06.190Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
asset_identifier: '*.krisp.ai'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Error Page Content Spoofing or Text Injection

## Metadata

- HackerOne Report ID: 1444031
- Weakness: Violation of Secure Design Principles
- Program: krisp
- Disclosed At: 2022-03-09T17:57:06.190Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:

Error Page Content Spoofing or Text Injection in two urls

Target: https://download.prelive.krisp.ai/
Target:https://upld.prelive.krisp.ai/


Description: Content spoofing, also referred to as content injection, "arbitrary text injection" or virtual defacement, is an attack targeting a user made possible by an injection vulnerability in a web application. When an application does not properly handle user-supplied data, an attacker can supply content to a web application, typically via a paramete value, that is reflected back to the user. This presents the user with a modified page under the context of the trusted domain.

Steps to Reproduce:

1.Go to https://download.prelive.krisp.ai/  and this url :https://upld.prelive.krisp.ai/
2.Type any thing after slash, it will be reflected on the page.

Reference: 
https://hackerone.com/reports/498562
https://hackerone.com/reports/1245051
https://hackerone.com/reports/327671

## Impact

This attack is typically used as, or in conjunction with, social engineering because the attack is exploiting a code-based vulnerability and a user's trust. As a side note, this attack is widely misunderstood as a kind of bug that brings no impact.

poc:

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
