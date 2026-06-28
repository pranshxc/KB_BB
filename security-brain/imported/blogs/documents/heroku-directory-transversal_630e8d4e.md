---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-12-03_heroku-directory-transversal.md
original_filename: 2013-12-03_heroku-directory-transversal.md
title: Heroku Directory Transversal
category: documents
detected_topics:
- path-traversal
- command-injection
tags:
- imported
- documents
- path-traversal
- command-injection
language: en
raw_sha256: 630e8d4e1789a80af49d562a6f4023edb495ad12196c50bf34e07af913d6cabe
text_sha256: 336bf0aa16ac22ed5b557fad9c853f2ea9e55c19ea09d3995688022b03e1bd51
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Heroku Directory Transversal

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-12-03_heroku-directory-transversal.md
- Source Type: markdown
- Detected Topics: path-traversal, command-injection
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `630e8d4e1789a80af49d562a6f4023edb495ad12196c50bf34e07af913d6cabe`
- Text SHA256: `336bf0aa16ac22ed5b557fad9c853f2ea9e55c19ea09d3995688022b03e1bd51`


## Content

---
title: "Heroku Directory Transversal"
page_title: "Shashank's Security Blog: Heroku Directory Transversal"
url: "http://blog.shashank.co/2013/12/heroku-directory-transversal.html"
final_url: "https://blog.shashank.co/2013/12/heroku-directory-transversal.html"
authors: ["Shashank (@cyberboyIndia)"]
programs: ["Heroku"]
bugs: ["Path traversal"]
publication_date: "2013-12-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6386
---

Long back I spotted a Directory Traversal bug in Heroku.  
  
"Heroku is a cloud platform is a cloud application platform – a new way of building and deploying web apps. Heroku was acquired by Salesforce.com in 2010."  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGaKgvhe5zhiV3_EKxw8l78I-zZlUQAEdiMN0ySH-7-bxT4IXKtx6HmajzWLyCSik39RGVj3Bq3bMptvbUTXYS7RWeqGDWg2-6E-W2DrfqwDi-9EzJGPLBREYpImang3LkheAG0pBIM-7q/s400/herokuLFI.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGaKgvhe5zhiV3_EKxw8l78I-zZlUQAEdiMN0ySH-7-bxT4IXKtx6HmajzWLyCSik39RGVj3Bq3bMptvbUTXYS7RWeqGDWg2-6E-W2DrfqwDi-9EzJGPLBREYpImang3LkheAG0pBIM-7q/s1600/herokuLFI.PNG)

  
They were quite quick and fixed it without delays  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_SNgJMUbkLBfs0YEAF66hM-4ruMmoRpPiaiUwJir-JYxqYFA2k3fwv7iQKk_fl1pbhR2aEI6KVDbhRNXOIdsHDDDbA7UYFGKO73RPdkgP4NIp2M17-z4F_lcOD0gjv3hL_JjUANATZj_j/s400/reply.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_SNgJMUbkLBfs0YEAF66hM-4ruMmoRpPiaiUwJir-JYxqYFA2k3fwv7iQKk_fl1pbhR2aEI6KVDbhRNXOIdsHDDDbA7UYFGKO73RPdkgP4NIp2M17-z4F_lcOD0gjv3hL_JjUANATZj_j/s1600/reply.PNG)

  
Later they even started their hall of fame page and included my name there :)  
<https://www.heroku.com/policy/security-hall-of-fame>  
  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgJUljgHpKj22wL9ofqWok8m8_v7f1PSRbQ-YVbZsQNlTBrKNNWb7Kbpia2aQ05cwU16peBp34R4DXZ9Du1iKMkIRFuIasIlwZQ1eKo5G5KIKtIO4ravhOCvIE-DK52PA7JjJX5ZYD34tl/s400/hof.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgJUljgHpKj22wL9ofqWok8m8_v7f1PSRbQ-YVbZsQNlTBrKNNWb7Kbpia2aQ05cwU16peBp34R4DXZ9Du1iKMkIRFuIasIlwZQ1eKo5G5KIKtIO4ravhOCvIE-DK52PA7JjJX5ZYD34tl/s1600/hof.PNG)
