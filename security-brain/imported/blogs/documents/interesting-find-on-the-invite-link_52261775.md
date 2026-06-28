---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-02_interesting-find-on-the-invite-link.md
original_filename: 2022-12-02_interesting-find-on-the-invite-link.md
title: Interesting find on the Invite link
category: documents
detected_topics:
- command-injection
- otp
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- otp
- business-logic
- api-security
language: en
raw_sha256: 52261775cfbb80a9a274e2a24624c165d5d005e5ee6b2cdb635b6e51e7c88ce0
text_sha256: 8d84f7d58b62e11e5104ba0a3e8b4514b81b5324886177de1f9b6b54ac0efc65
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Interesting find on the Invite link

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-02_interesting-find-on-the-invite-link.md
- Source Type: markdown
- Detected Topics: command-injection, otp, business-logic, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `52261775cfbb80a9a274e2a24624c165d5d005e5ee6b2cdb635b6e51e7c88ce0`
- Text SHA256: `8d84f7d58b62e11e5104ba0a3e8b4514b81b5324886177de1f9b6b54ac0efc65`


## Content

---
title: "Interesting find on the Invite link"
url: "https://medium.com/@sathvika03/interesting-find-on-the-invite-link-17cf5a46d747"
authors: ["Sathvika"]
bugs: ["Logic flaw"]
publication_date: "2022-12-02"
added_date: "2022-12-09"
source: "pentester.land/writeups.json"
original_index: 1829
scraped_via: "browseros"
---

# Interesting find on the Invite link

Interesting find on the Invite link
Sathvika
Follow
2 min read
·
Dec 2, 2022

50

2

Hi everyone, hope everyone is doing good

Today I would like to talk about how I found an interesting bug that could create numerate accounts without the need of any subscription. So lets find out more about it.

Since it is a private program and due to its disclosure policy I cannot disclose its name. But let us call it redacted.com

How I found

The application has a unique feature that doesn’t let you register for an account indeed you need to request an account. When you request them with your details such as First name, Last name, and email ID they will send you an invitation link that looks like this

https://redacted.com/invite=eyJmaXJzdE5hbWUiOiJIYWNrdDNyIiwibGFzdE5hbWUiOiJNNHplIiwibG9naW5JZCI6ImhhY2t0M3JAbTR6ZS5jb20iLCJpbnZpdGVFbWFpbFRlbXBsYXRlIjpmYWxzZX0=

You need to open the link, and set a password for yourself and you are good to use your account.

Seems very secure right!!!

But here comes the problem. The link they sent has only one parameter called “invite” which caught my attention. So, I tried to decode the URL using base64 and to my surprise, the data I sent for registration was in the decoded string.

{"firstName":"Hackt3r","lastName":"M4ze","loginId":"hackt3r@m4ze.com","inviteEmailTemplate":false}

This doesn’t seem to be that big of an issue. Then I thought what would happen if I change the details, encode it, and use it again for another account. I have tried it and now I could create another account on behalf of some x person without having to request for another signup link.

Get Sathvika’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This may not be a huge vulnerability if it were a normal application, but since the application has no registration page and works on a one-time subscription an attacker can pay for one account and create any number of accounts with the same URL. I reported the vulnerability and it was a high issue.

How to prevent it

There are multiple ways to prevent it but I will tell you a few and it is your duty to find the other and let me and others know your ways in comments.

Using a specially crafted token instead of an Invite parameters
Hiding the details of the user in the invite link
Making sure to expire the link once it is used

So, here is how I have found an interesting catch. Hope you have enjoyed this and learned something new. Check out my Instagram to learn more about Tips and Tricks for finding bugs.

Till then take care and Happy Hacking!!!

PS: I am not being very active for a few months but whenever I find free time and an interesting vulnerability I will share it with you all.
