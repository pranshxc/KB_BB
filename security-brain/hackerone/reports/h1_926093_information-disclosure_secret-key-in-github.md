---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '926093'
original_report_id: '926093'
title: Secret_key in GitHub
weakness: Information Disclosure
team_handle: weblate
created_at: '2020-07-17T10:41:23.798Z'
disclosed_at: '2020-07-18T09:28:51.362Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
asset_identifier: https://github.com/WeblateOrg/weblate
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Secret_key in GitHub

## Metadata

- HackerOne Report ID: 926093
- Weakness: Information Disclosure
- Program: weblate
- Disclosed At: 2020-07-18T09:28:51.362Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

hello 
I have found secret_key in GitHub is public and noticed something this key have comment # Make this unique, and don't share it with anybody. and it's public in GitHub also I noticed this file has coding to do the payment.db I think information like this must be private 

SECRET_KEY = "qov6(*cp%)b*ot+8c%#4@4or(t@_$y5#d8k9u1^+pknz%lms0x"
Link : https://github.com/WeblateOrg/website/blob/bc65d95a80d90ed95a8e59d0fa5dc14d7c060b3a/weblate_web/settings.py

## Impact

i don't know what attacker can do but i know this info must be private

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
