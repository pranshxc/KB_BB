---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-28_stored-xss-on-edmodo.md
original_filename: 2019-05-28_stored-xss-on-edmodo.md
title: Stored XSS on Edmodo
category: documents
detected_topics:
- xss
- idor
- command-injection
- rate-limit
- supply-chain
tags:
- imported
- documents
- xss
- idor
- command-injection
- rate-limit
- supply-chain
language: en
raw_sha256: f3ee16a5e24697391c608b1bd09035db730dd5f7f70c1fcbfbb58bc0362a0d6b
text_sha256: 435b7dfc75476bff4674ece3f5752c4a3876c46593744df8e9430e2d6f3857b6
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS on Edmodo

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-28_stored-xss-on-edmodo.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, rate-limit, supply-chain
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `f3ee16a5e24697391c608b1bd09035db730dd5f7f70c1fcbfbb58bc0362a0d6b`
- Text SHA256: `435b7dfc75476bff4674ece3f5752c4a3876c46593744df8e9430e2d6f3857b6`


## Content

---
title: "Stored XSS on Edmodo"
url: "https://medium.com/@matarpan33r/stored-xss-on-edmodo-67b244824fa5"
authors: ["Rohit Verma (@rv0x00)"]
programs: ["Edmodo"]
bugs: ["Stored XSS"]
publication_date: "2019-05-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5240
scraped_via: "browseros"
---

# Stored XSS on Edmodo

Stored XSS on Edmodo
Rohit Verma
Follow
1 min read
·
May 28, 2019

97

Hello everyone,
I believe sharing is caring, and I have been learning from multiple security researchers in the Infosec community. So here is the write-up of my recent finding.

The web application allows you to create a virtual library.
In the library, you can add files, folder, links, quiz.
And when a user adds the name to the folder with evil chars, it was sanitized correctly.

After hours of enumeration, I found another endpoint where only the folder name was getting reflected, and it was not correctly being sanitized.

Below are the steps to reproduce the stored XSS vulnerability:

Get Rohit Verma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1: Open Https://edmodo.com/library
2: Make a new folder
3: Input this payload “</title></head><body onload=alert(1)></body><! — “ in the name field.
4: Intercept the request and note down the [folder-id]
5: Open https://www.edmodo.com/folder/[folder-id], a pop-up will come.

Press enter or click to view image in full size

Thanks, everyone for reading my write-up!

Thanks a lot, Chip for quick responses and cool swag.

About me:
https://twitter.com/5eren1ty

https://facebook.com/5eren1ty
