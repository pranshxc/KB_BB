---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '126374'
original_report_id: '126374'
title: Uploading Plain Text to uber-documents.s3.amazonaws.com Through the Driver
  Document Upload Page
weakness: Violation of Secure Design Principles
team_handle: uber
created_at: '2016-03-27T20:24:29.640Z'
disclosed_at: '2016-06-13T22:17:31.291Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Uploading Plain Text to uber-documents.s3.amazonaws.com Through the Driver Document Upload Page

## Metadata

- HackerOne Report ID: 126374
- Weakness: Violation of Secure Design Principles
- Program: uber
- Disclosed At: 2016-06-13T22:17:31.291Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi, 

When a new driver is registering on Uber, they have to upload a variety of files (proof of insurance, ID, etc). When these files are being uploaded, Uber.com only checks whether the files have the correct extension. This means that one can upload a plain text file with a ```.png``` extension and it will be rendered as plain text when viewed in Internet Explorer. 

At first I was attempting to get js execution with this (similar to how I did #126197), but that is not possible. When the file extension (```.png``` in our case) and the MIME type (```image/png```) match, Internet Explorer will not render it as HTML, it is only willing to render it as plain text. This still opens up a possibility of a fishing attach by doing something like this: 

```
https://uber-documents.s3.amazonaws.com/f7e83fb2-a309-4845-a038-8cb3846a0f0d.png?Signature=eQwYlK31HVRqaHN%2FdvaImVEDQuI%3D&Expires=1459110446&AWSAccessKeyId=AKIAIQSUTKT5KJFDBULQ
```

While this is not as bad as JS execution, I believe that this still qualifies as a vulnerability. In all other image upload forms (e.g. profile picture upload), Uber carefully checks that the image is valid before accepting it and hosting it. In this case, Uber fails to do so. 

Thanks,
David Dworken

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
