---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '43280'
original_report_id: '43280'
title: HTTPS is not enforced for objects stored by HackerOne on Amazon S3
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2015-01-11T11:03:12.648Z'
disclosed_at: '2015-03-08T01:20:59.283Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# HTTPS is not enforced for objects stored by HackerOne on Amazon S3

## Metadata

- HackerOne Report ID: 43280
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2015-03-08T01:20:59.283Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

SSL is not enforced for objects stored by HackerOne on Amazon S3. Currently I see all the screenshots uploaded are stored in Amazon S3 bucket "hackerone-attachments" and by default HTTPS connection is made. However even HTTP connections are open to these URLs indicating that SSL is not enforced by HackerOne on these buckets.

Steps to reproduce:
1. Submit a vulnerability on any program and upload a screenshot. 
2. The URL of the screenshot looks like this:
https://hackerone-attachments.s3.amazonaws.com/production/<some_unique_path>/<filename>
3. Access the same without HTTPS.
http://hackerone-attachments.s3.amazonaws.com/production/<some_unique_path>/<filename>


Proposed Solution:
Always Force SSL on Amazon buckets and deny any HTTP request. This can be done by following these instructions here:
http://stackoverflow.com/questions/21087474/force-ssl-on-amazon-s3

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
