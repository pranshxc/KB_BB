---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1443211'
original_report_id: '1443211'
title: Bypass Email Verification in Customer Portal
team_handle: mattermost
created_at: '2022-01-07T07:51:31.899Z'
disclosed_at: '2022-02-26T08:20:49.145Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 37
asset_identifier: h1-*your-own-instance*.cloud.mattermost.com
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# Bypass Email Verification in Customer Portal

## Metadata

- HackerOne Report ID: 1443211
- Weakness: 
- Program: mattermost
- Disclosed At: 2022-02-26T08:20:49.145Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team hope you doing well :) 
i found a vulnerability [  OTP Bypass  ] on [ https://portal.test.cloud.mattermost.com ] .
Summery : 
I was able to use the otp that was sent to victim email and i used it in the attacker's email verify .when i tried this issue first time the server log me out  , and second time i do intercept for request and i was still in and click [next step ] on payment step and am still in without the server log me out and stop the burp after that and am in and i can using my account normally .

## Steps To Reproduce:

  1. [make two account :  victim / attacker]
  1. [ used otp that send to victim and inter it on attacker email verify and intercept the request  by burp. ]
  1. [when you doing intercept by burp click on next step and full the form and click enter and you can stop proxy and you can used the account normally.  ]


## Supporting Material/References:
[https://link.medium.com/xFYjx29xAmb]

## Impact

OTP bypass .

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
