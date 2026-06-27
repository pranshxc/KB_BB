---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '74518'
original_report_id: '74518'
title: The email updates issues
team_handle: digitalsellz
created_at: '2015-07-08T21:19:29.475Z'
disclosed_at: '2015-08-25T21:30:41.362Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
---

# The email updates issues

## Metadata

- HackerOne Report ID: 74518
- Weakness: 
- Program: digitalsellz
- Disclosed At: 2015-08-25T21:30:41.362Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

1. The email message content at the https://www.digitalsellz.com/user/#/email-updates page (contrary to the [email customization one](https://www.digitalsellz.com/user/#/custom-email)) is not validated properly. So this form allows all the html tags and their parameters. For example, all the following tags are sent as is:

> <a href="javascript:alert(0)">Link</a>
<a href='javascript:alert(1)'>Link</a>
<img src=x onerror="alert(2)" />
<script>alert(3)</script>

and all their scripts will be executed if the email service the customer uses doesn't have a proper protection itself. Of course most of the modern email services do this, but there are still some not too widespread ones that don't. This also relates to the customers that have their own servers and have the emails there.

Well, it's the recipient system's vulnerability mostly, but you also shouldn't send executable code there. Otherwise it would be something like distributing viruses over your clients and saying it's their fault they don't use antivirus software :) Especially since it won't be too hard to fix it, cause you already have this done for the [email customization page](https://www.digitalsellz.com/user/#/custom-email) mentioned above — all the unnecessary tags and parameters are properly sanitized, so you just have to copy the validating code from there.

2\. Also I don't think it's a good idea to let anyone send whatever he wants on your behalf in general

For example, the attacker can send emails as follows:

> Due to the recent security issue some of our accounts have been compromised.
>
> We recommend you to change your password as soon as possible. To do this please click the following link:
>
>[Change your password](http://phishing_link)

Being sent on behalf of support@digitalsellz.com and designed kinda like your forget password mail, it can easily mislead the customers, so they will open the attacker's phishing link and put their login and password there.

He can also send something abusive or prohibited by law.

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
