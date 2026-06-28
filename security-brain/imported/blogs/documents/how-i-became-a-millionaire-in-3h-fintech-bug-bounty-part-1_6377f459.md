---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-12_how-i-became-a-millionaire-in-3h-fintech-bug-bounty-part-1.md
original_filename: 2022-12-12_how-i-became-a-millionaire-in-3h-fintech-bug-bounty-part-1.md
title: How I became a millionaire in 3h | Fintech Bug Bounty — Part 1
category: documents
detected_topics:
- rate-limit
- idor
- command-injection
- path-traversal
- graphql
- business-logic
tags:
- imported
- documents
- rate-limit
- idor
- command-injection
- path-traversal
- graphql
- business-logic
language: en
raw_sha256: 6377f459de5c5bcf9f0b7a6aed175c197616f01a0ad2c1f8c4477c49e5235e57
text_sha256: 4e2c90d2764a5f7601e8032f352eaacfc24111057ea08584d31628cc9f554d4b
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# How I became a millionaire in 3h | Fintech Bug Bounty — Part 1

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-12_how-i-became-a-millionaire-in-3h-fintech-bug-bounty-part-1.md
- Source Type: markdown
- Detected Topics: rate-limit, idor, command-injection, path-traversal, graphql, business-logic
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `6377f459de5c5bcf9f0b7a6aed175c197616f01a0ad2c1f8c4477c49e5235e57`
- Text SHA256: `4e2c90d2764a5f7601e8032f352eaacfc24111057ea08584d31628cc9f554d4b`


## Content

---
title: "How I became a millionaire in 3h | Fintech Bug Bounty — Part 1"
url: "https://0x4kd.medium.com/how-i-became-a-millionaire-in-3h-fintech-bug-bounty-part-1-90193c5bd86f"
authors: ["0x4KD (@0x4kd)"]
bugs: ["IDOR", "Lack of rate limiting", "Logic flaw"]
publication_date: "2022-12-12"
added_date: "2022-12-12"
source: "pentester.land/writeups.json"
original_index: 1789
scraped_via: "browseros"
---

# How I became a millionaire in 3h | Fintech Bug Bounty — Part 1

How I became a millionaire in 3h | Fintech Bug Bounty — Part 1
0x4KD
Follow
4 min read
·
Jul 28, 2022

344

2

This article is the 1st part of the “Fintech Bug Bounty” series.

Summary
How I became a millionaire in 3h | Fintech Bug Bounty — Part 1
GraphQL Exploitation Techniques | Fintech Bug Bounty — Part 2
Running a MITM on a Google Play App | Fintech Bug Bounty — Part 3
(REDACTED) | Fintech Bug Bounty — Part 4 | Available on Mar 2023
(REDACTED) | Fintech Bug Bounty — Part 5 | Available on Apr 2023
Press enter or click to view image in full size

Lately, I’ve been doing some pentesting on a bank. It’s not like they hired me, but I felt curious about their infrastructure and asked them if I could search for security vulnerabilities. They agreed.

I was not going to spend much time looking at their main webpage because it’s a WordPress, and I’m not really used to seeing custom behaviours on it. Most people just install their desired plugins and go live.

Anyway, I decided to give it a try.

A little bit of context

It’s common to see new Fintech companies appear every single day. This one was created like a year ago, and they don’t have a significant amount of clients.

They’re trying to build what would be a Social Network tied to a Banking System (which is actually a brilliant idea).

If you think about it, having content creators inside your bank is fantastic if you’re trying to teach users how to operate, take care of their earnings, etc. It’s like the Coinbase App News tab, but more personal and direct.

Exploiting the vulnerability

These guys wanted to give rewards every time a user did a specific action (like learning new terms, understanding the market, etc.). So they created video tutorials and questionnaires that awarded some special coins to everyone who completed them. These coins can later use these coins in exchange for goods and services!

Get 0x4KD’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

It may seem a very straightforward feature, but it didn’t look like it when I inspected the requests: I couldn’t find any reference to plugins that implemented this feature in the way they were using it.

This is important because I was not intending to find a CVE in a known plugin.

The first thing that I noticed is that every time a video was played, a request was sent to the server indicating the percentage of the video that’s been seen by the user. I tried changing the percentage value to 100%, and the questionnaire appeared when the request came back. Cool, I don’t need to look at the videos to fulfil the form.

But guess what: the next request in Burp was a fetch for the questionnaire questions and answers… And it included which one was the correct one 😅.

So I just guessed and tried sending a request pretending I had clicked the correct answer, and suddenly some coins appeared in my wallet. That’s it!

Now I needed to automate this process to get infinite coins. I didn’t know how many questionnaires they had, so I just went for it and brute-forced all the tutorial IDs from 1 to 10000.

The big surprise was that every request that I made awarded me coins. Just to double-check, I tried answering questionnaire n.99999999, and it also worked.

Not sure if this can be considered an IDOR since the items don’t really exist, but I basically used this to answer non-existing tutorials.

I also noticed there was no throttling at all. I could send around 1000 requests simultaneously, and they all went through.

Conclusions

I ended up with around 1,000,000 coins that I could have used for my benefit. Obviously, I didn’t use them: Once the vulnerability was confirmed and fixed, they removed them from my account.

And when it comes to development, keep this in mind:

Stream your videos: The backend knows which part of the video is sent to you, so it can assume you’ve looked at it as soon as the duration of the section has passed and mark it as seen. Let the backend decide if the user can move to the next page or not.
Don’t return information in regard to which is the right or wrong answer in a questionnaire. Let the front-end send the answer, and the back-end will let you know whether it’s correct or not.
Add a Rate Limit to your requests. Users shouldn’t be able to send unlimited requests in a short time.
And for god’s sake, make sure the item you’re receiving exists in your database!
