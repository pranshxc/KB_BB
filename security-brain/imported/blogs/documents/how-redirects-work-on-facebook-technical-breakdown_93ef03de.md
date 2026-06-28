---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-06_how-redirects-work-on-facebook-technical-breakdown.md
original_filename: 2020-12-06_how-redirects-work-on-facebook-technical-breakdown.md
title: How Redirects work on Facebook? Technical breakdown
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 93ef03de90c4e5ad33a8226b418da037a03b76f2139fd97aab8631b9ac74e747
text_sha256: 09ff3fb340d3b742bc50254c2e20e0937f282792bebe6ba728a3a0f94459126e
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# How Redirects work on Facebook? Technical breakdown

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-06_how-redirects-work-on-facebook-technical-breakdown.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `93ef03de90c4e5ad33a8226b418da037a03b76f2139fd97aab8631b9ac74e747`
- Text SHA256: `09ff3fb340d3b742bc50254c2e20e0937f282792bebe6ba728a3a0f94459126e`


## Content

---
title: "How Redirects work on Facebook? Technical breakdown"
url: "https://abhisek3122.medium.com/how-redirects-work-on-facebook-technical-breakdown-6699de52996c"
authors: ["Abhisek R (@abh1sek_r)"]
programs: ["Meta / Facebook"]
bugs: ["Open redirect"]
publication_date: "2020-12-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4088
scraped_via: "browseros"
---

# How Redirects work on Facebook? Technical breakdown

How Redirects work on Facebook? Technical breakdown
Abhisek R
Follow
3 min read
·
Dec 5, 2020

16

Recently I was been working on Facebook Whitehat program and I wanted to explain a bug which I found — OPEN REDIRECT

Hey, hope all are good. I’m Abhisek here

Disclaimer: This is for educational purposes only. I’m not in any way liable for any misuse.

When I was looking for low hanging bugs on Facebook, open redirect was the one which attracted me. So quickly launched Facebook and looked the requests sent during the process of redirection.

Press enter or click to view image in full size

Request No-32, caught my eyes on Open redirection bug. Took the request URL and tried to change the destination from

Press enter or click to view image in full size
Changes in the Request URL

You know what? Request succeeded and I was able to redirect from Facebook domain!!!!!

MEME [WOW VERY NICE]

But wait what does Facebook Whitehat program says? Request to https://evilzone.org is only been accepted as open redirect. So tried to redirect to Evilzone site, but Facebook security Linkshim detected it was malicious and request did not pass.

Press enter or click to view image in full size
MEME [UNLUCKY]

Tried to bypass in different ways, Some of them are domain.evilzone.org, Domainevilzone.org, domain.org.evilzone.org, but none of them succeeded. Then I left this bug and worked on some other but I was unlucky. After some time link shortening caught my attention, as expected the redirect worked.

Again unlucky, Then after a long time. A small idea sparked on my head,

Get Abhisek R’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Why don’t I redirect using IP address? YES you know, I was able to redirect without any errors or defense. Finally Again reported!

After this response, Me

However it maybe, Consistency is very important in Bug Bounty and Cyber Security Field.

Byee, Hope you had a good read!
