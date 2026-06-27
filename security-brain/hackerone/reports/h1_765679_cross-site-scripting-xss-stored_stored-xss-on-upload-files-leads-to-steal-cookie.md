---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '765679'
original_report_id: '765679'
title: Stored XSS on upload files leads to steal cookie
weakness: Cross-site Scripting (XSS) - Stored
team_handle: palo_alto_software
created_at: '2019-12-29T07:39:05.231Z'
disclosed_at: '2020-04-18T12:39:36.397Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 56
asset_identifier: app.outpost.co
asset_type: URL
max_severity: none
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS on upload files leads to steal cookie

## Metadata

- HackerOne Report ID: 765679
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: palo_alto_software
- Disclosed At: 2020-04-18T12:39:36.397Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
There isn't a check mechanism on file format in Inbox which an attacker can send an SVG file as other formats such as png, gif or bmp by rename and change file format leads XSS attack and steal victim cookies.

## Steps To Reproduce:
You should create 2 accounts :
First account for the attacker and second one for the victim.

The attacker in my scenario: seq@seq.teamoutpost.com
The victim in my scenario: seq1@seq1.teamoutpost.com

  1. Please log in to the first account via this [link] (https://app.outpost.co/sign-in) 
  1. From Inbox create New Conversation and attached following files (Attached on this report) and send 
       These files are an SVG file which changes file format to png, bmp, gif
       If you want to see payload open file by notepad. you'll see payload like the following code :

```
<svg version="1.0" xmlns="http://www.w3.org/2000/svg"
 width="2560.000000pt" height="1600.000000pt" viewBox="0 0 2560.000000 1600.000000"
 preserveAspectRatio="xMidYMid meet" onload="alert(document.cookie)">
```
  1. Whenever victim clicks on each file, open a new tab and XSS attack occurs and steal the victim's cookie.

## Supporting Material/References:

Browsers :
Mozilla Firefox 71.0
Google Chrome 79.0.3945.88

  * [attachment / reference]

For clarification, you can watch POC file (Attached on this report)

If you have any questions, let me know.

Best regards.

## Impact

Attacker can send malicious files to victims and steals victim's cookie leads to account takeover.

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
