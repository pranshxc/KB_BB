---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '15362'
original_report_id: '15362'
title: Flash Sandbox Bypass
weakness: Information Disclosure
team_handle: ibb
created_at: '2014-06-06T18:39:15.242Z'
disclosed_at: '2014-06-19T18:07:45.941Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- information-disclosure
---

# Flash Sandbox Bypass

## Metadata

- HackerOne Report ID: 15362
- Weakness: Information Disclosure
- Program: ibb
- Disclosed At: 2014-06-19T18:07:45.941Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Adobe Flash Player issue 2719 and 2720.
Exploit of this bug uses 2 separate vulnerabilities. 
2720 is a bug which is able to, from the local-with-file sandbox, (default local sandbox), open both local and remote files, (local files and http/https resources). An attacker could for example read your email, or simply retrieve a local password store/cookies etc. After retrieving the desired data/file it can exfiltrate it out of the local-sandbox to a remote recourse (server from the attacker) using the same vector.

2719 is a vulnerability which can mount a Flash applet from a http:// or https:// origin in the local-with-file-sandbox  mode, which is normally only used for files opened locally on the users file-system. Due to this issue the other 2720 vulnerability can be linked in such a way that it is remotely exploitable.

By mounting 2719 before 2720 the user does not have to download anything, accept anything.
The vulnerability requires no additional user interaction, simply visiting the site prepared to serve the exploit is enough.

These vulnerabilities are already reported  to Adobe and will be patched next week's patch Tuesday (June 10). The CVE number assigned to the combination of these issues is CVE-2014-0535.

The link below is a  video demonstration of the proof of concept:
https://www.youtube.com/watch?v=EjXPAwBt_J4

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
