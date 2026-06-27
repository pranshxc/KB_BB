---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '150560'
original_report_id: '150560'
title: XSS @ *.olx.com.ar
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-07-11T11:15:41.677Z'
disclosed_at: '2016-07-13T14:46:05.505Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS @ *.olx.com.ar

## Metadata

- HackerOne Report ID: 150560
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2016-07-13T14:46:05.505Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I see you have just launched the program on HackerOne.
And I have visited your site olx.com.ar and found an interesting XSS.

Let's see.
**Summary**
The bug lies in the 'description' of any posting. It seems you're removing and `<` and `>` sign to prevent including any html tags but there are some other ways ;-). I found that the `<meta>` tag is including everything from description.

**Steps to reproduce**
Go to https://www.olx.com.ar/posting
Now create an ad with everything you want.
In description put the following `;url=data:text/html;base64,PHNjcmlwdD5hbGVydCgneHNzIGJ5IHphd2FkJyk8L3NjcmlwdD4="HTTP-EQUIV="refresh" blah="`
Now Publish the ad.
and Visit the ad. You will see XSS being triggered.

**PoC**
https://adolfogonzaleschaves.olx.com.ar/xss-poc-for-hackerone-iid-891023785

Hope you fix it  and offer some rewards :-)

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
