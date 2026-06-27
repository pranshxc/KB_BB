---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '93157'
original_report_id: '93157'
title: SPF Protection not used, I can hijack your email server
weakness: Cryptographic Issues - Generic
team_handle: gratipay
created_at: '2015-10-09T21:15:40.866Z'
disclosed_at: '2017-08-08T16:07:59.034Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- cryptographic-issues-generic
---

# SPF Protection not used, I can hijack your email server

## Metadata

- HackerOne Report ID: 93157
- Weakness: Cryptographic Issues - Generic
- Program: gratipay
- Disclosed At: 2017-08-08T16:07:59.034Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Description

Companies like Twiter,Facebook and even Hackerone implemented a strict email security policy (combining SPF, DKIM, and DMARC) but I don't see that from gratipay You should apply strict SMPT policy to stop spoofed email sending from your domain. POC is attached.

Exploit scenario:

An attacker would send a Fake email from security@gratipay.com saying that Please change your password, The victim is aware of phishing attacks, But when he sees that the mail originated from security@gratipay.com , He has no other way than to believe it. Clicking on the link takes him to a website where certain JavaScript is executed which steals his gratipay.com id and password (SESSION COOKIE). The results can be more dangerous.

Code to Exploit:

<?php
$to = "VICTIM@example.com";
$subject = "Password Change";
$txt = "Change your password by visiting here - [VIRUS LINK HERE]l";
$headers = "From: security@agratipay.com";
mail($to,$subject,$txt,$headers);
?>
You should do the fix (see the fix below) To prevent misunderstanding and to protect your users.

FIX

Replace ~all with -all to prevent fake email.

POC IS ATTACHED HERE

Read why i am saying you to replace ~ with - : http://www.howtoforge.com/forums/archive/index.php/t-9007.html

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
