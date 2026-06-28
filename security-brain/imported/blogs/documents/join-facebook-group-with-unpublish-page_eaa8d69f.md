---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-01_join-facebook-group-with-unpublish-page.md
original_filename: 2021-03-01_join-facebook-group-with-unpublish-page.md
title: Join Facebook Group With Unpublish Page
category: documents
detected_topics:
- sso
- idor
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- sso
- idor
- access-control
- command-injection
- api-security
language: en
raw_sha256: eaa8d69f4e16e8f88f004824573a6a5d97c5cccf16d159935e4e0b154406bb9a
text_sha256: aeb144205ee04b45a223f112fcb275908d34c32f33d7c6b3131f0e1c26154494
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Join Facebook Group With Unpublish Page

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-01_join-facebook-group-with-unpublish-page.md
- Source Type: markdown
- Detected Topics: sso, idor, access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `eaa8d69f4e16e8f88f004824573a6a5d97c5cccf16d159935e4e0b154406bb9a`
- Text SHA256: `aeb144205ee04b45a223f112fcb275908d34c32f33d7c6b3131f0e1c26154494`


## Content

---
title: "Join Facebook Group With Unpublish Page"
url: "https://gevakun.medium.com/join-facebook-group-with-unpublish-page-cb649a20fb0e"
authors: ["gevakun"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
publication_date: "2021-03-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3850
scraped_via: "browseros"
---

# Join Facebook Group With Unpublish Page

Join Facebook Group With Unpublish Page
Publish a page without publishing it
Geva-Kun
Follow
4 min read
·
Feb 28, 2021

121

بِسْمِ للَّٰهِ لرَّحْمَٰنِ لرَّحِيمِ

Hey, welcome to this write-up!

What I’ve found is only from Allah’s will, actually I’m nothing.

Note:

There’s “TL;DR” section for those who only need the main point of this write-up.
I really apologize if my write-up is bad.
By the way, this is my first write-up.

Enjoy :)

I. TL;DR
You can join public facebook group using your facebook page. But, you can’t do it with unpublish page.
When you click join group button, there’s profile selector to choose your page/profile.
Intercept the request when you choose one of it.
There’s “actor_id” parameter with selected facebook page/profile ID as value.
Change the value to your unpublish page ID.
Also, i can post a limited status with that unpublish page by changing “actor_id” value in “Create Post” feature.
II. Introduction

Groups are a place to communicate about shared interests with certain people. You can create a group for anything — your family reunion, your after-work sports team or your book club.

To join group, you can use your primary Facebook profile or your Facebook page as long as the group admin allow it.

Press enter or click to view image in full size
Admin Settings (https://www.facebook.com/groups/{id}/edit)

If the group admin allow page to join, you’ll notice selector like this when clicking “Join Group” button, so you can choose how to join group:

Profile Selector

But only published page that able to join group.

Actually, can i see unpublish page?

The answer is, no. If you try to directly access the unpublish page with their URL, you’ll get this message:

“Not Found” message.
III. The Findings

When I testing around group features back then, I just found out that I can join the group with my page, without thinking too much, I immediately mess with it.

Get Geva-Kun’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And then I noticed a weird situation, I only saw a few of the many created pages I have. Apparently, the page that didn’t appear was the page that still unpublished or I don’t have enough permissions (I’m not the page admin, etc).

So i tried to intercept the request when i choose one of my page/profile, and request like this appear:

Press enter or click to view image in full size
Profile Selector Request (Illustration)

I change “actor_id” value to my unpublish page, then send the request.

Immediately I check my dummy account (group admin), it’s success, the unpublish page appear in group “Member Request” page (it’s because I enabled pre-approved feature)

Press enter or click to view image in full size
Just Illustration

Also, I able to approve it.

IV. Exploitation

As far as I can remember, I couldn’t post anything using that page, because I couldn’t choose the profile (maybe because it’s unpublish), so I try to find way how to exploit this. Actually, the successful of joined page is enough, but i tried to increase the impact.

I decided to test “Create Post” feature.

Create Post Feature

By intercepting request after clicking “Post” button, request like this appear:

Press enter or click to view image in full size
“Post” feature request illustration

As you can see, there’s also “actor_id” parameter, then I change the value with the previous unpublish page ID, and send the request.

It’s worked!

But I can’t post “Attachment” things like image, file, watchparty, etc. Except for GIF, I don’t know why.

I tried to do the same things on “Like” and “Comment” feature (by changing the “actor_id” value), but I only able to comment on my post.

V. Lesson Learned

When you are faced with a selector that you can select some things (in this case, profile), always try to do IDOR. Also, try to increase the impact of what you’ve found until you get stuck.

VI. Timeline

September 16, 2020 — Report sent

September 19, 2020 — Triaged by Facebook team

September 29, 2020 — Facebook team need more info

September 29, 2020 — I Sent more info

October 15, 2020 — Vulnerability patched

October 16, 2020 — Bounty rewarded

Alhamdulillah, finally this write-up ends here.

Hit me up if you have any inquiries: https://twitter.com/Geva_7

VII. Credits
https://www.facebook.com/help/1629740080681586
