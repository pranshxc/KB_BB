---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-28_out-of-bond-remote-code-executionrce-on-de-nederlandsche-bank-nv-with-burp-suite.md
original_filename: 2022-08-28_out-of-bond-remote-code-executionrce-on-de-nederlandsche-bank-nv-with-burp-suite.md
title: Out-Of-Bond Remote code Execution(RCE) on De Nederlandsche Bank N.V. with burp-suite
  collaborator
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 1bf738607cead1033303b551f57c087303bafda3de1aae02a06aaca4362a0f0e
text_sha256: 855c595cfe4ce907f4d27dfc7e0ebc8b809868a2cc36e9652107d1058f871642
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Out-Of-Bond Remote code Execution(RCE) on De Nederlandsche Bank N.V. with burp-suite collaborator

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-28_out-of-bond-remote-code-executionrce-on-de-nederlandsche-bank-nv-with-burp-suite.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `1bf738607cead1033303b551f57c087303bafda3de1aae02a06aaca4362a0f0e`
- Text SHA256: `855c595cfe4ce907f4d27dfc7e0ebc8b809868a2cc36e9652107d1058f871642`


## Content

---
title: "Out-Of-Bond Remote code Execution(RCE) on De Nederlandsche Bank N.V. with burp-suite collaborator"
url: "https://infosecwriteups.com/out-of-bond-remote-code-execution-rce-on-de-nederlandsche-bank-n-v-with-burp-suite-collaborator-2ce50260e2e4"
authors: ["Santosh Kumar Sha (@killmongar1996)"]
programs: ["De Nederlandsche Bank"]
bugs: ["OS command injection", "RCE"]
publication_date: "2022-08-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2249
scraped_via: "browseros"
---

# Out-Of-Bond Remote code Execution(RCE) on De Nederlandsche Bank N.V. with burp-suite collaborator

Member-only story

Out-Of-Bond Remote code Execution(RCE) on De Nederlandsche Bank N.V. with burp-suite collaborator
Santosh Kumar Sha(@killmongar1996)
Follow
4 min read
·
Aug 28, 2022

196

7

Hi, everyone

My name is Santosh Kumar Sha, I’m a Security Researcher/Ethical Hacker from India(Assam). In this article, I will be Describing How I found Out-Of-Bond Remote code Execution(RCE) on De Nederlandsche Bank N.V. with burp-suite collaborator

I am now offering 1:1 sessions to share my knowledge and expertise:

topmate.io/santosh_kumar_sha

SPECIAL Note:

Don’t go outside test scope without any permission. Stay safe and also hack safe . Special request to my fellow bug-bounty hunter Take care of your health and always abide the rule of engagement.

TOOLS used for the exploitation

1. Subfinder (https://github.com/projectdiscovery/subfinder)

2. httpx (https://github.com/projectdiscovery/httpx)

3. gau(Corben) — https://github.com/lc/gau

4. waybackurls(tomnomnom) — https://github.com/tomnomnom/waybackurls.

5. Burpsuite — https://portswigger.net/burp

Story Behind the bug:

This is the write-up of my how i found Out-Of-Bond Remote code Execution(RCE) on De Nederlandsche Bank N.V. with burp-suite collaborator is on different domains with fuzzing parameters at a same time. So, while casually browsing and exploring the main…
