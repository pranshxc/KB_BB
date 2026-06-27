---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '34112'
original_report_id: '34112'
title: SMPT Protection not used, I can hijack your email server.
weakness: Cryptographic Issues - Generic
team_handle: blockio
created_at: '2014-11-06T05:35:08.435Z'
disclosed_at: '2015-08-13T13:36:19.065Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cryptographic-issues-generic
---

# SMPT Protection not used, I can hijack your email server.

## Metadata

- HackerOne Report ID: 34112
- Weakness: Cryptographic Issues - Generic
- Program: blockio
- Disclosed At: 2015-08-13T13:36:19.065Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description

Companies like Coinbase, Yahoo,Google,Facebook and even hackerone implemented a strict email security policy (combining SPF, DKIM, and DMARC) but I don't see taht from block.io , You should apply strict SMPT policy to stop spoofed email sending from your domain. POC is attached.

Exploit scenario:

An attacker would send a Fake email from support@block.io saying that Please change your password, The victim is aware of phishing attacks, But when he sees that the mail originated from support@block.io , He has no other way than to believe it. Clicking on the link takes him to a website where certain JavaScript is executed which steals his block.io id and password (SESSION COOKIE). The results can be more dangerous.

Code to Exploit:

    <?php
    $to = "VICTIM@example.com";
    $subject = "Password Change";
    $txt = "Change your password by visiting here - [VIRUS LINK HERE]l";
    $headers = "From: support@block.io";
    mail($to,$subject,$txt,$headers);
    ?>
You should do the fix (see the fix below) To prevent misunderstanding and to protect your users.

FIX

Replace `?all` with `-all` to prevent fake email.

Your's record:
`v=spf1 include:spf.mandrillapp.com ?all`

It should be
`v=spf1 include:spf.mandrillapp.com -all `



POC IS ATTACHED HERE: http://gyazo.com/1f753428abff659b3f83df625dc380bc

OUTPUT:

    SPF record lookup and validation for: Block.io

    SPF records are published in DNS as TXT records.

    The TXT records found for your domain are:
    v=spf1 include:spf.mandrillapp.com ?all 

    Checking to see if there is a valid SPF record. 

    Found v=spf1 record for Block.io: 
    v=spf1 include:spf.mandrillapp.com ?all <---------- this is your mistake

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
