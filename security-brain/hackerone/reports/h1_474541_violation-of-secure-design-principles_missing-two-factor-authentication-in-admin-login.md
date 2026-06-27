---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '474541'
original_report_id: '474541'
title: Missing Two Factor Authentication in /admin/login
weakness: Violation of Secure Design Principles
team_handle: cfptime
created_at: '2019-01-05T09:04:11.284Z'
disclosed_at: '2019-01-07T12:50:52.913Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 3
asset_identifier: www.cfptime.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Missing Two Factor Authentication in /admin/login

## Metadata

- HackerOne Report ID: 474541
- Weakness: Violation of Secure Design Principles
- Program: cfptime
- Disclosed At: 2019-01-07T12:50:52.913Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hello Team,
>First of all this report is just mainly concern for `Suggested security improvements` based on your policy page.
>If and only if not mean possible, please do let me know. Thanks!

#### INTRODUCTION
Administrative panel is one of the main entry point for the website owner to manage their web apps from outside, making it expose not only to website owner but to public as well.

#### DESCRIPTION
It have found out that `https://www.cfptime.org/` has an endpoint of `admin/login`  which was a written django web application python framework (i should say based on the login page UI). 

Though the web application looks okay, i do suggests that you'll need to setup an additional Two Factor Authentication on the login page to ensure that only the website owner can access the site internally and nothing else.

#### RECOMMENDATIONS

>###Things To Look For
> - Suggested security improvements

I highly recommend to install 2FA from the following modules in python `django-otp`,`qrcode` which uses otp token for verification since csrf token are mean to use only on public, while otp can only be received by the website owner itself only.

#### REFERENCES
Finally the references i used for this report, you might consider checking this also for even more ways to fortify your web application.
https://hackernoon.com/5-ways-to-make-django-admin-safer-eb7753698ac8

## Impact

Prone to password guessing attacks/brute force attacks.

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
