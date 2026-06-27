---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '906907'
original_report_id: '906907'
title: IDOR with Geolocation data not stripped from images
weakness: Insecure Direct Object Reference (IDOR)
team_handle: irccloud
created_at: '2020-06-24T15:26:46.071Z'
disclosed_at: '2020-07-26T15:36:33.868Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 48
asset_identifier: www.irccloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR with Geolocation data not stripped from images

## Metadata

- HackerOne Report ID: 906907
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: irccloud
- Disclosed At: 2020-07-26T15:36:33.868Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Vulnerable URL :-   https://usercontent.irccloud-cdn.com/file/0wXMTrPu/hgjbk

Vulnerability Discription:
When an image is taken using a smartphone or camera certain metadata fields are often attached to it. These fields could include the model of the camera, the time it was taken, whether the flash was used, the shutter speed, focal length, light value and even the location. In Inturn, while uploading the image as a profile picture, the exif data is not stripped from images. The exif data in images contains sensitive data like Geoloacation, latitude, longitude, etc. Also it contains the camera information and other details. 

And your website vulnerable to image IDOR which allows attacker to see other users images and retrive data using tool.

Tools Used: exiftool.

Steps TO reproduce:

Use  2 accounts in two browser

Download images from here 

https://github.com/ianare/exif-samples/tree/master/jpg/gps

1)In 1st account in network user can upload files just upload the image their and open image link in new tab.

 new tab that image url like

https://usercontent.irccloud-cdn.com/file/0wXMTrPu/hgjbk

2)In second account do same things and that url like down 

https://usercontent.irccloud-cdn.com/file/ZUsZU7az/3.jpg

3) Change 1st account Url parameter value to 2nd acoount Url parameter(see poc for it).

4) now image will shows up copy that url again and paste it to image data retrival website

http://exif.regex.info/exif.cgi

5) and see sensitive data   exposed.

## Impact

1) By this the attacker tracks your location and use it for personal things.
2) Sensitive data exposed.

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
