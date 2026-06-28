---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-25_idor-revealing-images-cdn-links.md
original_filename: 2021-01-25_idor-revealing-images-cdn-links.md
title: IDOR Revealing Images CDN Links
category: documents
detected_topics:
- idor
- command-injection
- api-security
tags:
- imported
- documents
- idor
- command-injection
- api-security
language: en
raw_sha256: d0f8dbd8709c061abe6c46d3973ecc73c4422176e16cc231497c0403a683dc5b
text_sha256: 40dd1a08fc0a1dc733b884ef0f068b82ebf37783d132a93992b39a14ac8565c0
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR Revealing Images CDN Links

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-25_idor-revealing-images-cdn-links.md
- Source Type: markdown
- Detected Topics: idor, command-injection, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `d0f8dbd8709c061abe6c46d3973ecc73c4422176e16cc231497c0403a683dc5b`
- Text SHA256: `40dd1a08fc0a1dc733b884ef0f068b82ebf37783d132a93992b39a14ac8565c0`


## Content

---
title: "IDOR Revealing Images CDN Links"
url: "https://susanwagle123.medium.com/idor-revealing-images-cdn-links-6589e19bdbaf"
authors: ["susan wagle"]
bugs: ["IDOR"]
publication_date: "2021-01-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3970
scraped_via: "browseros"
---

# IDOR Revealing Images CDN Links

IDOR Revealing Images CDN Links
susan wagle
Follow
1 min read
·
Jan 25, 2021

23

Hi Bug Bounty community, this is my first write up for a bug I found in a private HackerOne program. Let’s call it redacted.com for this article.

So there was a subdomain for redacted.com which was something.redacted.com for people could post queries and answer then via comments.

One interesting thing that I noticed was there was a markdown editor as well. I uploaded a image and I attached it to the comment and after attaching the image in the comments what I noticed was the markdown editor was phrased like this [IMAGE]ID[IMAGE].

Get susan wagle’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Upon changing the image ID and posting the comment I would directly get access to the CDN Link of other people’s images, also the images that people deleted (which weren’t actually deleted from the CDN servers) and all the private images.

This issue was quite simple to exploit but was still a fun one to find.

TIMELINE

22 JAN 2021 — Reported.
24 JAN 2021 — Bounty awarded $XXX.
24 JAN 2021 — Triaged.
25 JAN 2021 — Fixed.
