---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1039750'
original_report_id: '1039750'
title: Stored XSS in Intense Debate comment system
weakness: Cross-site Scripting (XSS) - Stored
team_handle: automattic
created_at: '2020-11-20T17:01:25.222Z'
disclosed_at: '2021-02-14T16:29:23.546Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 52
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in Intense Debate comment system

## Metadata

- HackerOne Report ID: 1039750
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: automattic
- Disclosed At: 2021-02-14T16:29:23.546Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

## _Summary:_
The  Intense Debate comment system is vulnerable to stored xss by users , this would allow for atacking admins/users on the blog ,

## Platform(s) Affected:
*  Intense Debate comment system



________________________________________________________________________________________
________________________________________________________________________________________

## _Steps To Reproduce:_


  1. Go to **intensedebate.com/moderate/{{-ID-}}**
  2. Go to comments > allow images in comments
  3. Now go to your blog and add this payload as comment :

```html
<img src="https://intensedebate.com/images/a-addblog.png" onload="alert()">
```
  4. You'll notice the alert will pop as result for the "onload" attribute ,
  

________________________________________________________________________________________
________________________________________________________________________________________


A helpful video :
{F1087899}

## Impact

* Stealing cookie and secter tokens 
* Editing html/css/js content for phishing attacks



Thanks for taking your valuable time to read and validate this report

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
