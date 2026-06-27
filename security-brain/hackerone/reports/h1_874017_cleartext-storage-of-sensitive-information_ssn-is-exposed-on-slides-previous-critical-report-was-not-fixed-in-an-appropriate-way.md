---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '874017'
original_report_id: '874017'
title: SSN is exposed on slides, previous critical report was not fixed in an appropriate
  way
weakness: Cleartext Storage of Sensitive Information
team_handle: deptofdefense
created_at: '2020-05-14T09:20:06.307Z'
disclosed_at: '2020-06-11T18:19:46.012Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# SSN is exposed on slides, previous critical report was not fixed in an appropriate way

## Metadata

- HackerOne Report ID: 874017
- Weakness: Cleartext Storage of Sensitive Information
- Program: deptofdefense
- Disclosed At: 2020-06-11T18:19:46.012Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
SSN is exposed on slides, previous critical report was not fixed in an appropriate way

**Description:**
1. SSN is exposed on a screenshot. Slide 13th. SSN is covered by an olive/green rectangle which is moveable. The image itself was not updated. 
██████wp-content/uploads/2018/12/████████

2. The issue was previously submitted and was not fixed in an appropriate way.
https://hackerone.com/reports/█████████

3. The file is easy to find by the file name.
https://duckduckgo.com/?q=%22███%22&t=hj&ia=web

## Impact
Critical
███████ is a real person (officer) according to  ██████████

## Step-by-step Reproduction Instructions
1. Download the file ████████wp-content/uploads/2018/12/█████
2. Navigate to slide 13
3. Move the olive rectangle which covers SSN

## Product, Version, and Configuration (If applicable)
N/A

## Suggested Mitigation/Remediation Actions
Blur/remove/cover the SSN on the image and replace the image on the slides.

## Impact

PII leakage. Name and SSN.

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
