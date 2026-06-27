---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1425'
original_report_id: '1425'
title: SSL Not Enforced
team_handle: secret
created_at: '2014-02-14T02:16:57.796Z'
disclosed_at: '2014-03-16T09:02:27.811Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
---

# SSL Not Enforced

## Metadata

- HackerOne Report ID: 1425
- Weakness: 
- Program: secret
- Disclosed At: 2014-03-16T09:02:27.811Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Although by default, all the communication in the Secret web app happens over HTTPS, if this is changed to HTTP, the requests are still normally processed. 

For example, the request to send a download link to a phone number can be as simple as
POST /_/send-download-link HTTP/1.1
Host: www.secret.ly

{"PhoneNumber":"xxxxxxxxxx"}

The above request is sent to the target www.secret.ly over HTTP. This is successfully processed and the phone number in question gets a link to download the application.

Not to mention, an attacker can automate this and spam users sending them links to download this app even if they are not interested. There is also no controlling factor to stop the spam. This might be considered a totally different issue but I am reporting it together with this.

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
