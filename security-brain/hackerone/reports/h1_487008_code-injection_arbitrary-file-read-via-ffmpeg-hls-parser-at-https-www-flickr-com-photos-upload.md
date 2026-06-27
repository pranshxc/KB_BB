---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '487008'
original_report_id: '487008'
title: Arbitrary file read via ffmpeg HLS parser at https://www.flickr.com/photos/upload
weakness: Code Injection
team_handle: flickr
created_at: '2019-01-27T21:25:51.237Z'
disclosed_at: '2020-01-25T00:03:06.058Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 336
asset_identifier: '*.flickr.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- code-injection
---

# Arbitrary file read via ffmpeg HLS parser at https://www.flickr.com/photos/upload

## Metadata

- HackerOne Report ID: 487008
- Weakness: Code Injection
- Program: flickr
- Disclosed At: 2020-01-25T00:03:06.058Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary: FFmpeg is a video and audio software that is used for generating previews and for converting videos. Your current installation allows HLS playlists that contain references to external files, which leads to local file disclosure.


Steps to Reproduce:
1.Download the attached file. {F413554}

2.Go to https://www.flickr.com/photos/upload/ and upload the attached file.

3.Now go to https://www.flickr.com/cameraroll and you should be able to see contents of /etc/passwd. {F413555}
For clear view open the video from **Photostream** section.

Please let me know if you need any help :)

## Impact

An attacker can read files of etc/passwd or other contents.Also what I've seen it is possible to escalate this vulnerability to SSRF(https://www.blackhat.com/docs/us-16/materials/us-16-Ermishkin-Viral-Video-Exploiting-Ssrf-In-Video-Converters.pdf).Since I don't have any server I couldn't test :(

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
