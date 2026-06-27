---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1194293'
original_report_id: '1194293'
title: Wrong implementation of Telegram link on the main page for PC users
weakness: Misconfiguration
team_handle: sifchain
created_at: '2021-05-12T17:07:16.856Z'
disclosed_at: '2021-06-12T18:35:56.538Z'
has_bounty: true
visibility: full
substate: informative
vote_count: 8
tags:
- hackerone
- misconfiguration
---

# Wrong implementation of Telegram link on the main page for PC users

## Metadata

- HackerOne Report ID: 1194293
- Weakness: Misconfiguration
- Program: sifchain
- Disclosed At: 2021-06-12T18:35:56.538Z
- Has Bounty: Yes
- Visibility: full
- Substate: informative

## Original Report

## Summary:
 I found that there is a broken link for your telegram group.
When a PC user click on telegram icon on your main page he is redirected to tg://resolve?domain=sifchain instead of https://t.me/sifchain due to some errors in configuration(coding).
That idea is good for mobile view not deskptop.
## Steps To Reproduce:
Go to the main page and click on the Instagram link.
You will observe something like
{F1298980}

## Supporting Material/References:
{F1298980}

## Impact

Users will not be able to open your telegram group on PC through clicking your telegram icon on the main page

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
