---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '324548'
original_report_id: '324548'
title: Html injection mycrypto.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mycrypto
created_at: '2018-03-12T09:13:00.824Z'
disclosed_at: '2018-03-16T17:51:25.344Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
asset_identifier: beta.mycrypto.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Html injection mycrypto.com

## Metadata

- HackerOne Report ID: 324548
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mycrypto
- Disclosed At: 2018-03-16T17:51:25.344Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello. I remembered that a couple of months ago I found an HTML injection vulnerability on myetherwallet.com, I sent it, but my message was ignored.
Since you have the same interface, I decided to check this vulnerability on your site and it was reproduced. The vulnerability works both on www.mycrypto.com and on mycrypto.com.
Html injection is in a pop-up message

 <div class = "alert-message ng-binding" ng-bind-html = "alert.message"> You are successfully connected
<br> URL: <strong> https://www.mycrypto.com/?txHash=qwqwq%3C%20SRC=%22jav
ascript: alert (0); "& gt; <a href="https://securityz.net"> <img src =" https://securityz.net/mycrypto.jpeg "> </a> qwqw # check- tx-status </ strong> <br> Network: <strong> ETH </ strong> provided by <strong> mycryptoapi.com </ strong> </ div>

Unfortunately, you have filtering there, I could not execute js and could hardly display a picture with href on the page. 
## PoC
 https://mycrypto.com/?txHash=qwqwq%3C%20SRC=%22jav&#x0D;ascript:alert(0);"> <a href="https://securityz.net"><img src="https://securityz.net/mycrypto.jpeg"></a>qwqw#check-tx-status 

##PoC video
 https://www.youtube.com/watch?v=JmP9AU8sX5k .
##Impact
Since your site and myetherwallet are often subjected to phishing attacks, this vulnerability is dangerous. You can put in the href url of the phishing site, then you can steal the private key of the victim. Perhaps you can upload js to the site, but I could not do it.

## Impact

Since your site and myetherwallet are often subjected to phishing attacks, this vulnerability is dangerous. You can put in the href url of the phishing site, then you can steal the private key of the victim. Perhaps you can upload js to the site, but I could not do it.

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
