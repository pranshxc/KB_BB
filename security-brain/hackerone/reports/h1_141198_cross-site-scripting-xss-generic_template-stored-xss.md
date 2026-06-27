---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '141198'
original_report_id: '141198'
title: Template stored XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: drchrono
created_at: '2016-05-26T14:22:29.769Z'
disclosed_at: '2016-07-21T12:33:20.801Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Template stored XSS

## Metadata

- HackerOne Report ID: 141198
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: drchrono
- Disclosed At: 2016-07-21T12:33:20.801Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The template filed names are not escaped properly, which gives an opportunity to inject HTML tags with javascript there.

1. Log into your account
2. Open the template builder https://%your_domain%.drchrono.com/clinical/advanced_form_builder
3. Create a new template with a field called **<svg onload=alert(document.domain)>**
4. Save the template and share it to the library

I created one such template as a proof of concept:

> https://www.drchrono.com/medical-forms/1460752/aaabbbcccdddeee

The script can also be executed at the search page by onmouseover event:

> https://www.drchrono.com/medical-forms/?query=aaa%22bbb%27ccc%3Cddd%3Eeee

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
