---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '20873'
original_report_id: '20873'
title: rsync hash collisions may allow an attacker to corrupt or modify files
weakness: Cryptographic Issues - Generic
team_handle: ibb
created_at: '2014-07-20T22:42:52.832Z'
disclosed_at: '2014-11-17T23:54:19.088Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- cryptographic-issues-generic
---

# rsync hash collisions may allow an attacker to corrupt or modify files

## Metadata

- HackerOne Report ID: 20873
- Weakness: Cryptographic Issues - Generic
- Program: ibb
- Disclosed At: 2014-11-17T23:54:19.088Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The rsync algorithm synchronizes remote files in 3 steps:
- The receiver divides the basis file into 700-byte blocks, performing two checksums on each block (a rolling checksum based on Addler32) and an md5 sum
- The sender then scans it's version of the file byte-by-byte looking for matches against both sums, transmitting either literal data, or a copy command (copy offset length)
- The receiver makes a copy of the file by applying the delta commands from the sender

While it is known that md5 doesn't offer much collision resistance, it is perhaps unknown that the fast md5 collisions can be combined with a collision against the rolling sum.  They can.

For files where all of the data is in the same privilege domain, this may allow bypassing validation rules.

More critically, for files where data for the system and other users is mixed with untrusted data (VM images, databases), this could allow privilege escalation.

There are two different classes of attack on md5 - collisions and chosen-prefix collisions:
- Collisions are very quick to generate on a normal PC, but require a fully crafted file to work (the original demo was a postscript file).  This is what I have attached.
- Chosen-prefix attacks are more serious, but require more work to generate (approx 2^50) - I do not have an example of one of these yet.

Also note that rsync does a final full-file hash, which will fail.  This reduces this to just a DoS attack unless --inplace is used (common for syncing large files).

Since rsync is used for mirroring large open-source projects, and is used in the background for many open source, closed-source and in-house systems, I believe this may qualify for an internet bug bounty.

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
