---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '457829'
original_report_id: '457829'
title: SPF Records (SMTP protection not used)
weakness: Violation of Secure Design Principles
team_handle: mycrypto
created_at: '2018-12-07T06:51:28.898Z'
disclosed_at: '2018-12-17T22:02:19.091Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: www.mycrypto.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# SPF Records (SMTP protection not used)

## Metadata

- HackerOne Report ID: 457829
- Weakness: Violation of Secure Design Principles
- Program: mycrypto
- Disclosed At: 2018-12-17T22:02:19.091Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello MyCrypto Team ,

I am checking your website and found something is missing in SPF record.I don't find you have applied strict SMTP policy to stop spoofed email sending from your domain.

I would like to recommend you to read the following article :

https://www.digitalocean.com/community/tutorials/how-to-use-an-spf-record-to-prevent-spoofing-improve-e-mail-reliability

Problem description :

The above article strictly guide us about difference between soft mail and fail. MyCrypto should use fail because Soft mail allows anyone to send spoofed emails from your domains.

In your SPF record you should replace ~ with - at last before all , - is strict which prevents all spoofed emails except if you are sending. Your bug is that you are using ~ , you should use -

FIX :

Your SPF record : v=spf1 include:_spf.google.com ~all 

It should be : v=spf1 include:_spf.google.com -all 

Best Regards ,

Shantanu

## Impact

An attacker can send a Fake email from support@mycrypto.com saying that Please change your password, The victim is aware or not of phishing attacks, But when he sees that the mail originated from support@mycrypto.com , then he can blindly believe on it. Clicking on the link takes him to a website where certain JavaScript is executed which steals his PayPal id and password (SESSION COOKIE). 
Later results are more harmful.

<?php
$to = "VICTIM@example.com";
$subject = "Password Change";
$txt = "Change your password by visiting here - [VIRUS LINK HERE]l";
$headers = "From: support@mycrypto.com";
mail($to,$subject,$txt,$headers);
?>

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
