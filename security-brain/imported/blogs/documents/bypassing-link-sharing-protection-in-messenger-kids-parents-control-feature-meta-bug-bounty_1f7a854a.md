---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-20_bypassing-link-sharing-protection-in-messenger-kids-parents-control-feature-meta.md
original_filename: 2023-04-20_bypassing-link-sharing-protection-in-messenger-kids-parents-control-feature-meta.md
title: Bypassing Link Sharing Protection in Messenger Kids Parent’s Control Feature
  | Meta Bug Bounty
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
raw_sha256: 1f7a854ae09861e73edaf6aab11d877e23f3b60afbcf39c57a198ac22122d996
text_sha256: 37d4f33b7d298cdbac81677591554775d263f76e4cd3357597a69c66df374e3e
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Link Sharing Protection in Messenger Kids Parent’s Control Feature | Meta Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-20_bypassing-link-sharing-protection-in-messenger-kids-parents-control-feature-meta.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `1f7a854ae09861e73edaf6aab11d877e23f3b60afbcf39c57a198ac22122d996`
- Text SHA256: `37d4f33b7d298cdbac81677591554775d263f76e4cd3357597a69c66df374e3e`


## Content

---
title: "Bypassing Link Sharing Protection in Messenger Kids Parent’s Control Feature | Meta Bug Bounty"
url: "https://zerocode-ph.medium.com/bypassing-link-sharing-protection-in-messenger-kids-parents-control-feature-meta-bug-bounty-e53f2d148bd9"
authors: ["Syd Ricafort (@devsyd11)"]
programs: ["Meta / Facebook"]
bugs: ["URL validation bypass"]
bounty: "500"
publication_date: "2023-04-20"
added_date: "2023-04-27"
source: "pentester.land/writeups.json"
original_index: 1240
scraped_via: "browseros"
---

# Bypassing Link Sharing Protection in Messenger Kids Parent’s Control Feature | Meta Bug Bounty

Bypassing Link Sharing Protection in Messenger Kids Parent’s Control Feature | Meta Bug Bounty
Syd Ricafort (0cod3)
Follow
2 min read
·
Apr 20, 2023

30

1

Press enter or click to view image in full size

Hello guys, this is Syd again for another article. Today I will share one of my findings in Meta BBP on how I bypassed link protection in Messenger Kids.

What is Messenger Kids?

Messenger Kids is an app for kids to connect and keep in touch with friends and family. Features include messaging, video calling, games, and stickers.

Using the Parent Dashboard from their Facebook account, parents can manage their child’s friends, monitor their activity, and change their account settings.

At the time of reporting, I was testing different functionality in the parent’s dashboard. Then I noticed that it has a link-sharing control. When it is off, contacts of the Kid’s account will be unable to send messages containing links as it will be blocked automatically by the server.

Get Syd Ricafort (0cod3)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I was thinking what if I can bypass this restriction will it becomes valid? So without wasting time, I tried to apply different techniques to bypass the link protection. First I tried to shorten the URL using tinyurl and then send it to the kid’s account but the server still blocked it. Next, I try to encode the URL but still it was blocked. I also tried to change the case characters of the URL for example from “google.com” => “GooGLE.com” but still it does not work.

Then I thought what if I append localhost at the end of the URL so instead of “google.com” now it becomes “google.com.localhost”. I tried to send the crafted URL and guess what it works. The server failed to validate now the URL and it was sent to the victim’s account.

I quickly created a report and submitted it to Meta. After 5 days my report was accepted and I was rewarded $500 for this report.

Report Timeline:
12/10/2022 -Submitted the report
12/15/2022 -Facebook Accepted my report
02/7/2023 -Vulnerability Fixed
02/18/2023 -Bounty Awarded

Video PoC:

Follow me on twitter https://twitter.com/devsyd11
