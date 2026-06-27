---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '288966'
original_report_id: '288966'
title: POODLE SSLv3 bug on multiple twitter smtp servers (mx3.twitter.com,199.59.148.204,199.16.156.108
  and 199.59.148.204)
weakness: Cryptographic Issues - Generic
team_handle: x
created_at: '2017-11-09T21:44:16.746Z'
disclosed_at: '2018-02-22T00:11:25.195Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 27
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cryptographic-issues-generic
---

# POODLE SSLv3 bug on multiple twitter smtp servers (mx3.twitter.com,199.59.148.204,199.16.156.108 and 199.59.148.204)

## Metadata

- HackerOne Report ID: 288966
- Weakness: Cryptographic Issues - Generic
- Program: x
- Disclosed At: 2018-02-22T00:11:25.195Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** POODLE SSLv3 bug on multiple twitter smtp servers

**Description:** CVE-2014-3566: The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and other products, uses nondeterministic CBC padding, which makes it easier for man-in-the-middle attackers to obtain cleartext data via a padding-oracle attack, aka the "POODLE" issue.


## Steps To Reproduce:

Hi Twitter Sec team here is the POC

  1. get a nmap installation and twitter_smtp_ssl_servers.txt file (attached)  
  2. run this command :
"nmap -sV --version-light -Pn --script ssl-poodle -p 25 -iL twitter_smtp_ssl_servers.txt | grep -B 5 VULNERABLE"
  3. See the results 

## Supporting Material/References:

  * An output screentshot  and the twitter_smtp_ssl_servers.txt are attached.

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
