---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '244432'
original_report_id: '244432'
title: Missing SPF Flags
weakness: Violation of Secure Design Principles
team_handle: wakatime
created_at: '2017-06-29T16:12:28.128Z'
disclosed_at: '2017-07-01T21:45:07.656Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- violation-of-secure-design-principles
---

# Missing SPF Flags

## Metadata

- HackerOne Report ID: 244432
- Weakness: Violation of Secure Design Principles
- Program: wakatime
- Disclosed At: 2017-07-01T21:45:07.656Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I am just looking at your SPF records then found following. SPF Records missing safe check which can allow me to send mail and phish easily any victim.

#PoC:
```
<?php
$to = "VICTIM@example.com";
$subject = "Password Change";
$txt = "Change your password by visiting here - [VIRUS LINK HERE]l";
$headers = "From: support@wakatime.com";
mail($to,$subject,$txt,$headers);
?>
```
The TXT records found for your domain are:
v=spf1 include:_spf.google.com include:mailgun.org include:spf.sendinblue.com ~all 

Checking to see if there is a valid SPF record. 

Found v=spf1 record for wakatime.com: 
>v=spf1 include:_spf.google.com include:mailgun.org include:spf.sendinblue.com ~all 

#Fix:
>v=spf1 include:_spf.google.com include:mailgun.org include:spf.sendinblue.com -all 

You can check yourself here http://www.kitterman.com/getspf2.py
You can refer this https://www.digitalocean.com/community/tutorials/how-to-use-an-spf-record-to-prevent-spoofing-improve-e-mail-reliability

Let me know if any further info is required.

Regards,
Mr_R3boot.

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
