---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '87531'
original_report_id: '87531'
title: Mail spaming
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2015-09-04T20:00:42.878Z'
disclosed_at: '2016-01-06T08:54:06.129Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Mail spaming

## Metadata

- HackerOne Report ID: 87531
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2016-01-06T08:54:06.129Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,
We can bomb (spam) any email we want using your website. 
POC : 
1.register
2.go to https://gratipay.com/~hussein98d/emails/ and add your victim's email
3.start intercepting requests and click on "resend"
4.replay the same request many time , the victim's email will be spammed with Gratipay messages.

Thanks,
Hussein

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
