---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '576288'
original_report_id: '576288'
title: Testnet address being sent in cleartext as http://rinkeby.chain.link/ is missing
  SSL certificate
weakness: Cleartext Transmission of Sensitive Information
team_handle: chainlink
created_at: '2019-05-10T10:56:33.963Z'
disclosed_at: '2019-07-17T20:49:08.716Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: rinkeby.chain.link
asset_type: URL
max_severity: high
tags:
- hackerone
- cleartext-transmission-of-sensitive-information
---

# Testnet address being sent in cleartext as http://rinkeby.chain.link/ is missing SSL certificate

## Metadata

- HackerOne Report ID: 576288
- Weakness: Cleartext Transmission of Sensitive Information
- Program: chainlink
- Disclosed At: 2019-07-17T20:49:08.716Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** SSL certificate missing for page: http://rinkeby.chain.link/ which is letting an attacker to sniff sensitive information, in this case, user's testnet address as it is being transmitted unencrypted in clear text

**Description:** http://rinkeby.chain.link/ missing SSL encryption, data sent over this address is leaking information to any malicious user and be utilized in any malicious manner, also redirection to correct HTTPS link is missing which is making more vulnerable to sniffing or MiMT attacks.

## Steps To Reproduce:

  1. Go to: http://rinkeby.chain.link/ and submit your personal testnet address
  1. Setup Wireshark and you will get the User's testnet address

## Supporting Material/References:

  * Please see the attached POC doc

## Impact

Pages missing SSL certifications send data in clear text, if the data include sensitive information that can be exposed to anyone who is using any traffic sniffer over the local or wireless network (take Wireshark application as an example)

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
