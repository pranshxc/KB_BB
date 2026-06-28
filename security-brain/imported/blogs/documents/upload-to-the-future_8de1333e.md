---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-22_upload-to-the-future.md
original_filename: 2020-08-22_upload-to-the-future.md
title: Upload to the future
category: documents
detected_topics:
- idor
- xss
- command-injection
- cloud-security
tags:
- imported
- documents
- idor
- xss
- command-injection
- cloud-security
language: en
raw_sha256: 8de1333e5a131bb23f98b7b1911a9adda7efde9fa0fceb0a65c892c72c142062
text_sha256: 9ba0799bd40b5b5651805de48476813eb350aeeb4deff6297a25f63b722e92a9
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Upload to the future

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-22_upload-to-the-future.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `8de1333e5a131bb23f98b7b1911a9adda7efde9fa0fceb0a65c892c72c142062`
- Text SHA256: `9ba0799bd40b5b5651805de48476813eb350aeeb4deff6297a25f63b722e92a9`


## Content

---
title: "Upload to the future"
url: "https://medium.com/bugbountywriteup/upload-to-the-future-1fd38fd502bd"
authors: ["Vuk Ivanovic"]
bugs: ["IDOR"]
publication_date: "2020-08-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4300
scraped_via: "browseros"
---

# Upload to the future

Member-only story

Upload to the future
Vuk Ivanovic
Follow
5 min read
·
Aug 22, 2020

109

1

A bit of an odd title, eh? Either way, this article will be about a very peculiar bug that I discovered somewhat recently, where it was possible to overwrite user’s/victim’s profile images. But, there’s also a twist to it.

Initial recon:

When a website has any kind of upload function, there are a few things to immediately take a look at, it’s not even hacking really, it’s using the upload function of the website as it is intended.

The first thing that I tend to look for is whether I can select any file to upload (if I can, I just make a note of that while still uploading the expected type of file which is usually of image type)

Upon uploading the expected file type, usually an image of some kind, the next thing to look for is where is that image being stored and the naming convention. If the image is stored on aws then I note that and get XXE payloads ready, if it’s the same domain, then I note that, but if it’s some third party host then I leave it be (this doesn’t take into consideration whether the pulled name inside img src can be xss payload)

In this case, the upload location was the domain, which meant it was time to try various tricks in order to see if I can get any other file type uploaded, or whether I can trick in any way for the uploaded file to be executed as anything other than a regular…
