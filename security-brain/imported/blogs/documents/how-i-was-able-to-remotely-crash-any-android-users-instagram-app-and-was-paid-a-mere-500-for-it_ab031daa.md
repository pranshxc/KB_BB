---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-15_how-i-was-able-to-remotely-crash-any-android-users-instagram-app-and-was-paid-a-.md
original_filename: 2018-02-15_how-i-was-able-to-remotely-crash-any-android-users-instagram-app-and-was-paid-a-.md
title: How I was able to remotely crash any android user’s instagram app and was paid
  a mere 500$ for it.
category: documents
detected_topics:
- command-injection
- automation-abuse
- mobile-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- mobile-security
language: en
raw_sha256: ab031daaa11d6b0d207efc479cbc72d181213265081be1860afd7025e4e5d2fa
text_sha256: 5a670fbee38dffb95b2f427f8d6c36013972748dca28973c89cd40f206329081
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to remotely crash any android user’s instagram app and was paid a mere 500$ for it.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-15_how-i-was-able-to-remotely-crash-any-android-users-instagram-app-and-was-paid-a-.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, mobile-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `ab031daaa11d6b0d207efc479cbc72d181213265081be1860afd7025e4e5d2fa`
- Text SHA256: `5a670fbee38dffb95b2f427f8d6c36013972748dca28973c89cd40f206329081`


## Content

---
title: "How I was able to remotely crash any android user’s instagram app and was paid a mere 500$ for it."
url: "https://medium.com/bugbountywriteup/how-i-was-able-to-remotely-crash-any-android-users-instagram-app-and-was-paid-a-mere-500-for-it-d4420721290e"
authors: ["Waleed Ahmed"]
programs: ["Meta / Facebook"]
bugs: ["Android", "DoS"]
bounty: "500"
publication_date: "2018-02-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5974
scraped_via: "browseros"
---

# How I was able to remotely crash any android user’s instagram app and was paid a mere 500$ for it.

How I was able to remotely crash any android user’s Instagram app
Waleed Ahmed
Follow
3 min read
·
Feb 16, 2018

173

2

Let me start the article by introducing myself, I am Waleed Ahmed, a 16 year old boy from Pakistan. So, last December I found a vulnerability in Instagram's android app by which I was able to remotely crash any Instagram android user’s app instantly just by just sending a simple message. The vulnerability didn’t even require the victim to even open the message. Let me go through how was I able to discover the bug.
One day, I was just scrolling through some of my old convos in my DM folder. I found in one particular chat with one person, If I tried to scroll up in the chat, the app immediately crashed. I figured out that some message was causing the the app to crash on the new android Instagram app version. In order to find and view the message, I downloaded an older version of the android instagram app. On this version, I was able to scroll normally and view the message that was causing my app to crash. The message was 40 emojis with a space between any of the two emojis. It was a really weird behaviour from the app. I tried sending this message from my old instagram app to other accounts controlled by me and in every case, it instantly crashed the app. I tried it on multiple android smartphones and it worked all the time. Furthermore the vulnerability also allowed me to do the following things:
1: Making previous messages between the attacker and victim inaccessible. when an attacker sends the attack message to the victim. All the previous messages between the attacker and victim will become inaccessible to the victim and he will not be able to see the messages.
2: Making the message requests folder of a celebrity or a normal person inaccessible by sending the celebrity a message request containing the emojis. when an attacker sends this message to any user that has not followed him/her, the message will go into the message requests folder of the victim. When the victim will try to open his/her message requests folder, the message requests folder will get stuck on the loading icon.
3: Making the entire DM folder of a user inaccessible. This happens when the user logs in after the attacker has sent the message. This causes the instagram DM folder to never load and it is stuck on the loading icon.

I had tested all of these things personally and I had reported them in my Facebook bug report.

TIMELINE:

28 November: Initial Report

1 December: Facebook staff creates an instagram account for me to demonstrate the bug

6 December: Acknowledgement of bug.

Get Waleed Ahmed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

14 December: Bug fixed.

20 December: Bug bounty of 500$ issued.

20 December: I write a follow up asking if the bug bounty correctly reflects the impact of the bug.

22 December: Facebook replies that they have determined that this is the appropriate bounty for this bug

Press enter or click to view image in full size
Press enter or click to view image in full size

Here is my conversation with one of the Facebook staff member who created an account for me to demonstrate the bug.

Consider some bots sending millions of these messages to millions of instagram users, disrupting the usage of instagram app for those millions of users. It would be a great nightmare for instagram.
