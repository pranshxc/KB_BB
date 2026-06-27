---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145463'
original_report_id: '145463'
title: 'Nextcloud server software: Content Spoofing'
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2016-06-17T16:31:11.824Z'
disclosed_at: '2016-07-19T10:30:00.935Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Nextcloud server software: Content Spoofing

## Metadata

- HackerOne Report ID: 145463
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2016-07-19T10:30:00.935Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

In Nextcloud the "dir" parameter is vulnerable to content spoofing attack.
If anyone puts a valid directory name in dir parameter then it goes that directory other wise it redirects
to the home directory (/)
By putting `../../` in dir parameter I was able to stop the redirect then I had put some messages after that and that messages reflected with the same given format.

So here an  attacker can send his messages directly through url.  
Poc link
`http://192.168.0.118/nextcloud/index.php/apps/files/?dir=../../Welcome+to+Nexcloud+You+can+get+pro+account+by+navigating+this+example.com`

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
