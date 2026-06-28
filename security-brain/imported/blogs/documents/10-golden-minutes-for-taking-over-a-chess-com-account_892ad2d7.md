---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-14_10-golden-minutes-for-taking-over-a-chesscom-account.md
original_filename: 2021-09-14_10-golden-minutes-for-taking-over-a-chesscom-account.md
title: 10 golden minutes for taking over a Chess.com account
category: documents
detected_topics:
- rate-limit
- command-injection
tags:
- imported
- documents
- rate-limit
- command-injection
language: en
raw_sha256: 892ad2d776cffa545f882115f601641d6742335ff4760d174f510429ac29db0f
text_sha256: d325484718cd3c8a8c2f2f4dd32baa455c443de130e565acca4fb1e8744ab6bc
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# 10 golden minutes for taking over a Chess.com account

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-14_10-golden-minutes-for-taking-over-a-chesscom-account.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `892ad2d776cffa545f882115f601641d6742335ff4760d174f510429ac29db0f`
- Text SHA256: `d325484718cd3c8a8c2f2f4dd32baa455c443de130e565acca4fb1e8744ab6bc`


## Content

---
title: "10 golden minutes for taking over a Chess.com account"
url: "https://infosecwriteups.com/10-golden-minutes-for-taking-over-a-chess-com-account-56e73f7c5f0d"
authors: ["Seqrity (@seqrity9)"]
programs: ["Chess.com"]
bugs: ["Lack of rate limiting", "Bruteforce", "Session expiration issue"]
bounty: "400"
publication_date: "2021-09-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3318
scraped_via: "browseros"
---

# 10 golden minutes for taking over a Chess.com account

10 golden minutes for taking over a Chess.com account
Seqrity
Follow
2 min read
·
Sep 14, 2021

110

3

Chess.com logo

Hi folks, this is the second write-up about finding bugs on Chess.com. You can find the first one here.
Chess.com is the most famous website for playing & learning chess.

You can log in to the site by two parameters, the first one is your email and the second one is your username. This story learn us to check all features and look for anomalies on each feature.
I’ve found that if you change your password, it changes just for one parameter (email) and after changing the password you can’t log in by your username and new password. In fact, the changes apply just to email and new password changes after 10 minutes on the username. So if your password leaks and you change your password, someone who has your password can log in after changing your password by username and old password. The process of update query for changing the password is like the following image:

Press enter or click to view image in full size
This is schematic and imaginary for a better understanding.

After sending this bug to Chess.com, they said this delay was for replication and was temporary. I checked it tomorrow and the bug existed!
Finally, the report scored at 3.5 based on CVSS

In more investigating, I find that after 10 minutes session won’t expire! Checked the change password form and there wasn’t any rate limit! BOOM!!!

Get Seqrity’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

By using burp intruder ran a brute force attack and found the new password. I escalated the bug to full account takeover.

Press enter or click to view image in full size
Burp intruder

The report scored at 4.4 based on CVSS and they increased bounty to $400.

You can find me on Twitter by the following link:

https://twitter.com/seqrity9
