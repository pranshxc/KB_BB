---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-29_facebook-bug-bounty-story-x000-for-an-information-disclosure-bug.md
original_filename: 2019-12-29_facebook-bug-bounty-story-x000-for-an-information-disclosure-bug.md
title: 'Facebook Bug bounty Story: $X000 for an Information Disclosure Bug'
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 428c87a4a95bbab7f64be8f64109dce2bee4cd25b319b005618f390ab8d43d58
text_sha256: 8e1720e370a5dcff52f49323f626027fc11ab7d5b0c987a4ffd4a0f961bbf962
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Bug bounty Story: $X000 for an Information Disclosure Bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-29_facebook-bug-bounty-story-x000-for-an-information-disclosure-bug.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `428c87a4a95bbab7f64be8f64109dce2bee4cd25b319b005618f390ab8d43d58`
- Text SHA256: `8e1720e370a5dcff52f49323f626027fc11ab7d5b0c987a4ffd4a0f961bbf962`


## Content

---
title: "Facebook Bug bounty Story: $X000 for an Information Disclosure Bug"
url: "https://medium.com/bug-bounty-hunting/facebook-bug-bounty-story-x000-for-an-information-disclosure-bug-f0c0d19d7815"
authors: ["Circle Ninja (@circleninja)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
publication_date: "2019-12-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4856
scraped_via: "browseros"
---

# Facebook Bug bounty Story: $X000 for an Information Disclosure Bug

Facebook Bug bounty Story: $X000 for an Information Disclosure Bug
Ronnie Joseph
Follow
2 min read
·
Dec 29, 2019

395

1

Press enter or click to view image in full size

Around last year, I reported a valid security bug in Facebook but didn’t know how to explain the impact of the issue. Even after finding the bug, I couldn’t figure out the attack scenario / or what the security team would accept! Some weeks later, I find that FB rewarded Sarmad Hassan (jubabaghdad) with $3k . (https://bugreader.com/jubabaghdad@disclose-thumbnail-of-any-video-in-facebook-workplace-87)

Kudos to him. :)

Then Bountycon happened. Very grateful for the team to invite me. Never expected. Met and saw some great security researchers :P !

Revived my interest to hunt bugs on Facebook to give a “return gift”

Bug-

My friend had started a Facebook page to post funny videos.

One video was very funny. I knew his fb id and also that he is the admin of the page.

Example admin id- xxxx

While viewing a video, I simply right clicked, View Page Source, searched xxxx.

Boom! One result found.

Get Ronnie Joseph’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The page source was leaking the id of the person who was the content owner.

Press enter or click to view image in full size
Impact-

Fb Page Admin, editor... Disclosure

Attacker can view page source from the video section of the Facebook page and find the users with page roles. ( If editor had uploaded the video, it will leak his/her fb id. )

This was fixed within < day. Nice Reward!

I think this maybe the most easiest of security bugs found ever on Facebook which maybe be exploited at large scale without any proxy or advanced steps.

This bug was found sub consciously. I never was hunting for any security issue. So always be humble, honest and grateful!

I would like to thank @phwd, Max Pasqua, Sarmad Hassan, Kassem Bazzoun ,Richard Cao and others for the inspiration of this writeup. There are only a few people who do writeups and I respect them !

Connect with me on Twitter: https://twitter.com/CircleNinja and join me to write your hacking story on this Not for Profit publication !
