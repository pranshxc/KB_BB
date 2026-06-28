---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-11_magic-of-the-back-slash.md
original_filename: 2020-05-11_magic-of-the-back-slash.md
title: Magic of the Back Slash
category: documents
detected_topics:
- command-injection
- path-traversal
tags:
- imported
- documents
- command-injection
- path-traversal
language: en
raw_sha256: 95d919ed238e228effbcd7bd3b4b8bb31f23a6972d096d4305b2b64eb72b836d
text_sha256: e5d31805855d560d639fd400a3ced763f0849915074af64a44f25712876d5c76
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Magic of the Back Slash

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-11_magic-of-the-back-slash.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `95d919ed238e228effbcd7bd3b4b8bb31f23a6972d096d4305b2b64eb72b836d`
- Text SHA256: `e5d31805855d560d639fd400a3ced763f0849915074af64a44f25712876d5c76`


## Content

---
title: "Magic of the Back Slash"
url: "https://medium.com/@aniltom/magic-of-the-back-slash-d868e66b532a"
authors: ["Anil Tom (mr_4nk)"]
bugs: ["Path traversal"]
bounty: "2,100"
publication_date: "2020-05-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4594
scraped_via: "browseros"
---

# Magic of the Back Slash

Member-only story

Magic of the Back Slash
Anil Tom
Follow
5 min read
·
May 11, 2020

261

1

Hello guys,

This is Anil back with another write-up on my bug hunting adventures. Here, I am sharing a few of my findings in one of the Bugcrowd Private Program.

Press enter or click to view image in full size

At Nullcon 2020, I met my fellow bug bounty hunters and we had discussion about bugs. They also shared their experiences and I was motivated from them because for the last few months I was not doing any bug hunting.

After Nullcon 2020 I came back and I was planning to do some bug hunting. And then I recollected a bug which I found earlier but I could not exploit. So, I started with it again at evening 7.30 and I was doing recon and trying to exploit it. However, till 10.30 PM I could not find any way to exploit it and I was frustrated like hell. Then I got a conference call from Eldho, Nesooh and Abdulali and we were talking about some of our future plans in YAS and many other things. I told them about my situation and they told me to change the target and take some new target.

So, I opened my Bugcrowd account and I checked in the Program invitation and there are some new Targets. I choose one of them and when I checked the program there is no vulnerabilities so far reported. And I was like “Okay I…
