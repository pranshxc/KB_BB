---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-03_accessing-admin-dashboard-in-5-seconds-hall-of-fame.md
original_filename: 2023-05-03_accessing-admin-dashboard-in-5-seconds-hall-of-fame.md
title: 'Accessing Admin Dashboard in 5 seconds: Hall of Fame.'
category: documents
detected_topics:
- sso
- sqli
- command-injection
tags:
- imported
- documents
- sso
- sqli
- command-injection
language: en
raw_sha256: 6c9afe874e2ab369ee7bd1635a00d5a4545d133e168531ce7f7448b13cb63966
text_sha256: 871c18fa97fc32f016e6e188fabca4af67b41321d17f1b0e191d56220d5807ad
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Accessing Admin Dashboard in 5 seconds: Hall of Fame.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-03_accessing-admin-dashboard-in-5-seconds-hall-of-fame.md
- Source Type: markdown
- Detected Topics: sso, sqli, command-injection
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `6c9afe874e2ab369ee7bd1635a00d5a4545d133e168531ce7f7448b13cb63966`
- Text SHA256: `871c18fa97fc32f016e6e188fabca4af67b41321d17f1b0e191d56220d5807ad`


## Content

---
title: "Accessing Admin Dashboard in 5 seconds: Hall of Fame."
url: "https://sumedh00.medium.com/accessing-admin-dashboard-in-5-seconds-acee737eacfb"
authors: ["Sumedh Dawadi"]
bugs: ["Default credentials"]
publication_date: "2023-05-03"
added_date: "2023-05-04"
source: "pentester.land/writeups.json"
original_index: 1194
scraped_via: "browseros"
---

# Accessing Admin Dashboard in 5 seconds: Hall of Fame.

Accessing Admin Dashboard in 5 seconds: Hall of Fame.
Sumedha Dawadi
Follow
2 min read
·
May 3, 2023

151

Executive Summary.

Although I consider myself a mediocre bug hunter, this discovery was a stroke of pure luck.
Through the use of permutations, I was able to successfully enumerate a number of subdomains that had previously gone unnoticed. To my surprise, one of the subdomains I discovered led me to a Grafana dashboard, Surprisingly password for the dashboard was set to default ie. admin:admin. I was prompted to change the admin’s password.

Press enter or click to view image in full size

Later, I was able to set the password and successfully logged-in as admin.

Press enter or click to view image in full size

After, Successfully logged in as admin, I tried escalating further attack but no luck ¯\_(ツ)_/¯

Get Sumedha Dawadi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Again, I tried using httpx to probe path to other subdomains with the same port number and path. For this I used :

httpx -l subdomains.txt -path ":32000/login" -sc -mc 200

I was able to find another subdomain using Grafana, and tried logged in as admin but this time with the password that I changed earlier. As a result, another subdomain was pwned.

What did I learn ?
Trying default credentials in a login portal can sometimes be more effective than attempting SQL injection at first sight.
Mapping out the other different subdomains, with same associated ports and paths can help to identifying same potential vulnerability in other subdomains.
HALL OF FAME
Press enter or click to view image in full size
https://www.surf.nl/en/hall-of-fame-0
References
WSTG - Latest
Many web applications and hardware devices have default passwords for the built-in administrative account. Although in…

owasp.org

Enabled default credentials | Fluid Attacks Documentation
Description

docs.fluidattacks.com
