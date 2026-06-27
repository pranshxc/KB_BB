---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '454'
original_report_id: '454'
title: PNG compression DoS
weakness: Uncontrolled Resource Consumption
team_handle: security
created_at: '2013-11-23T21:21:28.099Z'
disclosed_at: '2015-05-28T04:45:07.299Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- uncontrolled-resource-consumption
---

# PNG compression DoS

## Metadata

- HackerOne Report ID: 454
- Weakness: Uncontrolled Resource Consumption
- Program: security
- Disclosed At: 2015-05-28T04:45:07.299Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

[ztxt]: http://www.libpng.org/pub/png/spec/1.1/PNG-Chunks.html#C.zTXt "zTXT Documentation"
[tech]: http://www.zlib.net/zlib_tech.html "zlib technical details"
[zlibvuln1]: http://www.kb.cert.org/vuls/id/680620
[zlibvuln2]: http://www.kb.cert.org/vuls/id/238678


PNG compression DoS
---------------------
 Because I did JPEG and GIF I just had to check out the PNG format.

Found
---------------------
A PNG file is composed of multiple chunks.
One of the optional ancillary chunks is called zTXT ([ztxt]).
This chunk allows storage of compressed text data using the zlib library.
From the zlib [tech] details:
"The test case was a 50MB file filled with zeros; it compressed to roughly 49 KB"
I used this to store a huge amount of data in a small PNG (smaller than 1 MB). When sent to HackerOne the service timed out. I think it's because Paperclip tried to `identify` and `convert` my image again.

As a attachment I sent the Python code I made to create the PNG, and the PNG itself. 
Usage: python createpng.py filename

Fixes
---------------------
For an easy fix every PNG file with the string "zTXt" in it should be rejected. Other data chunks may be exploitable, but I haven't looked into them yet. When this bug is fixed I will continue my research.

Theory
---------------------
Make sure your zlib library is updated . Because of old exploits in zlib's inflate() ([zlibvuln1], [zlibvuln2]), attackers might make a PNG that can exploit old machines.

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
