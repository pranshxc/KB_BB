---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-29_manual-broken-link-monitoring.md
original_filename: 2020-10-29_manual-broken-link-monitoring.md
title: Manual broken link monitoring
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: e9a109f629360e4c817515e2020b6b4b8a216aa18d775708035d2415ae3eba66
text_sha256: 9e135fa659a68d8cfd109f5c436aaf079865d918785e041d819d2087b0f58d80
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Manual broken link monitoring

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-29_manual-broken-link-monitoring.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `e9a109f629360e4c817515e2020b6b4b8a216aa18d775708035d2415ae3eba66`
- Text SHA256: `9e135fa659a68d8cfd109f5c436aaf079865d918785e041d819d2087b0f58d80`


## Content

---
title: "Manual broken link monitoring"
url: "https://grumpinout.medium.com/manual-broken-link-monitoring-bcc064f5f5f2"
authors: ["GrumpinouT (@RVerwilghen)"]
bugs: ["Broken link hijacking"]
publication_date: "2020-10-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4172
scraped_via: "browseros"
---

# Manual broken link monitoring

Manual broken link monitoring
GrumpinouT
Follow
Oct 29, 2020

3

1

When I started with bug bounty hunting, I became interested in all bugs related to URLs, one of my favorite and easy to exploit / find bugs, are broken link takeovers.

Get GrumpinouT’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I have found a few since I started, but all of them were links to nonexistent social media accounts. So nothing really critical here, but it’s always fun to have a big company link customers to your social media account. Some companies even give you a bounty if you report it to them!

I’ve noticed that most of the broken links to social media, happen because companies rename their pages. Especially pages made for Belgian customers, or maybe customers from countries where they speak more than one language in general. For example, I’ve seen renames from company_benl to company_be or CompanyBelgium to CompanyBenelux.

One way to manually monitor this kind of name changes, is by following them on Facebook. Facebook notifies followers of pages, once the page name has been changed. I just found a broken link to a Facebook page this way, and because of this I found out the URL to their Instagram is also broken. I immediately reported this to the company. Once I have a reply I will update this post.
