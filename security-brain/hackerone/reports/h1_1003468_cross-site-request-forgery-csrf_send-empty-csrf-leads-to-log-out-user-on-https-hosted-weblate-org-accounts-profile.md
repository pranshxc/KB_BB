---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1003468'
original_report_id: '1003468'
title: Send Empty CSRF leads to log out user on [https://hosted.weblate.org/accounts/profile]
weakness: Cross-Site Request Forgery (CSRF)
team_handle: weblate
created_at: '2020-10-09T13:35:36.712Z'
disclosed_at: '2020-10-12T11:30:29.239Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: hosted.weblate.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Send Empty CSRF leads to log out user on [https://hosted.weblate.org/accounts/profile]

## Metadata

- HackerOne Report ID: 1003468
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: weblate
- Disclosed At: 2020-10-12T11:30:29.239Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi 
There is a CSRF bug on your [Website](https://hosted.weblate.org/) leads to logout user from the dashboard.
If the user click on the attached file (CSRF.html) redirect to another page and see the following error and the user log out immediately:

{F1029146}

## Steps to reproduce:
1- Login to your account via [Login page](https://hosted.weblate.org/accounts/login/)
2- Click on CSRF.html that attached. 
After that, you will redirect to a new page an see the error, the user after clicking on this file log out from account.

You can see in the CSRF file there isn't any token, but if you place a vaid CSRF token from the source page, this attack will be successful too.

{F1029164}

If you have any questions, please let me know.

Best.

## Impact

An attacker can send the CSRF file to the victim or host it on a website. Whenever the user login in to your website click on file or link will be logged out.

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
