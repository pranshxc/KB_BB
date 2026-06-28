---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-26_elasticsearch-smash-grab_2.md
original_filename: 2024-07-26_elasticsearch-smash-grab_2.md
title: ElasticSearch Smash & Grab
category: documents
detected_topics:
- command-injection
- information-disclosure
- cloud-security
- supply-chain
tags:
- imported
- documents
- command-injection
- information-disclosure
- cloud-security
- supply-chain
language: en
raw_sha256: 664a7fa6a53066d2bc10553da8eeb7aeb7247ddbe2d579bbad10d4745fd22486
text_sha256: e606d0107c7738d232ed6749c1c4f793be246c999b075fa5e76dcfb599852d44
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: false
---

# ElasticSearch Smash & Grab

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-26_elasticsearch-smash-grab_2.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: False
- Raw SHA256: `664a7fa6a53066d2bc10553da8eeb7aeb7247ddbe2d579bbad10d4745fd22486`
- Text SHA256: `e606d0107c7738d232ed6749c1c4f793be246c999b075fa5e76dcfb599852d44`


## Content

---
title: "ElasticSearch Smash & Grab"
url: "https://hogarth45.medium.com/elasticsearch-smash-grab-99cf36cdefbb"
authors: ["Jesse Clark (@Hogarth45_)"]
bugs: ["Elasticsearch", "Information disclosure", "Missing authentication"]
publication_date: "2024-07-26"
added_date: "2024-08-06"
source: "pentester.land/writeups.json"
original_index: 132
scraped_via: "browseros"
---

# ElasticSearch Smash & Grab

Member-only story

ElasticSearch Smash & Grab
Jess
Follow
2 min read
·
Jul 26, 2024

11

View Full Article: https://hogarth45.com/elasticsearch-smash-grab/

While iterating through subdomains I got a response like

You Know, for fun

Judging by the domain it was clearly an AWS instance of OpenSearch running ElasticSearch. I knew a bit about this, but decided to learn more.

There was only one disclosed Hackerone report talking about such a thing: https://hackerone.com/reports/2231261

roland_hack points to using tools like elasticsearch-dump (NPM) and estk (Go). I fired up the dump tool to see what I’d find.

elasticdump --input=https://domain.com/list --output temp222.txt

It spit out a starting dump line and decided to sit for a few hours and never do anything again. So either the tool is dumb, or I am dumb.
Not willing to admit I’m the dumb one I moved on to the estk, which was to be a handy tool to get all the indices of the ES via estk dump -h

Well like all BugBounty folks, my Go environment is a mess and I didn’t feel like spending an hour to clean it up.

Certainly there had to be a better way.

Some googling led me to: https://ghostlulz.com/elastic-search/

And he told me about /_cat/indices?v and /_all/_search?q=email

Boom

Press enter or click to view image in full size
That Hit Count is NUTS

After the fact I found this Medium article that has a ton of great info: https://systemweakness.com/elasticsearch-a-easy-win-for-bug-bounty-hunters-how-to-find-and-report-ddd900395bcb
