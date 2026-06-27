---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '122113'
original_report_id: '122113'
title: OpenSSH / dropbearSSHd xauth command injection
weakness: Privilege Escalation
team_handle: ibb
created_at: '2016-03-10T17:49:34.074Z'
disclosed_at: '2019-11-12T09:45:23.558Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- privilege-escalation
---

# OpenSSH / dropbearSSHd xauth command injection

## Metadata

- HackerOne Report ID: 122113
- Weakness: Privilege Escalation
- Program: ibb
- Disclosed At: 2019-11-12T09:45:23.558Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

* OpenSSH 
 * affects all version <= 7.2p1 with `X11Forwarding yes` (acc. to OpenSSH this bug is 20 years old and affects all versions back to openssh v1)
 * status: fixed, vendor advisory: http://www.openssh.com/txt/x11fwd.adv
* dropbearSSHd
 * affects <= 2015.71 (basically all versions that come with x11 support; dates back 12 years [1])
 * status: fixed, vendor info: https://matt.ucc.asn.au/dropbear/CHANGES
* other
 * mobaSSH; they're just based on openssh but for windows - mobassh.mobatek.net

allows to bypass ssh-forced-commands and login-shell restrictions (/bin/false, specific binary) by injecting xauth commands. The latter only affects OpenSSH. Capabilities: arbitr. file read/write, info disclosure (xauth env. info), initiate outbound X connections

reported to OpenSSH first, provided detailed vulnerability analysis, PoC and a simple patch. OpenSSH kindly coordinated patch and release with dropbearSSHd. fixed within a few days (first contact march 3rd. coordinated release with dropbear 10th)

details and the actual research material that was securely disclosed to OpenSSH will be pushed to the following repo (note this llink is subject to change once there's a cve assigned for that issue):
https://github.com/tintinweb/pub/tree/master/pocs/cve-2016-xxxx-openssh-dropbearsshd

[1] https://github.com/mkj/dropbear/blob/790726519e69f5d93b579a21951d78f8f777a5cb/svr-x11fwd.c

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
