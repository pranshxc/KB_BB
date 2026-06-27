---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1209681'
original_report_id: '1209681'
title: OOB read in libuv
weakness: Buffer Over-read
team_handle: nodejs
created_at: '2021-05-26T06:22:37.469Z'
disclosed_at: '2021-07-05T08:30:01.209Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- buffer-over-read
---

# OOB read in libuv

## Metadata

- HackerOne Report ID: 1209681
- Weakness: Buffer Over-read
- Program: nodejs
- Disclosed At: 2021-07-05T08:30:01.209Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 

The pointer p is read and increased without checking whether it is beyond pe, with the latter holding a pointer to the end of the buffer. This can lead to information disclosures or crashes. This function can be triggered via uv_getaddrinfo().  nodejs seems to use libuv and is possibly affected by this as well.

**Description:**
An out-of-bound read can occur when uv__idna_toascii() is used to convert strings to ASCII. The pointer p is read and increased without checking whether it is beyond pe, with the latter holding a pointer to the end of the buffer. This can lead to information disclosures or crashes. This function can be triggered via uv_getaddrinfo().  nodejs seems to use libuv and is possibly affected by this as well.

## Steps To Reproduce:

i attached a testcase and the ad-hoc fuzzer I used to identify the issues. If you need further help reproducing, please let me know.

~~~
static unsigned uv__utf8_decode1_slow(const char** p,
                                      const char* pe,
                                      unsigned a) {
  unsigned b;
  unsigned c;
  unsigned d;
  unsigned min;

  if (a > 0xF7)
    return -1;

  switch (*p - pe) {
  default:
    if (a > 0xEF) {
      if (p + 3 > pe)
        return -1;
      min = 0x10000;
      a = a & 7;
      b = (unsigned char) *(*p)++;   // OOB READ
      c = (unsigned char) *(*p)++;   // OOB READ
      d = (unsigned char) *(*p)++;   // OOB READ
      break;
    }
    /* Fall through. */
~~~



## Impact: [add why this issue matters]

Possiblity to crash the process when untrusted hostnames are passed to uv__getaddrinfo()

## Supporting Material/References:

-

## Misc

This issue was found during an audit of Cure53 for ExpressVPN but ExpressVPN is not affected by the issue. I reported it to the libuv project, whose maintainers suggested that i report it to nodejs directly as well.

## Impact

An oob read that does not seem to be abused to leak data, but possibly read to a guarded page which segfaults the process.

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
