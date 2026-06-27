---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '776153'
original_report_id: '776153'
title: There is any issue No valid SPF Records
weakness: Improper Authentication - Generic
team_handle: kubernetes
created_at: '2020-05-02T10:55:15.569Z'
disclosed_at: '2020-07-24T00:36:14.829Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 0
asset_identifier: kubernetes.io
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# There is any issue No valid SPF Records

## Metadata

- HackerOne Report ID: 776153
- Weakness: Improper Authentication - Generic
- Program: kubernetes
- Disclosed At: 2020-07-24T00:36:14.829Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

There is a email spoofing vulnerability.Email spoofing is the forgery of an email header so that the message appears to have originated from someone or somewhere other than the actual source. Email spoofing is a tactic used in phishing and spam campaigns because people are more likely to open an email when they think it has been sent by a legitimate source. The goal of email spoofing is to get recipients to open, and possibly even respond to, a solicitation.

I found :

SPF record lookup and validation for: Kubernetes.io

SPF records are published in DNS as TXT records.

The TXT records found for your domain are:
v=spf1 include:_spf.google.com ~all
google-site-verification=oPORCoq9XU6CmaR7G_bV00CLmEz-wLGOL7SXpeEuTt8

Checking to see if there is a valid SPF record.

Found v=spf1 record for Kubernetes.io:
v=spf1 include:_spf.google.com ~all

evaluating...
SPF record passed validation test with pySPF (Python SPF library)!

Use the back button on your browser to return to the SPF checking tool without clearing the form.

Remediation :

Replace ~all with -all to prevent fake email.

Refferences :

https://www.digitalocean.com/community/tutorials/how-to-use-an-spf-record-to-prevent-spoofing-improve-e-mail-reliability

## Impact

An attacker would send a Fake email. The results can be more dangerous.

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
