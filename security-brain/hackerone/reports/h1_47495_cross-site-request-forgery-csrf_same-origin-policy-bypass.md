---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '47495'
original_report_id: '47495'
title: Same Origin Policy bypass
weakness: Cross-Site Request Forgery (CSRF)
team_handle: mailru
created_at: '2015-02-12T00:35:46.540Z'
disclosed_at: '2015-03-27T14:29:12.748Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Same Origin Policy bypass

## Metadata

- HackerOne Report ID: 47495
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: mailru
- Disclosed At: 2015-03-27T14:29:12.748Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

After small investigation I've probably found something that can be exploited to bypass Same Origin Policy on mail.ru services (specially your main domain and e.mail.ru). 

First of all - let's take a look about your crossdomain.xml (both for mail.ru and e.mail.ru):

<cross-domain-policy>
<allow-access-from domain="*.files.mail.ru" to-ports="80"/>
<allow-access-from domain="img.imgsmail.ru" to-ports="80"/>
<allow-access-from domain="win.mail.ru" to-ports="80"/>
<allow-access-from domain="e.mail.ru" to-ports="80"/>
<allow-access-from domain="*.corp.mail.ru" to-ports="80"/>
<allow-access-from domain="img.mail.ru" to-ports="80"/>
<site-control permitted-cross-domain-policies="all"/>
</cross-domain-policy>

After time spent on searching useful files I found flash uploader on files.mail.ru which is mentioned in crossdomain. 

Few important things about this Flash file (https://files.mail.ru/uploader9.swf):

1) It uses Security.allowDomain("*") which is extreamly dangerous
2) It have interesting callback to ajaxCall() method. 

I want to tell you more about ajaxCall() actionscript function - here's snippet: https://gist.github.com/ZoczuS/82ad1e7509dd436a2db9

You can see that before request will go on there are few checks - provided URL must starts with http:// schema, must have .mail.ru before first / (to prevent sending requests to other domain). Bypass is simple here - we can use username@hostname notation - http://.mail.ru@lab.ropchain.org/r.php?r=HTTPS://ANY-OTHER-URL.COM ;-) (r.php returns 301 and redirects us where $_GET['r'] tells). 

To make this attack even simpler - ajaxCall() function have js_callback parameter, where we can handle our Cross-Origin response, and parse it. 

So the example attack scenario goes like this:
1. Attacker create specially crafted webpage where he embeds uploader9.swf
2. Because of Security.allowDomain('*') we can interact with this file from any domain, so it works. 
3. Because ajax() callback we can send requests to any other webpage.
4. Because of crossdomain.xml of mail.ru we can gain full response from mail.ru and pass it to our js_callback (that "works" for attacker's origin).

In this scenario I'll call https://mail.ru/?json=1&nano=0 that returns sort of informations about logged in user in JSON format. To watch exploit in action - visit this page: https://eip.uid0.pl/mail.php (it requires SSL, sorry for self-signed cert).

Video demonstration: https://www.youtube.com/watch?v=iIUlSJ-Wvgk (unlisted one - only me and you have this link)

Thanks for reading it - have a nice day!
Jakub Zoczek

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
