---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2453328'
original_report_id: '2453328'
title: Assertion failed in node::http2::Http2Session::~Http2Session() leads to HTTP/2
  server crash
weakness: Uncontrolled Resource Consumption
team_handle: ibb
created_at: '2024-04-08T20:41:07.680Z'
disclosed_at: '2024-04-29T21:01:40.904Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 37
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Assertion failed in node::http2::Http2Session::~Http2Session() leads to HTTP/2 server crash

## Metadata

- HackerOne Report ID: 2453328
- Weakness: Uncontrolled Resource Consumption
- Program: ibb
- Disclosed At: 2024-04-29T21:01:40.904Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

An attacker can make the Node.js HTTP/2 server completely unavailable by sending a small amount of HTTP/2 frames packets with a few HTTP/2 frames inside. It is possible to leave some data in nghttp2 memory after reset when headers with HTTP/2 CONTINUATION frame are sent to the server and then a TCP connection is abruptly closed by the client triggering the Http2Session destructor while header frames are still being processed (and stored in memory) causing a race condition.

* Advisory: https://nodejs.org/en/blog/vulnerability/april-2024-security-releases
* HackerOne report: 2319584

## Impact

Server crashes instantly after sending a few HTTP/2 frames.

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
