---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '300817'
original_report_id: '300817'
title: Secure Client-Initiated Renegotiation
weakness: Cryptographic Issues - Generic
team_handle: localtapiola
created_at: '2017-12-27T15:57:52.331Z'
disclosed_at: '2024-02-16T13:58:55.747Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
asset_identifier: www.lahitapiola.fi
asset_type: URL
max_severity: critical
tags:
- hackerone
- cryptographic-issues-generic
---

# Secure Client-Initiated Renegotiation

## Metadata

- HackerOne Report ID: 300817
- Weakness: Cryptographic Issues - Generic
- Program: localtapiola
- Disclosed At: 2024-02-16T13:58:55.747Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Renegotiation can open the door to attacks. There are two primary worries:

CVE-2009-3555: This vulnerability allows a “man-in-the-middle” attacker to inject data into an HTTPS session and execute requests on behalf of the victim. Refer to CVE-2009-3555 for more details.

Denial of Service (DoS): Establishing a secure SSL connection requires more processing power on the server, around 15 times, than on the client. An attacker can exploit this processing-power property along with renegotiation to trigger hundreds of handshakes in the same TCP connection; an assault can bring down a 30Gb-link server using only a laptop and DSL connection.

The THC group demonstrated the DoS attack and released a tool, THC-SSL-DoS, as a proof of concept. An SSL DoS attack can be carried out without SSL renegotiation by simply establishing a new TCP connection for every new handshake. SSL renegotiation makes it very easy to carry out this DoS attack.

Reference Link : https://securingtomorrow.mcafee.com/technical-how-to/tips-securing-ssl-renegotiation/

Step to reproduce :

Run the following command in Open SSL : openssl s_client -connect lahitapiola.fi:443

Below is the POC screenshot :

## Impact

DOS Attack

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
