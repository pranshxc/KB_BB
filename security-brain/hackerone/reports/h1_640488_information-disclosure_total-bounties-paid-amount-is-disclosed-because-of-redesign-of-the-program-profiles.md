---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '640488'
original_report_id: '640488'
title: Total bounties paid amount is disclosed because of redesign of the Program
  Profiles
weakness: Information Disclosure
team_handle: security
created_at: '2019-07-11T14:55:51.754Z'
disclosed_at: '2019-08-02T22:45:28.619Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 49
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Total bounties paid amount is disclosed because of redesign of the Program Profiles

## Metadata

- HackerOne Report ID: 640488
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2019-08-02T22:45:28.619Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description: On July 2 Hackerone redesigned the [Program Profiles](https://twitter.com/jobertabma/status/11460679483536834570).After the new program page design, I noticed that it is disclosing total bounties paid amount. For some program total bounties paid amount was hidden (████). It used to show like <$4000 if the bounty was $3990.But after the redesign, it is disclosing total bounty paid amount.


Steps to reproduce:

Go to any program page which used to hide total bounty amount (████████)


Now you should be able to see total bounties paid amount.


Please note that even if those above changed are made intentionally, this would allow others to know exact bounty amount paid to someone. For example, ███ does not disclose bounty awarded to a particular researcher. Since their total bounty amount is public one can determine how much they rewarded a particular researcher by **New Total bounty paid Amount - Old Total Bounty Paid Amount**. I see that there is a similar [report] (https://hackerone.com/reports/148050)

## Impact

This could disclose total bounty paid amount and bounty amount paid to a particular researcher in spite of program settings.

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
