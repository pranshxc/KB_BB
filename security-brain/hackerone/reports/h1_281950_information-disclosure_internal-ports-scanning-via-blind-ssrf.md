---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '281950'
original_report_id: '281950'
title: Internal Ports Scanning via Blind SSRF
weakness: Information Disclosure
team_handle: infogram
created_at: '2017-10-23T10:27:21.203Z'
disclosed_at: '2017-11-03T14:12:43.562Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Internal Ports Scanning via Blind SSRF

## Metadata

- HackerOne Report ID: 281950
- Weakness: Information Disclosure
- Program: infogram
- Disclosed At: 2017-11-03T14:12:43.562Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Introduction:

I found a Blind SSRF issue that allows scanning internal ports.

## How to reproduce:

* Login
* Send the request `https://infogram.com/api/web_resource/url?q=[TARGET_URI]`
* Look up the response. If valid, it returns status code 200 and the website's title will be exposed, or 404 for otherwise.
For demonstration, I try scanning the *localhost* with a limited port range, then found some available ports: *80*, *81*, *6000*.

And here is the PoC:

```
GET /api/web_resource/url?q=http://0:6000/ HTTP/1.1
...
```

Response:

```
HTTP/1.1 200 OK
...

[{"title":"Create Infographics, Charts and Maps - Infogram","description":"Infogram is an easy to use infographic and chart maker. Create and share beautiful infographics, online charts and interactive maps. Make your own here.","url":"http://0:6000/"}]
```

As the filter does not validate the input, it allows the attacker to make the GET request to the internal network.

In conclusion, I think internal addresses should not be allowed.

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
