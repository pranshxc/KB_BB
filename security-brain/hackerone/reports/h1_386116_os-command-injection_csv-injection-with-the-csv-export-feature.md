---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '386116'
original_report_id: '386116'
title: CSV Injection with the CSV export feature
weakness: OS Command Injection
team_handle: chaturbate
created_at: '2018-07-24T06:11:19.552Z'
disclosed_at: '2018-09-20T00:05:50.076Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- os-command-injection
---

# CSV Injection with the CSV export feature

## Metadata

- HackerOne Report ID: 386116
- Weakness: OS Command Injection
- Program: chaturbate
- Disclosed At: 2018-09-20T00:05:50.076Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi there,

hope you are well,

The "Download as a CSV" feature of ``` does not properly "escape" fields. So that particular field is vulnerable to CSV injection.

**Steps of POC**

Step 1 : Go to any chat room and donate any token to some and in note insert ```=4+4```.
Step 2 : Now go to on this link and download transaction history. 
Step 3 : Download file as CSV and open it you can =4+4 become 8 so it's prove CSV injection.

**POC video**
███

Malicious user can take big advantage of this vulnerability because from that vulnerability we can run base OS command on any anonymous user account.

**Prevention**
Strip "=" only, it's not foolproof fix, see this report [#72785](https://hackerone.com/reports/72785) you have to strip +/-/@ and | as well.

Reference,

https://hackerone.com/reports/72785
https://hackerone.com/reports/223344
https://hackerone.com/reports/244292

Please let me know if you want more information regarding this report.

Cheers, 
Ninjan

## Impact

This vulnerability can be harm for normal user because if malicious user injected any malicious script in token note and when customer user download CSV file then inserted command directly runs when CSV file open.

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
