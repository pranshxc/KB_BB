---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1245094'
original_report_id: '1245094'
title: Exposed data of credit card details to hacker or attacker.
weakness: Privacy Violation
team_handle: urbancompany
created_at: '2021-06-26T13:10:16.534Z'
disclosed_at: '2021-06-28T04:53:50.066Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
asset_identifier: www.urbancompany.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- privacy-violation
---

# Exposed data of credit card details to hacker or attacker.

## Metadata

- HackerOne Report ID: 1245094
- Weakness: Privacy Violation
- Program: urbancompany
- Disclosed At: 2021-06-28T04:53:50.066Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

**Name of Vulnerability:** payment card details and cvv number can easily be traced!! 
**Areas affected:** payment tab in app
**User Details:**email: ███  
                                         Mobile no.: ████████  
**Summary:** exposed credit card details that are applying for online payment

**Description:** when user is applying for online payment throught debit or credit card then the hacker can take screenshots or screen record the page and get access to the card of the user this can lead to serious problem.the payment tab should not allow screenshots and screen recording at the time of typing the details of card . Their should be restriction on capturing screenshots and screen recording.hope you will work on this thing.thank you...

## Steps To Reproduce:

(Add details for how we can reproduce the issue through manual testing only)

  1. [add step]
  1. [add step]
  1. [add step]

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

Attacker can achieve the details of credit card through screenshots or screen recording.

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
