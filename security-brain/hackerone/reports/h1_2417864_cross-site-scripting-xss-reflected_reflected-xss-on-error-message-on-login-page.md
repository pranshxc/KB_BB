---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2417864'
original_report_id: '2417864'
title: Reflected XSS on error message on Login Page
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2024-03-15T07:51:53.203Z'
disclosed_at: '2024-05-03T18:06:08.817Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 29
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on error message on Login Page

## Metadata

- HackerOne Report ID: 2417864
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2024-05-03T18:06:08.817Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Greetings!

I've found a reflected XSS on a login page on█████ . The vulnerable link is: `https://███████/users/login?error=<img src='x' onerror="alert(document.domain)">`

█████████

## Impact

An attacker can inject crafted javascript that can steal user cookies, impersionate, steal information, deface the website and redirect user to another domain

## System Host(s)
██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Access `https://██████/users/login?error=<img src='x' onerror="alert(document.domain)">`

## Suggested Mitigation/Remediation Actions
Sanitize the output with htmlspecialchars();

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
