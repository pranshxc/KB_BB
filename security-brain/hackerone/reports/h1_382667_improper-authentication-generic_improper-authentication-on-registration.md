---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '382667'
original_report_id: '382667'
title: Improper authentication on registration
weakness: Improper Authentication - Generic
team_handle: semrush
created_at: '2018-07-17T17:11:52.614Z'
disclosed_at: '2018-08-24T13:34:05.332Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 5
tags:
- hackerone
- improper-authentication-generic
---

# Improper authentication on registration

## Metadata

- HackerOne Report ID: 382667
- Weakness: Improper Authentication - Generic
- Program: semrush
- Disclosed At: 2018-08-24T13:34:05.332Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

> Hope you are doing well, one can register himself to semrush with any email ID. It means that there is no authentication mechanism if that email id is valid/invalid. Therefore a person with email ID that does not exist can also register and login to your platform.

**Summary:** 
[one can register himself to semrush with any email ID. It means that there is no authentication mechanism if that email id is valid/invalid. Therefore a person with email ID that does not exist can also register and login to your platform.
]

**Description:** 
[Hope you are doing well, one can register himself to semrush with any email ID. It means that there is no authentication mechanism if that email id is valid/invalid. Therefore a person with email ID that does not exist can also register and login to your platform.
]

## Browsers Verified In:

  * [Google chrome]
  * [Mozilla]

## Steps To Reproduce:

[reproduce steps]
  1. [Register the email ID that does not exist]
  2. [Click register button and then login to the account]
  3. [Signout and again sign in using previous email ID]

## Supporting Material/References:
[**Obligated field**]
  * Screenshots
)

## Impact

Attacker can take benefit by using this weak access control and further login with the fake account that doesnot exit.

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
