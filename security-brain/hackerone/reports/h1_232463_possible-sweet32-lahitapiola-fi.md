---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '232463'
original_report_id: '232463'
title: Possible sweet32 lahitapiola.fi
team_handle: localtapiola
created_at: '2017-05-27T16:42:34.295Z'
disclosed_at: '2017-12-13T11:58:34.269Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
---

# Possible sweet32 lahitapiola.fi

## Metadata

- HackerOne Report ID: 232463
- Weakness: 
- Program: localtapiola
- Disclosed At: 2017-12-13T11:58:34.269Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Team.
I run the nmap with ssl-enum script to look for new Vulnerability that is known as "SWEET32"

Detail about sweet32 vuln:~
Cryptographic protocols like TLS, SSH, IPsec, and OpenVPN commonly use block cipher algorithms, such as AES, Triple-DES, and Blowfish, to encrypt data between clients and servers. To use such algorithms, the data is broken into fixed-length chunks, called blocks, and each block is encrypted separately according to a mode of operation. Older block ciphers, such as Triple-DES and Blowfish use a block size of 64 bits, whereas AES uses a block size of 128 bits.

note: this vulnerability and exploitation has been demo'ed at defcon
ref site: https://sweet32.info/

Steps:

1. run nmap 2. type nmap --script ssl-enum-ciphers lahitapiola.fi 3. now hit enter and let it do its work and after it done you will find that https:443 is vulnerable to sweet32. TLSv1.1 and TLSv1.2 both are vulnerable.
Thanks.

{F188590}

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
