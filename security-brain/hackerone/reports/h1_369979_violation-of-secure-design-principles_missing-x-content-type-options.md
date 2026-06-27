---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '369979'
original_report_id: '369979'
title: Missing X-Content-Type-Options
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2018-06-22T04:35:51.576Z'
disclosed_at: '2020-03-01T13:59:09.547Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: download.nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Missing X-Content-Type-Options

## Metadata

- HackerOne Report ID: 369979
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2020-03-01T13:59:09.547Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Nextcloud doesn't have a header settings for X-Content-Type Options which means it is vulnerable to MIME sniffing. The only defined value, "nosniff", prevents Internet Explorer and Google Chrome from MIME-sniffing a response away from the declared content-type. This also applies to Google Chrome when downloading extensions. This reduces exposure to drive-by download attacks and sites serving user uploaded content that by clever naming could be treated by MSIE as executable or dynamic HTML files.

Please have a look at below links

https://hackerone.com/reports/6935
https://hackerone.com/reports/77081
https://hackerone.com/reports/9479/

Implement

Add the X-Content-Type-Options header with a value of "nosniff" to inform the browser to trust what the site has sent is the appropriate content-type, and to not attempt "sniffing" the real content-type.

X-Content-Type-Options: nosniff

## Impact

MIME type sniffing is a standard functionality in browsers to find an appropriate way to render data where the HTTP headers sent by the server are either inconclusive or missing.

This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the intended content type.

The problem arises once a website allows users to upload content which is then published on the web server. If an attacker can carry out XSS (Cross-site Scripting) attack by manipulating the content in a way to be accepted by the web application and rendered as HTML by the browser, it is possible to inject code in e.g. an image file and make the victim execute it by viewing the image.

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
