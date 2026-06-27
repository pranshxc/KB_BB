---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '94637'
original_report_id: '94637'
title: Host Header Injection/Redirection
weakness: Open Redirect
team_handle: whisper
created_at: '2015-10-19T15:45:56.807Z'
disclosed_at: '2016-01-06T19:42:36.579Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- open-redirect
---

# Host Header Injection/Redirection

## Metadata

- HackerOne Report ID: 94637
- Weakness: Open Redirect
- Program: whisper
- Disclosed At: 2016-01-06T19:42:36.579Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

whisper.sh is vulnerable to host header injection because the host header can be changed to something outside the target domain (ie. whisper.sh) and cause it to redirect to to that domain instead (see below). 

Attack vectors are somewhat limited but depends on how the host header is used by the back-end application code. If code references the hostname used in the URL such as password reset pages, an attacker could spoof the host header of the request in order to trick the application to forwarding the password reset email to the attackers domain instead, etc. Other attack vectors may also be possible through manipulation of hyperlinks or other misc. code that relies on the host/domain of the request.

GET / HTTP/1.1
Host: crowdshield.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive

HTTP/1.1 301 Moved Permanently
Content-length: 0
Location: https://crowdshield.com/
Connection: close

If you search Google for this vulnerability, there are many, many blogs, articles and white papers describing this vulnerability and associated attack vectors. Every major commercial web application scanner like Accunetix will report this same vulnerability. 

For more details, please read: https://www.acunetix.com/blog/articles/automated-detection-of-host-header-attacks/.

Normally, most apps will reject any request that doesn't originate from the same origin (ie. whisper.sh). To fix, the application should reject anything that doesn't match the target domain. This may also be an error in the rewrite functions of the back-end web server as well.

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
