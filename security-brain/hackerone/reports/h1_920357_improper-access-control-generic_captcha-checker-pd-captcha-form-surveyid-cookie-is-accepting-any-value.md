---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '920357'
original_report_id: '920357'
title: Captcha checker "pd-captcha_form_SURVEYID" cookie is accepting any value
weakness: Improper Access Control - Generic
team_handle: automattic
created_at: '2020-07-09T22:18:21.401Z'
disclosed_at: '2020-11-18T14:21:27.551Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
tags:
- hackerone
- improper-access-control-generic
---

# Captcha checker "pd-captcha_form_SURVEYID" cookie is accepting any value

## Metadata

- HackerOne Report ID: 920357
- Weakness: Improper Access Control - Generic
- Program: automattic
- Disclosed At: 2020-11-18T14:21:27.551Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi team,
There is a `Captcha protection` feature on surveys and polls. If you captcha protection enabled survey, you will see this :
{F901789}

When you solve captcha and click `Submit Captcha`, website sets a cookie like this :
{F901799}

And if you delete this cookie and try access to survey, you will see captcha again. But if you change value of this cookie, you can access still. 
So any attacker can bypass this restriction via typing random value to cookie.

## Steps To Reproduce:

  1. Go to a captcha protected survey or poll
  1. Solve the captcha and click `Submit Captcha`
  1. Now change the value of `pd-captcha_form_SURVEYID` cookie to random value from browser's console.
  1. Refresh the page and you will see you can access to survey and submit the survey.

## Impact

Bypassing captcha protection on surveys and polls

Thanks,
Bugra

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
