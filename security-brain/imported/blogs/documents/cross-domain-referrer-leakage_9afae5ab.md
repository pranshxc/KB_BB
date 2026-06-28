---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-31_cross-domain-referrer-leakage.md
original_filename: 2020-12-31_cross-domain-referrer-leakage.md
title: Cross Domain Referrer Leakage
category: documents
detected_topics:
- idor
- xss
- command-injection
- password-reset
- otp
- rate-limit
tags:
- imported
- documents
- idor
- xss
- command-injection
- password-reset
- otp
- rate-limit
language: en
raw_sha256: 9afae5ab101b2254a8d9c44215e8ad22f56bf5fa9f09c360e2feb4cfa1de92a4
text_sha256: e4a0daa31cc0e0504cf6149fd8e396ceb292a3caf5d7c74c66405d9d0be79307
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Cross Domain Referrer Leakage

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-31_cross-domain-referrer-leakage.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, password-reset, otp, rate-limit
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `9afae5ab101b2254a8d9c44215e8ad22f56bf5fa9f09c360e2feb4cfa1de92a4`
- Text SHA256: `e4a0daa31cc0e0504cf6149fd8e396ceb292a3caf5d7c74c66405d9d0be79307`


## Content

---
title: "Cross Domain Referrer Leakage"
url: "https://mohsinalibukc.medium.com/cross-domain-referrer-leakage-7873ada102ad"
authors: ["Mohsinalibukc"]
bugs: ["Cross-Domain Referrer Leakage"]
bounty: "300"
publication_date: "2020-12-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4037
scraped_via: "browseros"
---

# Cross Domain Referrer Leakage

Cross Domain Referrer Leakage
Mohsinalibukc
Follow
2 min read
·
Dec 30, 2020

253

1

It is my first writeup so please ignore the mistakes.

I was searching for a program where I can test my skills and finally got it, I can’t disclose the program name so I will call it “target”.

I tried all my skills on finding IDOR, CSRF, XSS etc. but it is secured. Then I go to password reset area, user enumeration & victim flooding is out of scope. Finally I go for Cross Domain referrer Leakage.

What is Cross Domain Referrer Leakage?

Get Mohsinalibukc’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I am here to discuss how to reproduce it, not for discussing what this vulnerability is, so for understanding that you can read this:

Cross-domain Referer leakage
When a web browser makes a request for a resource, it typically adds an HTTP header, called the "Referer" header…

portswigger.net

Steps to Reproduce:

Go to Password Reset area and send forget password link to your email address.
Copy the password reset link and paste in browser to which Burp-suite is configured.
Now turn on the intercept and capture the request.
First check for referrer header, then check for password reset link in that header. If you find link in referrer header then check host.
If there is complete password reset link including token, and host is third party website, it is vulnerability.
Press enter or click to view image in full size
Request will look like this

I reported this to target website and finally get a reward of 300 USD :)

Press enter or click to view image in full size

Thanks :)
