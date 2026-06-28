---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-26_like-bypass-on-customer-reviews-500-bounty.md
original_filename: 2024-08-26_like-bypass-on-customer-reviews-500-bounty.md
title: “Like” Bypass on Customer Reviews — €500 bounty
category: documents
detected_topics:
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 44cb362a92984cfa930f4aef4ce718626a45cd5774fa9c0f12bba2e36e48a796
text_sha256: 4567d50c3a42b12d85540d48788d13a912ba9d73ab73926701b6fc6f5b0e2c1b
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# “Like” Bypass on Customer Reviews — €500 bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-26_like-bypass-on-customer-reviews-500-bounty.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `44cb362a92984cfa930f4aef4ce718626a45cd5774fa9c0f12bba2e36e48a796`
- Text SHA256: `4567d50c3a42b12d85540d48788d13a912ba9d73ab73926701b6fc6f5b0e2c1b`


## Content

---
title: "“Like” Bypass on Customer Reviews — €500 bounty"
url: "https://medium.com/@asharm.khan7/like-bypass-on-customer-reviews-500-bounty-b8d45a98c096"
authors: ["Ashar Mahmood (@Hx_0p)"]
bugs: ["Logic flaw"]
bounty: "500"
publication_date: "2024-08-26"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 43
scraped_via: "browseros"
---

# “Like” Bypass on Customer Reviews — €500 bounty

1

“Like” Bypass on Customer Reviews — €500 bounty
Ashar Mahmood
Follow
4 min read
·
Aug 26, 2024

439

4

Hello! I’m Ashar Mahmood, a 22-year-old cybersecurity enthusiast with a passion for uncovering hidden vulnerabilities. I’m excited to share the news of my latest security write-up, where I discovered a significant vulnerability that not only brought me immense satisfaction but also earned me a rewarding bounty of €500 💶🫰.

How I Discovered a “Like” Bypass on Customer Reviews

I recently stumbled upon an interesting vulnerability on a popular automobiles platform that allows users to leave reviews for dealers. The platform has a feature where users can “like” a review, but it’s supposed to limit each user to only one like per review. However, I found a way to bypass this restriction and give as many likes as I wanted using just one account Here’s how I did it.

The Discovery

While browsing the platform, I noticed that each customer review had a “like” button, which could only be clicked once by any logged-in user. Naturally, this intrigued me, so I decided to investigate further.

Initial Experimentation

First, I logged into my account and navigated to a dealer’s page that had several customer reviews. I picked a review at random and clicked the “like” button. As expected, it registered my like and prevented me from liking it again.

Press enter or click to view image in full size

But I wasn’t done yet.

Using Burp Suite

I turned on Burp Suite to intercept the request when I clicked the “like” button. As soon as I hit the button, I intercepted the request and sent it to the Repeater in Burp.

Here’s where things got interesting. When I tried to replay the request, I received a “500 Response,” indicating an error.

Press enter or click to view image in full size

The Breakthrough

Get Ashar Mahmood’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I noticed that the request had a cookie parameter labelled `vi=;`. The response shows the exact same parameter, Curiously, I stripped off the data from this parameter and resent the request. This time, the server responded with a “200 OK” — the like was registered again!

I tested it further by sending the same modified request multiple times. Each time, the server accepted the like, allowing me to artificially inflate the number of likes on the review.

Impact

This might seem like a small issue at first, but consider the broader implications. Customer reviews are a critical part of any platform that facilitates buying and selling, especially when it comes to automobiles. Dealers and customers rely heavily on these reviews, and being able to manipulate the number of likes could easily sway potential buyers. A dealer could artificially boost their review ratings, giving themselves an unfair advantage.

Reflection

Discovering this vulnerability was an eye-opening experience. It reminded me how even seemingly minor features can have significant security implications if not properly secured. This vulnerability could have allowed anyone to distort the integrity of customer reviews, which are crucial for maintaining trust on the platform.

Key Learning

Always thoroughly examine every request, and take the time to inspect any suspicious cookie or parameter. You never know where a vulnerability might be hiding.

For more Follow me on

LinkedIn 🔗 https://www.linkedin.com/in/asharmahmood
Twitter✖️

https://twitter.com/Hx_0p

Press enter or click to view image in full size
