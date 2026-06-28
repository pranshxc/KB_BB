---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-03_how-i-could-have-been-the-administrator-for-all-dutch-companies-and-create-invoi.md
original_filename: 2022-11-03_how-i-could-have-been-the-administrator-for-all-dutch-companies-and-create-invoi.md
title: How I could have been the administrator for all Dutch companies and create
  invoices. And still can be…
category: documents
detected_topics:
- command-injection
- automation-abuse
- business-logic
tags:
- imported
- documents
- command-injection
- automation-abuse
- business-logic
language: en
raw_sha256: 0392a933a6f6726b809fc166034befc0f3d05cfb9a8049e929ce478dcba67127
text_sha256: 8dc21ad156ac1298f2b20f0b4b8f96fccec0ade42516970f463cd172aeef0be7
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# How I could have been the administrator for all Dutch companies and create invoices. And still can be…

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-03_how-i-could-have-been-the-administrator-for-all-dutch-companies-and-create-invoi.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `0392a933a6f6726b809fc166034befc0f3d05cfb9a8049e929ce478dcba67127`
- Text SHA256: `8dc21ad156ac1298f2b20f0b4b8f96fccec0ade42516970f463cd172aeef0be7`


## Content

---
title: "How I could have been the administrator for all Dutch companies and create invoices. And still can be…"
url: "https://medium.com/@bobvanderstaak/how-i-could-have-been-the-administrator-for-all-dutch-companies-and-create-invoices-and-still-can-de181160cec5"
authors: ["bob van der staak"]
programs: ["Dutch Government"]
bugs: ["Logic flaw"]
publication_date: "2022-11-03"
added_date: "2022-11-03"
source: "pentester.land/writeups.json"
original_index: 1956
scraped_via: "browseros"
---

# How I could have been the administrator for all Dutch companies and create invoices. And still can be…

How I could have been the administrator for all Dutch companies and create invoices. And still can be…
bob van der staak
Follow
4 min read
·
Nov 3, 2022

25

Hallo, my name is Bob van der Staak. I am an ethical hacker and security enthusiast. I performed this security research in personal time and personal capacity. A few months ago on LinkedIn I came across a post which mentioned a celebration: a new government website had aired that day.

From the bug bounty / hacker’s perspective a new website can always contain some low hanging fruits. So, I was eager to check the website and there I noticed that there was a registration button.

However, instead of an account it requested you to enter the name of your company. The extra data would be retrieved from the Dutch KVK Business Register. After entering a company, (which I do not own personally). I was prompted to create an account for that company. It indicated that I would be the first contact person within “my” company. and that with this account I would later be able to add extra persons.

Press enter or click to view image in full size

I finished the account creation and received an automatic email from the Dutch government. It gave me a link to activate my account for the given company. I was amazed. I would have expected verification that I was really the owner that company.

I decided to go further and after activation I could login and was the administrator, debtor administrator and order manager for that company!

Press enter or click to view image in full size

This could easily be scripted with Burp suite to make me the administrator for all Dutch company’s which didn’t have an account yet! because the website was only life for a few hours the chance of being the first was huge!

Get bob van der staak’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

With this account I came across pages which indicated I would be able to write new invoices in the name of that company. I can even add my own bank account to the system. A bit like ‘impersonating company identity’.

Press enter or click to view image in full size

Besides the possibility for me to make invoices in the name of a company that I do not own, there was also the effect that the legitimate owner would be shut out. The owner will not be able to create an account for his or her own company. They would receive a message indicating that the company was already registered and that they should contact the administrator of the portal. However, I was that administrator, and the message did not disclose my information. So, the owner must request the helpdesk of the government, which could result in lots of work for the government agency.

Press enter or click to view image in full size

I reported this issue immediately to NCSC to there coordinated responsible disclosure program. To get this to the right party and get it validated and resolved.

Approximately 2 months later I receive the message that the party responsible for the software does not see this as a security issue. Therefor this issue will not be resolved.

I sent another message to party responsible, to make sure we were discussing the same issue about ‘impersonating company identity’. They indicated that we were and, the company involved reasoned that in the future they will use “eHerkenning” and that there are some control mechanisms in place to make sure no ghost invoices could be send.

However, I still see this as a vulnerability, although it isn’t a fancy RCE or something else difficult to exploit. For me it shows once again, that sometimes it can just be easy and obvious, so that everyone could be able exploit it.

Sadly, I am not allowed to distribute the name of the respected party or disclose the domain name. As part of this write up agreement with NCSC. However, if you are an owner of a specific Dutch company and want to register your company, please feel free to contact me.

I want to thank NCSC for there always kind support in these responsible disclosure processes.
