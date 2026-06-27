---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '18992'
original_report_id: '18992'
title: Possibility to attach any mobile number to any email
weakness: Improper Authentication - Generic
team_handle: mailru
created_at: '2014-07-04T12:08:54.945Z'
disclosed_at: '2016-07-18T16:44:33.819Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 54
tags:
- hackerone
- improper-authentication-generic
---

# Possibility to attach any mobile number to any email

## Metadata

- HackerOne Report ID: 18992
- Weakness: Improper Authentication - Generic
- Program: mailru
- Disclosed At: 2016-07-18T16:44:33.819Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi. With this bug you can attach any mobile number to any email box without any notification to the user. And after some time, you can get access to the email using the attached phone number.

To reproduce the steps, you will need mobile phone with any working number, Firefox and Tamper Data plugin.

Steps

1. Go to https://m.mail.ru/cgi-bin/signup

2. Put target email name and anything you want in other inputs

3. Submit form and modify on the fly the RegStep to 5 with Tamper Data

4. Submit your mobile number which you want to attach

5. Get SMS and confirm link in it.  Example: 
http://bk.ru/t/EucBxHz3nI2wdap => https://m.mail.ru/cgi-bin/reg?ID=YOUR_ID_HERE&code=YOUR_CODE_HERE&RegStep=10

6. Then go to https://m.mail.ru/cgi-bin/reg?ID=YOUR_ID_HERE&code=YOUR_CODE_HERE&RegStep=2

7. Submit form by typing your phone number and any strong password like Pa55wORd1234

8. Get SMS and again confirm the link

9. All done

Now you can log in to target email account and look the security settings. There are will be shown your confirmed mobile phone number. I hope it will be useful for you.
 	
P.S. If you do not get to reproduce the sequence, you can send me the email name to attach phone number.

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
