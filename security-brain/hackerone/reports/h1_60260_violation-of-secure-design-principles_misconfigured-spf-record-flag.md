---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '60260'
original_report_id: '60260'
title: Misconfigured SPF Record Flag
weakness: Violation of Secure Design Principles
team_handle: udemy
created_at: '2015-05-08T21:51:16.563Z'
disclosed_at: '2016-02-22T23:57:14.979Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Misconfigured SPF Record Flag

## Metadata

- HackerOne Report ID: 60260
- Weakness: Violation of Secure Design Principles
- Program: udemy
- Disclosed At: 2016-02-22T23:57:14.979Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello Team , 

####Description : 
this report is about misconfigured spf record flag , which can be use to abuse the organization by posing the identity , which allowing to fake mailing on behalf of respected organization .

####About the Issue : 
as i seen the __SPF__  and __TXT__ record for the __Udemy.com__ which is : 
````
v=spf1 include:_spf.google.com include:smtp1.uservoice.com include:mktomail.com ~all 
``````
as u can see the symbol at last which Tilde (__~all__) is the issue , which should be replace by Hyphen (__-all__) symbol . 

so valid record will be look like : 
````
v=spf1 include:_spf.google.com include:smtp1.uservoice.com include:mktomail.com -all 
```

####Whats the issue : 
as u can see in the article  difference between softmail and fail you should be using fail as Softmail allows anyone to send spoofed emails from your domains. 
in current SPF record you should replace ~ with - at last before all , - is strict which prevents all spoofed emails except if you are sending .


####Attack Scenario :
an attacker will send phishing mail or anything malicious mail to the victim via mail : __security@Udemy.com__ , even if the victim is aware of phishing attack , he will check the Origin email which will be __security@Udemy.com__ , so he will be sure that its not fake mail and get trapped by attacker !  

This can be done using any php mailer tool like this , 
````
<?php
$to = "VICTIM@example.com";
$subject = "Password Change";
$txt = "Change your password by visiting here - [VIRUS LINK HERE]l";
$headers = "From: security@Udemy.com";
mail($to,$subject,$txt,$headers);
?>
````

__u can check your SPF record form here : http://www.kitterman.com/spf/validate.html__ !

####Reference : https://www.digitalocean.com/community/tutorials/how-to-use-an-spf-record-to-prevent-spoofing-improve-e-mail-reliability
have a look on the __digitalocean__ article for the better understanding !

Please let me know if any more info needed !

__Thank You
Geekboy :)__

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
