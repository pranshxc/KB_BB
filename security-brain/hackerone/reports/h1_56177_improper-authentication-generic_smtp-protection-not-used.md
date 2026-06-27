---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '56177'
original_report_id: '56177'
title: SMTP protection not used
weakness: Improper Authentication - Generic
team_handle: coinspace
created_at: '2015-04-13T21:03:03.437Z'
disclosed_at: '2015-06-10T23:51:43.406Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# SMTP protection not used

## Metadata

- HackerOne Report ID: 56177
- Weakness: Improper Authentication - Generic
- Program: coinspace
- Disclosed At: 2015-06-10T23:51:43.406Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi

I'm checking your website found spf record there.
You should apply strict **SMPT policy** to stop spoofed email sending from your domain.

An attacker would send a Fake email from security@coin.space saying that Please change your password, The victim is aware of phishing attacks, But when he sees that the mail originated from security@coin.space , He has no other way than to believe it. Clicking on the link takes him to a website where certain JavaScript is executed which steals his coin.space id and pin (SESSION COOKIE). The results can be more dangerous.

```
<?php
$to = "VICTIM@example.com";
$subject = "Password Change";
$txt = "Change your password by visiting here - [VIRUS LINK HERE]l";
$headers = "From: security@coin.space";
mail($to,$subject,$txt,$headers);
?>
```

**Fix**

Your SPF record is `v=spf1 include:_spf.google.com ~all`

It should be `v=spf1 include:_spf.google.com -all`

I strongly recommend you to read this article :

https://www.digitalocean.com/community/tutorials/how-to-use-an-spf-record-to-prevent-spoofing-improve-e-mail-reliability

The problem
The article clearly shows difference between softmail and fail you should be using fail as Softmail allows anyone to send spoofed emails from your domains. in your SPF record you should replace `~` with `-` at last before all , `-` is strict which prevents all spoofed emails except if you are sending. Your bug is that you are using `~` , you should use `-`

Best Regard
**Shubham**

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
