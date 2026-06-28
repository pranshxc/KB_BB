---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-10_how-i-was-able-to-delete-any-facebook-story-where-am-i-mentioned-or-tagged.md
original_filename: 2021-09-10_how-i-was-able-to-delete-any-facebook-story-where-am-i-mentioned-or-tagged.md
title: How I Was Able to delete any facebook story where am I mentioned or tagged
category: documents
detected_topics:
- access-control
- command-injection
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- business-logic
language: en
raw_sha256: dac74182b852e3fc521e003cb82b5f5a6bf32d6a1aecfe379c8e70b9200491c4
text_sha256: 9b0c16c5371dd571f2dd3052221a25cee800cbdda5ea0c4e6de4b70055dc72ae
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How I Was Able to delete any facebook story where am I mentioned or tagged

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-10_how-i-was-able-to-delete-any-facebook-story-where-am-i-mentioned-or-tagged.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `dac74182b852e3fc521e003cb82b5f5a6bf32d6a1aecfe379c8e70b9200491c4`
- Text SHA256: `9b0c16c5371dd571f2dd3052221a25cee800cbdda5ea0c4e6de4b70055dc72ae`


## Content

---
title: "How I Was Able to delete any facebook story where am I mentioned or tagged"
url: "https://sank-dahal.medium.com/how-i-was-able-to-delete-any-facebook-story-where-am-i-mentioned-or-tagged-10c38a50e55c"
authors: ["Sank Dahal (@sank68034756)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
bounty: "1,000"
publication_date: "2021-09-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3327
scraped_via: "browseros"
---

# How I Was Able to delete any facebook story where am I mentioned or tagged

How I Was Able to delete any facebook story where am I mentioned or tagged
Sank Dahal
Follow
4 min read
·
Sep 9, 2021

272

1

Hello readers,

After many months I decided to write writeups regarding my first bounty from Facebook worth 1000$, before reading this writeup I would like to give credit to my big brother because without him I couldn’t have found this bug

Let’s start the story

So, It was a beautiful July 20 (which was my birthday) as it was my birthday many of my internet friends tagged me and said “Happy birthday” to me by posting my pic(Thanks btw) and on the same exact day my brother posted a story where he mentioned me and wrote a text of “Happy birthday Sankalpa” and on that day I used Facebook a lot, I spend over 10 hours straight scrolling Facebook and saying thanks to everyone lol. SO, I decided to deactivate my Facebook because I was using that shit for many hours, but at night my brother said where the hell is the story that I posted and tagged you, he said did you deleted the story and I said “No”, but then I remember my school assignments and thought to reactivate my account then my brother said “Wtf, just happened the story is back” he noticed that weird behavior and I thought to investigate on it a bit, then I found that whenever someone tags me and I deactivate my Facebook then the story will be deleted too, So without wasting my time I reported this issue to Facebook after checking it from all my devices,

Here What I Reported

Title
An attacker can delete victims story via Facebook lite if victim mention attacker in his story and attacker deactivate His account

Vuln Type
Privacy / Authorization

Product Area
FBLite

Description/Impact
Hello team, I encounter really a weird behaviour on Facebook, Today is my birthday(hope you will wish me) and my brother posted story regarding my birthday and mentioned me In his story after some hours I decided to delete my account and my brother said that the story has been deleted and I didn’t deleted, after analysis I came to know if victim mention attacker in his story and attacker delete or deactive his account then victim story will automatically get deleted

Impact

Now, an attacker can delete victim story by deactivating his account if victim mentions attacker on his story

Repro Steps
Steps to reproduce
USERS: user A(attacker), user B(victim)
1. From user B account post a story and mention user A
2. From user A account deactive or delete your account
3. From user B account the story gets automatically deleted

I think, the mention should be removed and not whole story and that’s damn weird

Get Sank Dahal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

At first, they replied me the following

Press enter or click to view image in full size
Couldn’t reporduces wtf?

SO, I sent them a POC’s video

here’s the link in case if you want: https://www.youtube.com/watch?v=ddZDN5jbTYc

Then they replied the following(I literally became mad from the excitement as that was my first Facebook bug which got triaged)

Press enter or click to view image in full size
Triageddddddddd

Then after some days they replied me the following(I literally cummed when they replied with this)

Press enter or click to view image in full size
cummedddd, when they said this lmao

Then they were taking too much time as I was frequently asking “Any update” and I got bored and they finally replied the following

Press enter or click to view image in full size
oh cool, best of luck on investigating

and the day came where I died because of my excitement

Press enter or click to view image in full size
Me *Dead* catch these motherfucker, they are terrorist

And Liked that I received my first motherfucking bounty worth 1000$ from Facebook, if you learned something(i know, you didn’t but lol who cares) then make sure you hit clapped ;) I hope, you enjoy this shitty writeup if you didn't then I don’t really gives a fuck lmao, bye see you next time

till then “Keep learning, keep fapping and keep progressing” jay Nepal ❤
