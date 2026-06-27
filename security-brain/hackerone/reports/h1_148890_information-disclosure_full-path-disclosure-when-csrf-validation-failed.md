---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '148890'
original_report_id: '148890'
title: Full path disclosure when CSRF validation failed
weakness: Information Disclosure
team_handle: paragonie
created_at: '2016-07-02T17:57:45.410Z'
disclosed_at: '2016-07-02T18:05:12.457Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Full path disclosure when CSRF validation failed

## Metadata

- HackerOne Report ID: 148890
- Weakness: Information Disclosure
- Program: paragonie
- Disclosed At: 2016-07-02T18:05:12.457Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi again , 

There are Full path disclosure  in airship when the CSRF validation failed . It will show the full path with files  this is can be useful for an attacker if he need some information about files and path ,identified the script and path . 

 PoC : 

Host: bridge.cspr.ng
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://bridge.cspr.ng/author/edit/7
Cookie: __cfduid=any; PHPSESSID=any; cf_clearance=any-any-any
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 199
If-Modified-Since: *


_CSRF_TOKEN=&name=%3Cxss%3E&byline=&format=Rich+Text&biography=%3Ch2%3Exxxxxx%3Cbr%3E%3C%2Fh2%3E&_wysihtml5_mode=1&save_btn=sav




{F102987}



The CSRF validation error should not show other info about the files path . 

Thanks

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
