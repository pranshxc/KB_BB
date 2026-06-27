---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1468962'
original_report_id: '1468962'
title: Binary output bypass
weakness: Classic Buffer Overflow
team_handle: curl
created_at: '2022-02-03T02:22:00.637Z'
disclosed_at: '2022-03-09T21:48:03.526Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- classic-buffer-overflow
---

# Binary output bypass

## Metadata

- HackerOne Report ID: 1468962
- Weakness: Classic Buffer Overflow
- Program: curl
- Disclosed At: 2022-03-09T21:48:03.526Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Binary output check bypass

## Summary:
When curl outputs content, it checks for binary output. If the output is large enough, it bypasses the check for binary output. This can mess with the terminal.

## Steps To Reproduce:
1. Setup a server of your choice.
2. Create a function f with these arguments: char and num. Num is number of characters repeating.
3. Before serving at a given endpoint, create an offset f(".", 16384)
4. Create the payload with unicode 0x0 like this f("unicode 0x0", 1)
5. Make the server serve this at a given endpoint.
6. Run this command: curl "Accept: application/xml" -H "Content-Type: application/xml" http://localhost:8080/yourendpoint
7. Change the offset f(".", 16384) to f(".", 16383) to check if it worked.


 curlpayload.png is the code
execution.png is output for when it worked
failed.png is when it failed, when I changed the offset to 16383

## Impact

There could be some further impact by this exploit. As of now it can make the terminal really buggy at times, but further implementations could lead to something else.

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
