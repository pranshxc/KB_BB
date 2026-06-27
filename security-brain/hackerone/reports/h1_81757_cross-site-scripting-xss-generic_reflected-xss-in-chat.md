---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '81757'
original_report_id: '81757'
title: Reflected XSS in chat.
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-08-11T17:25:34.010Z'
disclosed_at: '2015-09-02T16:43:15.599Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS in chat.

## Metadata

- HackerOne Report ID: 81757
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-09-02T16:43:15.599Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

hello 
login in the chat  and upload file with Payload name (code injection)
like  <img src="c" onerror=alert(1)>   the code html will execute 

<span>You are not allowed to upload '<img src="c" onload="alert(1)">' files, allowed types: jpg, jpeg, gif, png</span>



Hadji Samir

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
