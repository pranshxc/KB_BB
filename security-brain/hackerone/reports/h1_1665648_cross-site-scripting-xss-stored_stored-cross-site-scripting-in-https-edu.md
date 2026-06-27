---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1665648'
original_report_id: '1665648'
title: stored cross site scripting in https://████████.edu
weakness: Cross-site Scripting (XSS) - Stored
team_handle: deptofdefense
created_at: '2022-08-10T15:39:26.389Z'
disclosed_at: '2023-09-08T17:20:25.876Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# stored cross site scripting in https://████████.edu

## Metadata

- HackerOne Report ID: 1665648
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: deptofdefense
- Disclosed At: 2023-09-08T17:20:25.876Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

It was observed that the application is vulnerable to cross-site scripting (XSS). XSS is a type of attack that involves running a malicious scripts on a victim’s browser.
poc attached
another parameter at #1636345
q_23463
payload: %22%27%3e%3csvg%2fonload%3dconfirm(666)%3e

## Impact

Cookie Stealing - A malicious user can steal cookies and use them to gain access to the application.
Arbitrary requests - An attacker can use XSS to send requests that appear to be from the victim to the web server.
Malware download - XSS can prompt the user to download malware. Since the prompt looks like a legitimate request from the
site, the user may be more likely to trust the request and actually install the malware.
Defacement - attacker can deface the website usig javascript code.

## System Host(s)
████.edu

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
video attached

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
