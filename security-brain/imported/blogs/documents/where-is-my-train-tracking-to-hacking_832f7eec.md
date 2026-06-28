---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-17_where-is-my-train-tracking-to-hacking-.md
original_filename: 2020-03-17_where-is-my-train-tracking-to-hacking-.md
title: 'Where is my Train : Tracking to Hacking !'
category: documents
detected_topics:
- xss
- sqli
- command-injection
tags:
- imported
- documents
- xss
- sqli
- command-injection
language: en
raw_sha256: 832f7eecbca2e41db8ef81db52d5e155475fbb186a4eb0ba9ad46501963eaccd
text_sha256: b9fe1aa172a816ad5802c1cf76dda4013d732ba157336c09fa96440b3491fc11
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Where is my Train : Tracking to Hacking !

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-17_where-is-my-train-tracking-to-hacking-.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `832f7eecbca2e41db8ef81db52d5e155475fbb186a4eb0ba9ad46501963eaccd`
- Text SHA256: `b9fe1aa172a816ad5802c1cf76dda4013d732ba157336c09fa96440b3491fc11`


## Content

---
title: "Where is my Train : Tracking to Hacking !"
url: "https://medium.com/@aniltom/where-is-my-train-tracking-to-hacking-d388e4b97225"
authors: ["Anil Tom (mr_4nk)"]
programs: ["Google"]
bugs: ["Reflected XSS", "SQL injection"]
publication_date: "2020-03-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4703
scraped_via: "browseros"
---

# Where is my Train : Tracking to Hacking !

Member-only story

Where is my Train : Tracking to Hacking !
Anil Tom
Follow
4 min read
·
Mar 17, 2020

308

Hello guys,

I am Anil Tom . Since it’s been a long time that I have written a blog, I thought of writing one today. Here, I am sharing some of my findings in one of the Google acquisition domains.

Press enter or click to view image in full size

Where is my Train

“Where Is My Train” by Sigmoid Labs Pvt. Ltd., is a unique app for Trains, that displays live running status of trains and up-to-date schedules. The app can function offline without Internet or GPS. It is rated №1 travel app in India.

The Story

On December 10, 2018 Google acquired Sigmoid Labs Pvt Ltd, and Where Is My Train hence became a part of Google. According to the Google VRP rule, one can report vulnerabilities to Google after 6 months from acquisition date. I had always been fond of hunting in acquisition domains, so I did some recon on their website whereismytrain.in but could not find any vulnerabilities.

The Real Story begins here 😉

One day one of my friends travelling to Bangalore from Chennai wanted me to pick him from the station so he shared his train status through Where Is My Train application. When I saw…
