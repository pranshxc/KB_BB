---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-13_xss-in-microsoft-subdomain.md
original_filename: 2018-07-13_xss-in-microsoft-subdomain.md
title: XSS in Microsoft subdomain
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 0895a04c69851e48496b17d8fa5212c8050d7dfa209799c5e34125211a15dceb
text_sha256: 9f14ebdd8ed6667cfe4f69de81e8145f2b74ac1925c221354fdfa751ff274829
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# XSS in Microsoft subdomain

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-13_xss-in-microsoft-subdomain.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `0895a04c69851e48496b17d8fa5212c8050d7dfa209799c5e34125211a15dceb`
- Text SHA256: `9f14ebdd8ed6667cfe4f69de81e8145f2b74ac1925c221354fdfa751ff274829`


## Content

---
title: "XSS in Microsoft subdomain"
url: "https://medium.com/@sudhanshur705/xss-in-microsoft-subdomain-81c4e46d6631"
authors: ["Sudhanshu Rajbhar (@sudhanshur705)"]
programs: ["Microsoft"]
bugs: ["XSS"]
publication_date: "2018-07-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5811
scraped_via: "browseros"
---

# XSS in Microsoft subdomain

XSS in Microsoft subdomain
Sudhanshu Rajbhar
Follow
3 min read
·
Jul 14, 2018

333

4

Heyy Everyonee,

I am Sudhanshu, in this article I am going to share the story about my first xss which I found in Microsoft.

A great thanks to my masters and friends for the love and support.

This is my first article, so if there is any mistake in it forgive me.

So the story goes like this …..

It was the time during my school summer holidays,I got a lot of homework but who cares about it .I just want to spend my time on my laptop.So here we go 18 days got passed away and I didn’t even realised I wasted all the time searching for websites for defacement,but I really sucked at it I couldn’t even find a single site.

At that time, I asked myself something “Am I just going to waste my time like this searching for sites for defacement or I will do something else?” ,I decided that I will do something that gives me the satisfaction which I want.

And suddenly an idea came into my mind what about doing bug hunting,I was already having a idea about it.But my problem was that after seeing others bugbounty hunter getting rewarded for their findings,I used to think that they are experts(yeah they are) and they just spend f**king one hour for finding bugs, its is just a piece of cake for them .So I thought I will also spend just one hour or something and I will find some cool bugs.

I was totally wrong about it.Those guys out there are spending all their time searching for bugs,learning new things.I decided that I will do the same as them.

Here we go, the real story starts from here

Next day, I took my note and I watched around 30 XSS POC videos and some write-ups to understand where I can actually find those xss. I noted down the reproduce steps, then I read them again and again to understand it.After half-an-hour I started my search for the XSS . And guess what was my target “Microsoft”.

I got this site https://social.microsoft.com/Forums/en-US/home, then I tried everywhere on the homepage where I can see any input field I looked for xss, but nothing seems to work and I was like

And then I saw an button there “Ask Question”, i clicked on it.In the body field there were many options likes insert link,instert html,insert image so I put the payload in those fields and hoping that the xss will popup.

Get Sudhanshu Rajbhar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Just in the first attempt in “insert link” I put my paload in the link, title,tooltip field and guess what

Press enter or click to view image in full size

And guys I was just fucked up after seeing it, really I did it!!!!!!! I was feeling like

Then I looked for other Microsoft websites for the same xss bug and I got the same on social.msdn.microsoft.com .And then reported both of them.

POC video:

Time Line:

01/June/2018: Reported the bug to Microsoft

09/June/2018:Got a reply stating that Report has been sent to the team.

13/July/2018:Fixed

Press enter or click to view image in full size

Thankyou so much for reading it. :)

More where this came from

This story is published in Noteworthy, where thousands come every day to learn about the people & ideas shaping the products we love.

Follow our publication to see more product & design stories featured by the Journal team.
