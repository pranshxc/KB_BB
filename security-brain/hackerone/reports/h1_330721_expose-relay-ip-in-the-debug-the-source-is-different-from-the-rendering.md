---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '330721'
original_report_id: '330721'
title: Expose relay IP in the debug (The source is different from the rendering)
team_handle: torproject
created_at: '2018-03-28T10:22:07.534Z'
disclosed_at: '2018-07-21T17:57:04.911Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 7
tags:
- hackerone
---

# Expose relay IP in the debug (The source is different from the rendering)

## Metadata

- HackerOne Report ID: 330721
- Weakness: 
- Program: torproject
- Disclosed At: 2018-07-21T17:57:04.911Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Greetings,
--

I observed that it was possible to expose the ip of  a relay by doing this :

Poc :
--

- Go to https://sorry.google.com/sorry/misc/
- You must observe this visual.

{F279451}

- Open Tor Browser debug
- You must observe this visual 

{F279452}

Note :
--

You observe that between the debug and the main window there is no relation between the rendered text and the source code. The text discloses the IP of the client while the source discloses the IP of the relay.

Best regards 

@Rbcafe

## Impact

- Get the IP of the relay by changing the ip of the client.

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
