---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1176090'
original_report_id: '1176090'
title: Email Spoofing on sifchain.finance
team_handle: sifchain
created_at: '2021-05-10T23:50:14.228Z'
disclosed_at: '2021-05-11T14:23:23.981Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 6
asset_identifier: https://github.com/sifchain/sifnode
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Email Spoofing on sifchain.finance

## Metadata

- HackerOne Report ID: 1176090
- Weakness: 
- Program: sifchain
- Disclosed At: 2021-05-11T14:23:23.981Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

##Summary:

There is an Email Spoofing vulnerability on your domain sifchain.finance which allows an attacker to send an email with your domain name(such as admin@sifchain.finance and so on).

##Steps To Reproduce:

Go to http://emkei.cz
Fill "From Email" field to admin@sifchain.finance or any other sifchain.finance email.
Fill the victim's address (your email for test purpose) to "TO" field and fill in other details as you wish. You will receive email from sifchain.finance admin.

## Impact

an attacker can send malicious emails to users on your behalf(using your domain(

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
