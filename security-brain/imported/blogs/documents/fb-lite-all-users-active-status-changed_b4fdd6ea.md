---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-14_fb-lite-all-users-active-status-changed.md
original_filename: 2022-01-14_fb-lite-all-users-active-status-changed.md
title: FB Lite All Users Active Status Changed
category: documents
detected_topics:
- command-injection
- business-logic
tags:
- imported
- documents
- command-injection
- business-logic
language: en
raw_sha256: b4fdd6ea2d6560825f84bca917f5d6917e92e4bb1936ceb757d06e654d8463f1
text_sha256: eec975913a71cc47a42aed290d6f0f5da7d6c8fc918fc2a88f812037b49ad898
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# FB Lite All Users Active Status Changed

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-14_fb-lite-all-users-active-status-changed.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `b4fdd6ea2d6560825f84bca917f5d6917e92e4bb1936ceb757d06e654d8463f1`
- Text SHA256: `eec975913a71cc47a42aed290d6f0f5da7d6c8fc918fc2a88f812037b49ad898`


## Content

---
title: "FB Lite All Users Active Status Changed"
url: "https://nmochea.medium.com/fb-lite-all-user-active-status-changed-99c5c36029e5"
authors: ["Neil Mark Ochea (@nmochea)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
publication_date: "2022-01-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3008
scraped_via: "browseros"
---

# FB Lite All Users Active Status Changed

FB Lite All Users Active Status Changed
Neil Mark Ochea / mhl_0xnmo
Follow
1 min read
·
Jan 13, 2022

11

1

I’m glad you’re here. Please have fun reading (nmochea).

This write-up is all about how I change all FB Lite users’ active status that logged in on the same device.

To be honest I accidentally discover this vulnerability when I logged in to multiple users’ accounts in the FB Lite application on the same device.

Get Neil Mark Ochea / mhl_0xnmo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

That time I turn off my active status in my user_1 when I switch my account user_1 to user_2 I was suddenly notified that user_2 has changed the active status too, wait wtf so I try to switch account again user_2 to user_3 and it’s all turn off active status, hmmm it pretty looks like vulnerability I created a report regarding this issue.

Press enter or click to view image in full size
Vulnerability Disclosure

October 23, 2020 – Reported the vulnerability.

October 28, 2020 – Triaged my report.

February 1, 2021 — Resolved and Bounty Rewarded.

Thanks for reading this article, I hope you guys learn something new today. Please share this article to spread the knowledge.
