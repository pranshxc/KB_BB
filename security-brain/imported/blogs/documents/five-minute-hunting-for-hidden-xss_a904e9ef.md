---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-15_five-minute-hunting-for-hidden-xss.md
original_filename: 2022-08-15_five-minute-hunting-for-hidden-xss.md
title: Five-minute hunting for hidden XSS
category: documents
detected_topics:
- xss
- command-injection
- otp
- rate-limit
- api-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- rate-limit
- api-security
language: en
raw_sha256: a904e9ef0b39b2e794fef00fb79b67959024f7f0271ac45887c55b0897701b75
text_sha256: f744f51a3a6a23ef0ddc59e658ba9f854a8b24308ac32dda2f5bdc842f1049b5
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: true
---

# Five-minute hunting for hidden XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-15_five-minute-hunting-for-hidden-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: True
- Raw SHA256: `a904e9ef0b39b2e794fef00fb79b67959024f7f0271ac45887c55b0897701b75`
- Text SHA256: `f744f51a3a6a23ef0ddc59e658ba9f854a8b24308ac32dda2f5bdc842f1049b5`


## Content

---
title: "Five-minute hunting for hidden XSS"
page_title: "Five-minute hunting for hidden XSS - Bergee's Stories on Bug Hunting"
url: "https://bergee.it/blog/five-minute-hunting-for-hidden-xss/"
final_url: "https://bergee.it/blog/five-minute-hunting-for-hidden-xss/"
authors: ["Bartłomiej Bergier (@_bergee_)"]
bugs: ["Reflected XSS"]
publication_date: "2022-08-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2309
---

# Five-minute hunting for hidden XSS

Posted on [2022-08-152026-04-27](https://bergee.it/blog/five-minute-hunting-for-hidden-xss/) by [bergee](https://bergee.it/blog/author/bergee/)

One night I was about to go to sleep, however, set the goal of finding the bug within a max of 15 minutes. I did some google dorking like this:

> site:*.target.com ext:php

I found the site with an admin panel on it. I tried to log in with some common credentials combinations such as admin/admin, admin/test, test/test, etc., but nothing worked. I got the message: “Inloggen / Log In ((failed))”. I was about to give up here as I don’t like to brute force the credentials, as I saw GET parameter named e which was BASE64 encoded string. I decoded it and saw the following string:

> start.php?do=start|(failed)|***REDACTED-SUSPECT-TOKEN***Hmm, the same “(failed)” was visible after failed login. Now you may guess the rest :). What if I change this “(failed)” part of the string into XSS payload “<img src=x onerror=alert(document.domain)>”, so the string will be:

> start.php?do=start|<img src=x onerror=alert(document.domain)>|***REDACTED-SUSPECT-TOKEN***After encoding to base64 it would be:

> c3RhcnQucGhwP2RvPXN0YXJ0fDxpbWcgc3JjPXggb25lcnJvcj1hbGVydChkb2N1bWVudC5kb21haW4pPnxiNTZkZDhkZjI4***REDACTED-SUSPECT-TOKEN***So the final URL was:

> https://redacted.com/admin/index.php?e=c3RhcnQucGhwP2RvPXN0YXJ0fDxpbWcgc3JjPXggb25lcnJvcj1hbGVydChkb2N1bWVudC5kb21haW4pPnxiNTZkZDhkZjI4***REDACTED-SUSPECT-TOKEN***And guess what? It worked. I managed to get reflected XSS. Now I know, in this case, it was pretty easy escalable to account takeover, however I stopped on XSS back then.

![](https://bergee.it/blog/wp-content/uploads/2022/08/xss_base64_redacted.jpg)

Reward: Hall Of Fame

See you next bug 🙂
