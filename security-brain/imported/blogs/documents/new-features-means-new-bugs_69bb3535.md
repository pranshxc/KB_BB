---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-30_new-features-means-new-bugs_2.md
original_filename: 2020-07-30_new-features-means-new-bugs_2.md
title: New features means new bugs
category: documents
detected_topics:
- access-control
- command-injection
- business-logic
- api-security
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- business-logic
- api-security
- mobile-security
language: en
raw_sha256: 69bb35357e2083bdcf29a4593a96e82b481d5fe4e75af05311d2d94c089c1fea
text_sha256: 9e5ed9827cb4a8fb7f2ade3577f06265c321702a2122684dcbb04c44534b9d63
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# New features means new bugs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-30_new-features-means-new-bugs_2.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `69bb35357e2083bdcf29a4593a96e82b481d5fe4e75af05311d2d94c089c1fea`
- Text SHA256: `9e5ed9827cb4a8fb7f2ade3577f06265c321702a2122684dcbb04c44534b9d63`


## Content

---
title: "New features means new bugs"
url: "https://medium.com/@zseano/new-features-means-new-bugs-ece4d10cdf9d"
authors: ["Zseano (@zseano)"]
bugs: ["Logic flaw", "Broken authorization", "Payment bypass"]
publication_date: "2020-07-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4367
scraped_via: "browseros"
---

# New features means new bugs

New features means new bugs
Sean (zseano)
Follow
3 min read
·
Jul 30, 2020

234

Sometimes new features designed to generate revenue for a company can be rushed and sometimes not enough thought has gone into how to securely implement this new feature into the main web app. What does that usually mean? Bugs! The bigger the company the more products planned on the road map. The bigger the work load the more mistakes that are made.

How a new feature enabled me to bypass ID verification, very easily..

This is an interesting bug I found on a program which enabled me to bypass certain identification processes thanks to new features. The website in question required users to verify their ID in order to claim ownership of the company's page & honestly the process was pretty simple and straight forward. There wasn’t much to it and from my first tests it seemed pretty secure. There was nothing interesting when uploading my ID and I simply couldn’t find a way to achieve admin rights of a company. I moved on from testing on this feature for a long period of time.

~Enter a new feature~

A new feature was introduced which let page owners publish ads. Let’s get to play.

Get Sean (zseano)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Straight away I noticed one major problem and that was the fact anyone could purchase ads for any company. It didn’t require me to be a member of this company first, I could simply select any company I wish from a drop down box. However things went from bad to worse very quickly. Upon purchasing ads for my chosen company I was then granted ownership of the company. Wait, really? What?! Could this get worse?

Oh yes.. it can. The second major problem was Sandbox CC details worked when purchasing ads. (4111 1111 1111 1111). This means an attacker could choose any company’s page he wishes, purchase ads using a sandbox CC number, and suddenly they had admin rights, at zero cost. Easy right? After obtaining admin rights I had access to do… well, everything. Edit or remove the page, remove other admins, browse their information etc.

Sean, am I reading that right? That simple?

Yup! A new feature designed to generate revenue for the company undermined their entire identification process and allowed me to claim ownership of any page from purchasing ads using a sandbox CC. (The ads still ran as well lol!).

If the sandbox CC test had failed I would of still continued with a real CC just to see what would happen, because if you don’t try, how will you ever know? (as long as the cost is low!). The fact it allowed me to begin the process for buying ads for a company without even proving my ID is what sparked my curiosity.

Devs.. don’t rush things! Think it through when implementing new features.

And hackers… always be on the look out for new features. Be sure to follow them on twitter, browse news on them weekly, keep up to date with what they are planning on releasing. Also don’t be afraid to spend some $$ when testing features on websites, just don’t spend LOADS. Also I recommend a separate card used just for BB transactions.

~ zseano
