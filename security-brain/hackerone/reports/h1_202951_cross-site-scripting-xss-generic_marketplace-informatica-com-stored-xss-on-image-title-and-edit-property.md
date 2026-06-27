---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '202951'
original_report_id: '202951'
title: '[marketplace.informatica.com]- Stored XSS on Image title and Edit Property'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: informatica
created_at: '2017-02-02T17:08:00.847Z'
disclosed_at: '2017-04-21T12:06:39.594Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [marketplace.informatica.com]- Stored XSS on Image title and Edit Property

## Metadata

- HackerOne Report ID: 202951
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: informatica
- Disclosed At: 2017-04-21T12:06:39.594Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

By uploading and image with the title of ``` "><svg onload=alert(1)>.jpg``` and allowing anyone to edit the Document under collaboration settings, XSS can be triggered by any user attempting to edit the document.

 POC
====
1.  Log into marketplace and go to profile page.  Select New > Document
2.  Choose to upload document and browse to your image with the javascript payload as the name.
3.  Enter anything as Description and and tags field
4.  Select visibility open to anyone
5. Expand collaboration options and allow anyone to edit document. (This drastically increases security issue.)
6. Choose to publish
7. After publishing choose to Edit Document from the right hand menu and observe XSS.

Please see accompanying screenshots as POC

### Please let me know if you need any more information. Cheers!

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
