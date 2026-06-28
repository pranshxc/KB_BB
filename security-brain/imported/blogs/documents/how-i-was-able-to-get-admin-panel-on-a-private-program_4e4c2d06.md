---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-29_how-i-was-able-to-get-admin-panel-on-a-private-program.md
original_filename: 2018-05-29_how-i-was-able-to-get-admin-panel-on-a-private-program.md
title: How i was able to get admin panel on a private program
category: documents
detected_topics:
- access-control
- command-injection
- cors
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- cors
- api-security
language: en
raw_sha256: 4e4c2d06b08243326967ab82a5af3add3db2240ac2761bbccbc5e748026e5ab9
text_sha256: f0039437ae49e9bfcf3f3ca12a1443058ac87a21157eb46c8a7b4035f3045897
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How i was able to get admin panel on a private program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-29_how-i-was-able-to-get-admin-panel-on-a-private-program.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, cors, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `4e4c2d06b08243326967ab82a5af3add3db2240ac2761bbccbc5e748026e5ab9`
- Text SHA256: `f0039437ae49e9bfcf3f3ca12a1443058ac87a21157eb46c8a7b4035f3045897`


## Content

---
title: "How i was able to get admin panel on a private program"
url: "http://cybristerboy.blogspot.com/2018/05/how-i-was-able-to-get-admin-panel-on.html"
final_url: "http://cybristerboy.blogspot.com/2018/05/how-i-was-able-to-get-admin-panel-on.html"
authors: ["Shahzad Sadiq (@ShahzadSadiq25)"]
bugs: ["Weak credentials"]
bounty: "1,500"
publication_date: "2018-05-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5866
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
