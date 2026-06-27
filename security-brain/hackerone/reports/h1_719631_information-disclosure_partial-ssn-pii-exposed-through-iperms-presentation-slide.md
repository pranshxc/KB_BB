---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '719631'
original_report_id: '719631'
title: '[Partial] SSN & [PII] exposed through iPERMs Presentation Slide.'
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2019-10-22T03:15:50.117Z'
disclosed_at: '2019-12-02T20:03:29.777Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 22
tags:
- hackerone
- information-disclosure
---

# [Partial] SSN & [PII] exposed through iPERMs Presentation Slide.

## Metadata

- HackerOne Report ID: 719631
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2019-12-02T20:03:29.777Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello @deptofdefense, when performing reconnaissance, I came across a presentation slide that displayed live data since the data is blocked out & is formatted with `XXX-XX` with the last 4 digits.

The exposed data contains the following: `UPC, Division/Brigade, Rank, Soldier Name, Last 4 digits of SSN, FRR (Financial Record Reviews), PRR (Personal Record Reviews).`

Here are a few exposed users:
████████, XXX-XX-█████████
████████, XXX-XX-█████

The link that is hosting the Presentation Slide: `https://████████/wp-content/uploads/2017/12/Introduction-to-iPERMS-Slides.pptx` & on Slide 25, there is the exposed data.

The remediation/mitigation for this security flaw is the removal of the data/file & I have set the severity to `Critical` as it is exposing sensitive [PII] which could lead to a data breach.

## Impact

The sensitive information can be used to authenticate through various web-portals especially with the last 4 digits & full name with rank.

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
