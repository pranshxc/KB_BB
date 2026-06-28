---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-10_privacy-disclosure-on-facebook-lite-after-creating-a-post.md
original_filename: 2022-04-10_privacy-disclosure-on-facebook-lite-after-creating-a-post.md
title: Privacy Disclosure on Facebook Lite after Creating a Post
category: blogs
detected_topics:
- command-injection
- api-security
tags:
- imported
- blogs
- command-injection
- api-security
language: en
raw_sha256: 3149f26989fc097cf9d749a2c076bf9c31aad5eb77c826ba9e961948d25dff93
text_sha256: e3b3891599ad1f9bcd65c4ab5179934eee5df465384cafb141586a11457b2754
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Privacy Disclosure on Facebook Lite after Creating a Post

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-10_privacy-disclosure-on-facebook-lite-after-creating-a-post.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `3149f26989fc097cf9d749a2c076bf9c31aad5eb77c826ba9e961948d25dff93`
- Text SHA256: `e3b3891599ad1f9bcd65c4ab5179934eee5df465384cafb141586a11457b2754`


## Content

---
title: "Privacy Disclosure on Facebook Lite after Creating a Post"
url: "https://medium.com/@RheyJuls/privacy-disclosure-on-facebook-lite-after-creating-a-post-b12a1cad8d8a"
authors: ["Rhey"]
programs: ["Meta / Facebook"]
bugs: ["Privacy issue"]
bounty: "400"
publication_date: "2022-04-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2730
scraped_via: "browseros"
---

# Privacy Disclosure on Facebook Lite after Creating a Post

Privacy Disclosure on Facebook Lite after Creating a Post
Rhey
Follow
3 min read
·
Apr 10, 2022

71

1

Hello,

I’m Rey Julius Sanchez from the Philippines and I started Bug Hunting (META Platforms only) around October 2021.

Summary:

This bug is present after the user makes a post or sets his/her default privacy audience from “Public/Friends” to “Only Me” in FB4A, On Facebook Lite while creating a post the audience is now already set to “Only Me” and after making a post, The selected privacy settings “Only Me” is not applied (as the default audience changed back to “Public/Friends”).

=========

So let’s start, Around December 2021 While reading their Post Policy Privacy, I found an interesting and easy to find bug.

Press enter or click to view image in full size
I got curious here..

while reading I thought why don’t I try to change my default privacy audience from Public to “Only Me” in FB4A

Press enter or click to view image in full size

After Changing to “only me”, I make a post and share it to my news feed and timeline.

Press enter or click to view image in full size

After that I go to FB Lite and while creating a post, The selected audience is already applied or set to “only me”. Then I try to create a post on FB Lite(“Only Me”) and share it to my newsfeed/Timeline

Press enter or click to view image in full size

but after I make a post it is disclosed to my previous settings(“Public”).

Press enter or click to view image in full size

Impact:

Get Rhey’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This could lead to comprised the privacy of the users as they set their default privacy on FB4A to “Only Me” but after they create a post in FB Lite it disclosed to Public and set their default audience to their previous privacy settings (“Public”)

I was very happy to have this bounty reward ❤

Press enter or click to view image in full size
Press enter or click to view image in full size

Timeline:

Report Sent: 12/15/2021

Triaged: 12/18/2021

Fixed by Facebook: 04/04/2022

Bounty: $4,400 with bonus

Follow me on my Facebook Account. Thanks! :)
