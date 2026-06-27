---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223421'
original_report_id: '223421'
title: Open port leads to information disclosure
weakness: Information Disclosure
team_handle: weblate
created_at: '2017-04-24T12:25:25.022Z'
disclosed_at: '2018-09-10T09:40:40.291Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# Open port leads to information disclosure

## Metadata

- HackerOne Report ID: 223421
- Weakness: Information Disclosure
- Program: weblate
- Disclosed At: 2018-09-10T09:40:40.291Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Open port 10022 leads to disclosure of open-ssh version and current Debian version being used.

POC- 
1. I performed an nmap scan ( nmap -A -T4 -p- weblate.org)
2. I saw the port 10022 was open and I did a telnet connect to the port.
3. As soon as I did the telnet connect it returned me the openssh version and the debian version (check the .png file)
4.I wasn't able to run any sort of commands as whatever I typed returned a protocol mismatch error.


This doesn't necessarily mean a security issue as long as everything is being patched regularly.

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
