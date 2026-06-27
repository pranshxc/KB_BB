---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '783191'
original_report_id: '783191'
title: Clickjacking to change email address
weakness: UI Redressing (Clickjacking)
team_handle: gener8
created_at: '2020-01-25T14:00:26.294Z'
disclosed_at: '2022-01-12T08:33:43.087Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: '*.gener8ads.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking to change email address

## Metadata

- HackerOne Report ID: 783191
- Weakness: UI Redressing (Clickjacking)
- Program: gener8
- Disclosed At: 2022-01-12T08:33:43.087Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Summary



Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.

It allows remote attackers to do some clickjacking which can be used for adding arbitrary tasks . Why? Almost all of your page has missing X-FRAME-OPTIONS header.

Websites are at risk of a clickjacking attack when they allow content to be embedded within a frame.





##Proof of concept code :- 

Copy the above code and paste it in notepad and save it with .html extention
and open it in browser


<html> 
<head> 
<title>Clickjack test page</title> 
</head> 
<body> 
<p>Website is vulnerable to clickjacking!</p>

<iframe src="https://gener8ads.com/dashboard/account"  sandbox="allow-top-navigation allow-same-origin allow-scripts" width="500" height="500"></iframe> 

</body> 
</html>


Copy and paste above given code and  save it with hack.html and  open it in browser



------------------------------------------------------------------->

Recommendation :- 

Add X-FRAME-OPTIONS header to mitigate the issue

## Impact

An attacker may use this risk to invisibly load the target website into their own site and trick users into clicking on links which they never intended to. An "X-Frame-Options" header should be sent by the server to either deny framing of content, only allow it from the same origin or allow it from a trusted URIs.

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
