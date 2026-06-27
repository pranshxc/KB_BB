---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1708824'
original_report_id: '1708824'
title: No rate limit on subscribe form
weakness: Business Logic Errors
team_handle: yelp
created_at: '2022-09-22T13:10:36.967Z'
disclosed_at: '2022-10-05T20:55:39.542Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 10
asset_identifier: '*.yelp.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# No rate limit on subscribe form

## Metadata

- HackerOne Report ID: 1708824
- Weakness: Business Logic Errors
- Program: yelp
- Disclosed At: 2022-10-05T20:55:39.542Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
Hi team, I found that you missing a rate limit protection for subscribe form 

## Platform(s) Affected:
https://business.yelp.com/?source=consumer_site_header&utm_content=header&utm_medium=www&utm_source=cons_home

## Steps To Reproduce:


  1. go to https://business.yelp.com/?source=consumer_site_header&utm_content=header&utm_medium=www&utm_source=cons_home
  1. find a form with just email input (emailsub.png)
  1. fill it with email click on submit then intercept the request 
  1.  send to burp intruder  go to  -> positions
  1. clear `§`
  1. add `§` in email like `youremail§1§@gmail.com`
  1. go to -> payloads,  add numbers type paylaod like ( from : 2 , to : 100, step: 1)
  1. start attack you will see all response with 200 ok and contain msg `Thanks for subscribing!` so no rate limit implemented

##Fix:
add a recaptcha or 429 error (many requests)
## Supporting Material/References:
see screenshots

## Impact

No rate limit in form.

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
