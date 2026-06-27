---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '694988'
original_report_id: '694988'
title: Resource leak when using a normal site as DOH server
team_handle: curl
created_at: '2019-09-14T20:45:50.296Z'
disclosed_at: '2021-02-08T07:54:50.365Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Resource leak when using a normal site as DOH server

## Metadata

- HackerOne Report ID: 694988
- Weakness: 
- Program: curl
- Disclosed At: 2021-02-08T07:54:50.365Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
If a DOH server is used, which is not really a DOH server but just a normal web server, the DNS request is sent but the reply will not be the expected DNS payload. In that case, curl correctly thinks DNS resolution failed, but it does not clean up allocated memory properly.

## Steps To Reproduce:
See the attached demonstration program. It can use either no DOH, a valid DOH, a garbage DOH address, or a valid web server not serving DOH.
Valgrind sees that it leaks memory only in the last case, the others are cleaned up properly.

### Leaking case
This will use https://example.com/ both as the URL to reach and as a DOH.
```
valgrind ./a.out notadoh
 (snip)
==3096== HEAP SUMMARY:
==3096==     in use at exit: 98,252 bytes in 1,043 blocks
==3096==   total heap usage: 101,296 allocs, 100,253 frees, 9,473,596 bytes allocated
==3096== 
==3096== LEAK SUMMARY:
==3096==    definitely lost: 8,564 bytes in 3 blocks
==3096==    indirectly lost: 88,144 bytes in 995 blocks
==3096==      possibly lost: 0 bytes in 0 blocks
==3096==    still reachable: 1,544 bytes in 45 blocks
==3096==         suppressed: 0 bytes in 0 blocks
==3096== Rerun with --leak-check=full to see details of leaked memory
```
### Normal case - no DOH
This will use https://example.com/ without DOH.
```
valgrind ./a.out none
(snip)
==3217== HEAP SUMMARY:
==3217==     in use at exit: 1,544 bytes in 45 blocks
==3217==   total heap usage: 37,396 allocs, 37,351 frees, 3,332,013 bytes allocated
==3217== 
==3217== LEAK SUMMARY:
==3217==    definitely lost: 0 bytes in 0 blocks
==3217==    indirectly lost: 0 bytes in 0 blocks
==3217==      possibly lost: 0 bytes in 0 blocks
==3217==    still reachable: 1,544 bytes in 45 blocks
==3217==         suppressed: 0 bytes in 0 blocks
```
### Normal case - working DOH
This will use https://example.com/ with cloudflare DOH.
```
valgrind ./a.out cloudflare
(snip)
==3376== HEAP SUMMARY:
==3376==     in use at exit: 1,656 bytes in 49 blocks
==3376==   total heap usage: 101,564 allocs, 101,515 frees, 9,062,588 bytes allocated
==3376== 
==3376== LEAK SUMMARY:
==3376==    definitely lost: 0 bytes in 0 blocks
==3376==    indirectly lost: 0 bytes in 0 blocks
==3376==      possibly lost: 0 bytes in 0 blocks
==3376==    still reachable: 1,656 bytes in 49 blocks
==3376==         suppressed: 0 bytes in 0 blocks
```

## Supporting Material/References:

See the attached program.

## Impact

The failed DOH is invisible to the end user, it seems to fallback to normal DNS.
So if the user has the wrong DOH adress (perhaps confused, or the DOH url changed slightly and now points to some generic hello page), I guess the memory leaks will add up, eventually leading to denial of service because of resource depletion.

It does not feel like a serious issue but I wanted to go through hackerone instead of filing a public report right away.

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
