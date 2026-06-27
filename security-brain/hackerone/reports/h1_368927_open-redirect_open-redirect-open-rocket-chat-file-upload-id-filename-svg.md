---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '368927'
original_report_id: '368927'
title: Open redirect open.rocket.chat/file-upload/ID/filename.svg
weakness: Open Redirect
team_handle: rocket_chat
created_at: '2018-06-19T17:04:38.639Z'
disclosed_at: '2019-10-31T15:20:30.348Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- open-redirect
---

# Open redirect open.rocket.chat/file-upload/ID/filename.svg

## Metadata

- HackerOne Report ID: 368927
- Weakness: Open Redirect
- Program: rocket_chat
- Disclosed At: 2019-10-31T15:20:30.348Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** Open redirect through svg file upload

**Description:** When you upload a file to a chat, the link to it will look like https://open.rocket.chat/file-upload/ID/filename.svg, but the file will be on storage.googleapis.com.
We can embed js in our svg and when the victim goes to https://open.rocket.chat/file-upload/6ksXL2Mk4MonCcTpx/svgxss.svg, a redirect to the phishing site will occur, or any other js, for example, downloading the virus, will work.
I see you have forbidden downloading html, shtml and php file, I recommend you also prohibit svg, since it is also dangerous.

  1. Upload svg file in any chat (attached to the report)
  2. Go to open.rocket.chat/file-upload/ID/filename.svg.

**PoC:** https://open.rocket.chat/file-upload/6ksXL2Mk4MonCcTpx/svgxss.svg

## Impact

open redirect

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
