---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1061664'
original_report_id: '1061664'
title: Access to alerta.khanacademy.org leak sensitive data
weakness: Improper Access Control - Generic
team_handle: khanacademy
created_at: '2020-12-18T15:05:33.232Z'
disclosed_at: '2021-09-08T08:36:43.777Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 25
tags:
- hackerone
- improper-access-control-generic
---

# Access to alerta.khanacademy.org leak sensitive data

## Metadata

- HackerOne Report ID: 1061664
- Weakness: Improper Access Control - Generic
- Program: khanacademy
- Disclosed At: 2021-09-08T08:36:43.777Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi ,
I found to access https://alerta.khanacademy.org/ using signup bypass.That leak access to sensitive data of khanacademy.org

Step To Reproduce:

1. Go to https://alerta.khanacademy.org/#/signup
2. Inspect Q and remove ng-hide

{F1121291}

3. You got Signup Form. Signup account using anythings@khanacademy.org mail.

{F1121292}

4. When you successfully signup,You access alerta.khanacademy.org without confirm email.

{F1121297}

If you not login direct .
1. Go to alerta.khanacademy.org/#/login.
2. Inspect Q and remove ng-hide

{F1121293}

3. Login with your register info.

{F1121294}

## Impact

Attacker can access alerta dashboard

Thanks,
@nightmare_msf

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
