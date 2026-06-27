---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145727'
original_report_id: '145727'
title: Bruteforcing help.nextcloud.com
weakness: Improper Authentication - Generic
team_handle: nextcloud
created_at: '2016-06-18T17:28:45.781Z'
disclosed_at: '2016-06-19T09:59:10.843Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 9
tags:
- hackerone
- improper-authentication-generic
---

# Bruteforcing help.nextcloud.com

## Metadata

- HackerOne Report ID: 145727
- Weakness: Improper Authentication - Generic
- Program: nextcloud
- Disclosed At: 2016-06-19T09:59:10.843Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi I've found that the user is allowed to perform brute force in help.nextcloud.com login, i've tried to input wrong password 25 times , then input my correct password in my 26th attempt and it is successfully login, a malicious minded user can always continue guessing an account password.

Steps to reproduce

Go to https://help.nextcloud.com/ then click login button and you can now perform brute force attack.

Regards
Japz

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
