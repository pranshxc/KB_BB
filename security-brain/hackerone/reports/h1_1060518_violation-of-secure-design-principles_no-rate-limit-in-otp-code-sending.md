---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1060518'
original_report_id: '1060518'
title: No rate limit in otp code sending
weakness: Violation of Secure Design Principles
team_handle: mtn_group
created_at: '2020-12-16T22:44:15.693Z'
disclosed_at: '2021-08-16T19:57:32.255Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: mtnonline.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# No rate limit in otp code sending

## Metadata

- HackerOne Report ID: 1060518
- Weakness: Violation of Secure Design Principles
- Program: mtn_group
- Disclosed At: 2021-08-16T19:57:32.255Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

There is no rate limit in sendind otp code. Thus, attacker can use this vulnerability to bomb out the mobile inbox of the victim.

## Steps To Reproduce:

##Step 1.
Open burp suite, and click on "Intercept is on " button from Proxy tab.

##Step 2.
Launch browser and visit https://mtnonline.com/nim, and fill all the required fields, then submit.

##Step 3.
Open burp suite window, and click on "HTTP history" under "Proxy" Tab, scroll on the history list and navigate on the history with https://mtnonline.com host and /nim/otp URL, and right click to "Send to Intruder".

##Step 4.
Click on "Intruder" tab -> click "Position" -> click "Clear" button,
and click on "Payloads", under payload type -> Select "Null payloads", In generate input, enter 10 .

##Step 5.
Click on "Attack" button, and click ok on the pop-up screen.


##NOTE : I only limit the sms as 10 for testing, but attacker can send unlimited sms in short time.



## Supporting Material/References:

  * [attachment / reference]

## Impact

Attacker can bomb victim mobile inbox and cause MTN to loose the charges of sms in vein.

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
