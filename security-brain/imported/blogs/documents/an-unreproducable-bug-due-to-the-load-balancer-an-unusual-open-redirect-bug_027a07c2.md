---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-27_an-unreproducable-bug-due-to-the-load-balancer-an-unusual-open-redirect-bug.md
original_filename: 2020-07-27_an-unreproducable-bug-due-to-the-load-balancer-an-unusual-open-redirect-bug.md
title: An unreproducable bug due to the load balancer, an unusual Open Redirect bug
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 027a07c2b59ff2aacdace5287405440b80a967fa21aec6f68541e989d5e83268
text_sha256: 8744e93e7d7dd20d54365842ad5ead57f075d3059a5b1c0f88fd42ce0089b9ac
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# An unreproducable bug due to the load balancer, an unusual Open Redirect bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-27_an-unreproducable-bug-due-to-the-load-balancer-an-unusual-open-redirect-bug.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `027a07c2b59ff2aacdace5287405440b80a967fa21aec6f68541e989d5e83268`
- Text SHA256: `8744e93e7d7dd20d54365842ad5ead57f075d3059a5b1c0f88fd42ce0089b9ac`


## Content

---
title: "An unreproducable bug due to the load balancer, an unusual Open Redirect bug"
url: "https://tolo7010note.blogspot.com/2020/07/an-unreproducable-bug-due-to-load.html"
final_url: "https://tolo7010note.blogspot.com/2020/07/an-unreproducable-bug-due-to-load.html"
authors: ["tololovejoi (@tolo7010)"]
bugs: ["Open redirect"]
publication_date: "2020-07-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4383
---

###  An unreproducable bug due to the load balancer, an unusual Open Redirect bug 

on  [ July 27, 2020  ](https://tolo7010note.blogspot.com/2020/07/an-unreproducable-bug-due-to-load.html "permanent link")

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

Note that some of you may have read it since this is a bug bounty writeup from my old blog (I deleted them last year while I took a long break from bug bounty hunting).

  

This writeup is posted for educational purpose and no real program name and / or endpoints are being disclosed. I will use example.com doman in the reproduce steps.

  

I found an Open Redirection bug accidentially while testing a private program man web application. This website was supposed to redirects any endpoint from www-prefix to non-www version. For example, visiting:

  

www.example.com/page1.php

  

Will redirect user to:

  

example.com/page1.php

  

But for some reason (honesty I am not from software development field) I believed that the developer extracted the URL path:

  

www.example.com/page1.php

  

Into an array:

  

[www.]

[example.com]

[page1.php]

  

And then connect each of them (except [www.]) before the redirection. They forgot to add '/' between the original path and the server redirected the user to:

  

example.compage1.php

  

As I don't have any web development skill I was not sure why they did this. It should not be that hard to just redirect user to non-www version of a URL (I guess they used this data for an analytic work). So I filed a report with a quick PoC:

  

Steps to reproduce:

  

\- Visit www.example.com/evil.com

\- You will be redirected to example.comevil.com

  

On next day the program team member could not reproduce the bug. I tried to go to the PoC again and now it correctly redirected me to example.com/evil.com

  

Now you may think that someone has fixed this but after several atempts on this same URL (I sent the link to the Burp Repeater and keep pressing the Enter key) I noticed that sometimes my PoC worked (and most of the time it didn't).

  

I gave this information to the team and we had a conclusion that I just (luckily) hit one of the loadbalancer servers which incorrectly implemented non-www redirection. The bug was fixed (and bounty rewarded) within a week.

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

#### Post a Comment

[](https://www.blogger.com/comment/frame/1228437028158683973?po=5321354488638945092&hl=en&saa=85391&origin=https://tolo7010note.blogspot.com&skin=emporio)
