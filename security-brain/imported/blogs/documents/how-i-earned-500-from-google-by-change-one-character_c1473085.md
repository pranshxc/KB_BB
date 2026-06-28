---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-06_how-i-earned-500-from-google-by-change-one-character-.md
original_filename: 2020-06-06_how-i-earned-500-from-google-by-change-one-character-.md
title: How i earned $500 from google by change one character .
category: documents
detected_topics:
- csrf
- command-injection
- otp
tags:
- imported
- documents
- csrf
- command-injection
- otp
language: en
raw_sha256: c14730858005be15acc4d68e316fb21ed74937b2beda5eb6d71dac8c6593b452
text_sha256: 3553fe227665fcb91eb50cb9414e4de75c694d51fe9c6ff25ec594508c004140
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# How i earned $500 from google by change one character .

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-06_how-i-earned-500-from-google-by-change-one-character-.md
- Source Type: markdown
- Detected Topics: csrf, command-injection, otp
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `c14730858005be15acc4d68e316fb21ed74937b2beda5eb6d71dac8c6593b452`
- Text SHA256: `3553fe227665fcb91eb50cb9414e4de75c694d51fe9c6ff25ec594508c004140`


## Content

---
title: "How i earned $500 from google by change one character ."
url: "https://medium.com/@odayalhalbe1/how-i-earned-500-from-google-by-change-one-character-8350d2b618e5"
authors: ["Oday Alhalbe"]
programs: ["Google"]
bugs: ["CSRF"]
bounty: "500"
publication_date: "2020-06-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4520
scraped_via: "browseros"
---

# How i earned $500 from google by change one character .

How i earned $500 from google by change one character .
Greetings,
Oday Alhalabi
Follow
2 min read
·
Jun 7, 2020

249

My name is oday and today i will share one bug in Google from 4 bugs i discovered, Which is in “admanager”. I was able to turn off/on notification email victim account by bypassing the CSRF protection .

What is Cross site scripting forgery?

“Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they’re currently authenticated”.

Let’s start ..

When sign in to your account on admanager.google.com for first time,you will note that there is option to modify email notification settings.

Get Oday Alhalabi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I capture request using burp suite and i am start to try bypass CSRF_TOKEN:

Press enter or click to view image in full size

As you can see the security_token sent as parameter .I tried different ways to bypass security_token ,but unfortunately i couldn’t bypass it :( .

After try all bypass ways ,i crossed my mind to add random value with same length for security_token .And boom it work :)

After that i change just one character on my security_token ,and i tried poc on different accounts and it worked also .

Google vrp rewarded me $500 for this bug :D

Press enter or click to view image in full size
