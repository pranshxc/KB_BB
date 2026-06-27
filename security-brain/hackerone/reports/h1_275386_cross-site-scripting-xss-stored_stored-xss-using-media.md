---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '275386'
original_report_id: '275386'
title: Stored XSS Using Media
weakness: Cross-site Scripting (XSS) - Stored
team_handle: automattic
created_at: '2017-10-07T20:24:21.652Z'
disclosed_at: '2017-11-26T20:42:04.020Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS Using Media

## Metadata

- HackerOne Report ID: 275386
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: automattic
- Disclosed At: 2017-11-26T20:42:04.020Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Summary:
This exploits an XSS vulnerability on polldaddy.com

Steps to Reproduce:
1. Create a multiple-choice question quiz on Polldaddy
2. Insert stored XSS payload into Media Embed such that it matches the shortcode format
   Payload: [<img src="http://url.to.file.which/not.exist" onerror=alert("Hello!");>]
3. When someone goes on the quiz page through the quiz share link, the payload will execute. 

Proof of Concept (30-second video):
https://drive.google.com/file/d/0B_lsH7QMy9DkQnV5a3hHa05lSmM/view

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
