---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2383486'
original_report_id: '2383486'
title: Insecure S3 Bucket Exposing Git Directory in Mozilla Foundation Infographics
  Project
weakness: Improper Access Control - Generic
team_handle: mozilla
created_at: '2024-02-21T12:18:54.480Z'
disclosed_at: '2024-03-13T14:45:45.522Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 46
tags:
- hackerone
- improper-access-control-generic
---

# Insecure S3 Bucket Exposing Git Directory in Mozilla Foundation Infographics Project

## Metadata

- HackerOne Report ID: 2383486
- Weakness: Improper Access Control - Generic
- Program: mozilla
- Disclosed At: 2024-03-13T14:45:45.522Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary

I discovered an insecure S3 bucket associated with the Mozilla Foundation's Infographics project. While the bucket itself is inaccessible, the DotGit extension alerted me that the `/.git` directory is accessible. I was able to use the GitDump tool to dump the entire directory.

## Details

**Repository Link:** [Mozilla Foundation Infographics](https://github.com/MozillaFoundation/mofo-infographics#:~:text=https%3A//mofo%2Dinfographics.s3.amazonaws.com/projects/%3Claunch%20date%3E%2D%3Cproject%2Dname%2Dwith%2Dhypens%3E/index.html)

**S3 Bucket:** [mofo-infographics.s3.amazonaws.com](https://mofo-infographics.s3.amazonaws.com)

## Steps to Reproduce

1. Open terminal and enter `git clone https://github.com/Ebryx/GitDump.git`
2. Navigate to the GitDump directory with `cd GitDump`
3. Run the GitDump tool with `python3 ./git-dump.py https://mofo-infographics.s3.amazonaws.com/`
4. Navigate to the output directory with `cd output/.git`
5. Observe that all files have been dumped

##POC
█████████

## Impact

The exposure of the `/.git` directory can lead to unauthorized access to sensitive information, such as source code, configuration files, and potentially secrets or credentials stored in the repository.

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
