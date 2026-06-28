---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-10_the-easiest-bug-to-get-a-hall-of-fame-from-a-billion-dollar-company.md
original_filename: 2022-10-10_the-easiest-bug-to-get-a-hall-of-fame-from-a-billion-dollar-company.md
title: The easiest bug to get a Hall of fame from a Billion dollar company.
category: documents
detected_topics:
- command-injection
- graphql
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- graphql
- information-disclosure
- api-security
language: en
raw_sha256: 44700a82f7ab092bcfbfe4421e095f62a534ce8d328d01365fa61cb54795ef08
text_sha256: da42bd5f387a5f3c17e638cc543f9e7552fd04226719b1df86af51c7d3573784
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# The easiest bug to get a Hall of fame from a Billion dollar company.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-10_the-easiest-bug-to-get-a-hall-of-fame-from-a-billion-dollar-company.md
- Source Type: markdown
- Detected Topics: command-injection, graphql, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `44700a82f7ab092bcfbfe4421e095f62a534ce8d328d01365fa61cb54795ef08`
- Text SHA256: `da42bd5f387a5f3c17e638cc543f9e7552fd04226719b1df86af51c7d3573784`


## Content

---
title: "The easiest bug to get a Hall of fame from a Billion dollar company."
url: "https://debprasadbanerjee502.medium.com/the-easiest-bug-to-get-a-hall-of-fame-from-a-billion-dollar-company-8278fd7b3035"
authors: ["Ravaan"]
programs: ["GeHealthcare"]
bugs: ["GraphQL", "Information disclosure"]
publication_date: "2022-10-10"
added_date: "2022-10-10"
source: "pentester.land/writeups.json"
original_index: 2070
scraped_via: "browseros"
---

# The easiest bug to get a Hall of fame from a Billion dollar company.

The easiest bug to get a Hall of fame from a Billion dollar company.
Ravaan
Follow
3 min read
·
Oct 10, 2022

682

15

GeHealthcare, is a company that many might not have heard of. This company basically supports Healthcare related electronic machinery. Long story short- I wanted to hack them.

If you’ve been following me for a while you must have understood my primary methodology revolves around a specific tool that I built myself.

Check that out btw: Instant Bounties

so i run my tool and find all the subdomains.

The next step is I visit most of the subdomains and few 3 tier domains stand out and out of which one was https://Redacted-myinstall.cloud.gehealthcare.com/

I visit the page and its a white page. Interesting, I had previous experience with Microsoft bug bounty and Adobe’s bug bounty where most of these pages had hidden locations running a service so, you might have already guessed it what i used.

FFUFing:

Examples of GraphQL endpoints

It’s difficult to list all possible endpoints to find a GraphQL instance but many of them use a framework like “Appollo” and they use common GraphQL endpoints:

/v1/explorer
/v1/graphiql
/graph
/graphql
/graphql/console/
/graphql.php
/graphiql
/graphiql.php
(...)

You can find more complete list on SecLists. Another way to identify a hidden endpoint is by searching some keywords in JavaScripts files like “query“, “mutation“, “graphql” and it could reveal the presence of a GraphQL decommissioned/unofficial endpoint.

Get Ravaan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I used ffuf and tried to find files when i come across /graphql. If you’re unaware of it Graphql helps in querying API via schemas. One can query things which i did and extracted Sensitive information.

Press enter or click to view image in full size

Here’s an article explaining it. Meanwhile, let me know if you want Advanced API hacking stuff.

You can also use Graphql Voyager though it's not available at this moment.

Press enter or click to view image in full size
Findings and Hall of fame:
Press enter or click to view image in full size

So i report and another potential issue which turned out to be a new thing they were testing and they took down the entire server for few hours and it was again up.

Press enter or click to view image in full size

I was given a spot in their hall of fame:

GE Healthcare Guidance on Cyber - Thanks
GE Healthcare Guidance on Cyber - Thanks

GE Healthcare Guidance on Cyber - Thankswww.gehealthcare.com

Press enter or click to view image in full size
Announcement:

Almost at 1000 subscribers. I will be giving out 2 Tryhackme Premium VIP+ vouchers when I hit 1000 subscribers. Thanks for reading and I am sorry if I am not responding to the emails due to projects which I am currently working on.

Clapping more than once is possible and do comment to enter the Giveaway. PEACE — Ravaan:)

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
