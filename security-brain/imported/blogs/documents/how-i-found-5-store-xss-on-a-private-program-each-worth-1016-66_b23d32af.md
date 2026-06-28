---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-30_how-i-found-5-store-xss-on-a-private-program-each-worth-101666.md
original_filename: 2018-05-30_how-i-found-5-store-xss-on-a-private-program-each-worth-101666.md
title: How I found 5 store XSS on a private program. Each worth '1,016.66$'
category: documents
detected_topics:
- xss
- access-control
- command-injection
- cors
- api-security
tags:
- imported
- documents
- xss
- access-control
- command-injection
- cors
- api-security
language: en
raw_sha256: b23d32af2a57934dc9728facb44856d48332035fb4e044d8d7e04776843966c2
text_sha256: 62b74f049e4c183f9c07fa9858f9a426d8b9043af40a409a74b23f20abfeab54
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I found 5 store XSS on a private program. Each worth '1,016.66$'

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-30_how-i-found-5-store-xss-on-a-private-program-each-worth-101666.md
- Source Type: markdown
- Detected Topics: xss, access-control, command-injection, cors, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `b23d32af2a57934dc9728facb44856d48332035fb4e044d8d7e04776843966c2`
- Text SHA256: `62b74f049e4c183f9c07fa9858f9a426d8b9043af40a409a74b23f20abfeab54`


## Content

---
title: "How I found 5 store XSS on a private program. Each worth '1,016.66$'"
url: "http://cybristerboy.blogspot.com/2018/05/how-i-found-5-store-xss-on-private.html"
final_url: "http://cybristerboy.blogspot.com/2018/05/how-i-found-5-store-xss-on-private.html"
authors: ["Shahzad Sadiq (@ShahzadSadiq25)"]
bugs: ["Stored XSS"]
bounty: "5,083.3"
publication_date: "2018-05-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5864
---

### [How To Test Cross Origin Resource Sharing Vulnerability (OTG-CLIENT-007)](http://cybristerboy.blogspot.com/2018/06/hope-to-test-cross-origin-resource.html)

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

\-  [ June 30, 2018  ](http://cybristerboy.blogspot.com/2018/06/hope-to-test-cross-origin-resource.html "permanent link")

Hello Everyone, This blog is all about Cross Origin Resource Sharing (CORS) Vulnerability. In my one year of research, I found various type of bypass, that I would like to discuss. I will keep this blog to the point without discussing backend reason, so that beginner can find it an easy one. If a site is allowing access control header at the output response then play with all the request and capture it on burp or any proxy you use. After getting all directory on burp -> target -> sitemap, then this is a good time to test !! Most of the people just test it on one point, but each directory has its own way to set access control header. So, test it on every directory. For example -dir1 -sub_dir1 -sub_dir2 -dir2 -sub_dir1 -sub_dir2 Here you need to test on dir1 and dir2. How To Test First, put any random character at origin header at the inpu... 

[](http://cybristerboy.blogspot.com/2018/06/hope-to-test-cross-origin-resource.html)

[ 2 comments  ](http://cybristerboy.blogspot.com/2018/06/hope-to-test-cross-origin-resource.html#comments)

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps
