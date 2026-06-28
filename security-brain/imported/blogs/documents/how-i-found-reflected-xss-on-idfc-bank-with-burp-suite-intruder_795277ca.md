---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-28_how-i-found-reflected-xss-on-idfc-bank-with-burp-suite-intruder.md
original_filename: 2022-08-28_how-i-found-reflected-xss-on-idfc-bank-with-burp-suite-intruder.md
title: How I found reflected XSS on IDFC Bank with burp-suite Intruder
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 795277caf79d2a72ecdb8c704625cf35bf98a33f14d936f38172b93e3f3ae0b0
text_sha256: 3729f05f78fd1113191089e759109cd17051ba0a2c7efc88c65b2dc980f67636
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# How I found reflected XSS on IDFC Bank with burp-suite Intruder

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-28_how-i-found-reflected-xss-on-idfc-bank-with-burp-suite-intruder.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `795277caf79d2a72ecdb8c704625cf35bf98a33f14d936f38172b93e3f3ae0b0`
- Text SHA256: `3729f05f78fd1113191089e759109cd17051ba0a2c7efc88c65b2dc980f67636`


## Content

---
title: "How I found reflected XSS on IDFC Bank with burp-suite Intruder"
url: "https://notifybugme.medium.com/how-i-found-reflected-xss-on-idfc-bank-with-burp-suite-intruder-7c53275daf02"
authors: ["Santosh Kumar Sha (@killmongar1996)"]
programs: ["IDFC Bank"]
bugs: ["Reflected XSS"]
publication_date: "2022-08-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2250
scraped_via: "browseros"
---

# How I found reflected XSS on IDFC Bank with burp-suite Intruder

Member-only story

How I found reflected XSS on IDFC Bank with burp-suite Intruder
Santosh Kumar Sha(@killmongar1996)
Follow
4 min read
·
Aug 28, 2022

226

5

Hi, everyone

My name is Santosh Kumar Sha, I’m a Security Researcher/Ethical Hacker from India(Assam). In this article, I will be Describing How I found reflected XSS on IDFC Bank with burp-suite Intruder.

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

This is the write-up of my how i found multiple reflected XSS using burp-suite intruder and automated it to find multiple XSS is on different domains with fuzzing parameters at a same time.
I was working some automation and got invite for new for target. So, while casually browsing and exploring the main domain i got were i notice an endpoint where it was…
