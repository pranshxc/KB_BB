---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '825091'
original_report_id: '825091'
title: Array Index Underflow--http rpc
weakness: Array Index Underflow
team_handle: monero
created_at: '2020-03-20T07:40:45.783Z'
disclosed_at: '2021-10-11T20:35:12.885Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- array-index-underflow
---

# Array Index Underflow--http rpc

## Metadata

- HackerOne Report ID: 825091
- Weakness: Array Index Underflow
- Program: monero
- Disclosed At: 2021-10-11T20:35:12.885Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
parserse_base_utils.h:197
const unsigned char tmp = isx[(int)*++it];
Int type will cause the array subscript to appear negative and read wrong data, 
Solution:
const unsigned char tmp = isx[(unsigned char)*++it];

## Releases Affected:

  * up to date version on github
## Steps To Reproduce:
[add details for how we can reproduce the issue]

\#include <iostream>
\#include "serialization/keyvalue_serialization.h"
\#include "storages/portable_storage_template_helper.h"
\#include "storages/portable_storage_base.h"

\#ifdef __cplusplus
extern "C"
\#endif
int LLVMFuzzerTestOneInput(const char *data, size_t size) {
  std::string s(data,size);
  try
  {
    epee::serialization::portable_storage ps;
    ps.load_from_json(s);
  }
  catch (const std::exception &e)
  {
    std::cerr << "Failed to load from binary: " << e.what() << std::endl;
    return 1;
  }
  return 0;
}

## Supporting Material/References:

  * seed file attached

## Impact

1.crash
2.leaking of sensitive info

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
