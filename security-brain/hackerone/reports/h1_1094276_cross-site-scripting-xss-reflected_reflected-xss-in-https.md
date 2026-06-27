---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1094276'
original_report_id: '1094276'
title: Reflected XSS In https://███████
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-02-03T21:06:35.104Z'
disclosed_at: '2021-02-10T21:01:14.144Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS In https://███████

## Metadata

- HackerOne Report ID: 1094276
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-02-10T21:01:14.144Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi security team,
According to my report #1092618, The VDP team agreed that ***████*** and it's subdomains is in the scope of the DoD program
So I continue testing that domain

##Vulnerable Website URL:
https://███████████████%3CSvg%20OnLoad=alert(1)%3E

##Description of Security Issue:
Reflected XSS in path parameter (URI)

## Impact

Executing Javascript on behalf of the victim

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1 - Visit https://███
2 - Visit the error page /customerror
3 - Add the URI payload <Svg%20OnLoad=alert(1)>
4 - Final link https://██████████████████%3CSvg%20OnLoad=alert(1)%3E

## Suggested Mitigation/Remediation Actions
Sanitize the URI Path parameter

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
