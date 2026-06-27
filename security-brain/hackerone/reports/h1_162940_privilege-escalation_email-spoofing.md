---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '162940'
original_report_id: '162940'
title: Email Spoofing
weakness: Privilege Escalation
team_handle: skyliner
created_at: '2016-08-26T10:00:13.703Z'
disclosed_at: '2016-11-15T18:40:24.769Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 3
tags:
- hackerone
- privilege-escalation
---

# Email Spoofing

## Metadata

- HackerOne Report ID: 162940
- Weakness: Privilege Escalation
- Program: skyliner
- Disclosed At: 2016-11-15T18:40:24.769Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hey Skyliner,
I have found Email Spoofing type of Vulnerability in your Website.
Attacker can use your E-Mail to send emails to others.

Email spoofing is the creation of email messages with a forged sender address. Because the core email protocols do not have any mechanism for authentication, it is common for spam and phishing emails to use such spoofing to mislead the recipient about the origin of the message 

Not Only dan@skyliner.io involved in it, All the Emails develop in https://www.skyliner.io/ may be affect by it...

Steps to Produce this Issue:
1) Goto: https://emkei.cz/
2) Add dan@skyliner.io "From Email" in https://emkei.cz/
3) Click Send Button,
4) The Email from dan@skyliner.io will be send to the Email you enter.

Another way,
<?php
$to = "gopss.sharma@gmail.com";
$subject = "Email Spoofing Test";
$txt = "This is Email Spoofing";
$headers = "From: dan@skyliner.io";
mail($to,$subject,$txt,$headers);
?>

Save this code in PHP file, & upload it on online server, Execute it & you can see The email will be send to your Desired Email

See Screenshots below, I received Email from your website.

Fix: Improve Your Mailer, Turn on some more Security filters.
Read More about Email Spoofing here:
http://searchsecurity.techtarget.com/definition/email-spoofing

Thanks! I hope you will fix this issue soon as possible,
And i know this is not eligible for any bounty but i am expecting atleast a THANKS or SWAG maybe :)

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
