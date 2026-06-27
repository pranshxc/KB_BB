---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '255627'
original_report_id: '255627'
title: SSH backdated version open port
weakness: Improper Restriction of Authentication Attempts
team_handle: wakatime
created_at: '2017-08-01T20:53:11.352Z'
disclosed_at: '2017-11-23T17:47:22.774Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# SSH backdated version open port

## Metadata

- HackerOne Report ID: 255627
- Weakness: Improper Restriction of Authentication Attempts
- Program: wakatime
- Disclosed At: 2017-11-23T17:47:22.774Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

You are running a version of OpenSSH which is older than 6.7

Versions prior than 6.7 are vulnerable to an off by one error
that allows local users to gain root access, and it may be
possible for remote users to similarly compromise the daemon
for remote access.

In addition, a vulnerable SSH client may be compromised by
connecting to a malicious SSH daemon that exploits this
vulnerability in the client code, thus compromising the
client system.An attacker may use this flaw to set up a brute force attack against
the remote host.

Solution : Upgrade to OpenSSH 6.7 or apply the patch for
prior versions. (See: https://www.openssh.org)

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
