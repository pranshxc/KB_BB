---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1735622'
original_report_id: '1735622'
title: Reflected XSS in chatbot
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: mtn_group
created_at: '2022-10-14T14:27:13.218Z'
disclosed_at: '2022-11-19T15:56:51.530Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: mtn.com.gh
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in chatbot

## Metadata

- HackerOne Report ID: 1735622
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: mtn_group
- Disclosed At: 2022-11-19T15:56:51.530Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Reflected XSS attacks, also known as non-persistent attacks, occur when a malicious script is reflected off of a web application to the victim's browser. The script is activated through a link, which sends a request to a website with a vulnerability that enables execution of malicious scripts
Proof of Concept
1)Go to the website https://mtn.com.gh/
2)click on the MTN chat and where it asks to enter a number enter an xss payload
3)In my case I put the following payload:<button onClick="alert('xss')">Submit</button>

## Impact

If an attacker can control a script running in the victim's browser, they can usually completely compromise that user. Among other things, the attacker can: Perform any action in the application that the user can perform.

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
