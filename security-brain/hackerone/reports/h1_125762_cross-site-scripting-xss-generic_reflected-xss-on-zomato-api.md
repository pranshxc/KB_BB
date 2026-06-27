---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '125762'
original_report_id: '125762'
title: Reflected XSS on Zomato API
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zomato
created_at: '2016-03-24T18:35:58.767Z'
disclosed_at: '2016-05-27T08:46:33.934Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS on Zomato API

## Metadata

- HackerOne Report ID: 125762
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zomato
- Disclosed At: 2016-05-27T08:46:33.934Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

First of all [here] (https://hackerone.com/reports/115402) is another report looks like this report. 

Zomato using APIs for developers to create their restaurant search etc. 

You are using res_search_widget which is can be seen right [here] (https://www.zomato.com/widgets/res_search_widget.php). 

In the report which is 115402 number that i mentioned start of the report, reporter say something like this: 

I use a piece of javascript code that creates an alert box with the document.domain, which shows the SOP is bypassed: "}');alert(document.domain);console.log('.  But you dont need to add something to your API or widget code. You should only use '"> characters to bypass security and have xss alert.

So, here is xss:

Just go to your widget from [here](https://www.zomato.com/widgets/res_search_widget.php).

And just write this payload:

`'-->">'>'"<script>prompt(document.domain)</script>;" f0r=TRUE`

Here is your alert.

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
