---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6488'
original_report_id: '6488'
title: Weak Ciphers Enabled
weakness: Information Disclosure
team_handle: khanacademy
created_at: '2014-04-08T12:07:43.024Z'
disclosed_at: '2014-04-09T06:40:08.148Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- information-disclosure
---

# Weak Ciphers Enabled

## Metadata

- HackerOne Report ID: 6488
- Weakness: Information Disclosure
- Program: khanacademy
- Disclosed At: 2014-04-09T06:40:08.148Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Vulnerability Details:-
I detected that weak ciphers are enabled during secure communication (SSL).
You should allow only strong ciphers on your web server to protect secure communication with your visitors.

Impact:-
Attackers might decrypt SSL traffic between your server and your visitors.

Remedy:-
Configure your web server to disallow using weak ciphers.

POC Link :- https://www.ssllabs.com/ssltest/analyze.html?d=www.khanacademy.org&s=23.23.224.106

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
