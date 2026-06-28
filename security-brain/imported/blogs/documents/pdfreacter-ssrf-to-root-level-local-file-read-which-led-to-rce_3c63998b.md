---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-18_pdfreacter-ssrf-to-root-level-local-file-read-which-led-to-rce.md
original_filename: 2019-04-18_pdfreacter-ssrf-to-root-level-local-file-read-which-led-to-rce.md
title: PDFReacter SSRF to ROOT Level Local File Read which led to RCE
category: documents
detected_topics:
- sso
- ssrf
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- sso
- ssrf
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 3c63998bc8438df1ce794bcb1569bc6e864a700e14ec2725400d32eea3f30fd1
text_sha256: b1ad44ff66cae1ab679c57c1df82b8e6d899f5b3a68a3a109f4ea4a749e52e15
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# PDFReacter SSRF to ROOT Level Local File Read which led to RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-18_pdfreacter-ssrf-to-root-level-local-file-read-which-led-to-rce.md
- Source Type: markdown
- Detected Topics: sso, ssrf, xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `3c63998bc8438df1ce794bcb1569bc6e864a700e14ec2725400d32eea3f30fd1`
- Text SHA256: `b1ad44ff66cae1ab679c57c1df82b8e6d899f5b3a68a3a109f4ea4a749e52e15`


## Content

---
title: "PDFReacter SSRF to ROOT Level Local File Read which led to RCE"
page_title: "From SSRF To RCE in PDFReacter. What is PDFReacter?  - PDFReacter is a… | by Armaan Pathan | Medium"
url: "https://medium.com/@armaanpathan/pdfreacter-ssrf-to-root-level-local-file-read-which-led-to-rce-eb460ffb3129"
authors: ["Armaan Pathan (@armaancrockroax)"]
bugs: ["SSRF", "RCE"]
publication_date: "2019-04-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5303
scraped_via: "browseros"
---

# PDFReacter SSRF to ROOT Level Local File Read which led to RCE

From SSRF To RCE in PDFReacter
Armaan Pathan
Follow
2 min read
·
Apr 18, 2019

540

3

What is PDFReacter?
- PDFReacter is a parser which parses HTML content from HTML to PDF.

While testing an application I have identified that an application is using the PDFReacter parser.

PDFReacter is a formatting processor that parses the HTML content to PDF files.so Since an application has an option to insert data into forms, I started fuzzing with XSS and for that, I simply used <img> tag. there was an option to export the forms to PDF and when I exported the one of the form which has the payload, the final PDF file was like this.

Press enter or click to view image in full size

This means an application and PDFReacter both do not escapes the HTML tags and processes the HTML tags/XSS Payloads as well.

Since I knew that an application is using PDFReacter as a parser and both application and parsers are not escaping my payloads. So the next was with the iframe. I wanted to check if I can load external sites in a final pdf document or not and as you can see that Google is getting loaded in the frame.

Press enter or click to view image in full size

Now it was clear that I can hit to the external sites by using iframe(SSRF Confirmed).

Get Armaan Pathan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Next step was to read the local files with file:/// wrapper.Simple Payload “><iframe src=”file:///etc/passwd”/></iframe> I used for it.

Press enter or click to view image in full size

Bang !!!!!

Next is to check if the current user has root privileges or not. I Simply tried fetching the shadow file with the below-mentioned payload and I noticed that I was able to fetch the shadow file.
“/><iframe src=”file:///etc/shadow”></iframe>

Since the Current user has the root privileges, Next was to pop a shell, I Fetched Private SSH keys, And was able to SSH to the server.

Press enter or click to view image in full size

Although it was not my first RCE, I got goosebumps when I popped the shell. Rahul Maini’s blog helped me a lot to understand the current scenario. Thanks, Maini for an awesome blog.

Thanks everyone for reading.
