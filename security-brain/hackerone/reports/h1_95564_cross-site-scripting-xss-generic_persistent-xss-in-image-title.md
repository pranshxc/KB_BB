---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '95564'
original_report_id: '95564'
title: Persistent XSS in image title
weakness: Cross-site Scripting (XSS) - Generic
team_handle: imgur
created_at: '2015-10-24T09:05:04.072Z'
disclosed_at: '2016-03-31T15:12:01.486Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Persistent XSS in image title

## Metadata

- HackerOne Report ID: 95564
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: imgur
- Disclosed At: 2016-03-31T15:12:01.486Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When adding a title to uploaded images, one can insert XSS into the title which is then executed for anyone viewing the image.

PoC (contains a harmless XSS):
http://imgur.com/bSZwUBG&rAmpN4O

How to recreate:
1. Open the Image Options page for an album.
2. Press "Add Title / Description"
3. Enter some HTML into the title field. In my PoC, I used the following: <marquee><font size=72>XSS
4. Save. You are now redirected to the Image Options page, where the XSS is evaluated by the browser.

This XSS is persistent and will execute for anyone who visits the URL, in this case http://imgur.com/bSZwUBG&rAmpN4O

Images from steps 2, 3 and 4 attached.

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
