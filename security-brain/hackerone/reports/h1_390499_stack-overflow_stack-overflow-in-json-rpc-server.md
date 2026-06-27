---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '390499'
original_report_id: '390499'
title: Stack Overflow in JSON RPC Server
weakness: Stack Overflow
team_handle: monero
created_at: '2018-08-04T13:51:32.627Z'
disclosed_at: '2018-09-28T22:48:12.181Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- stack-overflow
---

# Stack Overflow in JSON RPC Server

## Metadata

- HackerOne Report ID: 390499
- Weakness: Stack Overflow
- Program: monero
- Disclosed At: 2018-09-28T22:48:12.181Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 

There is a stack overflow bug in json_parser when parsing nesting objects.

**Description:** 
Monero's json parser (handled by epee libraries)  doesn't  check object tree depth while parsing

## Steps To Reproduce:

Up the service
```bash
> monerod
```
run
```bash
> python2 poc.py
```
backtrace
```
SUMMARY: AddressSanitizer: stack-overflow /home/bug/monero/contrib/epee/include/storages/portable_storage_from_json.h:47 in void epee::serialization::json::run_handler<epee::serialization::portable_storage>(epee::serialization::portable_storage::hsection, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >&, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, epee::serialization::portable_storage&)
Thread T6 created by T0 here:
    #0 0x7fe374230a51 in __interceptor_pthread_create /build/gcc/src/gcc/libsanitizer/asan/asan_interceptors.cc:202
    #1 0x7fe371b463db in boost::thread::start_thread_noexcept(boost::thread_attributes const&) (/usr/lib/libboost_thread.so.1.67.0+0x133db)

==4088==ABORTING
```
Tested on 
```bash
> monerod --version
Monero 'Lithium Luna' (v0.12.3.0-master-0dddfeac)
```
## Supporting Material/References:
poc.py > Malicious json rpc request

## Impact

Attacker could run arbitrary code

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
