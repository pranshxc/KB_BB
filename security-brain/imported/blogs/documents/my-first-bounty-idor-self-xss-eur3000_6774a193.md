---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-02_my-first-bounty-idor-self-xss-3000.md
original_filename: 2022-02-02_my-first-bounty-idor-self-xss-3000.md
title: My first bounty, IDOR + Self XSS [€3000]
category: documents
detected_topics:
- xss
- idor
- command-injection
tags:
- imported
- documents
- xss
- idor
- command-injection
language: en
raw_sha256: 6774a193d370f093887ce3ca2d1790884dba3f2602455feedde8590584979235
text_sha256: 360ace39b1d2f345695240ebc9ab4a2b612d395e233d4bb3ae97e9154b2ec421
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# My first bounty, IDOR + Self XSS [€3000]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-02_my-first-bounty-idor-self-xss-3000.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `6774a193d370f093887ce3ca2d1790884dba3f2602455feedde8590584979235`
- Text SHA256: `360ace39b1d2f345695240ebc9ab4a2b612d395e233d4bb3ae97e9154b2ec421`


## Content

---
title: "My first bounty, IDOR + Self XSS [€3000]"
url: "https://medium.com/@ladecruze/my-first-bounty-idor-self-xss-3000-cde89cbbc1b1"
authors: ["Ladecruze (@ladecruze)"]
programs: ["Intigriti"]
bugs: ["Self-XSS", "IDOR"]
bounty: "3,000"
publication_date: "2022-02-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2947
scraped_via: "browseros"
---

# My first bounty, IDOR + Self XSS [€3000]

Member-only story

My first bounty, IDOR + Self XSS [€3000]
Ladecruze
Follow
6 min read
·
Feb 2, 2022

395

2

Every hacker would have come across this, the first bounty. I can’t actually explain how it feels but I know that most of you can understand how it feels. Let me tell you the story of my first bounty. When we started bug bounty in web application security, most of us would have started with XSS (Cross Site Scripting), the story starts from here.

Markdown — Websockets — Reflected XSS:

Before getting into the attack, let’s understand some basics of markdown, websockets and reflected xss.

Markdown

Markdown is a lightweight markup language that you can use to add formatting elements to plaintext text documents.

You could have come across this markdown when submitting reports in Intigriti, Bugcrowd or HackerOne. Markdown helps to represent the data better which improves the readability. Example,

# heading — Used for heading

** input ** — Used for bold text

Likewise backtick(`) is used to represent a code block.

Websockets

WebSocket is a computer communication protocol that operates over HTTP, and it provides a two-way communication channel between a client and a server.

Websockets are widely used by the chat applications to communicate without any hindrance. Unlike HTTP requests, a WebSocket connection stays open, and the server can send downstream data to the client anytime during the…
