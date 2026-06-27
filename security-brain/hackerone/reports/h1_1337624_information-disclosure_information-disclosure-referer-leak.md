---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1337624'
original_report_id: '1337624'
title: Information disclosure-Referer leak
weakness: Information Disclosure
team_handle: brave
created_at: '2021-09-12T19:40:55.597Z'
disclosed_at: '2022-02-01T19:32:16.611Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 39
asset_identifier: https://laptop-updates.brave.com/latest/winx64
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Information disclosure-Referer leak

## Metadata

- HackerOne Report ID: 1337624
- Weakness: Information Disclosure
- Program: brave
- Disclosed At: 2022-02-01T19:32:16.611Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Assigned to: Brave
Assigned by: Kirtikumar Anandrao Ramchandani
Assigned on: 13/09/2021
Browser information used to test (Up to date):
```
Brave	1.29.79 Chromium: 93.0.4577.63 (Official Build) (64-bit)
Revision	ff5c0da2ec0adeaed5550e6c7e98417dac77d98a-refs/branch-heads/4577@{#1135}
OS	Windows 10 OS Version 2009 (Build 19043.1165)
```

Vulnerability name: Information Disclosure
Vulnerability description: Brave browser has a function of    `New Private Window with Tor`. The browser when used with Tor shouldn't leak the referer.
Steps to reproduce:
1. Visit [exploit].
2. Click on `https://www.whatismybrowser.com/`.

Expected behavior: It should have shown a blank `referrer`
Actual behavior: It shows the referrer as: `kirtikumarar.com` which was the host from where we navigated

To know expected behavior, please refer to the below screenshot:
{F1445735}

Video POC showing the expected behavior can be found below:

{F1445736}

[exploit]: https://kirtikumarar.com/referrer/top-page.html

## Impact

1. This will leak users information
2. In the Tor network, we don't have common URLs as we have in the browsers. They usually are something like `dhxnafkaxlxdnackeudxdca.onion`, those can be leaked.

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
