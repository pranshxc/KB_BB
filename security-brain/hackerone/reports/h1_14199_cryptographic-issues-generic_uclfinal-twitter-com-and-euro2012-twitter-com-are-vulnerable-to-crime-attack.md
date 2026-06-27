---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '14199'
original_report_id: '14199'
title: uclfinal.twitter.com and euro2012.twitter.com are vulnerable to CRIME attack
weakness: Cryptographic Issues - Generic
team_handle: x
created_at: '2014-05-30T23:27:48.754Z'
disclosed_at: '2014-08-16T22:49:57.519Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- cryptographic-issues-generic
---

# uclfinal.twitter.com and euro2012.twitter.com are vulnerable to CRIME attack

## Metadata

- HackerOne Report ID: 14199
- Weakness: Cryptographic Issues - Generic
- Program: x
- Disclosed At: 2014-08-16T22:49:57.519Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

hi,

i hope this one is not dup :)

https://www.ssllabs.com/ssltest/analyze.html?d=uclfinal.twitter.com&hideResults=on

https://www.ssllabs.com/ssltest/analyze.html?d=euro2012.twitter.com&hideResults=on




mohameds-iMac:Downloads mohaab007$ java -jar TestSSLServer.jar uclfinal.twitter.com
Supported versions: SSLv3 TLSv1.0
Deflate compression: YES
Supported cipher suites (ORDER IS NOT SIGNIFICANT):
  SSLv3
     RSA_WITH_RC4_128_MD5
     RSA_WITH_RC4_128_SHA
     RSA_WITH_3DES_EDE_CBC_SHA
     RSA_WITH_AES_128_CBC_SHA
     RSA_WITH_AES_256_CBC_SHA
  (TLSv1.0: idem)
----------------------
Server certificate(s):
  fb77d158dc1724ac550804ec186c48c402210eb0: CN=*.twitter.com, O="Twitter, Inc.", L=San Francisco, ST=California, C=US, SERIALNUMBER=X5-6oDhQgpWsUADnOU2IdZ38YWlIV8/8
----------------------
Minimal encryption strength:     strong encryption (96-bit or more)
Achievable encryption strength:  strong encryption (96-bit or more)
BEAST status: protected
CRIME status: vulnerable


and


mohameds-iMac:Downloads mohaab007$ java -jar TestSSLServer.jar euro2012.twitter.com
Supported versions: SSLv3 TLSv1.0
Deflate compression: YES
Supported cipher suites (ORDER IS NOT SIGNIFICANT):
  SSLv3
     RSA_WITH_RC4_128_MD5
     RSA_WITH_RC4_128_SHA
     RSA_WITH_3DES_EDE_CBC_SHA
     RSA_WITH_AES_128_CBC_SHA
     RSA_WITH_AES_256_CBC_SHA
  (TLSv1.0: idem)
----------------------
Server certificate(s):
  fb77d158dc1724ac550804ec186c48c402210eb0: CN=*.twitter.com, O="Twitter, Inc.", L=San Francisco, ST=California, C=US, SERIALNUMBER=X5-6oDhQgpWsUADnOU2IdZ38YWlIV8/8
----------------------
Minimal encryption strength:     strong encryption (96-bit or more)
Achievable encryption strength:  strong encryption (96-bit or more)
BEAST status: protected
CRIME status: vulnerable

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
