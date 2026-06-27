---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '9479'
original_report_id: '9479'
title: Anti-MIME-Sniffing header X-Content-Type-Options header has not been set.
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2014-04-24T04:17:10.001Z'
disclosed_at: '2015-04-28T05:06:57.061Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- violation-of-secure-design-principles
---

# Anti-MIME-Sniffing header X-Content-Type-Options header has not been set.

## Metadata

- HackerOne Report ID: 9479
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2015-04-28T05:06:57.061Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

The following host "profile-photos-user-content.hackerone.com" does not set the x-content-type-options header to nosniff. If a malicious user is able to upload an image with script content (Possible within the comments metadata) Internet Explorer (up till IE8) might render the content as Javascript and execute malicious code.

The problem is more severe since the photos are uploaded to a subdomain of hackerone.com.

Cheers,

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
