---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '164916'
original_report_id: '164916'
title: Same origin policy bypass on e.mail.ru via Cross-Site Flashing
team_handle: mailru
created_at: '2016-09-01T06:58:16.732Z'
disclosed_at: '2018-04-02T11:15:20.853Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
---

# Same origin policy bypass on e.mail.ru via Cross-Site Flashing

## Metadata

- HackerOne Report ID: 164916
- Weakness: 
- Program: mailru
- Disclosed At: 2018-04-02T11:15:20.853Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Mail.Ru Security Team,

There is a Cross-Site Flashing vulnerability in e.mail.ru. this vulnerability is similar to XSS except it is Flash script execution. Ref : https://www.owasp.org/index.php/Testing_for_Cross_site_flashing_(OTG-CLIENT-008) This allow an attacker to execute requests to the vulnerable subdomain and read source code in the victim browser (with victims cookie and context), which is a Same origin policy bypass vulnerability that leads to info disclosure, CSRF, account takeover...

POC link :
http://opnsec.com/mailru/mailrugalleryPOC.html

POC requirements :
- Flash must be active
- You must be connected to e.mail.ru
- Tested on Windows 8/10 with Firefox 47 and Chrome 52

POC instructions :
- Open the POC link
- Wait a few seconds
- Your mail.ru info will show down including your email, a CSRF token, and details about one of your inbox email (subject, sender and body in html source)

------
Technical details :

The vulnerable SWF file is https://img.imgsmail.ru/r/foto2/galery.swf

the actionscript contains 
```
allowdomain("*")
```
which allow any attacker to access the galery.swf, and make request on his behalf.

https://e.mail.ru/crossdomain.xml contains 
```
<allow-access-from domain="img.imgsmail.ru" secure="true"/>
```
This means that the attacker can make request to any e.mail.ru URL on behalf of https://img.imgsmail.ru/r/foto2/galery.swf and read the source code. 

The attacker can extract private info from the source code like user account details, CSRF tokens, emails ...

------
Attack scenario

The attacker can create a webpage similar to the POC and send the link to the victim. When the victim opens the POC, if the victim is connected to e.mail.ru, the attacker gains access to the victims info.

------
Mitigation

To solve this problem you can either :
- Remove `allowdomain("*")` from https://img.imgsmail.ru/r/foto2/galery.swf
- Or Remove https://e.mail.ru/crossdomain.xml
- Or Move  https://img.imgsmail.ru/r/foto2/galery.swf to another subdomain which is not listed in https://e.mail.ru/crossdomain.xml


If you need more info feel free to contact me.

Regards,

Enguerran @opnsec

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
