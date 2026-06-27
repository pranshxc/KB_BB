---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '263728'
original_report_id: '263728'
title: Password Complexity
weakness: Improper Authentication - Generic
team_handle: legalrobot
created_at: '2017-08-27T06:09:48.892Z'
disclosed_at: '2017-09-21T07:32:26.175Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: app.legalrobot-test.com
asset_type: URL
max_severity: none
tags:
- hackerone
- improper-authentication-generic
---

# Password Complexity

## Metadata

- HackerOne Report ID: 263728
- Weakness: Improper Authentication - Generic
- Program: legalrobot
- Disclosed At: 2017-09-21T07:32:26.175Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi team, 
I observe this behaviour in your website and found poor password complexity forced when registering for an account. Here are the reprdouce steps below.
Reproduce steps:

1.Open app.legalrobot-uat.com 
2.Open registration form.
3.Fill all the fields but when going for a password write a password like this ''abcdefghijklmn''
4.And your account was successfully created with this simple type of password and can easily be guessed.
Fix Or Reccomendation: 
According to password policy for choosing a secure and complex password we must consider the following points in password policy: 
Passwords should use three of four of the following four types of characters:
1.Lowercase
2.Uppercase
3.Numbers
4.Special characters such as !@#$%^&*(){}[]

In reproduce steps you can see the password which is ''abcdefghijklmn''. there is no uppercase letter forced,no numbers forced and no special characters forced by your website. If you want to make your password complexity good your should consider these four points in your password field written above. 
i usually when visit other websites and go for registering an account and when writing a password in password i observe that these password complexity points are forced by the website and you cant make a password like ''abcdefghijklmn'' which can easily guessed by someone.

Hope you'll triage this. 
Thanks 
Regards: 
Husnain Iqbal

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
