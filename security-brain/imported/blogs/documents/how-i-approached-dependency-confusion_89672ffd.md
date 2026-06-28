---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-01_how-i-approached-dependency-confusion.md
original_filename: 2022-02-01_how-i-approached-dependency-confusion.md
title: How I approached Dependency Confusion!
category: documents
detected_topics:
- supply-chain
- command-injection
- api-security
tags:
- imported
- documents
- supply-chain
- command-injection
- api-security
language: en
raw_sha256: 89672ffd829988a709172d97ad66ea22f1b02edda51f920d11b48cdfdaf41130
text_sha256: 208d6f438c45ca08d826b1373f3ead5a46d9323e05ab67c849962ea931e16733
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# How I approached Dependency Confusion!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-01_how-i-approached-dependency-confusion.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `89672ffd829988a709172d97ad66ea22f1b02edda51f920d11b48cdfdaf41130`
- Text SHA256: `208d6f438c45ca08d826b1373f3ead5a46d9323e05ab67c849962ea931e16733`


## Content

---
title: "How I approached Dependency Confusion!"
url: "https://hetroublemakr.medium.com/how-i-approached-dependency-confusion-272b46f66907"
authors: ["Aditya Soni (@hetroublemakr)"]
bugs: ["Dependency confusion"]
publication_date: "2022-02-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2955
scraped_via: "browseros"
---

# How I approached Dependency Confusion!

Member-only story

How I approached Dependency Confusion!
Aditya Soni
Follow
6 min read
·
Jan 31, 2022

446

7

Hi People,

Hope you are doing good, I know I took a little longer to publish this blog, so apologies there.

In this blog, I will be sharing my approach for finding Dependency Confusion bugs. This blog is totally inspired by Alex Birsan's finding on Dependency confusion.

Let’s Begin! :)

Press enter or click to view image in full size
# What is Dependency Confusion?

A Dependency Confusion attack or supply chain substitution attack occurs when a software installer script is tricked into pulling a malicious code file from a public repository instead of the intended file of the same name from an internal repository.

Case Study

It was an interesting find when the blog was published and unknown to the internet which attracted many eyes and I was also one of many who wanted to find a dependency confusion bug.

Dependency confusion bugs can be reported when you found a package that is not listed in the public source directory and is still getting installed. Some languages where this vulnerability can be found are python, npm, ruby, etc...

The major bugs which I reported were npm-based dependencies.

#How to identify a vulnerable package?
