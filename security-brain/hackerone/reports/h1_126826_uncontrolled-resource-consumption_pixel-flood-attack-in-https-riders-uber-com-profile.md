---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '126826'
original_report_id: '126826'
title: Pixel flood attack in https://riders.uber.com/profile
weakness: Uncontrolled Resource Consumption
team_handle: uber
created_at: '2016-03-30T02:36:13.530Z'
disclosed_at: '2016-04-25T17:20:27.843Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Pixel flood attack in https://riders.uber.com/profile

## Metadata

- HackerOne Report ID: 126826
- Weakness: Uncontrolled Resource Consumption
- Program: uber
- Disclosed At: 2016-04-25T17:20:27.843Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

It is the exact issue described here:

https://hackerone.com/reports/390


Where uploading lottapixel.jpg it causes your service to time out




HTTP/1.1 504 Gateway Time-out
Server: nginx
Date: Wed, 30 Mar 2016 02:29:22 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 13928
Connection: close





Just upload the attached picture as your profile picture and you will get a time out!

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
