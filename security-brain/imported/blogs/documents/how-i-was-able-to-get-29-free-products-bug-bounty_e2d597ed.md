---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-06_how-i-was-able-to-get-29-free-products-bug-bounty.md
original_filename: 2022-08-06_how-i-was-able-to-get-29-free-products-bug-bounty.md
title: How i was able to get 29 free products. | Bug Bounty
category: documents
detected_topics:
- idor
- command-injection
- automation-abuse
- race-condition
tags:
- imported
- documents
- idor
- command-injection
- automation-abuse
- race-condition
language: en
raw_sha256: e2d597ed307daeb7a1eb9cec068b0a8247f716ead1ff20e00d5c5fedd52160a1
text_sha256: 3924593309287d5c799871d47ab8b592003cf1ac9eee235fe914773d76106011
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# How i was able to get 29 free products. | Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-06_how-i-was-able-to-get-29-free-products-bug-bounty.md
- Source Type: markdown
- Detected Topics: idor, command-injection, automation-abuse, race-condition
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `e2d597ed307daeb7a1eb9cec068b0a8247f716ead1ff20e00d5c5fedd52160a1`
- Text SHA256: `3924593309287d5c799871d47ab8b592003cf1ac9eee235fe914773d76106011`


## Content

---
title: "How i was able to get 29 free products. | Bug Bounty"
url: "https://infosecwriteups.com/how-i-was-able-to-get-29-free-products-bug-bounty-845667ab4ad4"
authors: ["Fırat"]
bugs: ["Race condition"]
publication_date: "2022-08-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2361
scraped_via: "browseros"
---

# How i was able to get 29 free products. | Bug Bounty

How i was able to get 29 free products. | Bug Bounty
Fırat
Follow
3 min read
·
Aug 6, 2022

112

2

First of all, What is a race condition ?

Race condition occurs when two or more threads can access shared data and they try to change it at the same time. If you have a hard time understanding theoretical stuff, let me give you an example. Let’s say a user has bank accounts A and B. Both A and B has an amount of 500$.

Press enter or click to view image in full size
image by https://www.baeldung.com

As you can see we transferred 300$ times from A to B two times. And there is no problem. However, if these two transfers were to perform simultaneously, we may see some problems.

image by www.baeldung.com

We’ve encountered a race condition and transferred 600$ from A to B, even the bank account A got 300$ in the beginning.

Get Fırat’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

My Finding

So the target company is a marketplace for drinks, and there is an monthly subscription. If you are subscribed to the service, you get an free sample every month. The product shows up on your profile and you can add to your basket. I clicked to add basket and captured the request to see what i can do.

Press enter or click to view image in full size
An example of the request.

So as soon as i saw the id’s i tried IDOR but there wasn’t an IDOR. So i thought of changing the quantity, i mean this is a sample and free so the quantity can be 10–15 and the price will be still 0. I changed the quantity to 3 and sent the request, but they tought of this one too. So i said why not trying race condition, sent the request to turbo intruder and after i saw all 200’s and took a loook at the responses, i understood there was an race condition.

I love race condition bugs because they are easy to exploit even and very impactful.

If you have questions to ask me, you can contact me on Twitter.

Press enter or click to view image in full size
Image created by MidJourney AI | Discord bot https://www.midjourney.com/home/

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 Github Repos and tools, and 1 job alert for FREE!
