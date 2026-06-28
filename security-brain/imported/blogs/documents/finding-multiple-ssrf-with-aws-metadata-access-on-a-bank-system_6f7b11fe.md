---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-14_finding-multiple-ssrf-with-aws-metadata-access-on-a-bank-system_2.md
original_filename: 2021-08-14_finding-multiple-ssrf-with-aws-metadata-access-on-a-bank-system_2.md
title: Finding multiple SSRF with aws metadata access on A BANK system
category: documents
detected_topics:
- ssrf
- command-injection
- cloud-security
tags:
- imported
- documents
- ssrf
- command-injection
- cloud-security
language: en
raw_sha256: 6f7b11fed3c7b0e983a5632f744e1e2f6d320b76883fb279eed7912e6ffce622
text_sha256: 4ab521c0760996bde2e0608be5f33a0df110524989ceed668adba554d6141dfe
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Finding multiple SSRF with aws metadata access on A BANK system

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-14_finding-multiple-ssrf-with-aws-metadata-access-on-a-bank-system_2.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `6f7b11fed3c7b0e983a5632f744e1e2f6d320b76883fb279eed7912e6ffce622`
- Text SHA256: `4ab521c0760996bde2e0608be5f33a0df110524989ceed668adba554d6141dfe`


## Content

---
title: "Finding multiple SSRF with aws metadata access on A BANK system"
page_title: "Finding multiple SSRF with AWS metadata access on A BANK system | by Santosh Kumar Sha(@killmongar1996) | Medium"
url: "https://notifybugme.medium.com/finding-multiple-ssrf-with-aws-metadata-access-on-a-bank-system-7e73ac28e50a"
authors: ["Santosh Kumar Sha (@killmongar1996)"]
bugs: ["SSRF"]
publication_date: "2021-08-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3420
scraped_via: "browseros"
---

# Finding multiple SSRF with aws metadata access on A BANK system

Member-only story

Finding multiple SSRF with AWS metadata access on A BANK system
Santosh Kumar Sha(@killmongar1996)
Follow
4 min read
·
Aug 14, 2021

343

7

Hi, everyone

My name is Santosh Kumar Sha, I’m a security researcher from India(Assam). In this article, I will be describing How I was able Find multiple SSRF with aws metadata access ON a BANK System and Get access to there production server.

I am now offering 1:1 sessions to share my knowledge and expertise:

topmate.io/santosh_kumar_sha

SPECIAL COVID-19 Note:

Don’t go outside without any reason . Stay home be safe and also safe other. Special request to my fellow bug-bounty hunter Take care of your health and get vaccinated.

TOOLS used for the exploitation

1. Subfinder (https://github.com/projectdiscovery/subfinder)

2. httpx (https://github.com/projectdiscovery/httpx)

3. gau(Corben) — https://github.com/lc/gau

4. waybackurls(tomnomnom) — https://github.com/tomnomnom/waybackurls.

Story Behind the bug:

This is the write of my compromising the bank production and get access to 100GB customer High profile data by SSRF and escalating it get their aws production server customer stored data.

There was no Responsive disclosure program or Bugbounty program but still i report 15 SSRF aws metadata access bug and Many other critical bug because of them the customer would have…
