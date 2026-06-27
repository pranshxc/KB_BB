---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '163067'
original_report_id: '163067'
title: Stealing users password (Limited Scenario)
weakness: Violation of Secure Design Principles
team_handle: uber
created_at: '2016-08-24T13:53:40.337Z'
disclosed_at: '2016-09-29T20:13:31.430Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 35
tags:
- hackerone
- violation-of-secure-design-principles
---

# Stealing users password (Limited Scenario)

## Metadata

- HackerOne Report ID: 163067
- Weakness: Violation of Secure Design Principles
- Program: uber
- Disclosed At: 2016-09-29T20:13:31.430Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

__Hello Team,__

####Description :
> This is report is about an interesting scenario where an user's password can be steal while password reset process due to wired user controlled redirection take place after password reset process.

By accepting the fact that URL redirect is not in scope for uber but this one is interesting on reset page that something need to look.


####Step To Reproduce : 
+ Go [Here](https://login.uber.com/forgot-password?source=auth&next_url=data:text/html;base64,PGlmcmFtZSBzcmM9aHR0cDovL2dvby5nbC92TkE3RHYgaGVpZ2h0PTEwMCUgd2lkdGg9MTAwJSBmcmFtZWJvcmRlcj0wPjwvaWZyYW1lPg==)
+ Where __`next_url`__ is user controlled on password reset page __`https://login.uber.com/forgot-password?source=auth&next_url=user_controlled_url`__ . 
+ Request password reset token for your account !
+ Get the reset link and change the password and will be redirected to supplied `next_url` url.
+ Where an well crafted form will ask to confirm your password !
+ And this is how someone can steal the password of someone !

####Impact :
>though impact is not very direct here , but still critical enough if any attacker succeeded to exploit this & that will allow him to access victim account , so this should be fixed !  

####Video POC (Tested in Mozilla) : https://dl.dropboxusercontent.com/u/62765113/ShareX/16/2016-08-24_19-18-20.mp4

####Possible Fix :
+ `next_url` should not be reflect after password reset also should not be user controlled .

Please let me know if any more info needed !

-------------
**Regards**
*Geekboy !*

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
