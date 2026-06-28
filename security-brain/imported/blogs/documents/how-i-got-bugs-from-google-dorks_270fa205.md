---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-25_how-i-got-bugs-from-google-dorks.md
original_filename: 2024-08-25_how-i-got-bugs-from-google-dorks.md
title: How I Got Bugs From Google Dorks
category: documents
detected_topics:
- command-injection
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: 270fa2059585066616cf15ddefc65666cc6a67e80f65126b0511122cf57bb380
text_sha256: 69c48b5af3af14af7109e69072a6bf803213737022a709ba62f84feac180861f
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# How I Got Bugs From Google Dorks

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-25_how-i-got-bugs-from-google-dorks.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `270fa2059585066616cf15ddefc65666cc6a67e80f65126b0511122cf57bb380`
- Text SHA256: `69c48b5af3af14af7109e69072a6bf803213737022a709ba62f84feac180861f`


## Content

---
title: "How I Got Bugs From Google Dorks"
page_title: "How I Got Sensitive Directory Using Google Dorks | by Ch4ndan das | Medium"
url: "https://ch44nd.medium.com/find-bugs-from-google-dorks-ec574c01471b"
authors: ["Chandan das"]
bugs: ["Information disclosure"]
publication_date: "2024-08-25"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 46
scraped_via: "browseros"
---

# How I Got Bugs From Google Dorks

How I Got Sensitive Directory Using Google Dorks
Ch4ndan das
Follow
2 min read
·
Aug 24, 2024

150

Hello everyone,

This is my first article. This article will talk about how to find information disclosure bug via google dorks. Let’s me introduce myself I’m Chandan das from India and I’m a web penetration tester.

Lets start !

The company didn’t want me to publish their name. For this reason, I’ll call it “redacted.com”. Let’s begin! I started hunting with some google dorks. ( site:redacted.com intitle:index.of) I found interesting directories.

Get Ch4ndan das’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

You want more details of google dorking click hare ==> https://pentest-tools.com/information-gathering/google-hacking (for automation)

Press enter or click to view image in full size

Then I click 2th website and I found dev.bz2 file download in my pc. Then open downloaded file (dev.bz 2) with winrar . I got the list of directories available with sensitive_data_exposure & disclosure_of_secrets. You can see in image .

Press enter or click to view image in full size
Press enter or click to view image in full size

Quickly I report this bug on bugcrowd after one day ago. I received reply from Bugcrowd this bug (P3) is valid But Duplicate.😞😞

Press enter or click to view image in full size

Thank you everyone for Reading 🧡

U can view my LinkedIn Profile

Happy Hunting :)))
