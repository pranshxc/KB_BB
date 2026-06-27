---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '874107'
original_report_id: '874107'
title: '[my.games] Stored XSS via untrusted bucket'
weakness: Cross-site Scripting (XSS) - Stored
team_handle: mailru
created_at: '2020-05-14T11:37:28.792Z'
disclosed_at: '2020-06-04T16:10:16.616Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: MY.GAMES
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# [my.games] Stored XSS via untrusted bucket

## Metadata

- HackerOne Report ID: 874107
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: mailru
- Disclosed At: 2020-06-04T16:10:16.616Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Domain, site, application
--
https://my.games/

Details
--
If you check page source of https://my.games, you can notice that site gets static files (scripts, styles, images) using following URL declaration:
https://my.games/hotbox/mygames/frontend/v3-6-13/img/share/main.png

**mygames** here is a name of S3 bucket.
After creating own S3 bucket in AWS and using https://my.games/hotbox/BUCKET_NAME/, I got "NoSuchBucket" error.

But my comrade investigated, that *hotbox* is one of the available types of S3 bucket in MCS.

...

Preconditions
--
1) Create your S3 bucket at https://mcs.mail.ru/app/services/storage/buckets/.
2) Upload any malicious file (e.g. HTML page).
3) Make this file public.

Steps to reproduce
--
1)  Open following link in browser:
https://my.games/hotbox/YOUR_BUCKET_NAME/YOUR_FILE_NAME

PoC, exploit code, screenshots, video, references, additional resources
--
https://my.games/hotbox/foobar1337/oops.html
{F828044}

## Impact

An attacker can host any malicious file on **my.games** domain.

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
