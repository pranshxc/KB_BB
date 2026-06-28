---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-14_automating-reflected-xss-with-burp-suite-intruder.md
original_filename: 2022-06-14_automating-reflected-xss-with-burp-suite-intruder.md
title: Automating reflected XSS with burp-suite Intruder
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
raw_sha256: ef25e54cf071383fd89944b03390d4633394acdfe4676056f71f05a7308ecd5b
text_sha256: 34faa1f55d5a4104c356058ae1048e8bc9fb0b275c62ece5985a2ca18cb71928
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Automating reflected XSS with burp-suite Intruder

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-14_automating-reflected-xss-with-burp-suite-intruder.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `ef25e54cf071383fd89944b03390d4633394acdfe4676056f71f05a7308ecd5b`
- Text SHA256: `34faa1f55d5a4104c356058ae1048e8bc9fb0b275c62ece5985a2ca18cb71928`


## Content

---
title: "Automating reflected XSS with burp-suite Intruder"
url: "https://notifybugme.medium.com/automating-reflected-xss-with-burp-suite-intruder-a39b2f060db7"
authors: ["Santosh Kumar Sha (@killmongar1996)"]
bugs: ["Reflected XSS"]
bounty: "750"
publication_date: "2022-06-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2552
scraped_via: "browseros"
---

# Automating reflected XSS with burp-suite Intruder

Member-only story

Automating reflected XSS with burp-suite Intruder
Santosh Kumar Sha(@killmongar1996)
Follow
4 min read
·
Jun 14, 2022

470

9

Hi, everyone

My name is Santosh Kumar Sha, I’m a Security Researcher/Ethical Hacker from India(Assam). In this article, I will be Describing how i found multiple reflected XSS using burp-suite intruder.

I am now offering 1:1 sessions to share my knowledge and expertise:

topmate.io/santosh_kumar_sha

SPECIAL COVID-19 Note:

Don’t go outside without any reason . Stay home be safe and also safe other. Special request to my fellow bug-bounty hunter Take care of your health and get vaccinated.

TOOLS used for the exploitation

1. Subfinder (https://github.com/projectdiscovery/subfinder)

2. httpx (https://github.com/projectdiscovery/httpx)

3. gau(Corben) — https://github.com/lc/gau

4. waybackurls(tomnomnom) — https://github.com/tomnomnom/waybackurls.

5. Burpsuite — https://portswigger.net/burp

Story Behind the bug:

This is the write-up of my how i found multiple reflected XSS using burp-suite intruder and automated it to find multiple XSS is on different domains with fuzzing parameters at a same time.
I was working some automation and got invite for new for target. So, while casually browsing and exploring the main domain i got were i notice an endpoint where it was reflected my input in HTML tag but it…
