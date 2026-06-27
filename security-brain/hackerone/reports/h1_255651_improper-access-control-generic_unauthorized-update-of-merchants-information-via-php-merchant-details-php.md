---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '255651'
original_report_id: '255651'
title: Unauthorized update of merchants' information via /php/merchant_details.php
weakness: Improper Access Control - Generic
team_handle: zomato
created_at: '2017-08-02T00:18:29.320Z'
disclosed_at: '2017-09-19T06:14:42.259Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Unauthorized update of merchants' information via /php/merchant_details.php

## Metadata

- HackerOne Report ID: 255651
- Weakness: Improper Access Control - Generic
- Program: zomato
- Disclosed At: 2017-09-19T06:14:42.259Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello!

I discovered an interesting file : 
`https://www.zomato.com/php/merchant_details.php`

If I add in post content :
`action=update-merchant&merchant_id=95292&type=1&email=update@hotmail.fr&contact=update@hotmail.fr&name=update`

With the report #255648, I was able to create a merchant, I should use this merchant to provide a screenshot like in a real situation.


I'm also able to change :
`address, pincode, city, email, phone tan_number, bank account name, company_id, payu_id, contact, restaurants` and more...


An attacker would change the mail to receive confidential mails it may can be leading to an merchant takeover if you use the mail to bound it with the account of the user. I couldn't try this scenario due to your rules about users data.

Do you have a test merchant_id i can play with to test that before you resolve the report?

Screenshot : updatehttp.png

If you have any questions...
nbsp

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
