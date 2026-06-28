---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-25_xss-via-qr-code.md
original_filename: 2023-05-25_xss-via-qr-code.md
title: XSS Via Qr Code
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 69b81a327568de490eaa19b60a660111a54b8a4560211d2e70073ddad2f31dd1
text_sha256: df72b868b4b549cc41b47fbd5db98922c80fe2a21e3e1dd03910f469eecee025
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# XSS Via Qr Code

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-25_xss-via-qr-code.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `69b81a327568de490eaa19b60a660111a54b8a4560211d2e70073ddad2f31dd1`
- Text SHA256: `df72b868b4b549cc41b47fbd5db98922c80fe2a21e3e1dd03910f469eecee025`


## Content

---
title: "XSS Via Qr Code"
url: "https://medium.com/@A0g/xss-via-qr-code-8022a1a0309f"
authors: ["Ahmed Osama (A0G)"]
bugs: ["XSS"]
publication_date: "2023-05-25"
added_date: "2023-05-29"
source: "pentester.land/writeups.json"
original_index: 1117
scraped_via: "browseros"
---

# XSS Via Qr Code

XSS Via Qr Code
Ahmed Osama (A0G)
Follow
2 min read
·
May 24, 2023

153

Hi Al Salam Alykum, it’s a simple XSS but with an unexpected vulnerable point, i hope the write-up is clear, if not ping me, happy hacking.

While Reconnaissance we found an http://example.com/index.html path with a response code 200 which was unexpected as the main URL (http://example.com) is a login page, then after visiting it found a QR code scanner.

Press enter or click to view image in full size

The button “ Code Scanner “ redirects to a GitHub tool “ https://github.com/mebjas/html5-qrcode “ then we used the QR Generator website “ https://www.the-qrcode-generator.com/ “ to create our QR code.
First we embed a random text in the QR Code to see how the application is handling the scanner output.

Press enter or click to view image in full size

Found that the application is printing the embed text.

Press enter or click to view image in full size

When inspect the text we found that it printed via HTML span tag.

Press enter or click to view image in full size

So we Created a new QR code with the simple following payload

Get Ahmed Osama (A0G)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

“ </span><img src=a onerror=alert(“XSS”)> “

Press enter or click to view image in full size

After Uploading it we Got An Alert !!!

Press enter or click to view image in full size
