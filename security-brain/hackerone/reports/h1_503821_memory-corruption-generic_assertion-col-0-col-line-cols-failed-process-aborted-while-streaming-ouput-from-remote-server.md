---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '503821'
original_report_id: '503821'
title: Assertion `col >= 0 && col < line->cols' failed, process aborted while streaming
  ouput from remote server
weakness: Memory Corruption - Generic
team_handle: putty_h1c
created_at: '2019-03-01T15:32:17.595Z'
disclosed_at: '2019-11-03T16:39:02.863Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
asset_identifier: https://www.chiark.greenend.org.uk/~sgtatham/putty/
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- memory-corruption-generic
---

# Assertion `col >= 0 && col < line->cols' failed, process aborted while streaming ouput from remote server

## Metadata

- HackerOne Report ID: 503821
- Weakness: Memory Corruption - Generic
- Program: putty_h1c
- Disclosed At: 2019-11-03T16:39:02.863Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
During the course of testing putty-0.70-2019-03-01.e0a7697 on Fedora 29 compiled with clang version 7.0.1 (Fedora 7.0.1-4.fc29), we discovered it was possible to abort a remote client by streaming data at it in such a way as to trigger an assertion failure in terminal.c.

```
putty: terminal.c:259: void clear_cc(termline *, int): Assertion `col >= 0 && col < line->cols' failed.
Aborted (core dumped)
```

**Description:** 
An assertion is a statement that a predicate (Boolean-valued function, i.e. a true–false expression) is always true at that point in code execution. It can help a programmer read the code, help a compiler compile it, or help the program detect its own defects. 

In this case, we can trigger the PuTTY client, using escape codes streamed from a remote connection, to resize itself in such a way as to trigger this Assertion Failure which aborts the client. 

## Steps To Reproduce:
1. Download https://tartarus.org/~simon/putty-snapshots/putty.tar.gz
2. Extract putty.tar.gz
3. change to the putty directory created in step 2.
3. `CC=clang CXX=clang++ ./configure && make -j5`
4. Launch PuTTY with your favorite debugger.
5. Connect to a remote host of your choice
6. On remote host: mkdir corpus && git clone https://gitlab.com/akihe/radamsa.git && cd radamsa && make && sudo make install && cd ~
7. On remote host, upload the attached JPG file to the corpus directory we created in step 4. 
8. On remote host type while true; radamsa -s 911 -o - -n inf corpus/*; done and let run until crashes.

## Supporting Material/References:
I've uploaded the core dump that happened at the time of the crash.

## Impact

Denial of service, crash, loss of data contained in scroll back

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
