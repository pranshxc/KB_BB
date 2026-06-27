---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '148865'
original_report_id: '148865'
title: HTML in Diffusion not escaped in certain circumstances
weakness: Cross-site Scripting (XSS) - Generic
team_handle: phabricator
created_at: '2016-07-02T14:39:29.049Z'
disclosed_at: '2016-08-01T14:45:33.265Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# HTML in Diffusion not escaped in certain circumstances

## Metadata

- HackerOne Report ID: 148865
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: phabricator
- Disclosed At: 2016-08-01T14:45:33.265Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

HTML in Diffusion source code listing is not escaped

Steps to reproduce:
* have the syntax hilight turned on
* the file is bigger than 256kB, thus syntax hilight is claimed in header to be turned off automatically, however, plaintext file doesn't display like with regular (manual) syntax highlight off, but the content is being parsed

File should contain HTML constructions, but could be of any type (extension).
Having javascript constructions there with alert() within the HTML causes such dialogues to pop up on given page obviously.

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
