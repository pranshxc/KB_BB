---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1086259'
original_report_id: '1086259'
title: Proxy-Authorization header carried to a new host on a redirect
weakness: Cleartext Transmission of Sensitive Information
team_handle: curl
created_at: '2021-01-25T02:37:39.824Z'
disclosed_at: '2021-03-08T08:25:39.680Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cleartext-transmission-of-sensitive-information
---

# Proxy-Authorization header carried to a new host on a redirect

## Metadata

- HackerOne Report ID: 1086259
- Weakness: Cleartext Transmission of Sensitive Information
- Program: curl
- Disclosed At: 2021-03-08T08:25:39.680Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

hi cURL team

I am not entirely sure this is an issue, please feel free to close of it isn't.

I noticed that when making an HTTP GET request with Proxy-Authorization header, together with the "-L" flag to follow redirects

 curl -H "Authorization-Proxy: Basic xxx==" http://host:8000 -L

If the remote web server redirects to an alternate host/port, cURL  will carry over the Proxy-Authorization header to the redirected new host along with the secret.

If Authorization header is used (vs Proxy-Authentication) then the header gets stripped as it should.

Client  sends GET request with Proxy-Authorization header to Server 1:8080
Server1 Redirects cURL to Server2:8081
Server2:8081 Receives the Proxy-Authorization header
This was reproducible in the following version:

curl 7.64.1 (x86_64-apple-darwin20.0) libcurl/7.64.1 (SecureTransport) LibreSSL/2.8.3 zlib/1.2.11 nghttp2/1.41.0
Release-Date: 2019-03-27

I believe the expected behaviour is that Proxy-Authorization header should be stripped upon a server redirection, since its not within the same domain origin.

I also noticed a similar issue was opened 3 years ago regarding Authorization header: https://curl.se/docs/CVE-2018-1000007.html

## Impact

If the password is sent via HTTPS, the server may redirect it to over unencrypted protocols if sent to an HTTP web server, making the Interception of the password possible.

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
