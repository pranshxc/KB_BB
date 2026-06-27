---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '688546'
original_report_id: '688546'
title: Clickjacking
team_handle: palo_alto_software
created_at: '2019-09-05T09:09:57.721Z'
disclosed_at: '2022-01-17T07:27:37.227Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: app.outpost.co
asset_type: URL
max_severity: none
tags:
- hackerone
---

# Clickjacking

## Metadata

- HackerOne Report ID: 688546
- Weakness: 
- Program: palo_alto_software
- Disclosed At: 2022-01-17T07:27:37.227Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Summary

Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.

Websites are at risk of a clickjacking attack when they allow content to be embedded within a frame.

An attacker may use this risk to invisibly load the target website into their own site and trick users into clicking on links which they never intended to. An "X-Frame-Options" header should be sent by the server to either deny framing of content, only allow it from the same origin or allow it from a trusted URIs.


##Proof of concept code :- 

Copy the above code and paste it in notepad and save it with .html extention
and open it in browser

```
<html> 
<head> 
<title>Clickjack test page</title> 
</head> 
<body> 
<p>Website is vulnerable to clickjacking!</p>

<iframe src="https://app.outpost.co/settings/preferences"  sandbox="allow-top-navigation allow-same-origin allow-scripts" width="500" height="500"></iframe> 

</body> 
</html>
```

Copy and paste above given code and  save it with hack.html and  open it in browser




##Recommendation :- 

Add X-FRAME-OPTIONS header to mitigate the issue

## Impact

It allows remote attackers to do some clickjacking which can be used for adding arbitrary tasks . Why? Almost all of your page has missing X-FRAME-OPTIONS header.


##Thanks

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
