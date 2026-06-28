---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-26_how-i-found-xss-on-amazon.md
original_filename: 2018-07-26_how-i-found-xss-on-amazon.md
title: How I found XSS on Amazon?
category: documents
detected_topics:
- sso
- xss
- command-injection
- csrf
tags:
- imported
- documents
- sso
- xss
- command-injection
- csrf
language: en
raw_sha256: b30cfd66606dfbfd87cb5bdff062c1098ea7bc8a57a278845563001cf11b9af0
text_sha256: 22f67ce0e14aca04803c5703157caf36d744b3e44766f1796aecc52b93f44b16
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I found XSS on Amazon?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-26_how-i-found-xss-on-amazon.md
- Source Type: markdown
- Detected Topics: sso, xss, command-injection, csrf
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `b30cfd66606dfbfd87cb5bdff062c1098ea7bc8a57a278845563001cf11b9af0`
- Text SHA256: `22f67ce0e14aca04803c5703157caf36d744b3e44766f1796aecc52b93f44b16`


## Content

---
title: "How I found XSS on Amazon?"
url: "https://medium.com/@codingkarma/how-i-found-xss-on-amazon-f62b50f1c336"
authors: ["Coding_Karma (@karma_coded)"]
programs: ["Amazon (CloudFront)"]
bugs: ["XSS"]
publication_date: "2018-07-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5788
scraped_via: "browseros"
---

# How I found XSS on Amazon?

How I found XSS on Amazon?
Coding_Karma
Follow
3 min read
·
Jul 26, 2018

128

2

I recently started with “Bug Bounty” after hearing and reading so much about it. I felt like it might be worth the efforts to actually try it out & guess what? It’s absolutely is!
As a beginner to anyone whose reading this post please always think about the impact “Imagine you are the bad guy and the evaluate your findings. Before running to submissions”.

Coming back to the topic XSS on amazon. So as always I was trying to “Hunt” for bugs on some program on some website and feeling absolutely drained so I started reading some posts about XSS and thought why not try it out myself.

After playing around some websites I came across “developer.amazon.com”.
so I created my account with “<script>alert()</script>” as you might have expected (*Beginner*). After initial futile efforts I started looking at the pattern of request and noticed that name for a feature called “Security Profile” is being directly thrown in the source code and can be elevated to XSS.

So I created the security profile with bunch of payload in place of names.

Press enter or click to view image in full size
This is how the profiles looked like

So once the payload is placed I wanted to trigger it so I ended up calling the “Dash Services” which I came to know is the place to trigger after looking at the request-response pattern!

Press enter or click to view image in full size

and I hit “Begin”.

Press enter or click to view image in full size
Document.Cookie

and my payload executed. So this is not the moment of joy as this is known as “Self-XSS” meaning you can only inject payload on yourself and can’t harm anyone else with it. I ended up escalating this issue to logout CSRF which indeed ended up as a valid issue.

Get Coding_Karma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Lessons :-

Every XSS isn’t XSS that’s a game winner. If you find a vulnerability that is limited always try to escalate it to something more severe.
Bug bounty isn’t easy and takes time learn through the process don’t “Quit”.
For the love of god listen to people more experienced and don’t act like an idiot. Read blogs/posts/write ups to get started and learn new methods!
Have Patience! Lots of it.

Time Line :-

Reported on 17th July.

Issue Acknowledged and Triaged on 18th July.

Fixed 24th July.

Amazon didn’t offer any momentary reward because they don’t have the policy for the bounties.

Before I end this post I would really like to thank @Karel_Origin and Robert Smith for helping me out with my journey to bug bounty.

Thank You!
