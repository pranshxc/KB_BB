---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-17_code-execution-evernote.md
original_filename: 2019-04-17_code-execution-evernote.md
title: Code execution - Evernote
category: notes
detected_topics:
- command-injection
- path-traversal
- api-security
tags:
- imported
- notes
- command-injection
- path-traversal
- api-security
language: en
raw_sha256: e1d97a32b00d39e35dde0af6529d6785aedc39e5b9c40899b7e9f5fc41a15597
text_sha256: 90817c1419400e7e1fb17d8226c0c86907e7876b32b366622ca6f0301fe38d5c
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Code execution - Evernote

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-17_code-execution-evernote.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `e1d97a32b00d39e35dde0af6529d6785aedc39e5b9c40899b7e9f5fc41a15597`
- Text SHA256: `90817c1419400e7e1fb17d8226c0c86907e7876b32b366622ca6f0301fe38d5c`


## Content

---
title: "Code execution - Evernote"
page_title: "Code execution - Evernote ~ inputzero"
url: "https://www.inputzero.io/2019/04/evernote-cve-2019-10038.html"
final_url: "https://www.inputzero.io/2019/04/evernote-cve-2019-10038.html"
authors: ["Dhiraj (@mishradhiraj_)"]
programs: ["Evernote"]
bugs: ["RCE", "Path traversal"]
publication_date: "2019-04-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5304
---

#  [Code execution - Evernote](https://www.inputzero.io/2019/04/evernote-cve-2019-10038.html)

Written by [Dhiraj](https://www.blogger.com/profile/17432054824339572035 "author profile") on [05:53](https://www.inputzero.io/2019/04/evernote-cve-2019-10038.html "permanent link") in [CVE-2019-10038](https://www.inputzero.io/search/label/CVE-2019-10038), [Evernote](https://www.inputzero.io/search/label/Evernote) with [ No comments ](https://www.inputzero.io/2019/04/evernote-cve-2019-10038.html#comment-form) [ ![](https://img2.blogblog.com/img/icon18_edit_allbkg.gif) ](https://www.blogger.com/post-edit.g?blogID=7052034537728065557&postID=7778803457758171631&from=pencil "Edit Post")

**Summary:**  
A local file path traversal issue exists in Evernote 7.9 for macOS which allows an attacker to execute arbitrary programs.  
  
  
  
**Technical observation:**  
A crafted URI can be used in a note to perform this attack using **file:///** as an argument or by traversing to any directory like  
(**../../../../something.app**).  
  
Since Evernote also has a feature of sharing notes, in such a case an attacker could leverage this vulnerability and send crafted notes (.enex) to the victim to perform further attacks.  
  
**Patch:**  
A patch for this issue was released in Evernote 7.10 Beta 1 and 7.9.1 GA for macOS [[MACOSNOTE-28840](https://evernote.com/security/updates)]. CVE-2019-10038 was assigned to this issue.

Share: [__](https://www.facebook.com/share.php?v=4&src=bm&u=https://www.inputzero.io/2019/04/evernote-cve-2019-10038.html&t=Code execution - Evernote "Share this on Facebook")[__](https://twitter.com/home?status=Code execution - Evernote -- https://www.inputzero.io/2019/04/evernote-cve-2019-10038.html "Tweet This!")[__](https://plus.google.com/share?url=https://www.inputzero.io/2019/04/evernote-cve-2019-10038.html "Share this on Google+")[__](https://pinterest.com/pin/create/button/?source_url=https://www.inputzero.io/2019/04/evernote-cve-2019-10038.html&media=https://i.ytimg.com/vi/BAp9rGRR3Mw/hqdefault.jpg&description=Code execution - Evernote "Share on Pinterest")

[Email This](https://www.blogger.com/share-post.g?blogID=7052034537728065557&postID=7778803457758171631&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=7052034537728065557&postID=7778803457758171631&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=7052034537728065557&postID=7778803457758171631&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=7052034537728065557&postID=7778803457758171631&target=facebook "Share to Facebook")
