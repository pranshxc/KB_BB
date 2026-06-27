---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '390346'
original_report_id: '390346'
title: IDOR in Facebook Messages webcam photos
team_handle: meta
created_at: '2011-12-03T21:10:28.000Z'
disclosed_at: '2018-08-03T20:13:56.978Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 173
tags:
- hackerone
---

# IDOR in Facebook Messages webcam photos

## Metadata

- HackerOne Report ID: 390346
- Weakness: 
- Program: meta
- Disclosed At: 2018-08-03T20:13:56.978Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I found that photos people take with their webcam within private message conversations can be accessed without proper authorization via a photo preview mechanism. Even when the sender decides to discard the image after seeing the preview, it can later still be retrieved through this same preview mechanism.

Below I'll explain the security issue and how to reproduce it. Probably the best way to reproduce the issue is by using an intercepting proxy like BurpSuite Pro so you can decide to forward, modify or drop every request that's being sent to Facebook through the proxy. 

1. Compose a new private message to a friend by using Messages on the FB web app.
2. Click the camera icon to load the Flash application which allows you to shoot a picture with your webcam. Make sure you grant Flash temporary access to the webcam resource.
3. Setup an intercepting proxy to route all HTTPS traffic to Facebook through this proxy.
4. Press the button to shoot a picture and wait until the counter reaches zero and actually shoots the picture.
5. Forward all requests until a request to /ajax/messaging/attachments/preview.php shows up. The response to this request will be some JSON with references to the preview of the uploaded image on the Facebook CDN. Save this request for later use.

It's possible to access photo previews of other people by modifying the ID in the GET request that's sent to preview.php to get the direct URLs to the photo stored on the FB CDN. It should look similar to this (I removed my private session/identifiable data):

```
GET /ajax/messaging/attachments/preview.php?id=188618221230552&__a=1&__user=1109857860 HTTP/1.1
Host: www.facebook.com
Connection: keep-alive
X-SVN-Rev: 484067
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.2 Safari/535.11
Accept: */*
Referer: https://www.facebook.com/
Accept-Encoding: gzip,deflate,sdch
Accept-Language: en-US,en;q=0.8
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3
Cookie: locale=en_US; c_user=1109857860; csm=1; datr=<datr goes here>; lu=<lu goes here>; s=<s goes here>; xs=<xs goes here>; p=4; act=<act goes here>; presence=<presence goes here>; a_user=1109857860; a_xs=<a_xs goes here>; L=2; sid=1; W=<W goes here>
```

Here are some IDs to test with (currently they're all still working and being served from the CDN):
ID: `188618221230552`
Resolves to: http://fbcdn-photos-a.akamaihd.net/hphotos-ak-ash4/384984_2728509647830_1109857860_33122783_1551454573_n.jpg

ID: `158481310920219`
Resolves to: http://fbcdn-photos-a.akamaihd.net/hphotos-ak-ash4/376464_113096208806978_100003197993582_73924_151328540_n.jpg

ID: `289683717741182`
Resolves to: http://fbcdn-photos-a.akamaihd.net/hphotos-ak-ash4/386189_2728395884986_1109857860_33122730_1125587545_n.jpg

Note that the IDs that are used for the previews are different from the ones that are used to uniquely identify a photo. Though the IDs look pretty random, just relying on one 15 digit number is risky. This makes the likelihood that the vulnerability is exploited lower, but the impact of the vulnerability remains the same. A brute force attack might be successful in revealing some private photos. Since preview.php is hosted on the facebook.com domain, it should be possible to implement authorization checks in this file before the static URLs to the pictures on the CDN are disclosed. If the user is not the owner of the picture, it should not be possible to retrieve the static CDN URLs.

Please let me know if I can be of any help in providing more details on the vulnerability or additional info to reproduce this issue.

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
