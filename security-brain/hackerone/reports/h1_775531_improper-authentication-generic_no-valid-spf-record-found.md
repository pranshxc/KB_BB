---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '775531'
original_report_id: '775531'
title: No valid SPF record found
weakness: Improper Authentication - Generic
team_handle: kubernetes
created_at: '2020-01-15T13:48:52.693Z'
disclosed_at: '2020-02-04T01:59:12.232Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
asset_identifier: prow.k8s.io
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# No valid SPF record found

## Metadata

- HackerOne Report ID: 775531
- Weakness: Improper Authentication - Generic
- Program: kubernetes
- Disclosed At: 2020-02-04T01:59:12.232Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Desciprition :

There is a email spoofing vulnerability.Email spoofing is the forgery of an email header so that the message appears to have originated from someone or somewhere other than the actual source. Email spoofing is a tactic used in phishing and spam campaigns because people are more likely to open an email when they think it has been sent by a legitimate source. The goal of email spoofing is to get recipients to open, and possibly even respond to, a solicitation.

I found :

SPF record lookup and validation for: prow.k8s.io
SPF records are published in DNS as TXT records.

The TXT records found for your domain are:


Checking to see if there is a valid SPF record.

No valid SPF record found of either type TXT or type SPF.

Remediation :

Replace ~all with -all to prevent fake email.

## Impact

An attacker would send a Fake email. The results can be more dangerous. Email spoofing is a tactic used in phishing and spam campaigns because people are more likely to open an email when they think it has been sent by a legitimate source. The goal of email spoofing is to get recipients to open, and possibly even respond to, a solicitation

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
