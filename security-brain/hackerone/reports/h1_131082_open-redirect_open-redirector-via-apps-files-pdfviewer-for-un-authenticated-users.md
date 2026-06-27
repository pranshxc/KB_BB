---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '131082'
original_report_id: '131082'
title: Open Redirector via (apps/files_pdfviewer) for un-authenticated users.
weakness: Open Redirect
team_handle: owncloud
created_at: '2016-04-15T12:37:01.271Z'
disclosed_at: '2016-07-02T08:45:32.784Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- open-redirect
---

# Open Redirector via (apps/files_pdfviewer) for un-authenticated users.

## Metadata

- HackerOne Report ID: 131082
- Weakness: Open Redirect
- Program: owncloud
- Disclosed At: 2016-07-02T08:45:32.784Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Affected Products:  OWNCLOUD (https://demo.owncloud.org/index.php/apps/files_pdfviewer)
Version Tested: v1.0.712, other versions might be vulnerable
Class:	Open Redirector
Remote:	Yes

A non authenticated user can be easily tricked into following one of the following links in order to download a supposedly uploaded file on an owncloud instance:
The EvilFile the pdfviewer is trying to redirect will not load in the viewer automatically. But if the user clicks the download button on the right upper corner of the viewer any file will be downloaded instantly and the browser will be redirected to a different domain (ex. https://evildomain.xx ).

****OPEN REDIRECT Attack Replication Steps: 

Step 1: Visit https://demo.owncloud.org/index.php/apps/files_pdfviewer?file=https://evildomain.xx/EvilFile.xx [ Check POC1.jpg ]

Step 2: Click Download button on the right upper corner of the viewer.

Step 3: Browser is redirected to https://evildomain.xx/EvilFile.xx

Comment: No user authentication is required for the user to be redirected. All owncloud installations in the wild are vulnerable to this attack.


****Example Phishing Message with OPEN REDIRECT Attack:


Message:

Please view the files i have shared with you by following the link below, if this file is not automatically opened please click the download button on the right upper corner: 

https://demo.owncloud.org/index.php/apps/files_pdfviewer?file=https://evildomain.xx/remote.php/webdav/Demo.pdf%20%3CIf%20this%20file%20is%20not%20available%20please%20click%20the%20dowload%20button%20on%20the%20right%20upper%20corner%3E [ Check POC2.jpg ]

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
