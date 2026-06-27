---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '137487'
original_report_id: '137487'
title: Amazon Bucket Accessible (http://inpref.s3.amazonaws.com/)
weakness: Information Disclosure
team_handle: localtapiola
created_at: '2016-05-10T13:42:35.864Z'
disclosed_at: '2016-05-12T21:43:22.455Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Amazon Bucket Accessible (http://inpref.s3.amazonaws.com/)

## Metadata

- HackerOne Report ID: 137487
- Weakness: Information Disclosure
- Program: localtapiola
- Disclosed At: 2016-05-12T21:43:22.455Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Searching through the source code of your homepage shows a few http://inpref.s3.amazonaws.com/ URLS.
I assume that you own this s3 Amazon bucket.
The problem here is, visiting that amazon bucket on a browser will shows the files on the bucket, whilst a secure bucket would bring up an access denied page. I have attached Screenshots showing Hackerone's bucket compared to your bucket to show you what a secure bucket looks like and where the bucket is being used in your source code.

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
