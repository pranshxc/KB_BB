---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-03_breaking-business-logic-via-coupons-the-story-of-my-1st-valid-bug-bounty.md
original_filename: 2020-07-03_breaking-business-logic-via-coupons-the-story-of-my-1st-valid-bug-bounty.md
title: Breaking Business Logic via Coupons — The Story of my 1st Valid Bug Bounty
category: documents
detected_topics:
- business-logic
- sso
- command-injection
- api-security
- cloud-security
- mobile-security
tags:
- imported
- documents
- business-logic
- sso
- command-injection
- api-security
- cloud-security
- mobile-security
language: en
raw_sha256: cfecb08080f7f4addbcaf46073ee0bd40f331f06b2b563df4fbf6c47c156c04a
text_sha256: 6b84378e351e9ec478c336f28dd20a8cd96570c336676d62ac855d6b3c999709
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Breaking Business Logic via Coupons — The Story of my 1st Valid Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-03_breaking-business-logic-via-coupons-the-story-of-my-1st-valid-bug-bounty.md
- Source Type: markdown
- Detected Topics: business-logic, sso, command-injection, api-security, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `cfecb08080f7f4addbcaf46073ee0bd40f331f06b2b563df4fbf6c47c156c04a`
- Text SHA256: `6b84378e351e9ec478c336f28dd20a8cd96570c336676d62ac855d6b3c999709`


## Content

---
title: "Breaking Business Logic via Coupons — The Story of my 1st Valid Bug Bounty"
url: "https://medium.com/@ifediri/breaking-business-logic-via-coupons-the-story-of-my-1st-valid-bug-bounty-89c30ff214dc"
authors: ["Dominic Ifediri (@Edi4all)"]
bugs: ["Payment tampering", "Logic flaw"]
publication_date: "2020-07-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4448
scraped_via: "browseros"
---

# Breaking Business Logic via Coupons — The Story of my 1st Valid Bug Bounty

Breaking Business Logic via Coupons — The Story of my 1st Valid Bug Bounty
Dominic Ifediri [edi]
Follow
5 min read
·
Jul 3, 2020

438

2

A Story of my first Valid Bug on a Private program —

In this article I will share:

How I got started in information security and bug bounty, my struggles and inconsistencies and what I learnt from them.
A different approach I had to take after learning a few things.
Then I’ll further discuss how I found my first valid bug, Finding the Bug.
And I’ll conclude with some takeaways or lessons from the finding.
How I got started

I heard about bug bounty in 2015, I interviewed a good friend of mine, and later became interested in information security in 2017.

I started learning about Infosec, as well as bug bounties on public programs like Facebook and Google from 2017, but I was very “inconsistent” throughout my learning phase. This is probably because I was doing it as a hobby, i.e only when I’m free from my main job as SEO consultant, digital marketer and Infopreneur.

So I initially started to hunt on Facebook, Laxman and Phwd were my inspiration, they were very helpful from the beginning, and I also got to know some more awesome individuals in the field.

I read a few eBooks, tried finding and reporting bugs but got no success, the truth is those public programs I started with, were the most challenging and difficult to hack on; due to the fact that most of the best security researchers / whitehat hackers in the world are already testing them and caught most bugs.

Over time, my reports always end up as “Not applicable”, “Informative” or “Duplicate”. After each reply, I often take a long break.

I also noticed that newbies (and sometimes even the experts or 1337s) feel this frustration as well.

I had little or no knowledge about valid bugs until I met a friend codenamed F007573P, who was always there to respond to my questions about hunting bugs in web applications.

A Different Approach

At this point, I felt the need to build my knowledge before hunting on difficult public programs again. A few good friends and some tweets in the Infosec community (had been helpful) recommended that security researchers can also try out private programs that are not on bug bounty platforms.

Wow, maybe I can try my little knowledge elsewhere then. So I decided to move out and try a different approach — Logical flaws came to my mind, that’s my favourite at the moment.

I decided I would be looking into breaking business logic till I am more knowledgeable or skilled enough to hunt higher technical bugs (in the wild) that have higher severity.

FINDING THE BUG

We will assume Private program’s site be called REDACTED

This bug existed at the endpoint that handles Coupons that are meant to be ONE TIME USE ONLY.

According to the mail I got, when you sign up, you get a coupon, the aim of that is to encourage customers to buy stuff and the coupon would expire in a few hours, I ignored that coupon initially.

2 WEEKS LATER

I wanted to shop on the site, so I applied my coupon after 2 weeks and the coupon still worked, this triggered my curiosity, I decided to go deeper testing that.

10 minutes later I realised that I could actually use my coupon as many times as I want.

With this I was able to trick REDACTED payment system which may lead to financial loss for the company.

PROOF OF CONCEPT

REQUIREMENTS: A New account and one-time-use only coupon for the new user.

Get Dominic Ifediri [edi]’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1. Login to REDACTED account

2. Copy your Coupon code

Let’s assume the coupon code is >> REDCOP300

3. I opened every item I want to Buy on separate Tabs

4. Apply the Codes on each tab before I placed Order in Each Tabs

This will reduce the Price for each item on each tab.

5. In one of my order, I hit check out, chose PayPal as Checkout option and Paid on PayPal’s site for the order.

At this point I knew I can place order for other items that were on the other tabs (I already applied same discount in them) since PayPal checkout is outside REDACTED, the REDACTED site can’t control the Price anymore.

I reported it.

TEAM STAFF REPLIES — I tried it on only one item, I didn’t fully demonstrate if I can place order on other tabs with same coupon, hence they’re not sure the payment will go through.

MY REPLY — I responded it will cost me some money to place order again, but I accepted the Challenge, I went ahead and performed Step 1–5 and made payment for many items in other tabs using “one-time use” coupon.

IMPACT,

Example:

Item worth $2,000 I can get -$100 discount

Item worth $3,000 can get -$300 discount

Item worth $5000 gets — $500 discount

And I can rule them all with one coupon

Few months later, they responded that the security team had looked into it and they’re grateful for my report and rewarded me with bounty.

REPORT TIMELINE:

Report Sent — Feb 9, 2020,

Team Staff responds — Feb 10, 2020 — They doubt the bug was valid. Then I made new POC to show full exploit.

Several Weeks and months of delayed communication, I gave up on the report — Mar 28, 2020

Team Staff Responds bug is valid — Apr 26 with Bounty reward in June 2020

TAKEAWAYS:

Premium Sections Likely has Bug(s) — This cannot be overemphasized, I’ve seen researchers say this alot and it’s true. Free Sections of a site are often more secure or already fixed, but the moment you pay and access Premium section where researchers don’t often go, then there’s higher chances of finding bugs there.

Always practice patience: I wanted to find a valid bug so bad but I waited alot for the efforts to come true. I even found and reported bug to some random company who silently fixed their issue but didn’t even reply me to say Thank you but that’s a story for another day :)

Secondly even when you’ve found a valid bug and reported it, these companies have their ways of doing their things. Triage and bug fixes go through various (most times long) processes which means you gotta wait or go do something else while waiting.

Always Check How an Endpoint reacts in Separate Tabs — When you open several tabs on your browser and perform Action A, before you go further with Action B on another tab, does the action A reflect in other tab? or does Action B stops Action A from doing something which you performed in other separate tabs, or can you perform those Actions and get away with it.

So that’s it, my journey as a hobbyist in InfoSec and bug bounty officially begins…

Thanks to my friend F007573P for helping me with proofreading & reviewing this write-up

P.s — if you need an infosec guy, you can contact me via my email ==> edithanos \\at// protonmail (dot) com
or send me a DM on X(twitter)
