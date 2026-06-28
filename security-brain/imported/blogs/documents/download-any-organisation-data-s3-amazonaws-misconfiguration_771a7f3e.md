---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-22_download-any-organisation-data-s3-amazonaws-misconfiguration.md
original_filename: 2019-02-22_download-any-organisation-data-s3-amazonaws-misconfiguration.md
title: Download any organisation Data — S3 amazonaws Misconfiguration
category: documents
detected_topics:
- xss
- access-control
- command-injection
- cloud-security
tags:
- imported
- documents
- xss
- access-control
- command-injection
- cloud-security
language: en
raw_sha256: 771a7f3e59a6d8e07c8df27a3b0f9d937590779c2a14dbc7c26e5f094514e36d
text_sha256: 75162239e16ebcc4bee5f656d7609c0eaffd9bef334d7a4d0ceb131e0058242e
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Download any organisation Data — S3 amazonaws Misconfiguration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-22_download-any-organisation-data-s3-amazonaws-misconfiguration.md
- Source Type: markdown
- Detected Topics: xss, access-control, command-injection, cloud-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `771a7f3e59a6d8e07c8df27a3b0f9d937590779c2a14dbc7c26e5f094514e36d`
- Text SHA256: `75162239e16ebcc4bee5f656d7609c0eaffd9bef334d7a4d0ceb131e0058242e`


## Content

---
title: "Download any organisation Data — S3 amazonaws Misconfiguration"
url: "https://medium.com/@ChandSingh/download-any-organisation-data-s3-amazonaws-64059847e06"
authors: ["Chand Singh (@Chand_42)"]
bugs: ["Broken authorization"]
bounty: "2,500"
publication_date: "2019-02-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5392
scraped_via: "browseros"
---

# Download any organisation Data — S3 amazonaws Misconfiguration

Download any organisation Data — S3 amazonaws Misconfiguration
Chand Singh
Follow
2 min read
·
Feb 22, 2019

28

Amazon

Hello Readers,

Note — This Vulnerabilty not in Amazon AWS S3

My First post related to a Protonmail Stored XSS , so now here I’m Publishing my second blog post which recently found one of the private bug bounty website. Let’s start —

The vulnerability was very easy to exploit but it’s very hard to find the vulnerable point during checking many things i reached export feature of the website…according to the company it’s allow admin’s to download there organisations data in csv format. So…

It’s need little-bit intentions to reach the Vulnerable point

Steps to Reproduce the issue :-

Login the account go to this page ( subdomain.example.com/members )

2. there right side option settings gear button click on it then > export members

3. Now website sent link to your registered email-id which is looks like

https://subdomain.example.com/members_exports/29956

4. when i click the link then my organisation data download automatically

what’s going on —

5. if i change the id then it logout my account without any notification

Get Chand Singh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So after some time i again checked the request and this time burp suite “HTTP history” Tab opened , and there was too many request going on when i clicked on the link i saw below request little-bit weird from another one’s so I checked the request why it’s different ? you will understand why this request got my intention ? You guys are smart so no need to explain further ! :)

Technical Information :

Request :

GET /uploads/export/file/29956/29956.csv HTTP/1.1
Host: XXXXXX.s3.amazonaws.com
User-Agent: Mozilla/5.0
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip
Upgrade-Insecure-Requests: 1

Are you notice what’s going on above request ?

No Session-key, Authentication key anything which verify the identity of previous user. So next you know that what can attacker do, change the id’s with other Organisation-Id and all the data in response !

P.S. Don’t know too much about it’s Amazon Misconfiguration or Developer mistake so don’t focus on title.

Thanks for Reading !

Regards

Follow me on Twitter if you want :)

Timeline :

26/10/2018 — Report Sent

26/10/2018 — Report Triaged

01/11/2018 — Report Resolved

01/11/2018 — Bounty $2000 and $500 Bonus
