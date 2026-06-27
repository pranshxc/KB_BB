---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '151847'
original_report_id: '151847'
title: The application uses basic authentication.
weakness: Improper Authentication - Generic
team_handle: nextcloud
created_at: '2016-07-17T00:23:47.250Z'
disclosed_at: '2016-07-18T19:53:39.463Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# The application uses basic authentication.

## Metadata

- HackerOne Report ID: 151847
- Weakness: Improper Authentication - Generic
- Program: nextcloud
- Disclosed At: 2016-07-18T19:53:39.463Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Basic authentication is enabled on file access requests
====================
Description
---------------------
Basic authentication is enabled on the server if we request for the direct URL of a file.  The issues of using Basic Authentication can be read here -> [OWASP: Basic Authentication](https://www.owasp.org/index.php/Basic_Authentication). Though your threat model considers brute-forcing as an acceptable risk, it is also worth noting that use of basic authentication makes the brute-force attacks much easier and faster. 

Detailed Steps
---------------------
**Step 1:** Open the browser and request for the direct URL of a file. Eg: (http://nc.hostiso.cloud/remote.php/webdav/Photos/Squirrel.jpg)
{F105383}
**Step 2:** Enter the username and password and capture the request in a proxy tool.
**Step 3:** It can be observed that the header with Base64 encoded username password is being sent in the request to server. 
{F105384}

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
