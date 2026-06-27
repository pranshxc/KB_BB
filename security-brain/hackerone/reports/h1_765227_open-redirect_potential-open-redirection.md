---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '765227'
original_report_id: '765227'
title: Potential Open-Redirection
weakness: Open Redirect
team_handle: iandunn-projects
created_at: '2019-12-27T19:07:32.542Z'
disclosed_at: '2019-12-27T20:54:00.331Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 7
asset_identifier: iandunn.name
asset_type: URL
max_severity: none
tags:
- hackerone
- open-redirect
---

# Potential Open-Redirection

## Metadata

- HackerOne Report ID: 765227
- Weakness: Open Redirect
- Program: iandunn-projects
- Disclosed At: 2019-12-27T20:54:00.331Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Steps To Reproduce:
=====================
>1_ visit : [Normal Link](https://iandunn.name/wordpress/wp-login.php?redirect_to=https%3A%2F%2Fiandunn.name%2Fwordpress%2Fwp-admin%2F&reauth=1).
>2_ Sign-in with your wordpress account and you will directed to [This](https://iandunn.name/wordpress/wp-admin/)
>3_Change the value of the **Parameter** : redirect_to .. To the attacker website let's say : (https://vul-example.com)
>4_**NOTE THAT** : you must URL-encode the vulnerable link first

## Impact

**Phishing** attacks to get Users to visit malicious sites without realizing it.

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
