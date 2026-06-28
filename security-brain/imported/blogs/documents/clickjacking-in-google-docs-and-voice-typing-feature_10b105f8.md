---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-05_clickjacking-in-google-docs-and-voice-typing-feature.md
original_filename: 2018-10-05_clickjacking-in-google-docs-and-voice-typing-feature.md
title: Clickjacking in Google Docs and Voice typing feature.
category: documents
detected_topics:
- clickjacking
- command-injection
tags:
- imported
- documents
- clickjacking
- command-injection
language: en
raw_sha256: 10b105f8e6013df0c4760bd06df80675c674cbc1f2956345eb40dd673107b7cb
text_sha256: 049df00e592a13406606ee19a7fb6be7420cce65c1a25f86e50bc57f80b881f3
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Clickjacking in Google Docs and Voice typing feature.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-05_clickjacking-in-google-docs-and-voice-typing-feature.md
- Source Type: markdown
- Detected Topics: clickjacking, command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `10b105f8e6013df0c4760bd06df80675c674cbc1f2956345eb40dd673107b7cb`
- Text SHA256: `049df00e592a13406606ee19a7fb6be7420cce65c1a25f86e50bc57f80b881f3`


## Content

---
title: "Clickjacking in Google Docs and Voice typing feature."
url: "https://medium.com/@raushanraj_65039/clickjacking-in-google-docs-and-voice-typing-feature-c481d00b020a"
authors: ["Raushan Raj (@raushan_rajj)"]
programs: ["Google"]
bugs: ["Clickjacking"]
bounty: "2,337"
publication_date: "2018-10-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5661
scraped_via: "browseros"
---

# Clickjacking in Google Docs and Voice typing feature.

Top highlight

Clickjacking in Google Docs and Voice typing feature.
Raushan Raj
Follow
1 min read
·
Oct 5, 2018

257

1

What is Clickjacking?

Unknowingly performing some sensitive actions on a webpage embedded(mostly in iframes) in any webpage with different or same domain/subdomain.

Google Docs page response doesn’t have x-frame-options headers i.e; it can be embedded into any other webpage.

There is a feature called voice typing in google docs where the user can speak and type in google docs.

Get Raushan Raj’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Tools → VoiceTyping → Click to speak

I have created a public google doc and embed it in an iframe into my webpage with allow microphone.

<iframe src=”https://docs.google.com/document/d/1VIhSkvFKar2bwHjORiI3GPT2wYWZ10P7QP42FpLrxY0/edit" allow=”microphone *”></iframe>

An attacker can then share the webpage with the victim and can record private conversations of the victim (with the help of few clicks).

Bounty: 2337$
