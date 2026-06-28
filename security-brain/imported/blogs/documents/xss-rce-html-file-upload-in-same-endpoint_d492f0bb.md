---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-29_xss-rce-html-file-upload-in-same-endpoint.md
original_filename: 2020-07-29_xss-rce-html-file-upload-in-same-endpoint.md
title: XSS, RCE & HTML File Upload in same endpoint
category: documents
detected_topics:
- xss
- command-injection
- file-upload
- csrf
- information-disclosure
- api-security
tags:
- imported
- documents
- xss
- command-injection
- file-upload
- csrf
- information-disclosure
- api-security
language: en
raw_sha256: d492f0bb71d240622dfd541227d3f177b459469a8113b1458270631f5d704b11
text_sha256: 36cc420178688ce2963bb31bbaa4b2fdc0dd93d066b8c926e9c8688230565c27
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# XSS, RCE & HTML File Upload in same endpoint

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-29_xss-rce-html-file-upload-in-same-endpoint.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload, csrf, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `d492f0bb71d240622dfd541227d3f177b459469a8113b1458270631f5d704b11`
- Text SHA256: `36cc420178688ce2963bb31bbaa4b2fdc0dd93d066b8c926e9c8688230565c27`


## Content

---
title: "XSS, RCE & HTML File Upload in same endpoint"
url: "https://sa1tama0.medium.com/xss-rce-html-file-upload-in-same-endpoint-4a03348445f4"
authors: ["Tarikul Islam (@sa1tama0)"]
bugs: ["XSS", "RCE", "Unrestricted file upload"]
bounty: "1,200"
publication_date: "2020-07-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4373
scraped_via: "browseros"
---

# XSS, RCE & HTML File Upload in same endpoint

XSS, RCE & HTML File Upload in same endpoint
Tarikul Islam
Follow
3 min read
·
Jul 29, 2020

153

3

Hello,
I’m Tarikul Islam, an acknowledging member of Sec Miner’s Bangladesh.

The basis of my knowledge comes from the bug bounty community & now it’s time to share a bit of my own experience.

A little while ago I targeted a private company. After some research, I found a sub-domain partners.site.com which is used for partners’ communication. I had the feeling that I can find XSS here. I tried for four days & got nothing but Information Discloser which was regenerating error because of the name character length set to 64 where I set my name more than 100+ characters which resulting to information disclosure.

Press enter or click to view image in full size
demo

206 An exception occurred while executing ‘INSERT INTO partners.user (id, site_id, name, email, avatar) VALUES (?, ?, ?, ?, ?)’ with params [283, 411571, “\”aaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbccccccccccccdddddddddd…”, “sa1tama0@wearehackerone.com”, “https:\/\/secure.gravatar.com\/avatar\/e5fbf987aa8c9f4b1ee0f05ad.jpg?d=mm”]: SQLSTATE[22001]: String data, right truncated: 7 ERROR: value too long for type character varying(64)

There was a possibility of using this error to execute XSS (Self XSS). I also tried to find CSRF in the name field to upgrade Self XSS to Stored XSS. Failed

Get Tarikul Islam’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Two days later I got the hidden user panel at partners.site.com/admin where I can change my details. There was also an option to upload a logo. The first thing that came in my mind, to upload an SVG file. SVG was uploaded successfully. I got an XSS (Non-Privileged User to Anyone) by uploading the SVG file.

And $200 was rewarded for the XSS. After that, I made an SVG for Blind XSS & upgrade the severity.

Press enter or click to view image in full size
RCE by PHP file upload.

After a week I was rechecking the site. I tried to upload the SVG file again also tried some bypass. But there was no luck. After a while, I upload an image without any extension. The image was successfully uploaded & it was showing the normal image in frontend. When I opened the full image it was showing raw code as content-type: text/html.

What the heck?

I tried to upload files with PHP extension. Failed

Then I tried JPG Shell Uploading (Ninja Method)

1. Select an image(bind with PHP code) click to upload.
2. Capture the request with the burp suite.
3. Change the file name to rce.php

BOOM!!!

$1000 was rewarded for RCE by PHP file upload.

After a month a friend of mine found HTML file upload to the same endpoint. He was rewarded $400 for it.
