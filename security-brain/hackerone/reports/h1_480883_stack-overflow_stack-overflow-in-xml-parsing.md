---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '480883'
original_report_id: '480883'
title: Stack overflow in XML Parsing
weakness: Stack Overflow
team_handle: notepad-plus-plus
created_at: '2019-01-16T11:03:23.213Z'
disclosed_at: '2019-08-25T12:50:13.333Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 98
tags:
- hackerone
- stack-overflow
---

# Stack overflow in XML Parsing

## Metadata

- HackerOne Report ID: 480883
- Weakness: Stack Overflow
- Program: notepad-plus-plus
- Disclosed At: 2019-08-25T12:50:13.333Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 

A stack buffer overflow vulnerability has been detected in XML parsing functionality  on Notepad++.

That's due to the fact that _invisibleEditView.getText function doesn't check buffer boundaries.

**Description:** 
Vulnerability src file: notepad-plus-plus/PowerEditor/src/Notepad_plus.cpp
Vulnerability line: line 1008
Variable affected: char encodingStr[128];
Function that overflows buffer: _invisibleEditView.getText

## Steps To Reproduce:

  1. Create a .xml file with a correct XML format
  2. Introduce a big XML field that overflows "encodingStr" buffer.
  3. Open the file with Notepad++ and application should crash.

## Supporting Material/References:

  * BoF_example1.xml -> Exploit example

## Impact

An attacker could create a malicious .xml file that triggers a stack buffer overflow on victim machine.

You only need to open attached .xml file example with Notepad++ to reproduce the exploit.

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
