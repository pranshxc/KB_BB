---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '156347'
original_report_id: '156347'
title: Stored XSS triggered by json key during UI generation
weakness: Cross-site Scripting (XSS) - Generic
team_handle: algolia
created_at: '2016-08-03T19:31:11.174Z'
disclosed_at: '2016-09-07T08:34:02.511Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS triggered by json key during UI generation

## Metadata

- HackerOne Report ID: 156347
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: algolia
- Disclosed At: 2016-09-07T08:34:02.511Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Stored XSS is triggred from **Indices** -> **Generate a UI Demo**. Typing anything in the **Primary, Secondary, Tertiary, Image or URL attributes** for **User Interface** section. These text box have a drop down which displays the json keys during which XSS is triggered. 

Sample json for XSS would be 
``{
  "<img src=1 onerror=alert(document.domain)>": "hello",
}``

Attached: screen shot

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
