---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '27651'
original_report_id: '27651'
title: Flash Local Sandbox Bypass
weakness: Information Disclosure
team_handle: ibb
created_at: '2014-09-09T20:51:19.206Z'
disclosed_at: '2014-10-07T22:55:38.832Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- information-disclosure
---

# Flash Local Sandbox Bypass

## Metadata

- HackerOne Report ID: 27651
- Weakness: Information Disclosure
- Program: ibb
- Disclosed At: 2014-10-07T22:55:38.832Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Vulnerability already reported to adobe (issue 2833) and patched (CVE-2014-0554)

http://helpx.adobe.com/security/products/flash-player/apsb14-21.html

First of all, note that the Adobe Security Bulletin notes: 'Bas Venis and Masato Kinugawa' for the acknowledgement of this CVE. The poc I have reported to Adobe was my own work.

My poc (issue 2833) exploited a security vulnerability which enabled an attacker to read files on the user's local disk. Adobe's patch involved adding a user confirmation step when navigating the page with navigateToURL. Although this doesn't really fix the underlying cause of this issue. It does provide a pretty solid protection to a whole plethora of exploits using the same kind of attack vector (relying on network requests to transfer data). My exploit could only leak a small amount of the targeted data per request, and thus required lots of requests to be made (poc implemented this in parallel, using iframes and a script to reconstruct the pieces into the original data.) 

Before this patch this was a realistic attack vector. But it is unlikely the user will accept 10 confirmation dialogs per second, without suspecting malicious intent. This pretty much protects the user from this and other similar vectors.

I haven't talked to Masato's about his research on this. It is most likely that his reported vulnerability also relies on network requests/page navigation, and thus mitigated with this patch. But I doubt his technique was the same.

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
