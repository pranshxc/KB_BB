---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7929'
original_report_id: '7929'
title: Arbitrary file uploads to Amazon WS.
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2014-04-17T21:13:51.467Z'
disclosed_at: '2014-04-26T23:13:30.980Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Arbitrary file uploads to Amazon WS.

## Metadata

- HackerOne Report ID: 7929
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2014-04-26T23:13:30.980Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

It seems one is able to upload arbitrary files to Amazon Webservices through the UI.

This allows for uploading malware such as [msf-payload-x86.jpg.exe](https://hackerone-attachments.s3.amazonaws.com/production/000/006/741/bf60ba068e72e767b93d3fa35c89a36639dd1f19/msf-payload-x86.jpg.exe?AWSAccessKeyId=AKIAJFXIS7KJADBA4QQA&Expires=1397769394&Signature=aoXXsjuCqUjReIFLzMtXYyMO5us%3D) or whatever.

Beyond free hosting this could potentially be used to entice teams into downloading stuff they probably don't want.

Actual exploitation would likely depend on obfuscating the filename to look more innocent, general human errors, a certain trust in files being served from `hackerone-attachments.*.amazonaws.com` or separate issues entirely.

I could imagine this to be working as intended but still believe it would be good to consider restrictions even if the result is to not enforce any.

I would propose to at least consider displaying a warning similar to the (excellent) one displayed when visiting an external link.

HTH,

-leander

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
