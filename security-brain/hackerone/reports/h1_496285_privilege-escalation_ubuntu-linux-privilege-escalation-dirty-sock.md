---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '496285'
original_report_id: '496285'
title: Ubuntu Linux privilege escalation (dirty_sock)
weakness: Privilege Escalation
team_handle: ibb
created_at: '2019-02-14T22:15:46.992Z'
disclosed_at: '2019-08-28T01:49:16.747Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 101
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- privilege-escalation
---

# Ubuntu Linux privilege escalation (dirty_sock)

## Metadata

- HackerOne Report ID: 496285
- Weakness: Privilege Escalation
- Program: ibb
- Disclosed At: 2019-08-28T01:49:16.747Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team,
This week, I have publicly disclosed the dirty_sock local root exploit affecting multiple Linux Operating Systems.

Very detailed information on the vulnerability can be found in my blog posting [here](https://initblog.com/2019/dirty-sock/).

And the exploit code can be found in my GitHub repository [here](https://github.com/initstring/dirty_sock).

The vulnerability exists in stock versions of Ubuntu Linux due to the default inclusion of the snapd service, but all Linux distributions are vulnerable if they install the package. The disclosure was handled directly with Canonical via the bug tracked [here](https://bugs.launchpad.net/snapd/+bug/1813365).

A large percentage of the Internet is safer today than it was a week ago, due to the amazing response by the team at Canonical.

## Impact

Linux relies on a functioning security model, particularly in environments shared by multiple users. The ability of any user to obtain immediate root access completely breaks this model, putting sensitive data all around the world at risk of exposure.

The exploits provided allow any user to immediately elevate to a root account.

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
