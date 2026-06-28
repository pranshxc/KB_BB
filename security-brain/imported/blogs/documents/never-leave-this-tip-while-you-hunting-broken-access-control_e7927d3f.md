---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-13_never-leave-this-tip-while-you-hunting-broken-access-control.md
original_filename: 2021-11-13_never-leave-this-tip-while-you-hunting-broken-access-control.md
title: Never leave this tip while you hunting Broken Access Control
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: e7927d3f6074bfd635399146f1a1c96af1409d8a9d0a6e0dba2f65dda8ebe580
text_sha256: 0404f6f9c050be628423814aaca34d804398bc4d96d5221bceba1defe9a395ea
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Never leave this tip while you hunting Broken Access Control

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-13_never-leave-this-tip-while-you-hunting-broken-access-control.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `e7927d3f6074bfd635399146f1a1c96af1409d8a9d0a6e0dba2f65dda8ebe580`
- Text SHA256: `0404f6f9c050be628423814aaca34d804398bc4d96d5221bceba1defe9a395ea`


## Content

---
title: "Never leave this tip while you hunting Broken Access Control"
url: "https://secureitmania.medium.com/never-leave-this-tip-while-you-hunting-broken-access-control-f63c00b1e96a"
authors: ["secureITmania (@secureitmania)"]
bugs: ["Broken Access Control"]
publication_date: "2021-11-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3174
scraped_via: "browseros"
---

# Never leave this tip while you hunting Broken Access Control

Member-only story

OWASP TOP10 APPLICATION SECURITY RISK
Never leave this tip while you hunting Broken Access Control
A special Bug-Bounty tip for Bug hunters and Pen-testers
secureITmania
Follow
2 min read
·
Nov 12, 2021

12

If you already know about Broken Access Control weakness. Please skip explanation and go to the “Observation” section.

What is Broken Access Control

Broken Access Control is a type of weakness in the software program or application. If the system gives unauthorized access to a low privileged user then we can say that the system had a Broken Access Control weakness.

Broken Access Control 
secureITmania

Broken access controls are a commonly tends to High/critical security vulnerability. Design and management of access controls is a complex and dynamic problem that applies business, organizational, and legal constraints to a technical implementation.

Access Controls are sub-divided into 2 categories
1. Vertical Access Controls
2. Horizontal Access Controls

Issue Observation:

We will assume that the target host name is REDACTED. The figures during the post just for demonstrations, might not relevant to REDACTED domain.
