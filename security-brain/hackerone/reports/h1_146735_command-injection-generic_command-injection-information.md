---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '146735'
original_report_id: '146735'
title: Command Injection, Information
weakness: Command Injection - Generic
team_handle: uber
created_at: '2016-06-23T07:11:38.994Z'
disclosed_at: '2016-07-07T23:03:59.007Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- command-injection-generic
---

# Command Injection, Information

## Metadata

- HackerOne Report ID: 146735
- Weakness: Command Injection - Generic
- Program: uber
- Disclosed At: 2016-07-07T23:03:59.007Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Dear Sir,

I am going to share information about content spoofing vulnerability present in 404 page. This vulnerability may not consider as in-scope but you can put it as informative.

Description :

"Content spoofing, also referred to as content injection or virtual defacement, is an attack targeting a user made possible by an injection vulnerability in a web application. When an application does not properly handle user supplied data, an attacker can supply content to a web application, typically via a parameter value, that is reflected back to the user. "

Attacker can modify page content in a way that "The requested URL /https://eng.uber.com has been changed to https://www.fakewebsite.com. so please visit https://www.fakewebsite.com as your requested link was not found on this server."

Affected URL: https://eng.uber.com

POC : https://eng.uber.com/has%20been%20changed%20to%20https%3A%2F%2Fwww.fakewebsite.com.%20so%20please%20visit%20https%3A%2F%2Fwww.fakewebsite.com%20as%20your%20requested%20link

Vulnerability reference: https://www.owasp.org/index.php/Content_Spoofing

Please find attachment for POC.

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
