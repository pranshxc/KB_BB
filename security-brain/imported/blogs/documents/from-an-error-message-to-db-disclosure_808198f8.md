---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-17_from-an-error-message-to-db-disclosure.md
original_filename: 2018-04-17_from-an-error-message-to-db-disclosure.md
title: From an error message to DB disclosure
category: documents
detected_topics:
- api-security
- command-injection
tags:
- imported
- documents
- api-security
- command-injection
language: en
raw_sha256: 808198f8d3b3a7437fc6971f9790bcab4cc09bfe8066838876e49607aaa673f2
text_sha256: 6a29fbcd91f9edf722c303d6c32b36ded159663bfc76c6cf41a600b267db8dd8
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# From an error message to DB disclosure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-17_from-an-error-message-to-db-disclosure.md
- Source Type: markdown
- Detected Topics: api-security, command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `808198f8d3b3a7437fc6971f9790bcab4cc09bfe8066838876e49607aaa673f2`
- Text SHA256: `6a29fbcd91f9edf722c303d6c32b36ded159663bfc76c6cf41a600b267db8dd8`


## Content

---
title: "From an error message to DB disclosure"
url: "https://medium.com/@YumiSec/from-an-error-message-to-db-diclosure-1af879c74474"
authors: ["Yumi"]
bugs: ["Hardcoded credentials"]
publication_date: "2018-04-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5914
scraped_via: "browseros"
---

# From an error message to DB disclosure

From an error message to DB disclosure
Yumi
Follow
2 min read
·
Apr 17, 2018

105

2

Hey everyone,

Welcome on my first write-up. Today, I would like to share a simple but interesting bug I found some months ago on a public program.

During my recon process, I discovered on a subdomain, a PHP file with an error message like this :

Press enter or click to view image in full size

We can see two main things on this screenshot, an URL pointing to mongolab.com and in this URL an Api Key.

My first reflex was to check what is mongolab, according to their website :

mLab is the leading Database-as-a-Service for MongoDB, powering over half a million deployments worldwide.

Oh a database service, interesting. Let’s go to check what is the « API key » functionality.

Get Yumi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

According to the documentation :

Press enter or click to view image in full size

It’s nice but we need to check if the API key is valid or not. I used the request provided by the documentation :

https://api.mlab.com/api/1/databases?apiKey=[KEY]

And …

Press enter or click to view image in full size

Nice, I can print the databases. But to be a valid issue, I need to verify if I can gain access to sensitive data. I played with the resources provided by the documentation and finally :

Press enter or click to view image in full size

To conclude, read carrefully error messages, they can contain interresting data and can lead to more serious issue.

Timeline:

2018/02/15: Submitted

2018/02/15: Need more infos

2018/02/15: Additional informations provided

2018/02/21: Triaged

2018/03/02: Resolved

I hope you enjoyed this reading !

Yumi

Thanks to: Cinabre, Yothard
