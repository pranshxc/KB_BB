---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1636345'
original_report_id: '1636345'
title: Reflected cross site scripting in https://███████
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2022-07-14T01:23:08.746Z'
disclosed_at: '2022-09-06T19:30:57.440Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected cross site scripting in https://███████

## Metadata

- HackerOne Report ID: 1636345
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2022-09-06T19:30:57.440Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

It was observed that the application is vulnerable to cross-site scripting (XSS). XSS is a type of attack that involves running a malicious scripts on a victim’s browser. 

request.txt attacked 
poc attached

## Impact

Cookie Stealing - A malicious user can steal cookies and use them to gain access to the application.
Arbitrary requests - An attacker can use XSS to send requests that appear to be from the victim to the web server.
Malware download - XSS can prompt the user to download malware. Since the prompt looks like a legitimate request from the
site, the user may be more likely to trust the request and actually install the malware.
Defacement - attacker can deface the website usig javascript code.

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
run request attached

## Suggested Mitigation/Remediation Actions

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
