---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '526265'
original_report_id: '526265'
title: DOM XSS on app.starbucks.com via ReturnUrl
weakness: Cross-site Scripting (XSS) - DOM
team_handle: starbucks
created_at: '2019-04-04T09:06:56.688Z'
disclosed_at: '2020-03-17T21:18:33.965Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 26
asset_identifier: app.starbucks.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# DOM XSS on app.starbucks.com via ReturnUrl

## Metadata

- HackerOne Report ID: 526265
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: starbucks
- Disclosed At: 2020-03-17T21:18:33.965Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** XSS Can be achieved via the ReturnUrl when signing in on app.starbucks.com

**Platform(s) Affected:** app.starbucks.com

## Steps To Reproduce:
1. Visit https://app.starbucks.com/account/signin?ReturnUrl=%09Jav%09ascript:alert(document.domain)
2. Sign in

## Supporting Material/References:
{F461364}


## How can the system be exploited with this bug? 
XSS could be used to steal the account of any victim that signs in via the url.
  

## How did you come across this bug ?
Retesting report #438240


## Recommendations for fix
Improve the checks on ReturnUrl such as not allowing hex characters 00-1F

## Impact

As with any xss, it could be used to steal the cookies of the victim to gain access to their account.

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
