---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-26_arbitrary-file-read-in-one-of-the-largest-crms.md
original_filename: 2018-09-26_arbitrary-file-read-in-one-of-the-largest-crms.md
title: Arbitrary File Read in one of the largest CRMs
category: documents
detected_topics:
- command-injection
- path-traversal
tags:
- imported
- documents
- command-injection
- path-traversal
language: en
raw_sha256: c03db80309ba01a8410d925953a16514e8bc1245c856277c45bf5167ab7c5692
text_sha256: 3e58b23e34f5b7fe6415431c60bdf5746b43c93ef03291f7104833d290a8a6af
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Arbitrary File Read in one of the largest CRMs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-26_arbitrary-file-read-in-one-of-the-largest-crms.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `c03db80309ba01a8410d925953a16514e8bc1245c856277c45bf5167ab7c5692`
- Text SHA256: `3e58b23e34f5b7fe6415431c60bdf5746b43c93ef03291f7104833d290a8a6af`


## Content

---
title: "Arbitrary File Read in one of the largest CRMs"
url: "https://medium.com/@mantissts/arbitrary-file-read-in-one-of-the-largest-crms-658caa2f05d2"
authors: ["Richard Clifford (@MantisSTS)"]
bugs: ["LFI"]
publication_date: "2018-09-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5679
scraped_via: "browseros"
---

# Arbitrary File Read in one of the largest CRMs

Arbitrary File Read in one of the largest CRMs
Richard Clifford
Follow
2 min read
·
Sep 26, 2018

36

Without going into too much detail as this was a private bug bounty program, I will explain how I managed to read arbitrary files on one of the largest Customer Relationship Managers (CRM).

First thing to point out was that this was not a quick find and it took quite a few days of non-stop poking around before I had even noticed the vulnerable parameter. The parameter was hidden within a JSON encoded lump of data which must have been parsed on the back-end without any validation.

Press enter or click to view image in full size
Example of the vulnerable request parameters

As with everything, I loaded up the request in Repeater and Intruder and went to town trying to identify any vulnerabilities here. Obviously, given the ‘page’ parameter I was hoping to get a file read bug. In intruder I loaded up some basic wordlists to go through but unfortunately it didn’t lead to any fruitful findings. So with one last attempt, I went through Repeater trying different combinations of payloads, encodings and escaping characters until I finally found a payload that worked. As I said before, this was a private program and I don’t want to disclose the exact payload that was used but it was very similar to this:

..\//..\//..\//{file}\;%00

Yes, I know that this isn’t an overly complex payload, nor should it have taken too long to identify it but what took the longest was finding and identifying the vulnerable parameter, not generating the payload itself.

Get Richard Clifford’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I found this vulnerability in multiple locations throughout the platform and the program paid me out for each item.

Initial finding (Listed above): $REDACTED
Finding #2 (Could only read config files): $REDACTED
Finding #3: $REDACTED
