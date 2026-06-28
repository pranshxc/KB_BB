---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-06_1000-for-a-simple-stored-xss.md
original_filename: 2023-08-06_1000-for-a-simple-stored-xss.md
title: $1000 for a simple Stored XSS
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 5ae41e763f988fde565abe17e09c72c847ec001dd9ac565a608e4862b118e99e
text_sha256: 27c4fcbee9b109c1cb55e2bbac47d0a59751447bdea571a68723c84a4f91d0df
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# $1000 for a simple Stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-06_1000-for-a-simple-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `5ae41e763f988fde565abe17e09c72c847ec001dd9ac565a608e4862b118e99e`
- Text SHA256: `27c4fcbee9b109c1cb55e2bbac47d0a59751447bdea571a68723c84a4f91d0df`


## Content

---
title: "$1000 for a simple Stored XSS"
url: "https://medium.com/@snoopy101/1000-for-a-simple-stored-xss-8be7083a7c2d"
authors: ["snoopy (@snoopy101101)"]
bugs: ["Stored XSS", "Account takeover"]
bounty: "1,000"
publication_date: "2023-08-06"
added_date: "2023-08-08"
source: "pentester.land/writeups.json"
original_index: 880
scraped_via: "browseros"
---

# $1000 for a simple Stored XSS

$1000 for a simple Stored XSS
snoopy
Follow
Aug 6, 2023

316

2

I was hacking on a private program and I couldn't get anything interesting by fuzzing or using the website’s features.

Then I started looking at the JS files till I came across this beautiful code:

Press enter or click to view image in full size
I was like: No way

Based on the URL and the parameter names, it appears that this request might generate HTML pages containing arbitrary code.

Get snoopy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Testing Request:

Press enter or click to view image in full size

Simple exploit:

Press enter or click to view image in full size

The “transactionHtmlData” parameter was writing the HTML code inside our new HTML page.

Openning the file

alert(document.domain)

Press enter or click to view image in full size
Account Takeover

Fortunately the session cookie lacked the “HttpOnly” flag, which allowed me to obtain it using JavaScript and gain access to the victim’s account.

Press enter or click to view image in full size
The name of the session cookie was like “{Part-Of-The-Company-Name}2Auth”

Bounty:

Press enter or click to view image in full size

Reach me at:

LinkedIn:

https://www.linkedin.com/in/ali-imani-2a896a266/

twitter:

https://twitter.com/snoopy101101
