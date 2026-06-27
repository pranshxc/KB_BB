---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '87854'
original_report_id: '87854'
title: XSS on vimeo.com/home after other user follows you
weakness: Cross-site Scripting (XSS) - Generic
team_handle: vimeo
created_at: '2015-09-07T13:43:25.171Z'
disclosed_at: '2017-08-31T10:25:58.730Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS on vimeo.com/home after other user follows you

## Metadata

- HackerOne Report ID: 87854
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: vimeo
- Disclosed At: 2017-08-31T10:25:58.730Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

__Description__

If some user follows you on Vimeo, the Name of the user appears in the header of your Home like "[Name] followed you. The staff posted...".
The problem is that the Name is not escaped, which allows to insert HTML code.

__Proof of concept__

1. Using the attacker's account, go to https://vimeo.com/settings.
2. Change the _Name_ to `<script src=//u00f1.xyz>`.
3. Click on _Save Changes_.
4. Go to the victim's Profile.
5. Click on _Follow_ (is at the bottom of the profile picture).
6. Using the victim's account, go to https://vimeo.com/home.
7. https://u00f1.xyz is loaded and `alert(document.domain)` is executed.

I attached a screen capture to identify where the Name of the attacker appears. In this case I used an `<img>` as the Name of the attacker, you can notice the broken image.

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
