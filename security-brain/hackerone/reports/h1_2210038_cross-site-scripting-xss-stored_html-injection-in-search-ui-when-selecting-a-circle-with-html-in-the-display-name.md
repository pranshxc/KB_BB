---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2210038'
original_report_id: '2210038'
title: HTML injection in search UI when selecting a circle with HTML in the display
  name
weakness: Cross-site Scripting (XSS) - Stored
team_handle: nextcloud
created_at: '2023-10-15T21:41:08.844Z'
disclosed_at: '2023-11-21T09:22:07.279Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: nextcloud/circles
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# HTML injection in search UI when selecting a circle with HTML in the display name

## Metadata

- HackerOne Report ID: 2210038
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: nextcloud
- Disclosed At: 2023-11-21T09:22:07.279Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

HTML injection is a web security issue where attackers insert harmful code into a web application, affecting how it appears and functions. This can lead to data theft, phishing, malware distribution, and session hijacking, posing significant risks to users and the application's integrity. Prevention involves thoroughly checking and encoding user-generated content to ensure it's safe for rendering in web pages.

Reproduction Steps: 

1. Log in to the application using a low-privilege user account.
2. Access the "Contacts" section and initiate the creation of a new Circle.
3. When naming the Circle, insert the following payload: ``<meta http-equiv="refresh" content="2; https://evil.com/" />``.
4. Share the Circle with a user account having an "Admin" role.
5. Switch to the "Admin" user role and go to "Files" > "Shared with Circles."
6. Observe that the browser will redirect to a malicious website within a 2-second timeframe.

Video POC : 
{F2775888}

## Impact

HTML injection can have significant impacts, including:

Data theft
Phishing attacks
Malware distribution
Session hijacking
These consequences can harm both users and the application's security.

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
