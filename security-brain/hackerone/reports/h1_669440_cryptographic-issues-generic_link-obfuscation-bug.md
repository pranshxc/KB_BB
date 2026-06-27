---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '669440'
original_report_id: '669440'
title: Link obfuscation bug
weakness: Cryptographic Issues - Generic
team_handle: brave
created_at: '2019-08-08T02:43:11.226Z'
disclosed_at: '2019-08-12T17:20:24.212Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- cryptographic-issues-generic
---

# Link obfuscation bug

## Metadata

- HackerOne Report ID: 669440
- Weakness: Cryptographic Issues - Generic
- Program: brave
- Disclosed At: 2019-08-12T17:20:24.212Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
Link preview in the left bottom of Brave Browser will show the link where the user will be redirected after clicking it, but after clicking the link, the affected user will be redirected to other website.

## Products affected: 
Latest Version of Brave browser

## Steps To Reproduce:
1. Open poc.html
2. Hover your mouse to a hyperlink named https://brave.com
3. You will see in the link preview in the bottom of the browser that the user should be redirected.
4. Click the hyperlink and you will be redirected to another domain.

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

The attacker can trick a user to go to an evil domain.

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
