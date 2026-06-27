---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '409237'
original_report_id: '409237'
title: Broken Authentication
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2018-09-12T22:53:21.159Z'
disclosed_at: '2022-02-14T21:29:11.035Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- improper-access-control-generic
---

# Broken Authentication

## Metadata

- HackerOne Report ID: 409237
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2022-02-14T21:29:11.035Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** IDOR

**Description:** It is possible to access other user account by changing the parameter 'email' to another valid e-mail, i managed to guess an existing user '███████@███.com' which discloses the ███ 
Name and Surname.

## Impact
Information Disclosure

## Step-by-step Reproduction Instructions

1.Visit: https://██████
2. Register for an account
3. Follow the steps like in the attached pictures

## Product, Version, and Configuration (If applicable)
Web Application

## Suggested Mitigation/Remediation Actions
https://www.owasp.org/index.php/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet

## Impact

Information Disclosure

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
