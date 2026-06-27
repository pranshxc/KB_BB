---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '265050'
original_report_id: '265050'
title: Blind SSRF in emblem editor (2)
weakness: Server-Side Request Forgery (SSRF)
team_handle: rockstargames
created_at: '2017-08-31T19:38:53.911Z'
disclosed_at: '2017-10-28T23:44:08.493Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 73
asset_identifier: socialclub.rockstargames.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Blind SSRF in emblem editor (2)

## Metadata

- HackerOne Report ID: 265050
- Weakness: Server-Side Request Forgery (SSRF)
- Program: rockstargames
- Disclosed At: 2017-10-28T23:44:08.493Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

As per your recommendation in #233301, I'm submitting a PoC for another blind SSRF in the emblem editor.

To oversight here is allowing absolute `url()` values for the `fill` attribute:

`<path fill="url(https://requestb.in/15rxmgv1#test)" stroke="#a1a1a1"  ... `

Upon publishing an emblem containing such an element, a HTTP request to the given URL is sent from a Rockstar server. (`███`). The destination port can be easily modified. This doesn't seem to work without including a fragment in the URL (`#test` in the example above).

Further testing showed that, if a valid SVG is found at the given URL, the `fill` data is actually used in the final image. Fortunately, ████████ doesn't seem to support scripts, although the possibility of finding another way to exfiltrate data doesn't seem that out of reach.

I've attached the full body of the emblem I've used to confirm this bug for ease of reproduction.

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
