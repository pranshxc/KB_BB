---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '739858'
original_report_id: '739858'
title: Able to download any hosted content on AWS S3 bucket(stripo)
weakness: Improper Access Control - Generic
team_handle: stripo
created_at: '2019-11-18T16:32:42.288Z'
disclosed_at: '2020-02-10T08:37:00.709Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-access-control-generic
---

# Able to download any hosted content on AWS S3 bucket(stripo)

## Metadata

- HackerOne Report ID: 739858
- Weakness: Improper Access Control - Generic
- Program: stripo
- Disclosed At: 2020-02-10T08:37:00.709Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

An AWS s3 bucket was found, with improper access controls, where all its contents could be downloaded.

Steps to reproduce:
1. List contents of the bucket with: ``aws s3 ls s3://stripo``
2. Download the hosted data with : ``aws s3 sync s3://stripo .``

## Impact

Any hosted data can be downloaded to an attackers personal storage.

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
