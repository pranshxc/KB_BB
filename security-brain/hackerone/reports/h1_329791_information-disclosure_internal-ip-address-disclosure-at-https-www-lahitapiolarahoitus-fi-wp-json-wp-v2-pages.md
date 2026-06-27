---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '329791'
original_report_id: '329791'
title: Internal IP Address Disclosure at https://www.lahitapiolarahoitus.fi/wp-json/wp/v2/pages
weakness: Information Disclosure
team_handle: localtapiola
created_at: '2018-03-25T20:12:22.714Z'
disclosed_at: '2018-04-28T10:03:07.045Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: www.lahitapiolarahoitus.fi
asset_type: URL
max_severity: none
tags:
- hackerone
- information-disclosure
---

# Internal IP Address Disclosure at https://www.lahitapiolarahoitus.fi/wp-json/wp/v2/pages

## Metadata

- HackerOne Report ID: 329791
- Weakness: Information Disclosure
- Program: localtapiola
- Disclosed At: 2018-04-28T10:03:07.045Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Basic report information
**Summary:** 
Hello, i found an internal ip address at https://www.lahitapiolarahoitus.fi/wp-json/wp/v2/pages.

**Description:** 
While digging the path in /wp-json/ directory, i found this url : https://www.lahitapiolarahoitus.fi/wp-json/wp/v2/pages and when i request this using Burp the internal ip address is leak in the response text.

**Impact:**
This information can help an attacker to identify other vulnerabilities in the future.

## Browsers / Apps Verified In:

  * Firefox ESR

## Steps To Reproduce:

1. Open this https://www.lahitapiolarahoitus.fi/wp-json/wp/v2/pages in your browser.
2. You will find this response : guid":{"rendered":"http:\/\/192.168.100.13\/?page_id=401"}.

### Request

 ```
GET /wp-json/wp/v2/pages HTTP/1.1
Host: www.lahitapiolarahoitus.fi
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Cookie: BIGipServerltr-prod_pool=224700608.20480.0000; TS01974a5b=0147052ac5151e01685567c85592aeda525d438000cfd6900beac37eb4d3ee457dbb9cda10259a7a56ccc6a3d09f0a5070f0a4ffba3fbd67e61eb198dbcb21ebb300f93d29; pll_language=fi
Connection: close
```

### Response

```
[{"id":401,"date":"2018-01-23T11:50:52","date_gmt":"2018-01-23T11:50:52","guid":{"rendered":"http:\/\/192.168.100.13\/?page_id=401"},"modified":"2018-01-23T12:10:19","modified_gmt":"2018-01-23T12:10:19","slug":"allekirjoitus-valmis","status":"publish","type":"page","link":"https:\/\/www.lahitapiolarahoitus.fi\/allekirjoitus-valmis\/","title":{"rendered":"Allekirjoitus valmis"}....
{"id":236,"date":"2017-12-12T09:08:25","date_gmt":"2017-12-12T09:08:25","guid":{"rendered":"http:\/\/localhost:82\/wordpress\/?page_id=236"},"modified":"2017-12-12T09:08:25","modified_gmt":"2017-12-12T09:08:25","slug":"tietoja-evasteista","status":"publish","type":"page","link":"https:\/\/www.lahitapiolarahoitus.fi\/tietoja-evasteista\/"......
```

## Additional material

  * {F278603}

## Related reports, best practices

  * https://portswigger.net/kb/issues/00600300_private-ip-addresses-disclosed

## Impact

This information can help an attacker to identify other vulnerabilities in the future.

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
