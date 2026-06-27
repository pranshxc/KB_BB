---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '148763'
original_report_id: '148763'
title: Email Spoofing With Your Website's Email
weakness: Improper Authentication - Generic
team_handle: paragonie
created_at: '2016-08-24T18:40:51.863Z'
disclosed_at: '2016-08-24T18:44:06.271Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Email Spoofing With Your Website's Email

## Metadata

- HackerOne Report ID: 148763
- Weakness: Improper Authentication - Generic
- Program: paragonie
- Disclosed At: 2016-08-24T18:44:06.271Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hey Parogine, I have found **Email Spoofing** type of Vulnerability in your Website, 

**E-Mail Spoofing**
Now the Question is, What is **E-mail Spoofing**:
**Email spoofing** is the creation of email messages with a forged sender address. Because the core email protocols do not have any mechanism for authentication, it is common for spam and phishing emails to use such spoofing to mislead the recipient about the origin of the message.
In Simple words, Attacker can use your E-Mail to send emails to others.
Not Only scott@paragonie.com Email Involved in it, All the Emails develop in https://paragonie.com/ may be affect by it...

How to Produce E-Mail Spoofing in your Website,
**Steps to Produce this Issue:**
1) Goto: https://emkei.cz/
2) Add scott@paragonie.com "From Email" in https://emkei.cz/
3) Click Send Button,
4) The Email from scott@paragonie.com will be send to the Email you enter.

**Another way,** 
`<?php
$to = "Muhaddisshah@gmail.com";
$subject = "Email Spoofing Test";
$txt = "This is Email Spoofing";
$headers = "From: scott@paragonie.com";
mail($to,$subject,$txt,$headers);
?>`
 
Save this code in PHP file, & upload it on online server, Execute it & you can see The email will be send to your Desired Email
Note: This code doesn't work on Localhost

See Screenshots below, I received Email from your website.
{F114692}
Fix: Improve Your Mailer, Turn on some more Security filters.
Read More about Email Spoofing here:
http://searchsecurity.techtarget.com/definition/email-spoofing

Thanks! I hope you will fix this issue soon as possible, 
Regards: -Muhammad Muhaddis (Cyber Security Researcher)

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
