---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-08-19_demopaypalcom-nodejs-code-injection-rce.md
original_filename: 2016-08-19_demopaypalcom-nodejs-code-injection-rce.md
title: '[demo.paypal.com] Node.js code injection (RCE)'
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 77ccce46a28931601eec518a31352a38526ebf78a916ff8a8b0b05ce8af8773f
text_sha256: 80819f8cf8702a2594286e0874ec3756410d7cc5d9d2002c4ea3e98c992173af
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# [demo.paypal.com] Node.js code injection (RCE)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-08-19_demopaypalcom-nodejs-code-injection-rce.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `77ccce46a28931601eec518a31352a38526ebf78a916ff8a8b0b05ce8af8773f`
- Text SHA256: `80819f8cf8702a2594286e0874ec3756410d7cc5d9d2002c4ea3e98c992173af`


## Content

---
title: "[demo.paypal.com] Node.js code injection (RCE)"
page_title: "Artsploit"
url: "http://artsploit.blogspot.com/"
final_url: "https://artsploit.blogspot.com/"
authors: ["Michael Stepankin (@artsploit)"]
programs: ["Paypal"]
bugs: ["RCE"]
publication_date: "2016-08-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6268
---

When I first encountered Kafka UI, I was thrilled that such a dangerous functionality is exposed without authentication. After some time I discovered different ways to turn it to Remote Code Execution.

Here is the technical analysis of these vulnerabilities in my GitHub blog: <https://github.blog/security/vulnerability-research/3-ways-to-get-remote-code-execution-in-kafka-ui/>
