---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-06_how-i-gained-access-to-sonys-database.md
original_filename: 2018-02-06_how-i-gained-access-to-sonys-database.md
title: How I gained access to Sony’s database
category: documents
detected_topics:
- command-injection
- path-traversal
- api-security
tags:
- imported
- documents
- command-injection
- path-traversal
- api-security
language: en
raw_sha256: f243786c229db8fb1845d7eef1e69d8c584e7935ec0c65c569ddd5dba0e013f4
text_sha256: 177453f461260b728a0d2644de75ed5c49e92810a59dce24b4e8f980267e54e0
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How I gained access to Sony’s database

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-06_how-i-gained-access-to-sonys-database.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `f243786c229db8fb1845d7eef1e69d8c584e7935ec0c65c569ddd5dba0e013f4`
- Text SHA256: `177453f461260b728a0d2644de75ed5c49e92810a59dce24b4e8f980267e54e0`


## Content

---
title: "How I gained access to Sony’s database"
url: "https://medium.com/bugbountywriteup/how-i-gained-access-to-sonys-database-f3ba08d0e035"
authors: ["Rahul R"]
programs: ["Sony"]
bugs: ["Path traversal"]
publication_date: "2018-02-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5983
scraped_via: "browseros"
---

# How I gained access to Sony’s database

Top highlight

How I gained access to Sony’s database
Rahul R
Follow
2 min read
·
Feb 6, 2018

1K

3

This was a bug that I found back in 2017. This started when a friend of mine (a.k.a 1337) showed me a T-Shirt that he got from Sony . So I thought why can’t I get one so I started doing Recon on the target Sony had a wide range of domains and Sub-domains. I spend 2 days looking for a bug on Sony's main domain and I got nothing

So went for the next thing Acquisitions Same result. So I thought I should do something else so started Dorking

site:*.sony.*

And I landed in sony.co.kr and found a sub-domain bpeng.sony.co.kr due to the difficulty in understanding Korean Language I didn’t knew any of the options in the page.

Then something interesting happened https://bpeng.sony.co.kr/handler/BPEtc-PageView?pagename=some page blah blah

so I changed the value of pagename to something else and boom it redirected to that page so lets try etc/passwd and nothing happened..

But Why..?

Get Rahul R’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Because the server is Microsoft IIS you dummy

So as per my experience I never had a chance to Exploit an IIS server so lets search for resources and found that the site uses jsp and has something called a WEB-INF that contains the configuration

and PayLoadAllThings gave me the perfect payload

jsp/etc/../../WEB-INF/web.xml

https://bpeng.sony.co.kr/handler/BPEtc-PageView?pagename=jsp/etc/../../WEB-INF/web.xml

and i got this as in response

Press enter or click to view image in full size
Press enter or click to view image in full size
DB Configuration Files

Reported It to Sony and Listed my name in their HOF and a they gave me a T-shirt.

Stay Creative and Happy HACKING
