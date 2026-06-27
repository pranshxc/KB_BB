---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1595905'
original_report_id: '1595905'
title: XSS in Widget Review Form Preview in settings
weakness: Cross-site Scripting (XSS) - Stored
team_handle: judgeme
created_at: '2022-06-09T11:59:48.246Z'
disclosed_at: '2022-09-29T08:35:33.287Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
asset_identifier: judge.me
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS in Widget Review Form Preview in settings

## Metadata

- HackerOne Report ID: 1595905
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: judgeme
- Disclosed At: 2022-09-29T08:35:33.287Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi team,

I found a XSS vulenrability in the widget review form preview. The payload is added in the success message and triggers when you preview the form

## Steps To Reproduce:

  1. Login to your Shopify account and open Judge.Me App
  1. Go to 'Settings' -> 'Review Widget' -> 'Widget Form'
  1. Go the the success message and add this XSS payload to the text: "><img src=x onerror=alert(document.domain)>
  1. Click Preview to trigger the XSS
  1. Save the changes and now every time someone preview the form XSS would trigger

{F1763124}

## Supporting Material/References:
{F1763127}

Admin can invite Staff user with limited permission, that staff can then add the payload and perform scripts to other users like the Admin.

If there's anything I can help with please let me know.

Have a great day!

Cheers,
PenguinsHelp

## Impact

Stored XSS

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
