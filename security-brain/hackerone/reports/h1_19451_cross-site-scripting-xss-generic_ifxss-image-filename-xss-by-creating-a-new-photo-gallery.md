---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '19451'
original_report_id: '19451'
title: IFXSS (image filename XSS) by creating a new Photo Gallery
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uzbey
created_at: '2014-07-08T22:15:28.117Z'
disclosed_at: '2014-07-23T15:37:23.628Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# IFXSS (image filename XSS) by creating a new Photo Gallery

## Metadata

- HackerOne Report ID: 19451
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uzbey
- Disclosed At: 2014-07-23T15:37:23.628Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello team! I think I've found a Stored XSS in the Photo Gallery. To reprodruce the possible vulnerability we must:
1. Login into our account.
2. Go to https://staging.uzbey.com/user/other-albums and click on the "add new album" button.
3.  Add random values and any image with this name ---> "onerror="alert(1)"a=".jpg
4. Publish your gallery.
5. XSS! 
Also, if you click on the image error icon you will obtain the alert.
I will attach a few images as a little help for understand my Proof of Concept of the vulnerability.
 Kind regards.

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
