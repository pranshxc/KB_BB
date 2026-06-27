---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145344'
original_report_id: '145344'
title: 'nextcloud.com: Content Injection  Custom 404 Error'
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2016-06-17T11:15:48.155Z'
disclosed_at: '2016-06-17T12:18:52.830Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# nextcloud.com: Content Injection  Custom 404 Error

## Metadata

- HackerOne Report ID: 145344
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2016-06-17T12:18:52.830Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Hello Team ,**

>> *Request: if u think the reported issues have acceptable risk and u r not going to make changes then kindly request to mark as Informative .*

####Description : 
>> This report is about how an attacker is able to spoof the content of 404 page and can add thr own Text in way that the Current Website is moved to someone new URL which is Attackers website , yet its not that much effective to make this attacker successful but still this need to fix .

####Vulnerable URL : https://nextcloud.com

####POC URL : https://nextcloud.com/has%2f%20been%20changed%20to%20https://www.ATTACKER.COM.%20so%20please%20visit%20https://www.ATTACKER.COM%20as%20your%20requested%20link

####Reference : https://www.owasp.org/index.php/Content_Spoofing

####POC : http://i.imgur.com/hQuzqvn.jpg

####Mediation : 
+ User Predefined 404 page , with fixed error content !

Please let me know if any more info needed !

__Regard's
Geekboy :)__

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
