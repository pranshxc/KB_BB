---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '852841'
original_report_id: '852841'
title: Reduced purmations on encryption
weakness: Cryptographic Issues - Generic
team_handle: nextcloud
created_at: '2020-04-18T10:43:45.222Z'
disclosed_at: '2020-10-28T09:13:52.904Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cryptographic-issues-generic
---

# Reduced purmations on encryption

## Metadata

- HackerOne Report ID: 852841
- Weakness: Cryptographic Issues - Generic
- Program: nextcloud
- Disclosed At: 2020-10-28T09:13:52.904Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## [`OC\Security\SecureRandom::generate`](https://github.com/nextcloud/server/blob/92692cdd7ab42453b38f1ba684649c86f2d488c0/lib/private/Security/SecureRandom.php#L49)

### Reduced Permutations

`OC\Security\SecureRandom::generate` will by default use `a-Z0-9+/` (64 bytes) character set. The numbers are not predictable, due to the use of [`random_int`](https://www.php.net/manual/en/function.random-int.php).

Most notably the [`OC\Security\Crypto::encrypt`](https://github.com/nextcloud/server/blob/92692cdd7ab42453b38f1ba684649c86f2d488c0/lib/private/Security/Crypto.php#L91) method uses an [IV](https://github.com/nextcloud/server/blob/92692cdd7ab42453b38f1ba684649c86f2d488c0/lib/private/Security/Crypto.php#L97) with a [length of 16 bytes](https://github.com/nextcloud/server/blob/92692cdd7ab42453b38f1ba684649c86f2d488c0/lib/private/Security/Crypto.php#L51). It is chosen randomly via `OC\Security\SecureRandom::generate` with the default character set. There are 256 possible bytes, but in this case it is *actually* 64 bytes. The permutations is 64^16 (instead of 256^16), which equates to a 12-byte, or 96-bit IV (instead of the expected 16-byte, or 128-bit IV). __Use raw bytes when doing cryptographic operations, via [`random_bytes`](https://www.php.net/manual/en/function.random-bytes.php).__

Do not use `OC\Security\Crypto::generate` for cryptographic keys.


### Cache Timing Attacks

It is *potentially* vulnerable to [cache timing attacks](https://en.wikipedia.org/wiki/Side-channel_attack) because the secret number is used as an index to look up a byte value in string. [Read more about cache-timing attacks here](https://blog.ircmaxell.com/2014/11/its-all-about-time.html#Other-Types-Of-Timing-Attacks-Index-Lookup).

## Impact

1. Reduced permutations increase the chances of IV re-use (which can destroy confidentially), and bring encryption key strength down (chances are still too low with a 256-bit encryption key).

2. If the complex cache timing attack vector exists, and is abused: it is possible to determine secret values generated with `OC\Security\SecureRandom::generate`.

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
