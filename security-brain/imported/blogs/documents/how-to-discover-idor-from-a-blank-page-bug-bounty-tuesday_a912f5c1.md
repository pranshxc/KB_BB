---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-17_how-to-discover-idor-from-a-blank-page-bug-bounty-tuesday.md
original_filename: 2024-01-17_how-to-discover-idor-from-a-blank-page-bug-bounty-tuesday.md
title: How to Discover IDOR from a Blank Page — Bug Bounty Tuesday
category: documents
detected_topics:
- idor
- command-injection
tags:
- imported
- documents
- idor
- command-injection
language: en
raw_sha256: a912f5c12406eb0c0b34e3e75f4bfe8cc79bf64f9ed14b4d74a63495f389002e
text_sha256: 43aa962cb45d9531884ecbdefa7b2079cbd0e2ee91e7a957d891df769c059dd6
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# How to Discover IDOR from a Blank Page — Bug Bounty Tuesday

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-17_how-to-discover-idor-from-a-blank-page-bug-bounty-tuesday.md
- Source Type: markdown
- Detected Topics: idor, command-injection
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `a912f5c12406eb0c0b34e3e75f4bfe8cc79bf64f9ed14b4d74a63495f389002e`
- Text SHA256: `43aa962cb45d9531884ecbdefa7b2079cbd0e2ee91e7a957d891df769c059dd6`


## Content

---
title: "How to Discover IDOR from a Blank Page — Bug Bounty Tuesday"
page_title: "Discovering IDOR from a Blank Page (Bug Bounty) | OSINT Team"
url: "https://medium.com/@kerstan/how-to-discovered-idor-from-a-blank-page-bug-bounty-tuesday-5af784533d1a"
authors: ["kerstan"]
bugs: ["IDOR"]
bounty: "200"
publication_date: "2024-01-17"
added_date: "2024-01-18"
source: "pentester.land/writeups.json"
original_index: 533
scraped_via: "browseros"
---

# How to Discover IDOR from a Blank Page — Bug Bounty Tuesday

Press enter or click to view image in full size

Member-only story

How to Discover IDOR from a Blank Page
Discovering IDOR from a Blank Page (Bug Bounty)
kerstan
Follow
3 min read
·
Jan 16, 2024

92

1

kerstan - Medium
Read writing from kerstan on Medium. AI | Programming Knowledge | Bug Bounty Hunter X: https://x.com/kerstan_hunter…

medium.com

👉 Subscribed Me.

👉 Follow me: X.

Hello everyone, I’m Kerstan.
I will share with you how to discover IDOR from a blank page in a private program.🧐

So, let’s dive right in.

1. Find Endpoints

Within a private project, I encountered a webpage that was merely a blank page.

Press enter or click to view image in full size

Obviously, the page has only a few characters.

So I utilized F12 Developer Tools to examine if JavaScript offers additional information. As luck would have it, multiple endpoints were located, capable of retrieving data from the API.
