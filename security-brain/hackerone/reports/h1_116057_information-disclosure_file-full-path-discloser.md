---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '116057'
original_report_id: '116057'
title: file full path discloser.
weakness: Information Disclosure
team_handle: paragonie
created_at: '2016-02-12T08:36:00.027Z'
disclosed_at: '2016-06-17T01:58:31.673Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# file full path discloser.

## Metadata

- HackerOne Report ID: 116057
- Weakness: Information Disclosure
- Program: paragonie
- Disclosed At: 2016-06-17T01:58:31.673Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,
Paragonie security team i found one directory browsing vulnerability in php-encryption-master where the user input will not been filtered from any security layer.
let me show you.
there is a autoload.php page in the php-encryption-master. where the input src will b used to browse the directory so this input will not been tested and fetch the file from directory and return to user.
this attack will highly affect your product and may invite for other attack to.

so i hope you will protch it as soon as possible.

thank you,
security researcher,
lucky sen

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
