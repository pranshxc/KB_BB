---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '175701'
original_report_id: '175701'
title: Status Bar Obfuscation
weakness: Cryptographic Issues - Generic
team_handle: brave
created_at: '2016-10-14T01:47:24.657Z'
disclosed_at: '2016-10-15T02:42:41.841Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cryptographic-issues-generic
---

# Status Bar Obfuscation

## Metadata

- HackerOne Report ID: 175701
- Weakness: Cryptographic Issues - Generic
- Program: brave
- Disclosed At: 2016-10-15T02:42:41.841Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

In this issue, Brave's Status Bar will show the link where the user will be redirected but after he clicks the link, he redirected to other website.

## Products affected: 

Latest Version of Brave

## Steps To Reproduce:

1. Open the HTML file
2. You will see a hyperlink of google.com, So hover your mouse.
3. See the Status Bar(located at the lower left of the browser) and you will see the link where it should be redirected
4. Now, click the hyperlink and you will be redirected to another website which is not the expected website.


## Supporting Material/References:

{F127785}

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
