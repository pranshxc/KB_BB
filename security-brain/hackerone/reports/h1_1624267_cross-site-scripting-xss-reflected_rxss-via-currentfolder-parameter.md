---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1624267'
original_report_id: '1624267'
title: '[████████] RXSS via "CurrentFolder" parameter'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2022-07-04T14:06:12.791Z'
disclosed_at: '2023-12-21T17:36:10.446Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# [████████] RXSS via "CurrentFolder" parameter

## Metadata

- HackerOne Report ID: 1624267
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2023-12-21T17:36:10.446Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The website █████ is vulnerable to reflected cross-site scripting via the `CurrentFolder` parameter.

## How to reproduce?

Visit: https://██████/landpower/resources.aspx?Directory=/20/&ParentID=27&CurrentFolder=%3Cimg%20src%20onerror=alert(domain)%3EResources&ID=17263

███

## Resources:

https://portswigger.net/web-security/cross-site-scripting

## Impact

An attacker who exploits a cross-site scripting vulnerability is typically able to:

* Impersonate or masquerade as the victim user.
* Carry out any action that the user is able to perform.
* Read any data that the user is able to access.
* Capture the user's login credentials.
* Perform virtual defacement of the web site.
* Inject trojan functionality into the web site.

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Visit: https://██████████/landpower/resources.aspx?Directory=/20/&ParentID=27&CurrentFolder=%3Cimg%20src%20onerror=alert(domain)%3EResources&ID=17263

## Suggested Mitigation/Remediation Actions
Escape user input

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
