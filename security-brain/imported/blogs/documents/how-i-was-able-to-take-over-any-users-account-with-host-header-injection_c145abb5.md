---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-23_how-i-was-able-to-take-over-any-users-account-with-host-header-injection.md
original_filename: 2020-01-23_how-i-was-able-to-take-over-any-users-account-with-host-header-injection.md
title: How I was able to take over any users account with host header injection
category: documents
detected_topics:
- xss
- idor
- command-injection
- password-reset
- otp
tags:
- imported
- documents
- xss
- idor
- command-injection
- password-reset
- otp
language: en
raw_sha256: c145abb53c25daf3eae4f8f9d8509f72d61033e0ee00dfa0fa2dba38c6c86608
text_sha256: a37bd64af2a6c214ed97b6fe610bdb1da9ca686cfbd8c1ff9b08adc052c88af1
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to take over any users account with host header injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-23_how-i-was-able-to-take-over-any-users-account-with-host-header-injection.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, password-reset, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `c145abb53c25daf3eae4f8f9d8509f72d61033e0ee00dfa0fa2dba38c6c86608`
- Text SHA256: `a37bd64af2a6c214ed97b6fe610bdb1da9ca686cfbd8c1ff9b08adc052c88af1`


## Content

---
title: "How I was able to take over any users account with host header injection"
url: "https://medium.com/nassec-cybersecurity-writeups/how-i-was-able-to-take-over-any-users-account-with-host-header-injection-546fff6d0f2"
authors: ["Ajay Gautam (@evilboyajay)"]
bugs: ["Host header injection"]
bounty: "900"
publication_date: "2020-01-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4815
scraped_via: "browseros"
---

# How I was able to take over any users account with host header injection

Member-only story

How I was able to take over any users account with host header injection
Ajay Gautam
Follow
4 min read
·
Jan 23, 2020

843

9

This article is about a vulnerability I was able to find in the BugCrowd private program.

At around midnight I got an alert message that said that I had been invited to pentest a new private program. Taking in regard the scope and reward range of the web application, I thought I would give it a try. However, it was midnight and I did not come across any vulnerabilities and it was quite late so I decided to go to sleep.

The next day was like every other with running important errands but I had some free time before office, so I decided to have a look and do some research about that new private program as of the night before.

Since I was already familiar with the web application working methodology, I tested for IDOR’s but I did not have much luck with it at that time. Also, if I had found any IDOR then the severity category would not have gotten any high severity vulnerability in a way because they were using MongoDB default encrypted ID which is hard to decrypt. However, I thought there might be some loopholes where they might have leaked their userId.

As I moved on, I found few stored XSS but I was very sure that I would get response of duplicate of those vulnerabilities but still, I reported these vulnerabilities and as I had thought got the response of them as duplicate.

Moving further in pentest I got a vulnerability where I was able to steal other user’s passwords reset token or…
