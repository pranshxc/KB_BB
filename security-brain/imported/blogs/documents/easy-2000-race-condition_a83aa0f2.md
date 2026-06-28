---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-25_easy-2000-race-condition.md
original_filename: 2023-01-25_easy-2000-race-condition.md
title: Easy 2000$ Race Condition
category: documents
detected_topics:
- command-injection
- race-condition
tags:
- imported
- documents
- command-injection
- race-condition
language: en
raw_sha256: a83aa0f2a16753ae0272669019411f3d58052cb7641fffe84ffe04dffef22cbb
text_sha256: c6f3d4cb79d019f5c556e00a09f50cca33796f6b831af7ed4d3caa3cc723b12a
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Easy 2000$ Race Condition

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-25_easy-2000-race-condition.md
- Source Type: markdown
- Detected Topics: command-injection, race-condition
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `a83aa0f2a16753ae0272669019411f3d58052cb7641fffe84ffe04dffef22cbb`
- Text SHA256: `c6f3d4cb79d019f5c556e00a09f50cca33796f6b831af7ed4d3caa3cc723b12a`


## Content

---
title: "Easy 2000$ Race Condition"
url: "https://medium.com/@_deshine_/easy-2000-race-condition-b4d093c9bc3c"
authors: ["Deshine"]
bugs: ["Race condition"]
bounty: "2,000"
publication_date: "2023-01-25"
added_date: "2023-01-26"
source: "pentester.land/writeups.json"
original_index: 1627
scraped_via: "browseros"
---

# Easy 2000$ Race Condition

Easy 2000$ Race Condition
Deshine
Follow
2 min read
·
Jan 25, 2023

216

2

Press enter or click to view image in full size

In this post, I will show you how Race Condition can be critical.

A few months ago, I was invited to a new Hackerone program. This program is about managing the games of basketball and baseball teams. It has a lot of roles and permissions but in this post I won’t talk about them.

This program has 2 domains that can be temporarily called:

https://redacted.com (This is the main site for people to join the team or create a team that invites everyone to join).
https://bv.redacted.com (This is a site for admins to manage teams, times, locations of matches, etc).

Admins can configure membership fees to participate in the tournament or join the team. They can also configure discount vouchers for participants.

Get Deshine’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If we use a voucher to join the team or enter the tournament, we will get a discount or free. But the voucher is limited.

So how can we make vouchers unlimited?

We will use multiple accounts to race at the same time, then all accounts registered to the team will be discounted or free.

This will cause the voucher to exceed the amount allowed in the configuration resulting in the organization losing money. And if it has anything to do with money, it will be CRITICAL.

Press enter or click to view image in full size

Thank you for spending time reading.

DESHINE
