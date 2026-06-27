---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '484398'
original_report_id: '484398'
title: Buffer overflow in libavi_plugin memmove() call
weakness: Classic Buffer Overflow
team_handle: vlc_h1c
created_at: '2019-01-23T03:31:55.215Z'
disclosed_at: '2019-06-12T14:32:59.767Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
tags:
- hackerone
- classic-buffer-overflow
---

# Buffer overflow in libavi_plugin memmove() call

## Metadata

- HackerOne Report ID: 484398
- Weakness: Classic Buffer Overflow
- Program: vlc_h1c
- Disclosed At: 2019-06-12T14:32:59.767Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** When parsing an invalid AVI  file, a buffer overflow might occur.

**Description:** The ReadFrame function in the avi.c file uses a variable i_width_bytes, which is obtained directly from the file. It is a signed integer. It does not do a strict check before the memory operation(memmove, memcpy), which may cause a buffer overflow.

## Steps To Reproduce:
1.) Open vlc.exe with windbg
2.) F5 makes the program run
3 ) Drag poc files into vlc
4.) Monitor the crash from WinDBG

vlc version 3.0.6 x64
system version win7 x64

More relevant information and poc in the attachment

## Impact

If successful, a malicious third party could trigger an invalid memory access, leading to a crash of the process of the VLC media player. May cause remote code execution.

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
