---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '767458'
original_report_id: '767458'
title: User input validation can lead to DOS
weakness: Uncontrolled Resource Consumption
team_handle: x
created_at: '2020-01-03T04:16:25.795Z'
disclosed_at: '2020-03-26T23:00:35.357Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# User input validation can lead to DOS

## Metadata

- HackerOne Report ID: 767458
- Weakness: Uncontrolled Resource Consumption
- Program: x
- Disclosed At: 2020-03-26T23:00:35.357Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Security Team,

**Summary:** 
There is no limit to the number of characters on phone numbers and using this you can perform a DOS Attack

**Description:**
On the input form of phone number in ***https://twitter.com/account/complete*** there's no Input validation using this you can send more payload and may cause of Denial of service or **503 Service Temporarily Unavailable**

## Steps To Reproduce:

So this is the normal page 
█████████

Input this payload on the Phone number textbox ████ then submit as you can see the payload was encoded on backend so the payload may load more

████

After submitting this is the response on burp **503 Service Temporarily Unavailable**

█████████

And on the page this is the result .

████████

## Supporting Material/References:

+ payload.txt

Thank you! 
Regards

## Impact

Attacker can perform a DOS because of lack of input validation

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
