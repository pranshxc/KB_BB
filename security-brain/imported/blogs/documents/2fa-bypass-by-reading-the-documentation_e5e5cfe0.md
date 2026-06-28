---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-09_2fa-bypass-by-reading-the-documentation.md
original_filename: 2022-01-09_2fa-bypass-by-reading-the-documentation.md
title: 2FA bypass by reading the documentation
category: documents
detected_topics:
- mfa
- api-security
- access-control
- command-injection
tags:
- imported
- documents
- mfa
- api-security
- access-control
- command-injection
language: en
raw_sha256: e5e5cfe0b13685fd7764e19956d630bcb0262152b0d1cc73283c33ad22963314
text_sha256: a6ae5b7c0feb49ff212be3711e35086426ec7ff2266f650d821ac83ce2d2c611
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# 2FA bypass by reading the documentation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-09_2fa-bypass-by-reading-the-documentation.md
- Source Type: markdown
- Detected Topics: mfa, api-security, access-control, command-injection
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `e5e5cfe0b13685fd7764e19956d630bcb0262152b0d1cc73283c33ad22963314`
- Text SHA256: `a6ae5b7c0feb49ff212be3711e35086426ec7ff2266f650d821ac83ce2d2c611`


## Content

---
title: "2FA bypass by reading the documentation"
url: "https://noob3xploiter.medium.com/2fa-bypass-by-reading-the-documentation-3260a372d8a8"
authors: ["tomorrowisnew (@tomorrowisnew_)"]
bugs: ["2FA / MFA bypass"]
bounty: "100"
publication_date: "2022-01-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3022
scraped_via: "browseros"
---

# 2FA bypass by reading the documentation

2FA bypass by reading the documentation
Brandon Roldan
Follow
2 min read
·
Jan 9, 2022

47

This is a fairly simple and short writeup, but i think is worth sharing, so lets get started.

This program is private so i will be redacting most of the information from it.

Like any other website, my program has a 2fa implemented, and their implementation is pretty good too. So i started reading the documentation. Most of the api functions requires api key for authorization

And this api key can be only obtained in the web client after logging in which require a 2fa verification. However, while reading other api functions, i found one odd api method.

Unlike the other api methods, it doesnt use the api key for authorization. Instead, it uses a basic authentication stated by the -u and only requires the email and the password . After trying it out myself, the request succeeds without the 2fa verification.

Get Brandon Roldan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This is fixed now and is accepted as low since it requires knowing the credentials of the target and only one api method is vulnerable but still interesting for me nonetheless.

Press enter or click to view image in full size

Thanks for reading, Join the Bounty Hunter Discord Server: https://discord.gg/bugbounty
