---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '205529'
original_report_id: '205529'
title: Combined attacks leading to stealing user's account
weakness: Violation of Secure Design Principles
team_handle: olx
created_at: '2017-02-11T15:09:01.192Z'
disclosed_at: '2017-05-24T10:37:57.357Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- violation-of-secure-design-principles
---

# Combined attacks leading to stealing user's account

## Metadata

- HackerOne Report ID: 205529
- Weakness: Violation of Secure Design Principles
- Program: olx
- Disclosed At: 2017-05-24T10:37:57.357Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,
First: I have found out that when I register an account with the an email already used it doesn't tell anything but it sends a link to the registered email and when the user visits the link the password is changed without any further checking if the user was the one who asked for password change.
But I thought this maybe known by you so I kept looking.
Second:After changing the password or registration, the browser is redirected to: https://olx.com.eg/account/checkemailafterpost/?email=[email here]
, the email parameter is vulnerable to text injection which leads to content spoofing.

How an attack happens:
1.The attacker knows the email of the victim, visits the site and registers with the same email but with a new password.
2.The attacker crafts an attack page through the content spoofing vulnerability.
eg: https://olx.com.eg/en/account/checkemailafterpost/?email=[Victim%27s%20email].%20%09%20and%20please%20to%20be%20more%20safe%20please%20go%20to%20our%20site%20%22%0Awww.attacker.com%22%20which%20will%20help%20you%20through%20all%20the%20instructions.
{F159775}
3.The attacker sends the link to the victim or makes him visit it in someway.
4.The victim won't doubt that the link is from attacker as the site is trusted.
5.The victim visits the link,the password is changed and the attacker now has access to the victim's email.


And through this an attacker can access victim's email.


Extra: I have found that < and > is removed, but using a new line[%0a] or a tab[%09] will bypass this and it will be entered.
as in {F159773}

Thank you.

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
