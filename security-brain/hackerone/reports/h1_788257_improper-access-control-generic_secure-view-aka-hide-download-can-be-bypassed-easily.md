---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '788257'
original_report_id: '788257'
title: '"Secure View" aka "Hide Download" can be bypassed easily'
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2020-02-03T13:18:19.732Z'
disclosed_at: '2020-04-10T09:12:36.773Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 20
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# "Secure View" aka "Hide Download" can be bypassed easily

## Metadata

- HackerOne Report ID: 788257
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2020-04-10T09:12:36.773Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The mid-2019 announced feature "Secure view" (https://nextcloud.com/blog/secure-view-prevent-your-shared-files-from-getting-downloaded/) allows for hiding the Download button on public shares.
Even though the announcement admits that there are always workarounds out there to get hands on the file anyway, the workaround for this one is way too simple: Just add **/download** to the URL (like you used to for every public share) and your browser starts downloading unhesitently.

For the sharee, the checkbox "Hide Download" is therefore very deceptive, since they very likely weigh themselves in false safety.

## Impact

Download a copy of a file or folder that's not supposed to be downloaded whatsoever

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
