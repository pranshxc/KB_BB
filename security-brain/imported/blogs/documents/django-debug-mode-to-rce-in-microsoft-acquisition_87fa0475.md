---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-19_django-debug-mode-to-rce-in-microsoft-acquisition.md
original_filename: 2020-08-19_django-debug-mode-to-rce-in-microsoft-acquisition.md
title: Django debug mode to RCE in Microsoft acquisition
category: documents
detected_topics:
- command-injection
- information-disclosure
- cloud-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- cloud-security
language: en
raw_sha256: 87fa04751f63f180ebbeb676ba7967efc81a54d577e8abefb17234bdcf278916
text_sha256: a0e0f90fdbb7a63d1c39cc51c9e430deacc4c5af6588e0bfa5e80f9d70e12b9a
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Django debug mode to RCE in Microsoft acquisition

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-19_django-debug-mode-to-rce-in-microsoft-acquisition.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, cloud-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `87fa04751f63f180ebbeb676ba7967efc81a54d577e8abefb17234bdcf278916`
- Text SHA256: `a0e0f90fdbb7a63d1c39cc51c9e430deacc4c5af6588e0bfa5e80f9d70e12b9a`


## Content

---
title: "Django debug mode to RCE in Microsoft acquisition"
url: "https://medium.com/@syedabuthahir/django-debug-mode-to-rce-in-microsoft-acquisition-189d27d08971"
authors: ["Syed Abuthahir (@writerabu)"]
programs: ["Microsoft"]
bugs: ["Information disclosure", "RCE"]
publication_date: "2020-08-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4305
scraped_via: "browseros"
---

# Django debug mode to RCE in Microsoft acquisition

Member-only story

Django debug mode to RCE in Microsoft acquisition
Syed Abuthahir
Follow
2 min read
·
Aug 19, 2020

120

4

As usual I was doing recon using Censys (https://censys.io/) and Shodan (https://www.shodan.io/). I was looking for Django debug mode enabled domains using the following search query.

censys -  443.https.get.body: "URLconf defined"
shodan -  html:"URLconf defined" 404

I open the main domains one by one and I noticed one domain redirect to microsoft’s acquisition domain, I was surprised. Then I open that Django ip address the response look like as follows

Press enter or click to view image in full size
Django Debug mode enabled.

As a Django developer I know 500 Internal server error return sensitive information but how to make it 500 status code response. I tried many ways but failed to make 500 response code. searching lot in google but i was not able to do it until an idea arises on my mind, Yes HTTP verb tempering I just change GET to POST method using burp suite I send the request to /admin path and I got 500 response.

my reaction

Press enter or click to view image in full size
Photo by Ben White on Unsplash

Then reading traceback error message for sensitive information i got bunch of information, many secret information hidden by Django like ********* but some credentials like Mongodb URI,redis URI,azure storage queue URI are not hidden.
