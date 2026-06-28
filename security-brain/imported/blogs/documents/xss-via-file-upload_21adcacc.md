---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-27_xss-via-file-upload.md
original_filename: 2021-12-27_xss-via-file-upload.md
title: XSS via file upload
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
raw_sha256: 21adcacc1bfe0697a826c133400be7f430d3519dfdc7a1220140befe6340ec37
text_sha256: 4dae01693095893c1dabc85e7119ea49ef329085d4d78e813b6a790243edac3e
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# XSS via file upload

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-27_xss-via-file-upload.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `21adcacc1bfe0697a826c133400be7f430d3519dfdc7a1220140befe6340ec37`
- Text SHA256: `4dae01693095893c1dabc85e7119ea49ef329085d4d78e813b6a790243edac3e`


## Content

---
title: "XSS via file upload"
url: "https://sharmajijvs.medium.com/xss-via-file-upload-a2bcc1e5d7f7"
authors: ["Jay Sharma"]
bugs: ["XSS", "Unrestricted file upload"]
publication_date: "2021-12-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3058
scraped_via: "browseros"
---

# XSS via file upload

XSS via file upload
Jay Sharma
Follow
Dec 27, 2021

28

Press enter or click to view image in full size

I found xss via file upload here i uploaded svg file which stored in google cloud and reflected with xss

1) login at app.xyz.com
2) go to online store >> settings >> Email Notification >> Email design
3) click edit
4) Upload the file with svg payload
5) save the file and open image in new tab

But it’s marked as duplicate

Next day I observed that bug got patched and we can’t do xss anymore.

Get Jay Sharma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But after I saw url changed

https://images.xyz.com/s/cdn/v1.0/i/m?url=https%3A%2F%2Fstorage.googleapis.com%2Fproduction-xyz-v1-3%2F823%2F1134823%2FUc1iyTw%2Fe843c14e4a5f46c6898aeb3133ea1a30&methods=convert%2Cpng

After URL decoding

https://images.xyz.com/s/cdn/v1.0/i/m?url=https://storage.googleapis.com/production-xyz-v1-3/823/1134823/Uc1iyTw/e843c14e4a5f42c6898aeb3133ea1a30&methods=convert,png

What if I remove the convert part from url.

Oh we get pop up again

Press enter or click to view image in full size

After reporting it’s got triaged

Press enter or click to view image in full size
