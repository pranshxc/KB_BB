---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '257335'
original_report_id: '257335'
title: 'ssh: unprivileged users may hijack due to backdated ssh version open port
  found(███.unikrn.com)'
weakness: Remote File Inclusion
team_handle: unikrn
created_at: '2017-08-07T09:27:13.968Z'
disclosed_at: '2019-03-04T12:45:50.856Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 54
asset_identifier: auctionbot.unikrn.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- remote-file-inclusion
---

# ssh: unprivileged users may hijack due to backdated ssh version open port found(███.unikrn.com)

## Metadata

- HackerOne Report ID: 257335
- Weakness: Remote File Inclusion
- Program: unikrn
- Disclosed At: 2019-03-04T12:45:50.856Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** Vulnerabilities in OpenSSH Session Hijacking Vulnerability is a Medium risk vulnerability that is one of the most frequently found on networks around the world. This issue has been around since at least 1990 but has proven either difficult to detect, difficult to resolve or prone to being overlooked entirely.

 

**Description:** You are running a version of OpenSSH which is older.

Versions prior than 7.5 or above are vulnerable to an off by one error
that allows local users to gain root access, and it may be
possible for remote users to similarly compromise the daemon
for remote access.

In addition, a vulnerable SSH client may be compromised by
connecting to a malicious SSH daemon that exploits this
vulnerability in the client code, thus compromising the
client system.An attacker may use this flaw to set up a brute force attack against
the remote host.
1. Session Hijacking
2.Remote file inclusion(high)
3.Brute force attack

## Steps To Reproduce:

Solution : Upgrade to OpenSSH 7.5 or apply the patch for
prior versions. 
(See: https://www.openssh.org)

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
