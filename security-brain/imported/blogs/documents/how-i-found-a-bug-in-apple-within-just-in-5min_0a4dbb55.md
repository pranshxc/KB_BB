---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-25_how-i-found-a-bug-in-apple-within-just-in-5min.md
original_filename: 2021-07-25_how-i-found-a-bug-in-apple-within-just-in-5min.md
title: How I found a bug in Apple within just in 5min.
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
raw_sha256: 0a4dbb554b954af546bba215a5be057666033ba444715ef00841a1476b758fae
text_sha256: b12228dd965d486ceeb633bea0ba9f0bd21a137fe0c951849de654e9e87b0060
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How I found a bug in Apple within just in 5min.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-25_how-i-found-a-bug-in-apple-within-just-in-5min.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `0a4dbb554b954af546bba215a5be057666033ba444715ef00841a1476b758fae`
- Text SHA256: `b12228dd965d486ceeb633bea0ba9f0bd21a137fe0c951849de654e9e87b0060`


## Content

---
title: "How I found a bug in Apple within just in 5min."
url: "https://medium.com/pentesternepal/how-i-found-a-bug-in-apple-within-just-in-5min-d7357237d7a0"
authors: ["Akash basnet (@noneofyou007)"]
programs: ["Apple"]
bugs: ["XSS"]
publication_date: "2021-07-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3481
scraped_via: "browseros"
---

# How I found a bug in Apple within just in 5min.

How I found a bug in Apple within just in 5min.
Akash basnet
Follow
2 min read
·
Jul 25, 2021

334

3

Summary: I discovered a Cross-site Scripting (XSS) vulnerability in one of the acquisition sites of apple which is Filemaker.com

It was May 15, 2020, I was looking in Apple web server notifications.

In which an article provides credit to people who have reported potential security issues in Apple’s web servers. I noticed here that apple is giving credit to researchers here along with the domain in which they found a bug, I was scrolling & found an acquisition domain name called “Filemaker.com” I quickly visit to see that if I can find any bug there..!

I was checking the tabs in a site where I found the event tab I click on it

www.filemaker.com/events/submission.html

Now here I can create an event that has a certain field to fill the event details. I quickly fill the fields with XSS payload wherever it is possible to put :D. And at last, I preview the form now the XSS is executed here BOOM !!!! :V.

Press enter or click to view image in full size
XSS executed after filling the fields with payload & click on the preview!

I quickly made a report & sent it to product-security@apple.com and they reply with an automated email response of receiving the report on May 19, 2020.

Get Akash basnet’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

On May 27, 2020, They fixed the issue & reply with this below email:-

Press enter or click to view image in full size
Although this issue does not qualify for a reward through the Apple Security Bounty program, we do provide the recognition of being listed in our security advisory when a reported issue is addressed.

I was aware of this but I was happy to be listed in their security advisory.

you can find my name on below Apple Credit page:-

Apple web server notifications
A server configuration issue was addressed. We would like to acknowledge Joseph Thacker for reporting this issue…

support.apple.com

#Moral:- If you didn’t found a bug in the main domain look into the acquisition domain.

Here is the proof of concept video file in the link below:-

URL:- https://youtu.be/LQBJIzcXphI

#Bugbounty

Regards
