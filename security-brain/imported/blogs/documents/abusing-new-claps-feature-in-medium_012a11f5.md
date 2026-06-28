---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-10-29_abusing-new-claps-feature-in-medium.md
original_filename: 2017-10-29_abusing-new-claps-feature-in-medium.md
title: Abusing new Claps feature in Medium
category: documents
detected_topics:
- sso
- idor
- command-injection
- api-security
tags:
- imported
- documents
- sso
- idor
- command-injection
- api-security
language: en
raw_sha256: 012a11f5f9a7a1cea3ca7c432d60e26c91d7d67a293c32eedfe8b1f0af65f286
text_sha256: c4c16150ff155cab43926e2b9c664b20fbe7b2e92ecc230172bc692c29697adf
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Abusing new Claps feature in Medium

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-10-29_abusing-new-claps-feature-in-medium.md
- Source Type: markdown
- Detected Topics: sso, idor, command-injection, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `012a11f5f9a7a1cea3ca7c432d60e26c91d7d67a293c32eedfe8b1f0af65f286`
- Text SHA256: `c4c16150ff155cab43926e2b9c664b20fbe7b2e92ecc230172bc692c29697adf`


## Content

---
title: "Abusing new Claps feature in Medium"
url: "https://medium.com/bugbountywriteup/abusing-new-claps-feature-in-medium-6bd8757a64a4"
authors: ["Sai Krishna Kothapalli (@kmskrishna)"]
programs: ["Medium"]
bugs: ["IDOR"]
publication_date: "2017-10-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6068
scraped_via: "browseros"
---

# Abusing new Claps feature in Medium

Abusing new Claps feature in Medium
Sai Krishna Kothapalli
Follow
4 min read
·
Oct 29, 2017

1.98K

Press enter or click to view image in full size
Medium Hall Of Fame

This story is going to be about how I got into the Medium Hall Of Fame. From this semester I started writing articles on Medium on the topics which I found interesting and was working on. Another reason to choose Medium over other platforms was its simplicity and convenience of use.

After one sleepless night, I opened Medium to write about something and then noticed that the infamous heart symbol with which you could love posts was gone. It had been replaced by ‘claps’. Surprised, I went on Twitter to check what had happened. Just like me, many other users were also confused. After a bit of digging, I landed on this blog post by Medium which explained the new feature.

The blog mentioned how the new feature works. There were some points which caught my attention.

You cannot clap for your own posts.

Only a post’s author can see how many claps individual users gave. Readers will see only a list of who clapped.

Claps on a post are limited to 50 per user.

At this point, the fellow Bug Bounty hunters out there would understand how I got triggered by these new features and wanted to test the claims immediately.

You cannot clap for your own posts.

You can not clap for your own story because the clap button is disabled on all of your own stories. That got me thinking: “Okay, but how about sending a POST request? Are they doing a back-end check or is it just front-end?” So I clapped for another story on Medium and captured the request using Burp Suite.

This is how the request looks for a Clap. As you can see a POST request is sent to /_/api/posts/STORY_ID/claps.

Get Sai Krishna Kothapalli’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As you can see after I changed the STORY_ID and made the request. I got a 200 status response and success:true. Which means it succeeded. Classic case of IDOR.

POST request

And one can clap 50 times to a story. I tried to bypass this too (by clapping more than 50 times). But none of the techniques worked. I clapped 50 times for my own post though. Luckily, Medium didn’t remove the claps on my story after I reported the same.

Clapping for my own stories.

Only a post’s author can see how many claps individual users gave. Readers will see only a list of who clapped.

Again a GET request to /p/POST_ID/upvotes gives you the list of users who clapped.According to Medium, readers will see only a list of those who clapped but not how many claps each user gave.

In the response to the GET request, there is a field called clapCount respective to every user who clapped to a particular post, which as the name says is the clap count. Any user can see the clap count of any post. Again they were using front-end checks instead of back-end checks.

This issue was reported to Medium and has since been fixed. As this does not have any security implication there was no bounty (was expecting none anyway). But they did offer some schwag and added my name to their Hall Of Fame page too. One lesson to learn from this is that never just rely on front-end restrictions; do everything on the back-end.

A couple of opinions on the Medium Bug Bounty program: they are really slow at fixing the issues. That is okay if they have some high priority issues. But, they are even slow at replying to your emails and reports and terrible at follow ups. I had to hit them up on Twitter every time I wanted a reply.

Well, this is not exactly abusing the claps feature :P. The title is just a click bait.

P.S: Still didn’t get the schwag.

If you are a Bug Bounty hunter and blog about some techniques or your experiences or write writeups on Medium please consider submitting them to this publication (BugBountyWriteup).

Peace ❤
