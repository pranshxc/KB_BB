---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-25_the-unknown-hero-app-logic-bugs.md
original_filename: 2018-04-25_the-unknown-hero-app-logic-bugs.md
title: The Unknown Hero-App Logic Bugs
category: documents
detected_topics:
- xss
- command-injection
- csrf
- business-logic
tags:
- imported
- documents
- xss
- command-injection
- csrf
- business-logic
language: en
raw_sha256: 4ac8b17c5f76f0ca320348e9af4dc74d20a2458915b03fde470db5a049b63076
text_sha256: c7983ea77b8b3a13039b73d1916339293ce8c84deef4fbf0956403d8ef471113
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# The Unknown Hero-App Logic Bugs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-25_the-unknown-hero-app-logic-bugs.md
- Source Type: markdown
- Detected Topics: xss, command-injection, csrf, business-logic
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `4ac8b17c5f76f0ca320348e9af4dc74d20a2458915b03fde470db5a049b63076`
- Text SHA256: `c7983ea77b8b3a13039b73d1916339293ce8c84deef4fbf0956403d8ef471113`


## Content

---
title: "The Unknown Hero-App Logic Bugs"
url: "https://medium.com/bug-bounty-hunting/application-logic-bugs-600245fb5bf0"
authors: ["Circle Ninja (@circleninja)"]
programs: ["Canva"]
bugs: ["Logic flaw"]
publication_date: "2018-04-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5899
scraped_via: "browseros"
---

# The Unknown Hero-App Logic Bugs

The Unknown Hero-App Logic Bugs
Ronnie Joseph
Follow
3 min read
·
Apr 25, 2018

374

Application Logic Vulnerabilities-

If you may know; the ratio of bug bounty hunters and bugs to be found remains very dissimilar and trust me, it will remain the same(far more worse)in the future too.

Bug hunters come in a hoard to find bugs like XSS, CSRF, open redirects and some more common bugs.

Remember that, if the program is not private,but public; that usually means that such common bugs would have been easily found by other bug bounty hunters. By the time you start your hacking, already the bugs would have
been patched or you will most probably end up getting a lot of duplicates.

So here comes one of the unique bug types- Application logic vulnerabilities.

These type of bugs are one of my favourite, though you will end up digging much further, taking more time but the moment you catch such bugs, it is a different type of feeling. :)

In this post, I will be simply telling how I got my first unexpected bounty for one of the application logic bugs.
Read on to find more-
The bug was really very easy to exploit and find . I was actively exploiting the bug for over 3–4 months for my personal use. I know it’s not that ethical, but you will definitely forgive me for this when you figure out,what I actually exploited ! ;)

In the beginning I usually see the number of hackers thanked in the programs Hackerone profile. There were some top white hat hackers and some where even in the top 50 Hackerone list. I was little unsure in the start. But since I came to the party; I would at least take a small bite of burger and go back hehe.

Before coming to this field, I was a blogger sharing tech tips and tricks. So I usually made my blog’s graphics from this site. Yes, it is one of the leading graphic design sites at present on the internet. You got the site’s name ? :)

Get Ronnie Joseph’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

There was a option to edit any image ,color etc . After that we have the option to download the image in PNG,JPEG etc.

But there was one premium feature “Transparent” which enabled to download any image in transparent mode.
So while clicking on it, it popped like

“This is a premium feature. Upgrade your account to enable this feature.”

SO I was only able to download images which were not transparent.
Later on further digging, I found that they have just disabled the button(yes, I found it via Inspect Element).

it was something like- ////blah/blah/=disable
Let’s see what happens if we put enable!!
////blah/blah/=enable

Yes, now i was able to make edits for any image and download it in transparent PNG format. Yeah.
I literally used this technique for over two months to download transparent images,until afterwards I decided to report the bug to get a nice bounty money. :)

I know this bug was very easy. Just replace disable with enable and there you go.
But why did other top elite guys couldn’t see it? Because most of them were busy finding XSS, redirect, SQL etc.
I believe that most bug hunters forget about such application logic. I definitely recommend all to first play with the logic of the website , and then go forward for testing other common vulnerabilities.

I request your contributions to this free publication. Share and follow.What more can I say ? Happy hacking!

Hey, I do appreciate some claps . HeHe. :)
