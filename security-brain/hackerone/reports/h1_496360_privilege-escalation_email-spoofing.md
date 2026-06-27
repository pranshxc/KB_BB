---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '496360'
original_report_id: '496360'
title: EMAIL SPOOFING
weakness: Privilege Escalation
team_handle: khanacademy
created_at: '2019-02-15T05:12:04.563Z'
disclosed_at: '2022-01-02T18:30:57.312Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- privilege-escalation
---

# EMAIL SPOOFING

## Metadata

- HackerOne Report ID: 496360
- Weakness: Privilege Escalation
- Program: khanacademy
- Disclosed At: 2022-01-02T18:30:57.312Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey KHANACADEMY,
I have found Email Spoofing type of Vulnerability in your Website.
Attacker can use your E-Mail to send emails to others.

Email spoofing is the creation of email messages with a forged sender address. Because the core email protocols do not have any mechanism for authentication, it is common for spam and phishing emails to use such spoofing to mislead the recipient about the origin of the message

Not Only contact@khanacademy.org involved in it, All the Emails develop in https://www.khanacademy.org/ may be affect by it...

Steps to Produce this Issue:
1) Goto: https://emkei.cz/
2) Add contact@khanacademy.org "From Email" in https://emkei.cz/
3) Click Send Button,
4) The Email from contact@khanacademy.org will be send to the Email you enter.

Another way,
<?php
$to = "hackthedevil@weareonhackerone.com";
$subject = "Email Spoofing Test";
$txt = "This is Email Spoofing";
$headers = "From: contact@khanacademy.org";
mail($to,$subject,$txt,$headers);
?>

Save this code in PHP file, & upload it on online server, Execute it & you can see The email will be send to your Desired Email

See Screenshots below, I received Email from your website.

Fix:
1.Improve Your Mailer, Turn on some more Security filters.
2. DMARC Policy Not Enabled-This Warning indicates that the DMARC record for this domain is not currently protected against phishing and spoofing threats. To resolve this Warning you will need to set a Quarantine or Reject policy on the domain's DMARC record. Setting a Quarantine or Reject value will prevent fraudsters from spoofing the domain as mail servers will Quarantine or Reject messages that fail authentication tests. (CHECK IT ON- https://mxtoolbox.com/SuperTool.aspx?action=mx%3akhanacademy.org&run=toolpage# )

Read More about Email Spoofing here:
http://searchsecurity.techtarget.com/definition/email-spoofing

## Impact

IT CAN BE USED TO STEAL USER DATA AND FAKE PAYMENT AND COSTUMERS.

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
