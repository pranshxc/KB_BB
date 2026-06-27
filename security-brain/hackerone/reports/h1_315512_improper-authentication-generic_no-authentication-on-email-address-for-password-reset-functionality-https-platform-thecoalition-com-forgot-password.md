---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '315512'
original_report_id: '315512'
title: No authentication on email address for password reset functionality/ https://platform.thecoalition.com/forgot-password
weakness: Improper Authentication - Generic
team_handle: coalition
created_at: '2018-02-13T10:02:59.618Z'
disclosed_at: '2018-05-03T08:06:18.244Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: platform.thecoalition.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# No authentication on email address for password reset functionality/ https://platform.thecoalition.com/forgot-password

## Metadata

- HackerOne Report ID: 315512
- Weakness: Improper Authentication - Generic
- Program: coalition
- Disclosed At: 2018-05-03T08:06:18.244Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** It was observed that the forgot password functionality on https://platform.thecoalition.com/forgot-password did not verify the email addresses of user accounts before sending an email to them. An attacker can use this functionality and send faulty password reset links to legitimate users.

**Description:** It was also observed that the website did not verify the authenticity of the email and accepted any arbitrary test mail. It also allowed multiple requests for the same email id without any limit. This vulnerability can be leveraged to spam genuine users of platform.thecoalition.com.

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1.Visit the site https://platform.thecoalition.com/login
  2.Go to the forgot password functionality on https://platform.thecoalition.com/forgot-password
  3.Write an arbitrary email of attackers choice and click email me reset functions.

## Impact

An attacker could leverage this vulnerability by sending faulty password reset links 'n' number of times to legitimate users of platform.thecoalition.com  . This can also be done to add unnecessary load to the server by sending illegitimate mails repeatedly via using this functionality

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
