---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '21064'
original_report_id: '21064'
title: Back - Refresh - Attack To  Obtain User Credentials
weakness: Information Disclosure
team_handle: phabricator
created_at: '2014-07-22T18:14:57.958Z'
disclosed_at: '2014-07-23T16:40:23.459Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Back - Refresh - Attack To  Obtain User Credentials

## Metadata

- HackerOne Report ID: 21064
- Weakness: Information Disclosure
- Program: phabricator
- Disclosed At: 2014-07-23T16:40:23.459Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Back - refresh attack is attack which enables an adversary to obtain application credentials by going by to previous page and re-submitting the expired-document.

How to perform:
1. Register to https://<some-site>/auth/register/
2. Once registered, press "Back" on the browser window. Now you'll see the "Document Expired" page.
3. Now run an interceptor (burp/tamper data)
4. Click "Tray again" on the web page
5. Click "Re-send data"
6. Watch the intercepted request.

You'll observe that login credentials both email and passwords being resubmitted by browser get captured.

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
