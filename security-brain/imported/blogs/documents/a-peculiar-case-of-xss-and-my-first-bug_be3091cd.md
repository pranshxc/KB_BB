---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-01_a-peculiar-case-of-xss-and-my-first-bug.md
original_filename: 2022-02-01_a-peculiar-case-of-xss-and-my-first-bug.md
title: A Peculiar Case of XSS and my first bug
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
raw_sha256: be3091cd724401259220aece27e6f49dce2d9f379893408b43831bd9e2e7a2b8
text_sha256: 0ab15d4bc4463f9c88931d0e05a28c10a1074f5a17f87a13afa606d3df2989b0
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# A Peculiar Case of XSS and my first bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-01_a-peculiar-case-of-xss-and-my-first-bug.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `be3091cd724401259220aece27e6f49dce2d9f379893408b43831bd9e2e7a2b8`
- Text SHA256: `0ab15d4bc4463f9c88931d0e05a28c10a1074f5a17f87a13afa606d3df2989b0`


## Content

---
title: "A Peculiar Case of XSS and my first bug"
url: "https://systemweakness.com/a-peculiar-case-of-xss-and-my-first-bug-19f2132390b6"
authors: ["Aman Pareek (@aman_notsogreat)"]
programs: ["Bentley Systems"]
bugs: ["XSS"]
publication_date: "2022-02-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2953
scraped_via: "browseros"
---

# A Peculiar Case of XSS and my first bug

A Peculiar Case of XSS and my first bug
Aman Pareek
Follow
3 min read
·
Feb 1, 2022

17

Hello everyone, I am new to security stuff and will share how I was able to get few XSS in not so common way.

After a lot of confusion about which program to hunt on, I somehow decided to hunt on bentley.com
And after gathering all possible subdomains (around 3000) i ran aquatone to get screenshots and started looking for something different type of subdomains.
And I came across some similar subdomains which looked like:

Press enter or click to view image in full size

And sub-domain was http://bip01.assetwiseonline.bentley.com/

And after some playing around with source of the page i stumbled upon an endpoint which was a login page:

Press enter or click to view image in full size
(This endpoint is removed now)

When you enter any arbitrary values in form and submit it then some text appears on screen which comes from “notification_msg” URL parameter.

And there is some weird text at the end on the URL which actually is something called md5_checksum which uniquely identifies the value of notification value.

Get Aman Pareek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now if we enter some arbitrary value to notification_msg (e.g. finally) this happens:

Press enter or click to view image in full size
checksum_error

Now this string is actually md5_checksum of entered text so we just replace it in URL to get this:

Press enter or click to view image in full size
(You can see text passed to url parameter is reflected now).

The parameter (notification_msg) does have some filter which prevented normal payloads but if we add ‘>’ just before last entered text in notification_msg (i.e. finally) so it becomes “notification_msg= >finally ” it gets directly reflected (without checksum error):

Press enter or click to view image in full size

Now modifying parameter to “><finally>” we get this:

Press enter or click to view image in full size

Something is not right let’s see source of this page:

Press enter or click to view image in full size

HTML5 treats finally like a tag and completes it. Now if we use some self-closing HTML tag to trigger XSS but generate its md5_checksum first. So we enter img src=1 onerror=alert(document.cookie) in the notification_msg to get its md5_checksum (and we retain this for later use):

Press enter or click to view image in full size
checksum for payload

Now if we add “><” and “>” before and after the value of notification_msg in URL and finally we get the popup:

Press enter or click to view image in full size
XSS triggered

And this was story of my first bug.
