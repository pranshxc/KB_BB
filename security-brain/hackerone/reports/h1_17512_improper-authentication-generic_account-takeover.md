---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '17512'
original_report_id: '17512'
title: Account takeover
weakness: Improper Authentication - Generic
team_handle: security
created_at: '2014-06-25T12:46:37.579Z'
disclosed_at: '2014-07-17T22:44:32.363Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
tags:
- hackerone
- improper-authentication-generic
---

# Account takeover

## Metadata

- HackerOne Report ID: 17512
- Weakness: Improper Authentication - Generic
- Program: security
- Disclosed At: 2014-07-17T22:44:32.363Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello,

I found another bug on hackerone.
This time it is very dangerous and creative.
Hope you will definitely love it.

Any valid account on hackerone can be hacked. eg Co-founders @jobert and @michiel can also be hacked.
I tried this one on my account only.

Lets go to the point ...

Things required to takeover complete account :
========================================
1. Valid email-id which is registered on hackerone.

Now, chaining from my previously i.e lately reported bugs.
User enumeration attack I reported recently.

One can find a registered email easily. eg michiel@hackerone.com or jobert@hackerone.com

Basic Idea :
==========
1. I am requesting a 'Reset Password link' to user's email. 
eg.
https://hackerone.com/users/password/edit?reset_password_token=MUm2xQ_TEtf2RaG1H3DK

2. Guessing the reset_password_token i.e reset_password_token=MUm2xQ_TEtf2RaG1H3DK

As everyone replying my bug reports know that there is no BRUTE FORCE protection. I am doing the same.


Proof of concept :
================
1. Generate a 'Reset Password link' of user whose account is to be compromised/hacked.
2. Use a burp suite and configure it to do a Brute Force Attack on token
eg. https://hackerone.com/users/password/edit?reset_password_token=MUm2xQ_TEtf2RaG1H3DK

Now, it is very easy to identify valid reset_password_tokens.

Server Status 200 ---> valid
Server Status 302 ----> invalid

length 4378 --->valid
length 1525 --->invalid

3. Try resetting password now.
4. Login with email and password.

Special Note :
===========
Attacker doing a brute force will get all valid tokens which are requested by user and are valid.
So attacker can reset password of users.

This was all from me. Hope now you understand the severity and power of Brute Force.
I am attaching a screenshot POC to show that there is no protection from server side as mentioned by @michiel and @jobert to me recently about brute force.

Just I made attack on my account. To show it I am attaching a screen shot. 
And there is really no protection from hackerone server. I have already made few thousands request and I am eagerly waiting for something to block me from server side.

Hope you quickly get back to me. :)

Regards,
Pranav

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
