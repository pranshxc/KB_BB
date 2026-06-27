---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1074930'
original_report_id: '1074930'
title: Keybase /AppData/Local/Keybase/uploadtemps folder stores pasted photos
weakness: Cleartext Storage of Sensitive Information
team_handle: keybase
created_at: '2021-01-09T08:06:25.483Z'
disclosed_at: '2021-02-22T16:19:04.371Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Keybase /AppData/Local/Keybase/uploadtemps folder stores pasted photos

## Metadata

- HackerOne Report ID: 1074930
- Weakness: Cleartext Storage of Sensitive Information
- Program: keybase
- Disclosed At: 2021-02-22T16:19:04.371Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

During research, I had noticed that Keybase does not adequately clear the cache and some residual files can be viewed, with no form of encryption on the files. In addition, these pasted photos remain even after clearing the containing chat. Not all of the pasted photos remain, so it's unclear what makes some stay within the cache while others are effectively cleared.

I haven't seen any CVE identifier, so I have requested a CVE-ID from MITRE.

**Replication**
1. On a Windows machine, navigate to C:\Users\yourusername\AppData\Local\Keybase\uploadtemps
2. Note that some directories remain and that inside of the directories, you may find that some files are here, particularly image pastes.
F1150615
F1150618

## Impact

This is problematic because Keybase is supposed to be privacy centric. An attacker that gains access to a victim machine can potentially obtain sensitive data through through gathered photos, especially if the user utilizes Keybase frequently. A user, believing that they are sending photos that can be cleared later, may not realize that occasionally pasted photos are not cleared from the cache and may send photos of credentials, etc, to friends or may even send other sensitive data. The photos then can be stored insecurely on a case-by-case basis.

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
