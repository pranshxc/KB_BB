---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-11_same-bug-different-platform.md
original_filename: 2022-06-11_same-bug-different-platform.md
title: Same bug different platform
category: documents
detected_topics:
- access-control
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 9253eda06644e952112e1212405c6b5d5cbded0fcf209af4a73a1336e092ea1c
text_sha256: de03483bbaff646fa066e8966256a4e7ad8309735fb6b27af21b1e4b9cd4ffed
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Same bug different platform

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-11_same-bug-different-platform.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `9253eda06644e952112e1212405c6b5d5cbded0fcf209af4a73a1336e092ea1c`
- Text SHA256: `de03483bbaff646fa066e8966256a4e7ad8309735fb6b27af21b1e4b9cd4ffed`


## Content

---
title: "Same bug different platform"
url: "https://prajwoldhungana487.medium.com/same-bug-different-platform-4c648e91af6b"
authors: ["Prajwol Dhungana (@PrajwolDhunga14)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Broken authorization"]
publication_date: "2022-06-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2566
scraped_via: "browseros"
---

# Same bug different platform

Same bug different platform
Prajwol Dhungana
Follow
1 min read
·
Jun 11, 2022

2

At the moment I am on a break from the Bug hunting so thought of writing this article about a bug I found couple of months ago.

If you have read my previous article it’s same as that bug but the platform was different.

So, the bug was on web version of facebook(facebook.com). Normally, facebook gives a page new experience for the celebrities, business person. So, I was testing I could find something in page new experience.

Then I started facebook live as a page named Urotropine which was already on page new experience and I set age restriction for <25 and restricted to men and when I shared that live video the video was shared publically instead of restricting the people age below 25 who are men which leads to the clash of content inappropriate user could get access to those post.

Get Prajwol Dhungana’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Timeline:

Feb11, 2022: Initial report

Feb11, 2022: Triaged

Feb24, 2022: $XXXX+ Fixed

POC: https://youtu.be/oyjLYdb3GSk

Buy me momo
