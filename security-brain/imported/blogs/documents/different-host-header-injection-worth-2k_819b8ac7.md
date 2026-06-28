---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-07_different-host-header-injection-worth-2k.md
original_filename: 2020-06-07_different-host-header-injection-worth-2k.md
title: Different host header injection worth 2k
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 819b8ac7f26e3671d800919da8ac44d42d36c41cdd64137fe47fdcbce527f57d
text_sha256: 1f95627aff64ec69cd1d2ed66591d6c4d070bb2b9e852c63b355a06cb3b3a71d
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Different host header injection worth 2k

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-07_different-host-header-injection-worth-2k.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `819b8ac7f26e3671d800919da8ac44d42d36c41cdd64137fe47fdcbce527f57d`
- Text SHA256: `1f95627aff64ec69cd1d2ed66591d6c4d070bb2b9e852c63b355a06cb3b3a71d`


## Content

---
title: "Different host header injection worth 2k"
url: "https://medium.com/@imunissar786/awesome-host-header-injection-worth-2k-a7e5be1dbb1d"
authors: ["Imran Nissar (@Imrannissar3)"]
bugs: ["Host header injection"]
bounty: "2,000"
publication_date: "2020-06-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4519
scraped_via: "browseros"
---

# Different host header injection worth 2k

Different host header injection worth 2k
Imran Nissar
Follow
2 min read
·
Jun 7, 2020

303

4

1

Hello guy’s i hope you’re doing great in this story i will be covering beautiful/challenging host header injection.

So the story goes like when i was new to bug bounty i was very curious one night i was trying to sleep i got the notification that let’s call it redacted program is now public as we know when someone is new to this field their is a strange excitement i fired up kali and began testing.

In this post i won’t be covering the basics of what host header injection is if you don’t know i would suggest you to google it thank you.

So in some few minutes i found this vulnerability called host header injection i reported but deep down i was getting feeling that this will be a dupe but lucky me when i woke up in the morning they already had fixed it and awarded me 1000$ bounty as it was my first 4 digit bounty but the story doesn’t seem to end here.

So i began to retest the same functionality i noticed that they are still accepting the user input as i don’t know why but their was a surprise they were not accepting anything like evil.com or something like this but only some few symbols that were # and ? but i noticed anything after ? for example

Get Imran Nissar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Host: redacted.com?anythin<b>imran</b>

It was getting reflected in the email so i thought let’s try <a href> tag in the host header

So the final payload that successfully erased the original host with the one given was

Host: redacted.com?"><a href='evil.com

Reported the bypass got rewarded again with some extra bonus this time.

I hope you guy’s have liked it sorry for any mistakes as this one is my first writeup.

Thank you
