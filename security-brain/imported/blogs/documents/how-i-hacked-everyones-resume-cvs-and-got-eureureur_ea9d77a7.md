---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-14_how-i-hacked-everyones-resumecvs-and-got-.md
original_filename: 2021-02-14_how-i-hacked-everyones-resumecvs-and-got-.md
title: How I Hacked Everyone’s Resume/CV’s and Got €€€
category: documents
detected_topics:
- idor
- access-control
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: ea9d77a768db99423190901b17a40dd88396850258e41c31ee5c5c2700575c3d
text_sha256: 11da12a67154e778f96bd20fb7c01eb7e39bc5b490a99326f2ac2edaf8c163d9
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# How I Hacked Everyone’s Resume/CV’s and Got €€€

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-14_how-i-hacked-everyones-resumecvs-and-got-.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `ea9d77a768db99423190901b17a40dd88396850258e41c31ee5c5c2700575c3d`
- Text SHA256: `11da12a67154e778f96bd20fb7c01eb7e39bc5b490a99326f2ac2edaf8c163d9`


## Content

---
title: "How I Hacked Everyone’s Resume/CV’s and Got €€€"
url: "https://vbharad.medium.com/how-i-hacked-everyones-resume-cv-s-and-got-851aaa4d75d9"
authors: ["Vishal Bharad"]
bugs: ["IDOR", "Broken authorization", "Information disclosure"]
bounty: "250"
publication_date: "2021-02-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3910
scraped_via: "browseros"
---

# How I Hacked Everyone’s Resume/CV’s and Got €€€

Member-only story

How I Hacked Everyone’s Resume/CV’s and Got €€€
Vishal Bharad
Follow
3 min read
·
Feb 14, 2021

278

1

Hello Members, I am Vishal Bharad. Works as Penetration Tester and from India.

Here I am Back with another Interesting blog on How I Hacked Everyone’s Resume/CV’s on Job Search Portal and got €€€ (Euro).

First of all this is the one of the Simplest Vulnerability which rated in CRITICAL Category on Intigriti.

I started Bug bounty on intigriti.com and while searching for programs I got one program which is related to job search portal. As there are so many programs on intigriti related to job search :D.

So they not allowed to exposed vulnerabilities related to there program so please consider the domain is target.com

Vulnerable Domain — Target.com (Redacted)

Vulnerability Type — Sensitive Information Disclosure

Affected Endpoint — https://www.target.com/profile/cv/

Attack Type — Remote

Impact — All Resume/CV’s Exposed

There is flaw of Resume/CV upload in which there is an endpoint https://www.target.com/profile-portlets/cv/ which is vulnerable to Sensitive Information Disclosure in which All CV’s are exposed to Public.

While testing I put wrong password to login and I got one mail in the Inbox which is related to my profile information and In that information I got the endpoint of my CV/Resume. Which is available publicly.
