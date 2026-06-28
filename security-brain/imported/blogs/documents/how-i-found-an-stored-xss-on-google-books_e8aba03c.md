---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-18_how-i-found-an-stored-xss-on-google-books.md
original_filename: 2023-09-18_how-i-found-an-stored-xss-on-google-books.md
title: How i found an Stored XSS on Google Books
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
raw_sha256: e8aba03c08f8fc2bc695de084b96c651eac269b54d304f89f6885368783436b4
text_sha256: e7c977e99a985a404cd791ac8f305e9d222bb2c047765d15092839599171732a
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# How i found an Stored XSS on Google Books

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-18_how-i-found-an-stored-xss-on-google-books.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `e8aba03c08f8fc2bc695de084b96c651eac269b54d304f89f6885368783436b4`
- Text SHA256: `e7c977e99a985a404cd791ac8f305e9d222bb2c047765d15092839599171732a`


## Content

---
title: "How i found an Stored XSS on Google Books"
url: "https://medium.com/@cavdarbashas/how-i-found-an-stored-xss-on-google-books-732d9eb64e36"
authors: ["Sokol Çavdarbasha (@sokolicav)"]
programs: ["Google"]
bugs: ["Stored XSS"]
publication_date: "2023-09-18"
added_date: "2023-09-27"
source: "pentester.land/writeups.json"
original_index: 768
scraped_via: "browseros"
---

# How i found an Stored XSS on Google Books

How i found an Stored XSS on Google Books
Sokol Çavdarbasha
Follow
2 min read
·
Sep 18, 2023

161

4

Hello Hackers, I’m Sokol Çavdarbasha, I’m 20 years old from Kosovo and welcome to my first story about a vulnerability that i found on Google Books.

Great. Now that we’re done with that, we can get to the real thing this article’s about.

One day I decided to hunt for vulnerabilities on Google.I was looking to find XSS (Cross Site Scripting) . So i start to digg into google.com and i was focused on Google Books.

Press enter or click to view image in full size

So i thought why no to try here for XSS, and i type in search bar the following payload “><img src=x onerror=alert(1)>, and i got an book that another Security Researcher uploaded it to https://play.google.com

Press enter or click to view image in full size

so i press the “Preview” button and the XSS gets triggered

Press enter or click to view image in full size
XSS Trigger

the XSS triggered successfully, so i quickly report it to Google VRP Team at https://bughunters.google.com, and they responded quickly with a …

Press enter or click to view image in full size
Google Response

i was so happy that i got an “Nice catch” response from Google VRP Team with Priority P1 and Severity S1, and got rewarded $XXXX as this is my first valid bug that i reported to Google.

Get Sokol Çavdarbasha’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

PoC:

I hope that you enjoyed reading this article and sorry if there are things that are not clear.

Thanks for Reading : )

Sincerely,

Sokol Çavdarbasha.

You Can Follow me on :

Instagram: https://www.instagram.com/sokolcav

Linkedin: https://www.linkedin.com/in/sokol-%C3%A7avdarbasha-845426232/

Twitter: https://twitter.com/sokolicav
