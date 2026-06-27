---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '721333'
original_report_id: '721333'
title: Buffer Overflow in smblib.c
weakness: Classic Buffer Overflow
team_handle: ibb
created_at: '2019-10-23T19:42:43.059Z'
disclosed_at: '2021-07-28T23:54:29.293Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- classic-buffer-overflow
---

# Buffer Overflow in smblib.c

## Metadata

- HackerOne Report ID: 721333
- Weakness: Classic Buffer Overflow
- Program: ibb
- Disclosed At: 2021-07-28T23:54:29.293Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

In Squid 4.8, a local buffer overflow vulnerability exists in the 
Smb_Connect() and Smb_Connect_Server() functions of Squid's smblib.c, in which an attacker can achieve code execution that can result in the disclosure of credential hashes. The cause of this overflow is due to the SMB domain controller names being passed down from user input and eventually into an array without performing appropriate bounds checking on said array.

I submitted a patch, which was accepted and merged, which can be found here: 
https://github.com/squid-cache/squid/pull/494

## Disclosure Timeline
15/10/19 - Initial discovery and disclosure to the Squid team via squid-bugs private email list
16/10/19 - Acknowledgement of the vulnerability by the Squid team
17/10/19 - I volunteered to fix the issue, and create a pull request on Github (See above link)
17-19/10/19 - The fix was reviewed, accepted, then merged (Fix is also backported to older Squid Versions)
23/10/19 - CVE-2019-18353 assigned

## To Note
Due to the fact that this is a local (as opposed to remote) overflow, and used primarily by squid auth helpers for downgrading (As pointed out by a member of the squid team when he said an advisory would not be released because of the 'nature' of what the squid helpers are doing); I am setting the severity as medium and not expectant for a bounty.

## Impact

Code execution resulting in the retrieval of credential hashes

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
