---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '450882'
original_report_id: '450882'
title: Able to bypass information requirements before launching a Chat.
weakness: Insecure Direct Object Reference (IDOR)
team_handle: starbucks
created_at: '2018-11-27T22:43:34.474Z'
disclosed_at: '2018-12-20T19:48:19.241Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
asset_identifier: www.starbucks.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Able to bypass information requirements before launching a Chat.

## Metadata

- HackerOne Report ID: 450882
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: starbucks
- Disclosed At: 2018-12-20T19:48:19.241Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

**Summary:**  Bypass of mandatory fields before a Chat session can begin.

**Description:**  URL allows for bypass straight into chat, and Chat personnel won't know my name, just that they are chatting with someone.

**Platform(s) Affected:** [website/mobile app - please include browsers and app versions used for repro.]
Chrome Web Browser

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Visit 
https://customerservice.starbucks.com/app/chat/chat_landing/euf/generated/optimized/1542660523/pages/chat/chat_landing.themes.starbucks.SITE.css
 2.  You have just bypassed the mandatory fields found on https://customerservice.starbucks.com/app/chat/chat_launch

3.  Voila you are effectively chatting with Starbucks employee without providing anything.

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

Attached.

## How can the system be exploited with this bug?
  Bypass of required info that is mandatory.

## How did you come across this bug ?
Fiddling around.

## Recommendations for fix

 
* List any recommendations for bug fix

## Impact

Bypass and confuse agents, I can open an unlimited number of windows and start chatting with hundreds of agents if I want and affect your service if I was a malicious person.

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
