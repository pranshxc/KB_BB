---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-16_my-first-reflected-xss-bug-bounty-google-dork-xxx.md
original_filename: 2022-02-16_my-first-reflected-xss-bug-bounty-google-dork-xxx.md
title: My First Reflected XSS Bug Bounty — Google Dork — $xxx
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: ff9c1893d5aab2487c18b9776f79c61d33680f273d0fa1071ae6dbf801412985
text_sha256: fc96ddf3a18ead2f3adf45a82013c566dc5f23bbb64461382539e56ba5ea4619
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# My First Reflected XSS Bug Bounty — Google Dork — $xxx

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-16_my-first-reflected-xss-bug-bounty-google-dork-xxx.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `ff9c1893d5aab2487c18b9776f79c61d33680f273d0fa1071ae6dbf801412985`
- Text SHA256: `fc96ddf3a18ead2f3adf45a82013c566dc5f23bbb64461382539e56ba5ea4619`


## Content

---
title: "My First Reflected XSS Bug Bounty — Google Dork — $xxx"
url: "https://infosecwriteups.com/my-first-reflected-xss-bug-bounty-google-dork-xxx-92ac1180e0d0"
authors: ["Proviesec (@proviesec)"]
bugs: ["Reflected XSS"]
publication_date: "2022-02-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2900
scraped_via: "browseros"
---

# My First Reflected XSS Bug Bounty — Google Dork — $xxx

Member-only story

My First Reflected XSS Bug Bounty — Google Dork — $xxx
Proviesec
Follow
3 min read
·
Feb 16, 2022

174

4

Today I will share a Reflected XSS vulnerability that was reported by me, to a security team as part of their bug bounty program at Hackerone. I became aware of this XSS flaw through a good Google Dork of mine.

What is Reflected XSS?

Cross-site scripting (XSS) is a web application vulnerability that allows an attacker to inject code (usually HTML or JavaScript) into the content of an external website. When the victim views the infected page on the website, the injected code will be executed in the victim’s browser. As a result, the attacker bypassed the browser’s same-origin policy and was able to steal private information from victims.

What are Google Dorks

Google Dorking is basically a search that uses advanced search query to find information that are not easily available on the websites. They are search strings which you enter into the Google search to find certain vulnerabilities.

Google Dorking is actually quite simple. You just need to know some basics about dorks that can give you the information you need.

intitle:"index of" 
intext:"Index of /" +.htaccess
filetype:log
site:medium.com

Here can you find more of them: https://github.com/Proviesec/google-dorks

And the Google Hacking Database contains a lot of google dorks that can find vulnerabilities or signs of a CVE…
