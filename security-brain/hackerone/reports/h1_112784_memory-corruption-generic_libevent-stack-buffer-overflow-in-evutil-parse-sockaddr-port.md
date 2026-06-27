---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '112784'
original_report_id: '112784'
title: libevent (stack) buffer overflow in evutil_parse_sockaddr_port
weakness: Memory Corruption - Generic
team_handle: torproject
created_at: '2016-01-25T22:43:17.005Z'
disclosed_at: '2017-10-19T10:16:39.032Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- memory-corruption-generic
---

# libevent (stack) buffer overflow in evutil_parse_sockaddr_port

## Metadata

- HackerOne Report ID: 112784
- Weakness: Memory Corruption - Generic
- Program: torproject
- Disclosed At: 2017-10-19T10:16:39.032Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

in ```evutil.c```:
```c
1798     char buf[128];
...
...
1809     cp = strchr(ip_as_string, ':');
1810     if (*ip_as_string == '[') {
1811         int len;
1812         if (!(cp = strchr(ip_as_string, ']'))) {
1813             return -1;
1814         }
1815         len = (int) ( cp-(ip_as_string + 1) );
1816         if (len > (int)sizeof(buf)-1) {
1817             return -1;
1818         }
1819         memcpy(buf, ip_as_string+1, len);
```

Length between '[' and ']' is cast to signed 32 bit integer on line 1815. Is the length is more than 2<<31 (INT_MAX), ```len``` will hold a negative value. Consequently, it will pass the check at line 1816. Segfault happens at line 1819.

Generate a resolv.conf with ```generate-resolv.conf```, then compile and run ```poc.c```. See ```entry-functions.txt``` for functions in tor that *might* be vulnerable.

Guido

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
