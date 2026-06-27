---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '87752'
original_report_id: '87752'
title: 'gallery_plus: Content Spoofing'
weakness: Violation of Secure Design Principles
team_handle: owncloud
created_at: '2015-09-06T23:59:59.571Z'
disclosed_at: '2015-09-11T09:02:45.429Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# gallery_plus: Content Spoofing

## Metadata

- HackerOne Report ID: 87752
- Weakness: Violation of Secure Design Principles
- Program: owncloud
- Disclosed At: 2015-09-11T09:02:45.429Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Attacker can send his messages directly through url. He can easily put his message on error message parameter .
Like that
http://192.168.0.107/owncloud/index.php/apps/galleryplus/error?message=Welcome to owncloud. You can get pro account by sending us 10 usd directly to our official paypal example@example.com. Thanks.&code=0


Thanks.

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
