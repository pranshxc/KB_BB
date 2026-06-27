---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '54094'
original_report_id: '54094'
title: HTTP MitM on Flash Player settings manager allows attacker to set sandbox settings
team_handle: ibb
created_at: '2015-03-31T20:55:29.703Z'
disclosed_at: '2018-12-23T21:09:32.056Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
---

# HTTP MitM on Flash Player settings manager allows attacker to set sandbox settings

## Metadata

- HackerOne Report ID: 54094
- Weakness: 
- Program: ibb
- Disclosed At: 2018-12-23T21:09:32.056Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This vulnerability is present in both Google Chrome's PepperFlash aswell as browsers
with the NPAPI Flash Player versions.

It works by MITM'ing the Flashplayer settings manager.
Although this settings manager is served over HTTPS, it is still
possible to place or edit the local settings cookie by serving it over
HTTP over the corresponding path. 

This leads to the attacker being able to edit several sandbox settings, for example, the attacker can:
  -Give the domain/payload permanent access to webcam/microphone,
  -Permanently exempt the domain/payload from any CORS Policy restrictions
  -Effectively disable auto updates (NPAPI versions) by setting the auto-update interval to ~9999 days

For this, an attacker would only need access to the HTTP communication
of the victims network. Either embedding the remote SWF in the attackers own site, or injecting the embed code in other HTTP traffic from the victim.

The POC was peformed against Google Chrome 41.0.2272.101 (PPAPI 17.0.0.134) on Windows 8.1
MITMProxy (https://mitmproxy.org/) was used to serve the altered SWF (Without using HTTPS/Certificate modes).

This attack is demonstrated in this video: https://www.youtube.com/watch?v=2Q52q_kZtTc (unlisted)

This issue is reported to Adobe, I am currently awaiting a response from their PSIRT.

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
