---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '136454'
original_report_id: '136454'
title: User credentials leak and arbitrary local file read/leak due to same-origin-policy
  violation
weakness: Information Disclosure
team_handle: ibb
created_at: '2016-05-05T12:20:49.997Z'
disclosed_at: '2019-11-12T09:41:37.845Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- information-disclosure
---

# User credentials leak and arbitrary local file read/leak due to same-origin-policy violation

## Metadata

- HackerOne Report ID: 136454
- Weakness: Information Disclosure
- Program: ibb
- Disclosed At: 2019-11-12T09:41:37.845Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Vulnerability details
=====================
A vulnerability exists in Flash Player that allows violating the same-origin-policy. An attacker can read sensitive local files and communicate with remote servers. As a result, this allows uploading the content of these local files to an attacker-controlled remote server. In addition, this vulnerability enables an attacker to obtain a user's Windows logon credentials.

On February 15, I submitted this vulnerability to Mozilla and Adobe.

On February 16, this vulnerability was confirmed by Jeromie Clark of Adobe.

On April 26, I received an update from Adobe PSIRT. To mitigate the vulnerability, Adobe will introduce a new feature in Flash Player that will further restrict local filesystem access. This feature will be enabled by default. Adobe expects this feature will be available in Flash Player in Fall 2016.

I understand it is customary issues are resolved and publicly acknowledged before submission to ibb-flash. However, as indicated above, a solution is not expected to arrive before Fall 2016. Considering this is a long time from now, I would like to ask whether my report can be considered for a bug bounty at this time.

Should you decide to take my report into consideration at this time, I can provide a full advisory, including working PoCs for every affected host environment.



Case IDs
--------
**Adobe**: PSIRT-5019
**Mozilla BMO**: 1248487 / ADBE 4118316

**References at Adobe familiar with this case**:
Jeromie Clark, <jeclark@adobe.com>
Peleus Uhley, <puhley@adobe.com>



Affected host browsers
----------------------
All current versions of:
- Firefox
- Chrome
- Internet Explorer (8 and up)
- Edge
- Microsoft Office 2010, 2013 and 2016



Tested with
-----------
- Flash Player 20.0.0.306 and up
- Windows XP, Windows 7, Windows 8.1, and Windows 10. All Windows and IE/Edge updates available to date were applied.

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
