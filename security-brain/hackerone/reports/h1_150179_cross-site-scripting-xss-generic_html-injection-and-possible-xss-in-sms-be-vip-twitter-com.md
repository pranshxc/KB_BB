---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '150179'
original_report_id: '150179'
title: Html Injection and Possible XSS in sms-be-vip.twitter.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2016-07-09T04:46:26.833Z'
disclosed_at: '2016-08-28T23:45:09.867Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 82
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Html Injection and Possible XSS in sms-be-vip.twitter.com

## Metadata

- HackerOne Report ID: 150179
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2016-08-28T23:45:09.867Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I would like to report HTML Injection and possible cross site scripting (XSS) vulnerability in **sms-be-vip.twitter.com**

##Overview

The **sms-be-vip.twitter.com** 404 error page appears to be vulnerable to XSS and HTML Injection as it doesn't encode the HTML tags in the path name such as ```https://sms-be-vip.twitter.com/<h1>TEST</h1>```.

But the HTML tags have to be send without URL encoding. Most of the modern web browsers will encode the HTML tags in the request before it being sent to the webserver. However In Internet Explorer 11 and lower versions it's possible to make the browser send the request without any URL encoding.

### How to make MSIE 7 - 11 send the request without URL encoding ?

Internet Explorer won't encode the URL if it was sent from a 302 Redirect.

So you can use a simple PHP page like the following:

```php
<?php
$url = $_GET['x'];
header("Location: $url");
?> 
```

Then use the  page and perform a redirection to the endpoint which is vulenrable to XSS.

``` http://secgeek.net/POC/redir.php?x=https://sms-be-vip.twitter.com/<h1>TEST</h1> ```


Now you could notice that the friendly HTTP error messages in Internet Explorer will appear instead of showing the **<h1>TEST</h1>** in the error page.

There is a simple workaround for this issue. 
According to Microsoft the HTTP friendly error message will appears if it meets two criteria

1.The HTTP Status code must be [400, 403, 404, 405, 406, 408, 409, 410, 500, 501, 505]
2.The HTTP Response body’s byte length must be shorter than a threshold value

```Ruby
 The default threshold value for 404 errors is 512 bytes.
```
So we can add more data in the request to be returned in the server response that will overcome this issue.

```http://secgeek.net/POC/redir.php?x=https://sms-be-vip.twitter.com/<h1>TEST</h1>.................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................... ```

##Techincal Details

##Impact:

The vulnerability allow a malicious user to inject html tags and execute Javascript in the same context of sms-be-vip.twitter.com domain which could lead to steal user's session, peform CSRF attacks or open a phishing page.

##Affected Domain:
sms-be-vip.twitter.com

##Affected Insertion point:
The path name in the url ```https://sms-be-vip.twitter.com/<XSS Injection here>```

##HTML Injection POC
http://secgeek.net/POC/Twitter-HTML-POC.php

##XSS POC
http://secgeek.net/POC/Twitter-XSS-POC.php

**Note:** This XSS POC will work only if the XSS Auditor is disabled in Internet Explorer. 

I've Attached Sreenshots for the two POCs.

Kindly check and review the issue.
Thanks in advance!

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
