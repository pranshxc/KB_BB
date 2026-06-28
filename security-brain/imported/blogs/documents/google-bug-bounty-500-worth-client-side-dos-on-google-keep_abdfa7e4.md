---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-30_google-bug-bounty-500-worth-client-side-dos-on-google-keep.md
original_filename: 2021-07-30_google-bug-bounty-500-worth-client-side-dos-on-google-keep.md
title: 'Google Bug Bounty: $500 worth client-side DoS on Google Keep'
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: abdfa7e497662484f8400d55c13a61d681a482ad9dd315a8339ebc659921fdbe
text_sha256: dccd6c9b64674d295d94a85eb2b483fac64baef7b7ddcca61c8b5d9176040448
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Google Bug Bounty: $500 worth client-side DoS on Google Keep

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-30_google-bug-bounty-500-worth-client-side-dos-on-google-keep.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `abdfa7e497662484f8400d55c13a61d681a482ad9dd315a8339ebc659921fdbe`
- Text SHA256: `dccd6c9b64674d295d94a85eb2b483fac64baef7b7ddcca61c8b5d9176040448`


## Content

---
title: "Google Bug Bounty: $500 worth client-side DoS on Google Keep"
url: "https://infosecwriteups.com/google-bug-bounty-500-worth-client-side-dos-on-google-keep-35aab6aef279"
authors: ["Tommaso De Ponti (@heytdep)"]
programs: ["Google"]
bugs: ["Application-level DoS"]
bounty: "500"
publication_date: "2021-07-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3464
scraped_via: "browseros"
---

# Google Bug Bounty: $500 worth client-side DoS on Google Keep

Member-only story

Google Bug Bounty: $500 worth client-side DoS on Google Keep
A write-up about a Client-Side DoS on Keep that allowed me to block any user from accessing their keep notes
Tommaso De Ponti
Follow
3 min read
·
Jul 30, 2021

533

1

Press enter or click to view image in full size

[Friend Link for those with no subscription]

Hey there, those(if any) who follow me and track my work know that I haven’t posted about my findings in a while(I haven’t been hunting a lot lately), it’s time to fix that!

Today, I’m sharing with you how a simple payload chained with Google Keep notes functionalities could have allowed me to block any Google User to access its keep notes.

Also, I’ll be sharing more of my findings(I miss doing write-ups) and start tweeting Threads also about Cybersecurity and Bug Bounty.

Stay tuned to hear more about some sweet bugs on Vale, Wickr, Acronis, Basecamp, and more.

Why only $500 for such an impactful bug? DoS is rarely even accepted these days, I’m “lucky” they rewarded me.

The Bug

While testing I noticed that Keep has a maximum number of characters that can be in a note. And it has filters to prevent an attacker to write more.

I figured that if I am able to bypass the filter, some great things could happen. And…
