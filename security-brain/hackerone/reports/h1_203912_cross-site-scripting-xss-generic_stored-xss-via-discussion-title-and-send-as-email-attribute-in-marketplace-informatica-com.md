---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '203912'
original_report_id: '203912'
title: Stored XSS via Discussion Title and Send as Email attribute in [marketplace.informatica.com]
weakness: Cross-site Scripting (XSS) - Generic
team_handle: informatica
created_at: '2017-02-06T18:05:31.580Z'
disclosed_at: '2017-04-08T12:39:29.782Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS via Discussion Title and Send as Email attribute in [marketplace.informatica.com]

## Metadata

- HackerOne Report ID: 203912
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: informatica
- Disclosed At: 2017-04-08T12:39:29.782Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

POC
===
1.  Under "Your Stuff" choose to "Create a Discussion/Ask a question"
2. Choose a space to submit your discussion/question. Any space will do.
3. Title your discussion with the payload `"><img src=x onerror=alert(1)>`
4. Choose "Post message" to publish.
5. View the message as any user. Under "Actions" choose to "Send as Email"
6. Observe XSS poc alert box"

Please let me know if you have any questions.

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
