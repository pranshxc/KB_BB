---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '629087'
original_report_id: '629087'
title: No Valid SPF Records.
weakness: Improper Authentication - Generic
team_handle: chainlink
created_at: '2019-06-25T12:18:06.480Z'
disclosed_at: '2019-07-18T15:27:29.951Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 47
asset_identifier: chain.link
asset_type: URL
max_severity: medium
tags:
- hackerone
- improper-authentication-generic
---

# No Valid SPF Records.

## Metadata

- HackerOne Report ID: 629087
- Weakness: Improper Authentication - Generic
- Program: chainlink
- Disclosed At: 2019-07-18T15:27:29.951Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hiii,

There is any issue No valid SPF Records

Desciprition :

There is a email spoofing vulnerability.Email spoofing is the forgery of an email header so that the message appears to have originated from someone or somewhere other than the actual source. Email spoofing is a tactic used in phishing and spam campaigns because people are more likely to open an email when they think it has been sent by a legitimate source. The goal of email spoofing is to get recipients to open, and possibly even respond to, a solicitation.

I found : 

SPF record lookup and validation for: chain.link
SPF records are published in DNS as TXT records.

The TXT records found for your domain are:
google-site-verification=a4ghJBW7o-Ss_TB82G2VqvQKq_8Km3UfqcuTgfc8lSY
v=spf1 include:_spf.google.com ~all

Checking to see if there is a valid SPF record.

Found v=spf1 record for chain.link:
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
