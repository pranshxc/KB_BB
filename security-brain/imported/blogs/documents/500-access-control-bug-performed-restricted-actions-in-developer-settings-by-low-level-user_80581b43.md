---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-07_500-access-control-bug-performed-restricted-actions-in-developer-settings-by-low.md
original_filename: 2024-01-07_500-access-control-bug-performed-restricted-actions-in-developer-settings-by-low.md
title: '500$ Access Control Bug: Performed Restricted Actions in Developer Settings
  by low level user.'
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 80581b43614f60c4e5506e1623939533b9c7c5903d61668fcb8f8f3f760822b9
text_sha256: 0f146942f6a9714bef7fbfe6f8e25789bd2ff87f12e91a204dc6af3e552eb9b2
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# 500$ Access Control Bug: Performed Restricted Actions in Developer Settings by low level user.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-07_500-access-control-bug-performed-restricted-actions-in-developer-settings-by-low.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `80581b43614f60c4e5506e1623939533b9c7c5903d61668fcb8f8f3f760822b9`
- Text SHA256: `0f146942f6a9714bef7fbfe6f8e25789bd2ff87f12e91a204dc6af3e552eb9b2`


## Content

---
title: "500$ Access Control Bug: Performed Restricted Actions in Developer Settings by low level user."
url: "https://medium.com/@a13h1/500-access-control-bug-performed-restricted-actions-in-developer-settings-by-low-level-user-b4ecaa6d1aa1"
authors: ["Abhi Sharma (@a13h1_)"]
programs: ["ExamNote"]
bugs: ["Broken Access Control", "Privilege escalation"]
bounty: "500"
publication_date: "2024-01-07"
added_date: "2024-01-08"
source: "pentester.land/writeups.json"
original_index: 575
scraped_via: "browseros"
---

# 500$ Access Control Bug: Performed Restricted Actions in Developer Settings by low level user.

Member-only story

500$ Access Control Bug: Performed Restricted Actions in Developer Settings by low level user.
Abhi Sharma
Follow
3 min read
·
Jan 6, 2024

1.1K

3

Recently,i found an interesting bug during my testing that enables a supporter to carry out restricted actions within the developer settings, specifically tweaking notifications without proper authorization in an Private Program. This issue sheds light on a loophole where a low-level actor or a restricted supporter can attempt to manipulate the application’s logic.

Press enter or click to view image in full size

Understanding Target

ExamNote(Virtual Name of BBP) is a comprehensive platform designed to prioritize customer needs by offering an all-in-one solution for modern card issuer processing and program management. It empowers businesses to efficiently build and launch new revenue streams, providing a seamless experience for both businesses and their customers.In this context, the identified bug allowing unauthorized actions in the developer settings poses a potential risk.

The Bug

The bug I discovered in ExamNote a flaw that enables a supporter or low-level actor to perform restricted actions in the developer settings. Specifically, it allows the user to change notifications without the necessary permissions.

This issue becomes significant because a user with lower privileges, like a supporter, can attempt to manipulate the…
