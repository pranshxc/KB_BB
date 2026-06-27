---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '275960'
original_report_id: '275960'
title: Address Bar Spoofing on TOR Browser
weakness: Phishing
team_handle: torproject
created_at: '2017-10-09T21:58:07.986Z'
disclosed_at: '2023-01-02T08:43:51.692Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 14
tags:
- hackerone
- phishing
---

# Address Bar Spoofing on TOR Browser

## Metadata

- HackerOne Report ID: 275960
- Weakness: Phishing
- Program: torproject
- Disclosed At: 2023-01-02T08:43:51.692Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi TOR team,

I would like to report a security bug in your browser:

Step 1: Goto http://www.ոokia.com/(http://jsbin.com/wuyikedaxi/1/edit?html,output)
Step 2: Observe that address bar points to http://www.ոokia.com/ which actually to be pointing to http://xn--okia-zgf.com, however browser displays www.ոokia.com/

Actual results:

Address bar points to a spoofed domain http://www.ոokia.com/. Address bar fails to parse character "ո"(U+0578 Armenian Small Letter). Several other characters from Armenian family lead to the same effect. 

Expected results:

TORbrowser should have resolved the domain to real http://xn--okia-zgf.com.  On chrome, internet explorer and firefox it resolves to xn--okia-zgf.com.

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
