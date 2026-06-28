---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-18_ssrf-reading-local-files-from-downnotifier-server.md
original_filename: 2019-09-18_ssrf-reading-local-files-from-downnotifier-server.md
title: SSRF | Reading Local Files from DownNotifier server
category: documents
detected_topics:
- ssrf
- command-injection
tags:
- imported
- documents
- ssrf
- command-injection
language: en
raw_sha256: 12dbc7bade29de0f5d12244970db931e588034404ef517680c4a9f7d18f2b021
text_sha256: c3f040570e991afbac1c18791e71fb5ffcc53ddb752d85ebb5af11f128487bf0
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# SSRF | Reading Local Files from DownNotifier server

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-18_ssrf-reading-local-files-from-downnotifier-server.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `12dbc7bade29de0f5d12244970db931e588034404ef517680c4a9f7d18f2b021`
- Text SHA256: `c3f040570e991afbac1c18791e71fb5ffcc53ddb752d85ebb5af11f128487bf0`


## Content

---
title: "SSRF | Reading Local Files from DownNotifier server"
url: "https://www.openbugbounty.org/blog/leonmugen/ssrf-reading-local-files-from-downnotifier-server/"
authors: ["Dr.FarFar (@3XS0)"]
bugs: ["SSRF"]
publication_date: "2019-09-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5022
scraped_via: "browseros"
---

# SSRF | Reading Local Files from DownNotifier server

SSRF | Reading Local Files from DownNotifier server
Posted on September 18, 2019 by Leon

Hello guys, this is my first write-up and I would like to share it with the bug bounty community, it’s a SSRF I found some months ago.

DownNotifier is an online tool to monitor a website downtime. This tool sends an alert to registered email and sms when the website is down.

DownNotifier has a BBP on Openbugbounty, so I decided to take a look on https://www.downnotifier.com. When I browsed to the website, I noticed a text field for URL and SSRF vulnerability quickly came to mind.

Getting XSPA

The first thing to do is add http:127.0.0.1:22 on “Website URL” field.

Select “When the site does not contain a specific text” and write any random text.

I sent that request and two emails arrived in my mailbox a few minutes later. The first to alert that a website is being monitored and the second to alert that the website is down but with the response inside an html file.

And what is the response…?

Getting Local File Read

I was excited but that’s not enough to fetch very sensitive data, so I tried the same process but with some uri schemes as file, ldap, gopher, ftp, ssh, but it didn’t work.

I was thinking how to bypass that filter and remembered a write-up mentioning a bypass using a redirect with Location header in a PHP file hosted on your own domain.

I hosted a php file with the above code and the same process registering a website to monitor.

A few minutes later an email arrived at the mailbox with an html file.

And the response was…

I reported the SSRF to DownNotifier support and they fixed the bug very fast.

I want to thank the DownNotifier support because they were very kind in our communication and allowed me to publish this write-up. I also want to thank the bug bounty hunter who wrote the write-up where he used the redirect technique with the Location header.

Write-up: https://medium.com/@elberandre/1-000-ssrf-in-slack-7737935d3884

Categories
Security Researchers Insights
Tags
SSRF, Writeup

Leon

Cybersecurity enthusiast.
