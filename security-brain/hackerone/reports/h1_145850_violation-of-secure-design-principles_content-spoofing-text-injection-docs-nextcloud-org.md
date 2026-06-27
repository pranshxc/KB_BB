---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145850'
original_report_id: '145850'
title: Content Spoofing/Text Injection - docs.nextcloud.org
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2016-06-19T12:19:55.988Z'
disclosed_at: '2016-06-19T12:28:13.683Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Content Spoofing/Text Injection - docs.nextcloud.org

## Metadata

- HackerOne Report ID: 145850
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2016-06-19T12:28:13.683Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Issue:
======
Hey, I've found content spoofing also known as "Text Injection" in your sub-domain docs.nextcloud.org

URL:
-------
Here is the malicious URL:
https://docs.nextcloud.org/.htacessCONTENT%20SPOOFING%20BY%20AHSAN

Fix:
Use custom 403 error page which doesn't contain user's text!

I hope you'll fix it soon!

Thanks,
Ahsan Tahir

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
