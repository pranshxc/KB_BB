---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1166066'
original_report_id: '1166066'
title: No Rate Limit On Reset Password
weakness: Violation of Secure Design Principles
team_handle: upchieve
created_at: '2021-04-15T22:20:15.365Z'
disclosed_at: '2021-08-31T15:23:46.314Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: app.upchieve.org
asset_type: URL
max_severity: none
tags:
- hackerone
- violation-of-secure-design-principles
---

# No Rate Limit On Reset Password

## Metadata

- HackerOne Report ID: 1166066
- Weakness: Violation of Secure Design Principles
- Program: upchieve
- Disclosed At: 2021-08-31T15:23:46.314Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

welcome all :
i found that no rate limit in reset password in ::: ==https://app.upchieve.org/resetpassword==

Summary:
No rate limit check on forgot password which can lead to mass mailing and spamming of users and possible employees
A little bit about Rate Limit:
A rate limiting algorithm is used to check if the user session (or IP-address) has to be limited based on the information in the session cache.


Steps To Reproduce The Issue
1- create account and go to reset password 
2- intercept burp and send request to intruder 
3- make payload and start attack 

attchaments ::

please follow me in this vedio ::
{F1267144}

similar reports ::::

1-https://hackerone.com/reports/751604
2-https://hackerone.com/reports/441161
3- https://hackerone.com/reports/280534


Suggested fix
Use CAPTCHA verification if many request sent.

## Impact

1- Attacker could use this vulnerability to bomb out the email inbox of the victim.
2- Attacker could send Spear-Phishing to the selected mail address.

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
