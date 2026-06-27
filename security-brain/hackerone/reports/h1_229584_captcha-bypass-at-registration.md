---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '229584'
original_report_id: '229584'
title: Captcha bypass at registration
team_handle: weblate
created_at: '2017-05-18T10:26:39.869Z'
disclosed_at: '2017-06-28T02:12:30.956Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
---

# Captcha bypass at registration

## Metadata

- HackerOne Report ID: 229584
- Weakness: 
- Program: weblate
- Disclosed At: 2017-06-28T02:12:30.956Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

### Affected URL:
https://demo.weblate.org/accounts/register/

### Issue:
The captchas are implement so that the site can differentiate between the legitimate user and the bot. The captcha challenge should be something that a bot cannot solve easily and a human could easily solve. However, in the above URL captcha is simple enough that can be read by any script. 
An attacker can write a simple script to get value of those captcha ( as simple as `document.getElementById("div_id_captcha")` in JS ) and solve them.

### Solution:
Image captcha should be implemented whose value cannot be read by script.
Google captcha can be an effective solution.

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
