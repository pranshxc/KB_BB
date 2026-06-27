---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '43617'
original_report_id: '43617'
title: Adding profile picture to anyone on Vimeo
weakness: Violation of Secure Design Principles
team_handle: vimeo
created_at: '2015-01-13T21:59:05.483Z'
disclosed_at: '2015-02-26T10:35:21.064Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- violation-of-secure-design-principles
---

# Adding profile picture to anyone on Vimeo

## Metadata

- HackerOne Report ID: 43617
- Weakness: Violation of Secure Design Principles
- Program: vimeo
- Disclosed At: 2015-02-26T10:35:21.064Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi!

**Brief**
The profile picture upload feature at https://vimeo.com/settings/profile contains a bug where an access control is missing for uploading a profile picture to a profile ID. This leads to the possibility of uploading a profile picture to any account on Vimeo. Furthermore, since the upload doesn't have any rate limiting, it would in theory be possible to add a picture to every Vimeo account that exists (since the profile IDs are incremental).

**PoC**
1. Set up an intercepting proxy so that you can edit requests/responses to Vimeo
2. Visit https://vimeo.com/settings/profile
3. Click the "Upload" button
4. Choose any image
5. If you did everything correct, your browser should now send a request to /upload/_get_image_url with 2 post parameters. One of them is called "id". Change this id to another profile id then forward the request.
6. Your uploaded picture is now added to the other profile!

**Remediation**
The profile picture upload function should only work for the currently logged in users profile ID.

Mathias

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
