---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '25191'
original_report_id: '25191'
title: SMTP protection not used (please read carefully )
weakness: Improper Authentication - Generic
team_handle: greenhouse
created_at: '2014-08-19T01:15:21.614Z'
disclosed_at: '2014-12-07T15:22:49.750Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# SMTP protection not used (please read carefully )

## Metadata

- HackerOne Report ID: 25191
- Weakness: Improper Authentication - Generic
- Program: greenhouse
- Disclosed At: 2014-12-07T15:22:49.750Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Details:
Companies like Coinbase, Yahoo,Google,Facebook and even hackerone  implemented a strict email security policy (combining SPF, DKIM, and DMARC) but I don't see taht from mailgreenhouse.ioru , You should apply strict SMPT policy to stop spoofed email sending from your domain. POC is attached.

Exploit scenario:
-----------------------
An attacker would send a Fake email from support@greenhouse.io saying that Please change your password, The victim is aware of phishing attacks, But when he sees that the mail originated from support@greenhouse.io , He has no other way than to believe it. Clicking on the link takes him to a website where certain JavaScript is executed which steals his greenhouse.io id and password (SESSION COOKIE). The results can be more dangerous.


Code to Exploit:
-------------------
    <?php
    $to = "VICTIM@example.com";
    $subject = "Password Change";
    $txt = "Change your password by visiting here - [VIRUS LINK HERE]l";
    $headers = "From: support@greenhouse.io";
    mail($to,$subject,$txt,$headers);
    ?>

You should do the fix (see the fix below) To prevent misunderstanding and to protect your users.
FIX
----------

Your SPF record is `dig +short greenhouse.io txt
"v=spf1 include:sendgrid.net include:spf.recurly.com include:mailgun.org include:servers.mcsv.net ~all`

It should be `dig +short greenhouse.io txt
"v=spf1 include:sendgrid.net include:spf.recurly.com include:mailgun.org include:servers.mcsv.net   -all`

I **strongly** recommend you to read this article :

https://www.digitalocean.com/community/tutorials/how-to-use-an-spf-record-to-prevent-spoofing-improve-e-mail-reliability

**The problem**
The article clearly shows difference between softmail and fail you should be using fail as Softmail allows anyone to send spoofed emails from your domains. in your SPF record you should replace `~` with `-` at last before all , `-` is strict which prevents all spoofed emails except if you are sending. Your bug is that you are using`~` , you should use `-`

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
