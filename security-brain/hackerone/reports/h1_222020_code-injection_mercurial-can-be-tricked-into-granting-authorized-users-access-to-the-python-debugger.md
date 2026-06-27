---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '222020'
original_report_id: '222020'
title: Mercurial can be tricked into granting authorized users access to the Python
  debugger
weakness: Code Injection
team_handle: ibb
created_at: '2017-04-18T21:08:41.575Z'
disclosed_at: '2017-07-12T14:35:50.100Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- code-injection
---

# Mercurial can be tricked into granting authorized users access to the Python debugger

## Metadata

- HackerOne Report ID: 222020
- Weakness: Code Injection
- Program: ibb
- Disclosed At: 2017-07-12T14:35:50.100Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I reported this bug privately to Mercurial and they produced an out of band release to fix the bug here:

https://www.mercurial-scm.org/wiki/WhatsNew#Mercurial_4.1.3_.282017-4-18.29

I produced a very detailed proof of concept with a Metasploit exploit module, which can be seen publicly here:

https://github.com/rapid7/metasploit-framework/pull/8263

The TLDR is that many services which host Mercurial servers often write their own hg-ssh wrapper or heavily customize the hg-ssh wrapper.  If the customized wrapped does not explicitly validate user input to the repo attribute, an attacker can supply a string of "--debugger", which causes the internal hg binary to drop to a Pdb shell, which allows arbitrary Python code execution.

I'm submitting to this program because I believe source code management software like git and mercurial is considered critical infrastructure for the Internet.

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
