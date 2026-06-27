---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1033423'
original_report_id: '1033423'
title: Django Debug=True Leaks admin email addresss and serval system information
weakness: Information Exposure Through Debug Information
team_handle: mailru
created_at: '2020-11-13T06:15:47.374Z'
disclosed_at: '2021-01-07T09:00:28.725Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 22
asset_identifier: Foodplex
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- information-exposure-through-debug-information
---

# Django Debug=True Leaks admin email addresss and serval system information

## Metadata

- HackerOne Report ID: 1033423
- Weakness: Information Exposure Through Debug Information
- Program: mailru
- Disclosed At: 2021-01-07T09:00:28.725Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

#Domain, site, application
weblate.ucs.ru

#Steps to reproduce
##For getting all Url Patterns
  1.Open https://weblate.ucs.ru /
  2.now after / enter any random string
  3.It will open 404 page which contains all the Url Patterns of Website
##For getting all debug info
 1.Open https://weblate.ucs.ru
 2. Now go to https://weblate.ucs.ru/widgets/platformx/-/svg-badge.svg 
 3.Boom you got all details

Recommend Fix
Change Debug to False from True
Reference
https://www.troyhunt.com/graphic-demonstration-of-information/

## Impact

An attacker can obtain information such as:

Exact Django & Python version.
Used database type, database user name, current database name.
Details of the Django project configuration.
Internal file paths.
Email of admin is also disclosed
Exception-generated source code, local variables and their values.
All Urls of web App is also disclosed

This information might help an attacker gain more information and potentially to focus on the development of further attacks to the target system.

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
