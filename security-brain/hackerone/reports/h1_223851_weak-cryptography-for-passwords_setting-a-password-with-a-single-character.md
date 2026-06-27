---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223851'
original_report_id: '223851'
title: Setting a password with a single character
weakness: Weak Cryptography for Passwords
team_handle: weblate
created_at: '2017-04-25T17:54:24.566Z'
disclosed_at: '2017-05-18T07:58:16.660Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- weak-cryptography-for-passwords
---

# Setting a password with a single character

## Metadata

- HackerOne Report ID: 223851
- Weakness: Weak Cryptography for Passwords
- Program: weblate
- Disclosed At: 2017-05-18T07:58:16.660Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi!,

Following my previous report, #223618, I could see that you made a change to the site which https://demo.weblate.org/accounts/password/ says

>Your password can't be too similar to your other personal information.
>Your password must contain at least 6 characters.
>Your password can't be a commonly used password.
>Your password can't be entirely numeric.
>**Your password can't consist of single character or whitespace only.**

I found that it is possible to create a password with a single character

###Reproduction Steps
- Create a new account
- Load the link sent to your mail
- Now, set password to six spaces(tapping the space bar 6 times) and a letter included
- You'll get a success message.

##Screenshot
{F179412}
{F179413}

Regards,
Shuaib

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
