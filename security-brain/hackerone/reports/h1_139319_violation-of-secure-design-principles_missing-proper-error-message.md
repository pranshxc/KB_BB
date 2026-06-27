---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '139319'
original_report_id: '139319'
title: Missing proper error message.
weakness: Violation of Secure Design Principles
team_handle: ok
created_at: '2016-05-17T13:35:33.035Z'
disclosed_at: '2016-07-21T10:25:07.366Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Missing proper error message.

## Metadata

- HackerOne Report ID: 139319
- Weakness: Violation of Secure Design Principles
- Program: ok
- Disclosed At: 2016-07-21T10:25:07.366Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Steps to reproduce:
1.Load the URL: http://ok.ru/ in any browser.
2.Now goto Browser settings and disable the Cookies.
3.Try to login using valid credentials .
4.Observed that user is redirected to login page again without any proper error message .

Technical Impact: This leads user to feel discomfort as user is not aware of the issue which is stopping him from login into his account ,which leads to loss of reputation.


Suggested Remediation:Error message like “ For smooth functioning of this site make 
sure that cookies are enabled on your browser.” should be displayed to make aware the user about the vulnerability.

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
