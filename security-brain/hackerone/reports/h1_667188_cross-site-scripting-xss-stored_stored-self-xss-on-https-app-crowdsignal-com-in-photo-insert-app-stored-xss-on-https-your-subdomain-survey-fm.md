---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '667188'
original_report_id: '667188'
title: Stored Self XSS on https://app.crowdsignal.com (in Photo Insert App) + Stored
  XSS on https://*your-subdomain*.survey.fm
weakness: Cross-site Scripting (XSS) - Stored
team_handle: automattic
created_at: '2019-08-04T17:49:50.225Z'
disclosed_at: '2019-10-21T14:58:34.284Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 67
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored Self XSS on https://app.crowdsignal.com (in Photo Insert App) + Stored XSS on https://*your-subdomain*.survey.fm

## Metadata

- HackerOne Report ID: 667188
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: automattic
- Disclosed At: 2019-10-21T14:58:34.284Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Steps:
1. Go to https://app.crowdsignal.com/dashboard and click Create a New > Quiz
2. Add Multiple Choice to your page and click image button, upload a photo and click upload.
3. Start the burp suite and click Save button. Look at the request (poc1.png) and you will see media_code= parameter. It will be your photo's id and change it as payload and forward the request. Payload: "><svg/onload=alert(document.domain)> 
4. Now you will see xss (poc2.png). Copy the quiz link and open it the new tab. You will see second xss (poc3.png). And this one is stored xss.

## Impact

XSS

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
