---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '260239'
original_report_id: '260239'
title: Tampering the mail id on chatbox
team_handle: legalrobot
created_at: '2017-08-15T07:34:36.590Z'
disclosed_at: '2017-08-16T09:18:56.764Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: app.legalrobot-test.com
asset_type: URL
max_severity: none
tags:
- hackerone
---

# Tampering the mail id on chatbox

## Metadata

- HackerOne Report ID: 260239
- Weakness: 
- Program: legalrobot
- Disclosed At: 2017-08-16T09:18:56.764Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

hi sir , i found a vulnerability i.e tampering the data .

steps to reproduce

1) login to https://app.legalrobot-uat.com
2) open https://app.legalrobot-uat.com/account
3) at right side bottom corner , there is a chat symbol.
4) just enter the message there , and capture the request  using burpsuite and send the request in to repeater tab , after that change the maild owner mail id to some other xxxx mail id and click on send 
5) at the response tab we will get the response 200 ok.

Thank you sir , hope you understand . here is the poc pics,

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
