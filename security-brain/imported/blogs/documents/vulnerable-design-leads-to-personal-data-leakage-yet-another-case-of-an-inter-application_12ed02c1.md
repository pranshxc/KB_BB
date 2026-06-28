---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-09_vulnerable-design-leads-to-personal-data-leakage-yet-another-case-of-an-inter-ap.md
original_filename: 2020-03-09_vulnerable-design-leads-to-personal-data-leakage-yet-another-case-of-an-inter-ap.md
title: Vulnerable design leads to personal data leakage- yet another case of an inter-application
  vulnerability…
category: documents
detected_topics:
- sso
- command-injection
- automation-abuse
- business-logic
- supply-chain
tags:
- imported
- documents
- sso
- command-injection
- automation-abuse
- business-logic
- supply-chain
language: en
raw_sha256: 12ed02c1f4b6e24f43a6f2d5a5a102765862b9704448cd6359ebe50fe6199e93
text_sha256: 3848705b9fd55867dd05735da312276ca47978741daa022d87a12bb1084528dc
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Vulnerable design leads to personal data leakage- yet another case of an inter-application vulnerability…

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-09_vulnerable-design-leads-to-personal-data-leakage-yet-another-case-of-an-inter-ap.md
- Source Type: markdown
- Detected Topics: sso, command-injection, automation-abuse, business-logic, supply-chain
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `12ed02c1f4b6e24f43a6f2d5a5a102765862b9704448cd6359ebe50fe6199e93`
- Text SHA256: `3848705b9fd55867dd05735da312276ca47978741daa022d87a12bb1084528dc`


## Content

---
title: "Vulnerable design leads to personal data leakage- yet another case of an inter-application vulnerability…"
url: "https://medium.com/bugbountywriteup/vulnerable-design-leads-to-personal-data-leakage-yet-another-case-of-an-inter-application-8a9d7e2d0f1a"
authors: ["Marcin Szydlowski (@SecurityKsl)"]
bugs: ["Logic flaw"]
publication_date: "2020-03-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4725
scraped_via: "browseros"
---

# Vulnerable design leads to personal data leakage- yet another case of an inter-application vulnerability…

Vulnerable design leads to personal data leakage- yet another case of an inter-application vulnerability…
Marcin Szydlowski
Follow
3 min read
·
Mar 10, 2020

15

1

Foreword

It has been some time since I published my first article on inter-application vulnerabilities in modern web applications. Recently I identified one of them during bug bounty hunting and I personally think it is too good not to be shared with the broader community.

If you are one of tl;dr guys, we are speaking here about issues which exist because of cross-system dependencies and integrations of applications. Long story short — separately, two applications are free from vulnerabilities, however while considering them as a one, you have major security concerns within.

This kind of a situation…

If you want to know more on the concept I encourage you to read my article from 2018.

Background

Vulnerability was identified in a bug bounty program of a major international company, details of which I’m not able to share for confidentiality reasons.

Scope of company’s bug bounty program included multiple domains (applications), which were used for quite a similar purpose. While testing these apps, you could easily note that code of certain functionalities in them was shared. What do I mean by that? It seemed that both applications queried the same backend data source to get some information about users.

It is not an issue, right? Wrong.

There is one more gotcha. In our case the mechanisms which were shared included the ones processing (Read/Write) sensitive personal data, which could be updated after successful registration. However, the registration mechanism itself was clearly separated.

Get Marcin Szydlowski’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I tried to visualize our situation on the diagram below.

Press enter or click to view image in full size
Vulnerable design

Data retrieval process is relatively simple. If authentication is successful application server will send a request to the backend data source to query personal data based on the e-mail address provided during authentication.

Press enter or click to view image in full size
Vulnerable design — querying data from the database

You probably already know where it is going. If not, try to guess what happens if someone uses the same e-mail address which is already registered in App1 to register in App2.

Press enter or click to view image in full size
Vulnerable design — access to data of other users

Oops! We may access personal data of any user registered in the database just by knowing his e-mail address! And by the way there was no account activation e-mail nor any other mechanism to prevent this kind of an attack.

Imagine a situation when there is some random leakage of e-mail addresses on the Internet. We can simply pipe all of them through our vulnerable App1 and if we are lucky we will get personal details associated with some of these addresses. Then we do the same exercise again for App2 and gather some more personal details. Not bad, huh? At least good enough to get a bounty.

Summary

Building secure systems is way harder than finding vulnerabilities within them. Building is getting even harder if you need to integrate multiple applications design of which you cannot really impact. Good luck to the Builders and Architects. I hope this article will allow you to avoid inter-application vulnerabilities in your systems.

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com
