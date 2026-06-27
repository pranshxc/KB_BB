---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1660611'
original_report_id: '1660611'
title: stored cross site scripting in https://███
weakness: Cross-site Scripting (XSS) - Stored
team_handle: deptofdefense
created_at: '2022-08-05T15:59:35.833Z'
disclosed_at: '2023-01-06T19:11:17.990Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# stored cross site scripting in https://███

## Metadata

- HackerOne Report ID: 1660611
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: deptofdefense
- Disclosed At: 2023-01-06T19:11:17.990Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

It was observed that the application is vulnerable to cross-site scripting (XSS). XSS is a type of attack that involves running a malicious scripts on a victim’s browser.
poc attached
another parameter at #1636345
q_21675

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
video

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
