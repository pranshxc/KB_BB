---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-09_cookie-poisoning-leads-to-dos-and-privacy-violation.md
original_filename: 2021-04-09_cookie-poisoning-leads-to-dos-and-privacy-violation.md
title: Cookie poisoning leads to DoS and Privacy Violation
category: documents
detected_topics:
- ssrf
- command-injection
tags:
- imported
- documents
- ssrf
- command-injection
language: en
raw_sha256: 7271eca00597cc7f0bc74ef326c5d556eb24b5dfc1c2ef30bd487f6a1a8ed323
text_sha256: d3338b26bea595097e108a065428016ed2f0a3fe9e193c907069971f4d8490f1
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Cookie poisoning leads to DoS and Privacy Violation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-09_cookie-poisoning-leads-to-dos-and-privacy-violation.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `7271eca00597cc7f0bc74ef326c5d556eb24b5dfc1c2ef30bd487f6a1a8ed323`
- Text SHA256: `d3338b26bea595097e108a065428016ed2f0a3fe9e193c907069971f4d8490f1`


## Content

---
title: "Cookie poisoning leads to DoS and Privacy Violation"
url: "https://gatolouco.medium.com/cookie-poisoning-leads-to-dos-and-privacy-violation-8aa773547c96"
authors: ["Benjamin Walter"]
programs: ["CS Money"]
bugs: ["DoS", "SSRF"]
bounty: "700"
publication_date: "2021-04-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3751
scraped_via: "browseros"
---

# Cookie poisoning leads to DoS and Privacy Violation

Cookie poisoning leads to DoS and Privacy Violation
Benjamin Mauss
Follow
2 min read
·
Apr 9, 2021

150

1

When the verification goes wrong.

Avatar cookie contains the URL of the avatar image. But what if we change that?

Press enter or click to view image in full size

When I was hunting on cs.money, I noticed that the avatar cookie had the url for the user’s avatar on Steam. I changed the cookie to the URL of some other image and I saw that it was loading on the main page.

Until here there is nothing very special. We can load other images rather than the expected one. So what?

Get Benjamin Mauss’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Okay, I tried to chat with support and… my request got blocked. After playing around with the cookie value a little bit, I tried to insert part of the steam avatar url as a parameter for my server.

Privacy Violation
Press enter or click to view image in full size

Yes, I was right. The server was not checking the URL properly. The back-end verification was something like this (pseudocode):

Press enter or click to view image in full size

The right verification should be:

Press enter or click to view image in full size

I got a request on my server from the supporter browser. It tries to load the image url by sending a HTTP request to my server. So now I have access to supporter IP Address and User-Agent.

Denial of Service

Now, think. What if instead of the hacker server, we insert the cs.money logout URL? Bingo!

Press enter or click to view image in full size

The supporter browser makes a request to the logout URL and disconnect him.

Final thoughts

It is amazing to see how a small flaw, just a wrong verification o avatar cookie, have a impact like that.

Cs.money paid me a $ 500 reward (high impact at support.cs.money). As I had already reported the problem (able to change avatar to another images) and they closed as Not Applicable, they kindly gave me a $200 bonus. You can check my report here.

Let me know if you liked, clap!
