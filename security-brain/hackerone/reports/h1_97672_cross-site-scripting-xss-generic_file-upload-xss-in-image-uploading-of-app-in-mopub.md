---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '97672'
original_report_id: '97672'
title: File Upload XSS in image uploading of App in mopub
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2015-11-04T11:53:37.133Z'
disclosed_at: '2016-08-25T22:55:35.327Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# File Upload XSS in image uploading of App in mopub

## Metadata

- HackerOne Report ID: 97672
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2016-08-25T22:55:35.327Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

I want to report a File upload XSS in your Image upload functionality of Apps in mopub. Server doesn't check whether you are uploading a jpg/jpeg files and it upload the file on image.mopub.com .

POC link : https://images.mopub.com/app_icons/126cb3308e1a464385a49c4c7aaeac56

Steps to reproduce :
1.Go to App settings and select a html file with .jpg extension.
2.Intercept the request and change the .jpg to .html and change the content type to text/html and it will upload the file.
3.Open the link of image in new file and XSS will pop up.

HTTP request :

POST /inventory/app_icon/upload/ HTTP/1.0
Host: app.mopub.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:42.0) Gecko/20100101 Firefox/42.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-CSRFToken: YZ8hbuu1vB9p5s1ni2vPZ5kMrhMqeDo5
X-Requested-With: XMLHttpRequest
Referer: https://app.mopub.com/inventory/app/97142808ce5d4ace895480a3ffe7d631/
Content-Length: 389
Content-Type: multipart/form-data; boundary=---------------------------1714461176134095862036612614
Cookie: [Cookie values]
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache

-----------------------------1714461176134095862036612614
Content-Disposition: form-data; name="image_upload"; filename="xssfileuploadcopy.html"
Content-Type: text/html

HTML contetn
-----------------------------1714461176134095862036612614--


Let me know if you need any other help from my side.

Best Regards !
Vijay Kumar

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
