---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-20_how-i-found-my-first-xss-on-a-bug-bounty-program.md
original_filename: 2022-12-20_how-i-found-my-first-xss-on-a-bug-bounty-program.md
title: How I found my first XSS on a Bug Bounty Program
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 00b4789c1326fa039700cf65df9ee749c7fdc5895cc75f1a62483ffbe0f1d360
text_sha256: ce6193d3d42e35f6ae5e3f8375903fd6d25cef608f7812f3654d2bb335ec4f7b
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# How I found my first XSS on a Bug Bounty Program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-20_how-i-found-my-first-xss-on-a-bug-bounty-program.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `00b4789c1326fa039700cf65df9ee749c7fdc5895cc75f1a62483ffbe0f1d360`
- Text SHA256: `ce6193d3d42e35f6ae5e3f8375903fd6d25cef608f7812f3654d2bb335ec4f7b`


## Content

---
title: "How I found my first XSS on a Bug Bounty Program"
url: "https://kingcoolvikas.medium.com/how-i-found-my-first-xss-on-a-bug-bounty-program-c41107617ce1"
authors: ["Vikas Anand (@kingcoolvikas)"]
programs: ["Coinbase"]
bugs: ["XSS"]
bounty: "200"
publication_date: "2022-12-20"
added_date: "2022-12-23"
source: "pentester.land/writeups.json"
original_index: 1761
scraped_via: "browseros"
---

# How I found my first XSS on a Bug Bounty Program

Top highlight

How I found my first XSS on a Bug Bounty Program
Vikas Anand
Follow
3 min read
·
Dec 20, 2022

353

6

Hello there, Welcome back to my Article.

In this article, I will tell how I found my first valid XSS on a bug bounty program. So let’s start

I’m Vikas Anand, a security researcher and a bug bounty hunter from Bihar, India.

First, I tried to find the program through Google Dork. The dork I used is: intext:Cryptocurrency Exchange intext:Bug bounty

Press enter or click to view image in full size
Google dork

After finding the program, I checked the scope of the program, but unfortunately there was only one domain, and that was the main domain.

So I said to myself, “Let’s hunt on this and go deep into the target and try to find at least one valid bug.”

I gave up after about 2–3 days because I hadn’t found anything. After 2 weeks, I again visited the site, and I see that it has implemented some new features. New features mean new bugs. let’s hack

Get Vikas Anand’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I went through all of the features and captured all of the requests with BurpSuite, and one feature caught my eye, where you can translate the word into different languages.

Press enter or click to view image in full size
Translation helper

An input box, let’s try for XSS. After that, I type “>img src=x onerror=alert(1)> and then looking at the source code, the value is well sanitised.

well senitize

Now I sent the request to the repeater tab and tried some XSS bypasses but didn’t find anything useful. And lastly, I sent the request to the intruder tab, and I fuzzed with some XSS payload lists, and after finishing the intruder attack, when clicking on the length tab, I got a few payloads of bigger length.

Press enter or click to view image in full size
Possible XSS

The XSS payload is successfully fired when you click on show response.

Press enter or click to view image in full size
xss payload fire

XSS polygot was the payload that was executed :

javascript:/* →</title></style></textarea></script></xmp><details/open/ontoggle=’+/`/+/”/+/onmouseover=1/+/[*/[]/+alert(/@PortSwiggerRes/)//’>

And after reporting the bug, they said that your bug is eligible for a $200 bounty, and I received the bounty in crypto.

Bounty

So that’s all from this Article. I hope you like it. And please ignore my grammatical mistake, as I’m not good at writing Articles.

If you have any questions, you can connect with me.

https://twitter.com/kingcoolvikas

https://www.linkedin.com/in/kingcoolvikas/

Cheers✌️and thanks for Reading at the end of this Article.
