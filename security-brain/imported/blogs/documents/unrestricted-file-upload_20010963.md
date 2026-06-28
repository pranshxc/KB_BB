---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-12_unrestricted-file-upload.md
original_filename: 2021-01-12_unrestricted-file-upload.md
title: Unrestricted File Upload
category: documents
detected_topics:
- command-injection
- file-upload
- api-security
tags:
- imported
- documents
- command-injection
- file-upload
- api-security
language: en
raw_sha256: 200109635a2c80e13fdac0d1190d1be07a70ce77608f3609773cd14c19a48bb1
text_sha256: 4a09b2fc394eed27eb968ebb256aaa85c29581d80d4a7c3cc068dd8626eb2e96
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Unrestricted File Upload

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-12_unrestricted-file-upload.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `200109635a2c80e13fdac0d1190d1be07a70ce77608f3609773cd14c19a48bb1`
- Text SHA256: `4a09b2fc394eed27eb968ebb256aaa85c29581d80d4a7c3cc068dd8626eb2e96`


## Content

---
title: "Unrestricted File Upload"
url: "https://binamrapandey.medium.com/unrestricted-file-upload-e95e1c6fb80"
authors: ["Binamra Pandey"]
bugs: ["Unrestricted file upload"]
publication_date: "2021-01-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4006
scraped_via: "browseros"
---

# Unrestricted File Upload

Unrestricted File Upload
Binamra Pandey
Follow
1 min read
·
Jan 12, 2021

164

2

I was testing on a website let’s call it “buggyweb.xyz”. After some time I found that there was a discussion forum which URL was something like this “discussion.buggyweb.xyz”. So I started to explore there and after some time I found out that there was a File Upload feature to upload images.

I started testing that file upload feature so I tried to upload .php extension file but that was rejected. So after digging a little bit I found out that there was “WhiteListing” of the files. So only file extension which is allowed is being uploaded. Basically, it was only verifying the last extension of that file. So what I did was open Burpsuite, capture the request and change the file extension but I failed. So after some time, I found out that it was double-checking the file extension(Client Side and Server Side).

Get Binamra Pandey’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After I found out that I first uploaded an image file then capture it with burp suite and change its content to PHP code then forward the request while uploading it. Now here comes the main part, Even I have uploaded the file, I haven’t published it yet so before clicking the publish button I turn on burp suite again and change the extension of that file to .PHP, and BOOM! It got Uploaded

And then I reported it to that company.

Thank You for reading this post.
