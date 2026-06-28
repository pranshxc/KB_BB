---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-04_how-i-got-my-first-big-bounty-payout-with-tesla.md
original_filename: 2020-06-04_how-i-got-my-first-big-bounty-payout-with-tesla.md
title: How I got my first big bounty payout with Tesla
category: documents
detected_topics:
- command-injection
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: 3729843980bce98eb581a970fbd2285b3b52a0b2449a3b73d901101995d47233
text_sha256: 99a939d46cb9a32ee26fd49ff1837166363034378f33d13ab6cf7c9f53b7e991
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: true
---

# How I got my first big bounty payout with Tesla

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-04_how-i-got-my-first-big-bounty-payout-with-tesla.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: True
- Raw SHA256: `3729843980bce98eb581a970fbd2285b3b52a0b2449a3b73d901101995d47233`
- Text SHA256: `99a939d46cb9a32ee26fd49ff1837166363034378f33d13ab6cf7c9f53b7e991`


## Content

---
title: "How I got my first big bounty payout with Tesla"
url: "https://medium.com/heck-the-packet/how-i-got-my-first-big-bounty-payout-with-tesla-8d28b520162d"
authors: ["CJ Fairhead (@xyantix)"]
programs: ["Tesla"]
bugs: ["Information disclosure"]
bounty: "5,000"
publication_date: "2020-06-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4531
scraped_via: "browseros"
---

# How I got my first big bounty payout with Tesla

Member-only story

How I got my first big bounty payout with Tesla
CJ Fairhead
Follow
5 min read
·
Jun 4, 2020

409

Today I’m finally doing my write-up on how I got my first bug bounty, what I learned from the experience and some tips on how, (with a little luck and perseverance) you may find one too.

Before we get started — Any video, blog or article I mentioned will be linked as a reference at the end of this post.

The Setting

I had been working in the IT field in various roles for a few years (Service Desk, Sysadmin roles) but had barely dipped my toes in the Security space yet. I had always been interested but never had the confidence to pursue it.

I was watching a Github Recon video one night that was pulled together by @Th3G3nt3lman, when I decided to “follow along”. This particular video was about manual GitHub recon and included some key search terms that were likely to yield results.

I decided to try some for myself. The tutorial video focused on Tesla as a target, so I thought I’d do the same, starting with search terms like:

"tesla.com" password=***REDACTED*** of real interest caught my eye.

I then remembered that when I write code I don’t always give my variables the best names (I’m surely not the only one). So I also tried:

"tesla.com" pass=

Again, nothing really stood out to me. At this point I figured, “Hey, sometimes I barely even bother naming variables, let’s try something else…”
