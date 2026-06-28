---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-28_business-logic-error-methodology-easy-way-poc-s.md
original_filename: 2021-01-28_business-logic-error-methodology-easy-way-poc-s.md
title: Business Logic Error Methodology (easy way) + PoC-s
category: documents
detected_topics:
- business-logic
- sso
- command-injection
tags:
- imported
- documents
- business-logic
- sso
- command-injection
language: en
raw_sha256: 67b9210562a21d1b26f045d27a21a7cd70b3487775a9d603189a05fda148da09
text_sha256: 8f4479427a3a271d5337878b43e7a6585b82683d93a454628f7f74a5c907da01
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Business Logic Error Methodology (easy way) + PoC-s

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-28_business-logic-error-methodology-easy-way-poc-s.md
- Source Type: markdown
- Detected Topics: business-logic, sso, command-injection
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `67b9210562a21d1b26f045d27a21a7cd70b3487775a9d603189a05fda148da09`
- Text SHA256: `8f4479427a3a271d5337878b43e7a6585b82683d93a454628f7f74a5c907da01`


## Content

---
title: "Business Logic Error Methodology (easy way) + PoC-s"
url: "https://medium.com/bugbountywriteup/business-logic-error-methodology-easy-way-poc-s-8195d8dee95b"
authors: ["Vuk Ivanovic"]
bugs: ["Logic flaw"]
publication_date: "2021-01-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3959
scraped_via: "browseros"
---

# Business Logic Error Methodology (easy way) + PoC-s

Member-only story

Business Logic Error Methodology (easy way) + PoC-s
, or hacking the website’s functionality by editing HTML code on the fly
Vuk Ivanovic
Follow
4 min read
·
Jan 28, 2021

135

Press enter or click to view image in full size

I have found this type of bug once 3 years ago, and I was amazed by its existence. And then I found it again a few days ago. Amazing. But, in order to know what to look for first, it’s all about mapping the web application.

What to map — the easy approach:

Figuring out the logic behind how anything works can get complicated. But, sometimes there are breadcrumbs that one can easily follow, at least for the quick and easy test.

When I hear business logic the first thing that comes to mind is — business of some kind. Now, what every business has to have is a way to make money. Thus, the easy websites to look at are those that offer free and paid plans. With more paid plans there is more to test, and the pricier that the affected plan is the greater severity of the bug.

You can’t click the disabled button, or can you?

Some websites limit the paid features by hiding them, others by showing them, but with links/buttons to reach those features disabled. End of the road? Not necessarily. Now, the long way around to get to those features is to figure out with which requests they are associated with. Which can be a…
