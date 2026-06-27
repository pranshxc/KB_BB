---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '13506'
original_report_id: '13506'
title: Unchecking hidden parameter is vulnerable to XSS-attack
weakness: Cross-site Scripting (XSS) - Generic
team_handle: khanacademy
created_at: '2014-05-26T16:28:58.863Z'
disclosed_at: '2014-08-07T14:14:27.751Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Unchecking hidden parameter is vulnerable to XSS-attack

## Metadata

- HackerOne Report ID: 13506
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: khanacademy
- Disclosed At: 2014-08-07T14:14:27.751Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Unchecking parameter <input type="hidden" name="redirect">

Malicious users may inject JavaScript, VBScript, ActiveX, HTML or Flash into a vulnerable application to fool a user in order to gather data from them.

http://crowdin.khanacademy.org:/login

PoC
<input type="hidden" name="redirect" value="/project_actions/load_discussions/"><script>prompt(986874)</script>"/>

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
