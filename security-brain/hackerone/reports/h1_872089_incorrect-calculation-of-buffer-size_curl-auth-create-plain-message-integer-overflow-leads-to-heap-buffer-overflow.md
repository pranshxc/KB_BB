---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '872089'
original_report_id: '872089'
title: Curl_auth_create_plain_message integer overflow leads to heap buffer overflow
weakness: Incorrect Calculation of Buffer Size
team_handle: curl
created_at: '2020-05-12T16:26:28.342Z'
disclosed_at: '2021-01-08T10:27:32.095Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- incorrect-calculation-of-buffer-size
---

# Curl_auth_create_plain_message integer overflow leads to heap buffer overflow

## Metadata

- HackerOne Report ID: 872089
- Weakness: Incorrect Calculation of Buffer Size
- Program: curl
- Disclosed At: 2021-01-08T10:27:32.095Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:

There is an incorrect integer overflow check in `Curl_auth_create_plain_message` in `lib/vauth/cleartext.c` , leading to a potential heap buffer overflow of controlled length and data. The exploitation seems quite easy, yet the vulnerability can only be triggered locally and does not seem to lead to RCE.

This vulnerability is very similar to [CVE-2018-16839](https://curl.haxx.se/docs/CVE-2018-16839.html) but was introduced later in [this commit](https://github.com/curl/curl/commit/762a292f8783d73501b7d7c93949268dbb2e61b7)

## Vulnerability:

```C
  zlen = (authzid == NULL ? 0 : strlen(authzid));
  clen = strlen(authcid);
  plen = strlen(passwd);

  /* Compute binary message length. Check for overflows. */
  if(((zlen + clen) > SIZE_T_MAX/4) || (plen > (SIZE_T_MAX/2 - 2))) (1)
    return CURLE_OUT_OF_MEMORY;
  plainlen = zlen + clen + plen + 2; (2)

  plainauth = malloc(plainlen); (3)
  if(!plainauth)
    return CURLE_OUT_OF_MEMORY;

  /* Calculate the reply */
  if(zlen != 0)
    memcpy(plainauth, authzid, zlen); (4)
```
In (1), `zlen + clen` can overflow, making the check for integer overflow useless.

In (2), `plainlen` can thus overflow, leading to an incorrect size for memory allocation done in (3).

A heap buffer overflow of controlled size can then occur in (4), as we can compute `clen`, `plen` and `zlen` as needed for the overflow to occur in (1) and (2).

The data in `authzid` might be fully controlled and can lead to a trivial exploitation of the heap buffer overflow.

## Limitations:

This vulnerability is not trivially triggered, as it requires the `authzid`, `authcid` and `passwd` strings to be controlled by an attacker, and require at least 2 of them to be over 2GB-long, which is not very likely to happen.

Moreover, there are more limitations on strings, as they can not be over 2GB of size, if set through curl_easy mechanisms, but I believe they can be set with no such limitations through configuration files (untested).

I did not include any PoC code for such reasons. I can always try to make one later if necessary.

## Impact

This might lead to local code execution through a heap buffer overflow, or, in case of unknown usage of libcurl from an application, to RCE (yet not very likely).

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
