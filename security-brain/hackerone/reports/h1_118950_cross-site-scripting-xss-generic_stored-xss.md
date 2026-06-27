---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '118950'
original_report_id: '118950'
title: Stored XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: veris
created_at: '2016-02-26T14:05:13.563Z'
disclosed_at: '2016-06-12T16:05:39.961Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS

## Metadata

- HackerOne Report ID: 118950
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: veris
- Disclosed At: 2016-06-12T16:05:39.961Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I have found XSS on https://sandbox.veris.in/portal/members/

Steps to reproduce:

1.  Sign in your Veris account.
2. Go to Member Book -> Add new member.
3. Fill this payload <svg onload=alert(1)>  in "Name" and "Description" field.
4. Now visit  https://sandbox.veris.in/portal/members/ or go to groups->Add member from member book
5. Tadaa! XSS Triggers

Proof of Concept: Please find it attached.

Do evaluate it and inform me accordingly.

Best Regards,

Hely H. Shah

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
