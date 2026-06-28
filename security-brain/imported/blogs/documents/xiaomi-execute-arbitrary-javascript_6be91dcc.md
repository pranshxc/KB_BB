---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-13_xiaomi-execute-arbitrary-javascript.md
original_filename: 2022-01-13_xiaomi-execute-arbitrary-javascript.md
title: Xiaomi Execute Arbitrary JavaScript
category: documents
detected_topics:
- xss
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- mobile-security
language: en
raw_sha256: 6be91dcc4ff1137700b9d44ebc10f7ccc6252320ebdf517315ef801966a7516a
text_sha256: 3ae1cf4d8ce01caf574ead823dc6339b344005b7a9ebdc837f8766829fb64ce8
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Xiaomi Execute Arbitrary JavaScript

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-13_xiaomi-execute-arbitrary-javascript.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `6be91dcc4ff1137700b9d44ebc10f7ccc6252320ebdf517315ef801966a7516a`
- Text SHA256: `3ae1cf4d8ce01caf574ead823dc6339b344005b7a9ebdc837f8766829fb64ce8`


## Content

---
title: "Xiaomi Execute Arbitrary JavaScript"
url: "https://nmochea.medium.com/xiaomi-arbitrary-javascript-vulnerability-327a6f3a9b0e"
authors: ["Neil Mark Ochea (@nmochea)"]
programs: ["Xiaomi"]
bugs: ["XSS", "HTML injection", "Android"]
publication_date: "2022-01-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3010
scraped_via: "browseros"
---

# Xiaomi Execute Arbitrary JavaScript

Xiaomi Execute Arbitrary JavaScript
Neil Mark Ochea / mhl_0xnmo
Follow
2 min read
·
Jan 12, 2022

26

In this writeup, I’ll tell you how I was able to Execute Arbitrary JavaScript in Xiaomi Browser using HTML Injection.

Description

Due to lack of HTML Sanitization, It’s possible to Inject Malicious Iframe tag in Readmode and Execute Arbitrary JavaScript code.

I look the Browser file:///android_asset/readmode/Readability.js source code the HTML and JavaScript have sanitization, however after I read the java source code in readmode activity and reading_mode_html_internal.js source code.

I found out that I have a chance to use HTML payload without passing through sanitization inside <title> tag.

Get Neil Mark Ochea / mhl_0xnmo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In com.android.browser.readmode.e.java snippet code

Press enter or click to view image in full size

In file:///android_asset/readmode/reading_mode_html_internal.js snippet code

Press enter or click to view image in full size

After getting the HTML <title> tag to the string, it will not pass through sanitization.

Step to Reproduce
Create malware_frame.html file with following content
Press enter or click to view image in full size
Create poc.html file with following content
Press enter or click to view image in full size
Run local server localhost:8080
In browser, open the following url http://localhost:8080/poc.html
The JavaScript from malware_frame.html executed immediately after Readmode ON
Disclosure Timeline
April 30, 2021 — I reported it on HackerOne Platform regarding this vulnerability issue.
May 8, 2021 — My report has been triaged.
May 17, 2021 — Vulnerability has been fixed and got bounty.

Thanks for reading this article, I hope you guys learn something new today. Please share this article to spread the knowledge.

Don’t forget to follow and connect with me through LinkedIn, and Twitter.
