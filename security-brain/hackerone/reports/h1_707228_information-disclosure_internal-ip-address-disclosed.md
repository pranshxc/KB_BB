---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '707228'
original_report_id: '707228'
title: Internal IP Address Disclosed
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2019-10-03T16:40:38.679Z'
disclosed_at: '2020-05-14T16:58:03.203Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- information-disclosure
---

# Internal IP Address Disclosed

## Metadata

- HackerOne Report ID: 707228
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2020-05-14T16:58:03.203Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Target Url**
https://███████/███████/static/pubsite/js/main-header-dropdown.js?ver=0.87

**Summary**
Hello, I found an internal IP address disclosure in the page.

**Description:**
Extracted ip address: ████████
extracted port: ██████
place where I found it: `var logoutUrl = 'https://██████:███/█████/logout'`

## Step-by-step Reproduction Instructions

1. Navigate to the target url and search for the ip and you will find it.
█████████

## Suggested Mitigation/Remediation Actions
Avoid disclosing private ip addresses in public codes.

## Impact

Honestly there is no direct impact; however, I found that I should tell you about it in ██████e you don't know about this issue because this information can help an attacker identify other vulnerabilities or help during the exploitation of other identified vulnerabilities.

**Best Regards**

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
