---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '84740'
original_report_id: '84740'
title: Stored XSS On Statement
weakness: Cross-site Scripting (XSS) - Generic
team_handle: gratipay
created_at: '2015-08-26T00:32:01.939Z'
disclosed_at: '2015-09-03T16:00:59.165Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS On Statement

## Metadata

- HackerOne Report ID: 84740
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: gratipay
- Disclosed At: 2015-09-03T16:00:59.165Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,
I've Found a Stored Cross-Site Scripting (XSS) In [Gratipay.com](https://gratipay.com/) .. This XSS is in The Statement, It Happens Because You're Not Sanitizing This From Markdown Malicious Codes.

##Steps To Reproduce :
1. Login To Your Account At [Gratipay.com](https://gratipay.com/)
2. Go To Your Profile Page .. And Click **Edit Statement**
3. Enter Any Of These 2 Payload : 
 * `[notmalicious](javascript:window.onerror=alert;throw%20document.cookie)`
 * `<javascript:alert(document.cookie)>`
4. Click **Save**

Now You'll See 2 Links *(See Links.png)* .. Click On Any Of These 2 Links And The XSS Payload Will Be Triggered :)

Also This is Dangerous Because The Profile's Statement is Public .. 
So Anyone Visit The Attaker's Profile And Click On This Malicious Link, XSS Will Be Triggered On His Browser. 

Take a Look At My Profile On Gratipay : https://gratipay.com/~geekpero/.

Please Let Me Know If You Need Any Information.

**References About Markdown XSS:**
* http://stackoverflow.com/questions/1690601/markdown-and-xss
* https://michelf.ca/blog/2010/markdown-and-xss/

Best Regards,
Ebram Marzouk

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
