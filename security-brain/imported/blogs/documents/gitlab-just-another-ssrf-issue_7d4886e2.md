---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-13_gitlab-just-another-ssrf-issue.md
original_filename: 2021-02-13_gitlab-just-another-ssrf-issue.md
title: '[GITLAB] — Just another SSRF issue.'
category: documents
detected_topics:
- ssrf
- command-injection
- api-security
tags:
- imported
- documents
- ssrf
- command-injection
- api-security
language: en
raw_sha256: 7d4886e22f8384d4b1f690e6fee5d9d130267baae77fa825b647988782744352
text_sha256: 348955a75b387d714fd9a5cb7edb9e24daa50b289f1901515965792f51991079
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# [GITLAB] — Just another SSRF issue.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-13_gitlab-just-another-ssrf-issue.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `7d4886e22f8384d4b1f690e6fee5d9d130267baae77fa825b647988782744352`
- Text SHA256: `348955a75b387d714fd9a5cb7edb9e24daa50b289f1901515965792f51991079`


## Content

---
title: "[GITLAB] — Just another SSRF issue."
url: "https://ltsirkov.medium.com/gitlab-just-another-ssrf-issue-483bc040392b"
authors: ["Lyubomir Tsirkov (@lyubo_tsirkov)"]
programs: ["GitLab"]
bugs: ["SSRF"]
bounty: "1,000"
publication_date: "2021-02-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3913
scraped_via: "browseros"
---

# [GITLAB] — Just another SSRF issue.

[GITLAB] — Just another SSRF issue.
Lyubomir Tsirkov
Follow
2 min read
·
Feb 12, 2021

36

Today I am going to talk about the second SSRF vulnerability that I have identified in Gitlab. Just to emphasize again that I’ve never considered seriously participating in bug bounty programs as a full-time job so I discovered all vulnerabilities by chance.

For the next few months, I am planning to spend a little bit more time on HackerOne in order to test myself and my knowledge. I think it is a good way to earn some extra money.

After reporting my first SSRF issue, I considered it worth spending some more time so I spent a few hours reviewing Gitlab’s functionality. I would rather conduct white-box testing because of the bigger possibility of finding vulnerabilities at all, but due to the lack of knowledge with Rails, I stuck to the Black-Box.

SUMMARY

The Gitlab Kubernetes page suffers from server-side request forgery due to improper restriction of the “API URL” field. This vulnerability could affect the application in such a way as to allow an attacker to perform ports scanning against the internal network or services.

Steps to reproduce

Get Lyubomir Tsirkov’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1. Create a project.
2. Open the newly created project and go to the “Operations -> Kubernetes” page.
3. Open “Add Kubernetes cluster”.
4. Go to the “Add existing cluster” page.
5. Fill in the “API URL” field with the following value “http://localhost:22”.
6. Press “Add Kubernetes Cluster”.
7. In order to be able to see the output, you will need to open the “Monitoring Page”.

Output — Monitoring Page

wrong status line: "SSH-2.0-OpenSSH_7.4p1 Debian-10+deb9u4"

Press enter or click to view image in full size

The output confirmed that there was SSRF vulnerability.

Gitlab board decided to reward me $1,000 for this report.

Press enter or click to view image in full size
