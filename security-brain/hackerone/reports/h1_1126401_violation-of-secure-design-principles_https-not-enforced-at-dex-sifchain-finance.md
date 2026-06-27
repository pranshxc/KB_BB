---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1126401'
original_report_id: '1126401'
title: HTTPS not enforced at dex.sifchain.finance
weakness: Violation of Secure Design Principles
team_handle: sifchain
created_at: '2021-03-15T18:44:41.334Z'
disclosed_at: '2021-06-10T14:59:47.060Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
asset_identifier: https://github.com/sifchain/sifnode
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# HTTPS not enforced at dex.sifchain.finance

## Metadata

- HackerOne Report ID: 1126401
- Weakness: Violation of Secure Design Principles
- Program: sifchain
- Disclosed At: 2021-06-10T14:59:47.060Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi



The requestes using non secured `HTTP` do not automatically upgraded to HTTPS , The impact of this  an attacker can laucn a MITM attack and steal users information.

## Impact

Data sent over HTTP, is being transmitted in plain , sniffers can see it , edit it , poison ads , know what contents being surfed by Buzzfeed users.

**Reproduce**
*Use Curl to check the response*

```
curl -i -s -k  -X 'GET' \
    -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:49.0) Gecko/20100101 Firefox/49.0' \
    'http://dex.sifchain.finance'
```

#Fix
When a resource is requested using `http` your server should automatically upgrade the request to `HTTPS`

Get `http://dex.sifchain.finance`

the response should be 

```
HTTP/1.1 301 Moved Permanently
Location: https://dex.sifchain.finance/


```

**Other hosts**

```
http://x.sifchain.finance/
http://bn.sifchain.finance/
http://dex.sifchain.finance/
http://blockexplorer.sifchain.finance/
http://sandpit.sifchain.finance/
http://dex.sifchain.finance/
http://blockexplorer-merry-go-round.sifchain.finance/
http://blockexplorer.sifchain.finance/
http://blockexplorer-testnet.sifchain.finance/

```




#Ref

- https://www.owasp.org/index.php/Man-in-the-middle_attack
- https://www.owasp.org/index.php/Transport_Layer_Protection_Cheat_Sheet
- https://www.owasp.org/index.php/HTTP_Strict_Transport_Security_Cheat_Sheet
- https://www.owasp.org/index.php/Testing_for_SSL-TLS_(OWASP-CM-001)



Regards

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
