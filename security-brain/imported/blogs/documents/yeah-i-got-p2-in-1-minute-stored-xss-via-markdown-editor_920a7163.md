---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-02_yeah-i-got-p2-in-1-minute-stored-xss-via-markdown-editor.md
original_filename: 2019-07-02_yeah-i-got-p2-in-1-minute-stored-xss-via-markdown-editor.md
title: Yeah! I got P2 in 1 minute - Stored XSS via Markdown Editor
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 920a7163458836304d5e71275292026d4114236e33abb6619231547362d6f593
text_sha256: e181b0955153c96cd14ee67cda4cfb36a14f4e4dcd358bde01df4650236f1186
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Yeah! I got P2 in 1 minute - Stored XSS via Markdown Editor

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-02_yeah-i-got-p2-in-1-minute-stored-xss-via-markdown-editor.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `920a7163458836304d5e71275292026d4114236e33abb6619231547362d6f593`
- Text SHA256: `e181b0955153c96cd14ee67cda4cfb36a14f4e4dcd358bde01df4650236f1186`


## Content

---
title: "Yeah! I got P2 in 1 minute - Stored XSS via Markdown Editor"
page_title: "Bug Bounty: Stored XSS via Markdown (I got P2 in 1 minute!) | by November Rain | Medium"
url: "https://medium.com/@schopath/yeah-i-got-p2-in-1-minute-stored-xss-via-markdown-editor-7872dba3f158"
authors: ["Schopath"]
bugs: ["Stored XSS"]
publication_date: "2019-07-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5170
scraped_via: "browseros"
---

# Yeah! I got P2 in 1 minute - Stored XSS via Markdown Editor

Bug Bounty: Stored XSS via Markdown (I got P2 in 1 minute!)
November Rain
Follow
2 min read
·
Jul 2, 2019

91

1

Hello! I want to tell about my Bug Bounty Write-up, that was my fastest finding which has HIGH severity (P2).

I discovered Stored XSS vulnerability when I was reporting another Bug Bounty report.

The idiom says:
Kill two birds with one stone.

Okay, here we go!

While thinking some words to make a report, I was thinking to create XSS payload in markdown editor (but I didn’t expect to be an XSS issue).

Get November Rain’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

At the end of my report, I added a XSS Payload:

Cheers,

[Schopath](https://schopath.ninja/"/onmouseover="alert(/schopath/)"/x="ZeroByte.ID)

Then, I submit my report.

What the …
Boom! Gotcha!

Really? It’s work! and I still don’t believe it.
So many reports entered in that platform, only me who tried this?

Debugger (F12)
Press enter or click to view image in full size
View Source (CTRL + U)
Oh no, I’m just lucky kid

After that, I started to create my P2 submission.

Bonus! Markdown XSS payloads

Images:

![" onmouseover="alert(1);](https://img.uri/random.png)
![TEST](x"/onerror="alert`/Oops/`)

Anchor/URL/href:

[TEST](javascript:alert(document.domain))

Thank you for reading.
