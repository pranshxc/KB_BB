---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-05_how-i-found-open-redirect-on-hashnodecom_2.md
original_filename: 2021-08-05_how-i-found-open-redirect-on-hashnodecom_2.md
title: How I found Open Redirect on Hashnode.com
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: b2318ff3111f78e90afee494389d5dae7e3aa62efc6ec8e7685a1c7d2192aed7
text_sha256: 5fe8989076ff2e60d486a39329dae217db51f08b011ae2f4295d90dbc76a8e9b
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How I found Open Redirect on Hashnode.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-05_how-i-found-open-redirect-on-hashnodecom_2.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `b2318ff3111f78e90afee494389d5dae7e3aa62efc6ec8e7685a1c7d2192aed7`
- Text SHA256: `5fe8989076ff2e60d486a39329dae217db51f08b011ae2f4295d90dbc76a8e9b`


## Content

---
title: "How I found Open Redirect on Hashnode.com"
url: "https://gonzx.medium.com/how-i-found-open-redirect-on-hashnode-com-5f3e9ecb8dc6"
authors: ["Jefferson Gonzales (@gonzxph)"]
programs: ["Hashnode"]
bugs: ["Open redirect"]
publication_date: "2021-08-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3442
scraped_via: "browseros"
---

# How I found Open Redirect on Hashnode.com

How I found Open Redirect on Hashnode.com
Jefferson Gonzales
Follow
1 min read
·
Aug 5, 2021

164

Good day to all Bug Hunters again I’m Jefferson Gonzales and today I will share my findings on Hashnode.com

On July 30 my friend Shuvam Adhikari posted a writeup on how he got a SWAG from Hashnode.com so after reading he’s writeup I also try to hunt on Hashnode.com and I found Open Redirect Vulnerability

When I login to Hashnode.com I found this parameter

https://hashnode.com/login?next=/settings

When I login my account it redirect me to

https://hashnode.com/settings

Then I change the value of ?next= parameter to http://google.com

https://hashnode.com/login?next=http://google.com

Then login again my account and it redirect me to Google.com this confirm that its vulnerable to Open Redirect, but I have a problem only google.com, github.com and facebook.com will work in redirection, if you put other domains it will not redirect but I found a way to bypass it using \\ double backslash

https://hashnode.com/login?next=\\evil.com

When I login my account it redirect me to evil.com and successfully bypassed

Get Jefferson Gonzales’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Hashnode Appreciation:

Press enter or click to view image in full size

You can contact me on

https://twitter.com/gonzxph

https://web.facebook.com/g0nzxph

https://www.linkedin.com/in/gonzxph
