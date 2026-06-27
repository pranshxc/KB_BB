---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '583987'
original_report_id: '583987'
title: Periscope android app deeplink leads to CSRF in follow action
weakness: Cross-Site Request Forgery (CSRF)
team_handle: x
created_at: '2019-05-18T15:49:24.614Z'
disclosed_at: '2020-02-21T21:10:54.920Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 208
asset_identifier: '*.pscp.tv'
asset_type: WILDCARD
max_severity: none
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Periscope android app deeplink leads to CSRF in follow action

## Metadata

- HackerOne Report ID: 583987
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: x
- Disclosed At: 2020-02-21T21:10:54.920Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Twitter Team

#Summary
This issue is mainly in the Periscope Android app against CSRF follow action using deeplink.

#Description
In normal Periscope Website, when we share a follow link like `www.pscp.tv/<user-id>/follow`, we get a response whether to follow a person or not, giving us an option, means CSRF protection is there in Periscope web application.
However, in the Periscope Android App, there are some internal deep links by which we can perform Direct CSRF in terms of the following user using internal deeplinks.

#POC

In Android Manifest XML file, internal deeplinks are described as

```html
<data android:host="user" android:pathPrefix="/" android:scheme="pscp"/>
<data android:host="user" android:pathPrefix="/" android:scheme="pscpd"/>
<data android:host="broadcast" android:pathPrefix="/" android:scheme="pscp"/>
<data android:host="broadcast" android:pathPrefix="/" android:scheme="pscpd"/>
<data android:host="channel" android:pathPrefix="/" android:scheme="pscp"/>
<data android:host="channel" android:pathPrefix="/" android:scheme="pscpd"/>
<data android:host="discover" android:pathPrefix="/" android:scheme="pscp"/>
<data android:host="discover" android:pathPrefix="/" android:scheme="pscpd"/>
```
+ It means we can use ` pscp://user/<user-id> or pscpd://user/<user-id>`
+ Now,normally if we share follow link from website, it'll be like this, `www.pscp.tv/<user-id>/follow`, further give us option to follow them or not.

+ In deeplink, we can use the same follow-link in this way - `pscp://user/user-id/follow`, Once you visit this link from the browser, you'll directly follow any person in periscope android app.

+ Here is the Final POC
```html
<!DOCTYPE html>
<html>
<a href="pscp://user/<any user-id>/follow">CSRF DEMO</a>
</html>
```
+ Visit the above POC html page from android chrome browser, click on link and you'll follow anyone directly inside Periscope android app.

#Attachment (Video)
{F492266}

+ App Info - Periscope V 1.25.5.93

Thanks
Kunal

## Impact

+ Using Periscope deeplink like pscp://user/user-id/follow, it's possible to perform Direct CSRF Follow against any user in periscope android app.

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
