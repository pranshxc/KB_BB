---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223618'
original_report_id: '223618'
title: Null Password - Setting a new password doesn't check for empty spaces
weakness: Weak Cryptography for Passwords
team_handle: weblate
created_at: '2017-04-25T00:25:42.408Z'
disclosed_at: '2017-05-18T07:58:33.022Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- weak-cryptography-for-passwords
---

# Null Password - Setting a new password doesn't check for empty spaces

## Metadata

- HackerOne Report ID: 223618
- Weakness: Weak Cryptography for Passwords
- Program: weblate
- Disclosed At: 2017-05-18T07:58:33.022Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Again!

As seen your website at https://demo.weblate.org/accounts/password/
>Your password can't be too similar to your other personal information.
>Your password must contain at least 6 characters.
>Your password can't be a commonly used password.
>Your password can't be entirely numeric.

I found that it is possible to create a password with `empty spaces`, not useful anyway but renders the password security weak.

##Reproduction Steps
- Create a new account
- Load the link sent to your mail
- Now, set password to six spaces (tapping the space bar 6 times)
- You'll get a success message

##Screenshots
Here are screenshots confirming the vulnerability
{F179097}
{F179097}

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
