---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '324303'
original_report_id: '324303'
title: DOM Based XSS in mycrypto.com
weakness: Cross-site Scripting (XSS) - DOM
team_handle: mycrypto
created_at: '2018-03-10T22:16:08.521Z'
disclosed_at: '2018-03-18T01:11:40.974Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 41
asset_identifier: www.mycrypto.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# DOM Based XSS in mycrypto.com

## Metadata

- HackerOne Report ID: 324303
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: mycrypto
- Disclosed At: 2018-03-18T01:11:40.974Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Description & PoC
The "connected successfully" message is printed out without any output sanitation:
{F271357}
This is how it's being printed(this code snippet is taken from mycrypto-master.js, line 4072): 
{F271359}

An attacker can simply put his payload at the link and it'll be embedded within the page output:
```
https://mycrypto.com/#send-transaction<div/class="header__wrap"><a/href=javascript:alert(0)><h1>pwn3d</h1></a><img/src=//unskid.me/dist/jesus.gif></div>
```
{F271358}


##Notes
As you can see, I couldn't get any javascript running, that's because the application has an AngularJS XSS protection that goes through ALL the href\src\similiar attributes in the DOM and checks if it has a malicious content/XSS attempts with a tough regex(based on a whitelist). Couldn't bypass that.
Some screenshots of the "angular-XSS-blocker" from the chrome debugger :
{F271362}
{F271361}
Once it's triggered and see a malicious attempt(isImg==false), the malicious <a> tag:
```
<a href="javascript:alert(0)">click here</a>
```
turns into:
```
<a>click here</a>
```

## Impact

Although i did not get running javascript i still think that it's worth reporting because, well, still..anyone can inject other HTML code in that part of the application and it should be encoded. It can lead to other things like phishing/content spoofing/clickjacking.

The hacker selected the **Cross-site Scripting (XSS) - DOM** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://mycrypto.com/#here

**Verified**
Yes

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
