---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-13_hacking-on-a-private-program-salseforce-crm.md
original_filename: 2022-07-13_hacking-on-a-private-program-salseforce-crm.md
title: Hacking on a Private Program (Salseforce crm)
category: documents
detected_topics:
- command-injection
- file-upload
tags:
- imported
- documents
- command-injection
- file-upload
language: en
raw_sha256: bcc77dcf42d963e844642aefb741d81e68c4c1c57c2959040c1948b5038d2f5e
text_sha256: d7c33c28795d065ccb4d3fecf60cfc88a370870c3c00f8b1c71f13c8d34524ce
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking on a Private Program (Salseforce crm)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-13_hacking-on-a-private-program-salseforce-crm.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `bcc77dcf42d963e844642aefb741d81e68c4c1c57c2959040c1948b5038d2f5e`
- Text SHA256: `d7c33c28795d065ccb4d3fecf60cfc88a370870c3c00f8b1c71f13c8d34524ce`


## Content

---
title: "Hacking on a Private Program (Salseforce crm)"
url: "https://thinkermaruf.medium.com/hacking-on-a-private-program-salseforce-crm-12bfef43fcc7"
authors: ["Maruf Hosan (@thinkermaruff)"]
bugs: ["RCE", "OS command injection"]
bounty: "300"
publication_date: "2022-07-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2459
scraped_via: "browseros"
---

# Hacking on a Private Program (Salseforce crm)

Hacking on a Private Program (Salseforce crm)
Md Maruf Hosan (0xMaruf)
Follow
2 min read
·
Jul 11, 2022

7

I was hunting on a private program of HackerOne so lets call it developer.target.com i found a register option so i registered there after some recon i found that its a salseforce crm
while logging i encountered that it was logging through okta.

and my first attempt was logging okta to get some juicy stuff. cz account created on okta.
so i hit this target.okta.com than i logged in and encountered an error
which was

after watching that i changed my date and time but still getting same error.
after a lot of research i found that the issue can be resolved from okta console only.
so i lost hope from okta.
then i came back to developer.target.com logged in found nothing juicy
except this https://developer.target.com/developer/s/settings/{profileID}

then after wasting some time i changed this directory settings to profile like this https://developer.target.com/developer/s/profile/{profileID} and boom i have found more options including file uploading feature.
so i tried to upload php,jsp,asp files but getting no preview except jpg,png and other ext for image.

Get Md Maruf Hosan (0xMaruf)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

and more recon i found this endpoint https://developer.target.com/developer/s/sfsites/c/sfc/servlet.shepherd/doucument/download/{fileID}

after watching this i knew it what i have to do, i uploaded a csv file including csv injection payload and copied the fileID and put that here https://developer.target.com/developer/s/sfsites/c/sfc/servlet.shepherd/document/download/001fdkd193

then i opened this link from another browser did not work, i again opened that link as an authenticated user,means ACCOUNT on devloper.target.com

and boom file was downloaded, once other devs open the csv file OS command gets executed on their machine.
payload in csv file: =10+20+cmd|' /C calc'!A0

the system should filter these =,+,-,@ in start of every cell

and i was awarded a $300 bounty for that.

follow me: https://twitter.com/0xmaruf
