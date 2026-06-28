---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-25_my-first-two-valid-and-rewarded-web-cache-deceptions-earning-2250.md
original_filename: 2023-06-25_my-first-two-valid-and-rewarded-web-cache-deceptions-earning-2250.md
title: My first two valid and rewarded Web Cache Deceptions, earning $2250
category: documents
detected_topics:
- command-injection
- otp
- csrf
- api-security
tags:
- imported
- documents
- command-injection
- otp
- csrf
- api-security
language: en
raw_sha256: 5b5c612aac02e68538041737b4baeab317a8e77a471fa9960f06c738dc701886
text_sha256: 3b63487df059e1ac2eb9800475de8a440db20f72553e7c44c76e2e2d6f3be657
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# My first two valid and rewarded Web Cache Deceptions, earning $2250

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-25_my-first-two-valid-and-rewarded-web-cache-deceptions-earning-2250.md
- Source Type: markdown
- Detected Topics: command-injection, otp, csrf, api-security
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `5b5c612aac02e68538041737b4baeab317a8e77a471fa9960f06c738dc701886`
- Text SHA256: `3b63487df059e1ac2eb9800475de8a440db20f72553e7c44c76e2e2d6f3be657`


## Content

---
title: "My first two valid and rewarded Web Cache Deceptions, earning $2250"
url: "https://medium.com/@hbenja47/my-first-two-valid-and-rewarded-web-cache-deceptions-earning-2250-c8d2a6968713"
authors: ["Benja (bronxi) (@hbenja_m)"]
bugs: ["Web cache deception", "CSRF"]
bounty: "2,250"
publication_date: "2023-06-25"
added_date: "2023-06-27"
source: "pentester.land/writeups.json"
original_index: 1010
scraped_via: "browseros"
---

# My first two valid and rewarded Web Cache Deceptions, earning $2250

Benja (bronxi)
 highlighted

My first two valid and rewarded Web Cache Deceptions, earning $2250
Benja (bronxi)
Follow
2 min read
·
Jun 26, 2023

834

9

In April, I became interested in understanding how vulnerabilities related to web cache worked: web cache deception and web cache poisoning. I started with WCD and came across @bxmbon’s write-ups, which also mentioned findings of WCP. I also read Omer Gil’s white paper about WCD.

My First Web Cache Deception

In this case, I managed to cache the victim’s email, full name, role, and other info like a CSRF token. Obviously, one of the requirements for it to work was that the victim was already logged into the application, and the other requirement was that the attacker also had an account on the platform, otherwise accessing the data cached by the victim was not possible.

Steps to reproduce this bug:

The victim logs in.
The attacker sends the URL https://redacted/account/something.avif to the victim.
The victim clicks on https://redacted/account/something.avif.
The attacker logs into their account, goes to https://redacted/account/something.avif, and receives a 404 error. However, the victim’s email, user ID, and CSRF token can be read in the code.

In this case, many extensions worked for caching: avif, js, css, ico, etc.

May 9, 2023: Reported

May 22, 2023: Changed the severity to P2

May 22, 2023: Triaged

Get Benja (bronxi)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

May 24, 2023: Rewarded bronxi $1,750

My Second Web Cache Deception

In this case, I was able to obtain the victim’s email, phone number, full name, address, and even the PHPSESSID cookie. However, I couldn’t achieve an account takeover because it used an additional cookie to authenticate the session, and I couldn’t obtain that cookie.

Steps to reproduce this bug:

The attacker sends the following link to the victim: https://www.redacted2.com/bussines.php/non-existent.js
The victim opens the link, and the page loads normally (the web cache mechanism then saves this page).
The attacker opens the same link (https://www.redacted2.com/bussines.php/non-existent.js), and the victim’s personal page with all their private content is loaded.

In this case, when attempting to view the cached data in the web browser, it immediately redirected to the login page. So it seemed like WCD wasn’t working. However, if you observed the response prior to the redirection in Burp, the data was cached.

May 1, 2023: Reported

May 23, 2023: Changed the severity to P2

May 23, 2023: Triaged

June 5, 2023: Rewarded bronxi $500

Tips:

Remember that a 404 error can also cache sensitive information.
If you’re redirected, check the responses in Burp.
Try accessing cached data from another network. Sometimes it’s a requirement for the program’s proof of concept. Sometimes they may accept it if it’s from the same network and the application is used in a public space.

Happy hacking!
