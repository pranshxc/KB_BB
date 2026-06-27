---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '363658'
original_report_id: '363658'
title: Buffer overflow
weakness: Classic Buffer Overflow
team_handle: liberapay
created_at: '2018-06-09T06:51:22.024Z'
disclosed_at: '2018-06-10T06:06:40.411Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
asset_identifier: '*.liberapay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- classic-buffer-overflow
---

# Buffer overflow

## Metadata

- HackerOne Report ID: 363658
- Weakness: Classic Buffer Overflow
- Program: liberapay
- Disclosed At: 2018-06-10T06:06:40.411Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

A buffer overflow condition exists when a program attempts to put more data in a buffer than it can hold or when a program attempts to put data in a memory area past a buffer. In this case, a buffer is a sequential section of memory allocated to contain anything from a character string to an array of integers. Writing outside the bounds of a block of allocated memory can corrupt data, crash the program, or cause the execution of malicious code. 
For better refernce:
https://www.owasp.org/index.php/Buffer_Overflow

POC:
Go to
https://liberapay.com/sign-up
Now type(copy and paste using python) email address of size more than 100mb or in gbs and sign up.
After signing up for few times u will receive this error as shown in sent pic.

Steps to resolve:
Restrict size limit on input parameter.

## Impact

Category:Availability: Buffer overflows generally lead to crashes. Other attacks leading to lack of availability are possible, including putting the program into an infinite loop.
    Access control (instruction processing): Buffer overflows often can be used to execute arbitrary code, which is usually outside the scope of a program’s implicit security policy.
    Other: When the consequence is arbitrary code execution, this can often be used to subvert any other security service.

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
