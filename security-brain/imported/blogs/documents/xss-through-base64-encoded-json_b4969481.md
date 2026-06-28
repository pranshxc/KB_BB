---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-12_xss-through-base64-encoded-json.md
original_filename: 2022-03-12_xss-through-base64-encoded-json.md
title: XSS through base64 encoded JSON
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: b4969481b2ed9819d183bc20b1777a36dfb81a7222d87c5914cd99000f73d472
text_sha256: d441742b95b204e70df267e1794b31fbc1851f2c413558458834a0a3372625e4
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# XSS through base64 encoded JSON

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-12_xss-through-base64-encoded-json.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `b4969481b2ed9819d183bc20b1777a36dfb81a7222d87c5914cd99000f73d472`
- Text SHA256: `d441742b95b204e70df267e1794b31fbc1851f2c413558458834a0a3372625e4`


## Content

---
title: "XSS through base64 encoded JSON"
url: "https://apth3hack3r.medium.com/xss-through-base64-encoded-json-4b0d96e5ccd4"
authors: ["Aman Pareek (@aman_notsogreat)"]
bugs: ["XSS"]
publication_date: "2022-03-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2830
scraped_via: "browseros"
---

# XSS through base64 encoded JSON

XSS through base64 encoded JSON
Aman Pareek
Follow
2 min read
·
Mar 12, 2022

195

3

This is one of my very interesting and unexpected finding while testing an Application Tracking System.

Let the target be target.com and there was only one subdomain in scope let us call that sub.target.com. Now whenever you visit sub.target.com it would redirect to sub.target.com/members/index.php and after logging in the base URL would be like sub.target.com/members/modules/.

Get Aman Pareek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I did some basic walking of the application and couldn’t find anything worthwhile for almost a week but then i thought to fuzz and not just the base URL mentioned above but this sub.target.com/ using common php file names wordlist and found an interesting endpoint sub.target.com/i.php that looked like:

Press enter or click to view image in full size
Target Endpoint

We can see an GET base URL parameter at bottom of the page called “settings” which seems to take base64 encoded JSON lets verify:

Press enter or click to view image in full size
Decoded Base64

Cool, now lets try to enter some HTML in some of the value in decoded JSON and the encode it back to base64:

Press enter or click to view image in full size
XSS paylaod in JSON

Now we use the base64 encoded value of above JSON in the URL into settings parameter to get the XSS pop-up:

Press enter or click to view image in full size
XSS pop-up
