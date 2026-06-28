---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-17_how-i-got-stored-xss-using-file-upload.md
original_filename: 2018-04-17_how-i-got-stored-xss-using-file-upload.md
title: How I got stored XSS using file upload
category: documents
detected_topics:
- xss
- command-injection
- file-upload
- api-security
tags:
- imported
- documents
- xss
- command-injection
- file-upload
- api-security
language: en
raw_sha256: 2e0f03e5d9b6947d94c0135de4c293ccdbd9dfb6af641338cf151f51475023c6
text_sha256: 63e5290b7c8671a6d02deb17d524f9b445a22784cbe10592f0d1cfd7c31abd3a
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I got stored XSS using file upload

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-17_how-i-got-stored-xss-using-file-upload.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `2e0f03e5d9b6947d94c0135de4c293ccdbd9dfb6af641338cf151f51475023c6`
- Text SHA256: `63e5290b7c8671a6d02deb17d524f9b445a22784cbe10592f0d1cfd7c31abd3a`


## Content

---
title: "How I got stored XSS using file upload"
url: "https://medium.com/@vis_hacker/how-i-got-stored-xss-using-file-upload-5c33e19df51e"
authors: ["gujjuboy10x00 (@vis_hacker)"]
bugs: ["Stored XSS"]
publication_date: "2018-04-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5913
scraped_via: "browseros"
---

# How I got stored XSS using file upload

How I got stored XSS using file upload
Gujjuboy10x00
Follow
2 min read
·
Apr 17, 2018

647

7

Hi Everyone,

I always believed that sharing is caring, and i have been learning from multiple security researchers in the bug bounty field ,Today i am going to share simple method of getting xss in file upload. few days back i got invitation from hackerone private program. it was very old program (100+ report resolved). still i tried to get something interesting.

After looking inside that functionality i can see that there is option to upload data manually as well as using file upload (Only CSV).

there was a strict restriction of file upload for extension (.csv only). there was 4 option firstname , lastname , company , mobile number. Simply i tried to bypass using Burp by changing content-type to text/html , but no success in xss as there was something blocking at server level.

time to dig more

Later I tried to put simple payload in CSV file , like <script>alert(1)</script> in first 3 field , but something was blocking at server to not allow <script> tag. then i tried for many payload nothing was working.

Get Gujjuboy10x00’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Finally i tried with </Textarea/</Noscript/</Pre/</Xmp><Svg /Onload=confirm(document.domain)>” and got stored xss.

Press enter or click to view image in full size
Stored xss

and my expression was like (Mil gaya , mil gaya …):

Thanks for reading my blog , hope you like this blog.
