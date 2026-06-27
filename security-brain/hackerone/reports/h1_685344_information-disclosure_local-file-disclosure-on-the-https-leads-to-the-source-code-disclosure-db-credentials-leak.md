---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '685344'
original_report_id: '685344'
title: Local File Disclosure on the ████████ (https://████/) leads to the source code
  disclosure & DB credentials leak
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2019-08-31T01:46:36.296Z'
disclosed_at: '2021-01-12T21:53:16.766Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- information-disclosure
---

# Local File Disclosure on the ████████ (https://████/) leads to the source code disclosure & DB credentials leak

## Metadata

- HackerOne Report ID: 685344
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2021-01-12T21:53:16.766Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Description
I discovered another LFD on the https://████/ (virtual host on the █████ IP)

##POC
https://█████/file.ashx?path=web.config
will download the website configuration file.
It exposes different DB credentials than in previous reports:
███

Similarly, attacker able to get content of any server-side file, such as source code of application:
https://███/file.ashx?path=index.aspx

## Impact

Source code & sensitive configuration data leakage. Attacker can use it to compromise the resource.

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
