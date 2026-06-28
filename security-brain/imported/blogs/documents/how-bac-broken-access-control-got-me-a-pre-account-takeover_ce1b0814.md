---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-27_how-bacbroken-access-control-got-me-a-pre-account-takeover.md
original_filename: 2023-06-27_how-bacbroken-access-control-got-me-a-pre-account-takeover.md
title: How BAC(Broken Access Control) got me a Pre Account Takeover
category: documents
detected_topics:
- access-control
- idor
- command-injection
- password-reset
- mfa
- api-security
tags:
- imported
- documents
- access-control
- idor
- command-injection
- password-reset
- mfa
- api-security
language: en
raw_sha256: ce1b081442a61b4f665c47c1fbe05525e3a8feac046e48b49ff84db28d0f65fc
text_sha256: 0d6c645ba182239253431e7527f6738c514c1a4bc34503797cb7cafa73777905
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# How BAC(Broken Access Control) got me a Pre Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-27_how-bacbroken-access-control-got-me-a-pre-account-takeover.md
- Source Type: markdown
- Detected Topics: access-control, idor, command-injection, password-reset, mfa, api-security
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `ce1b081442a61b4f665c47c1fbe05525e3a8feac046e48b49ff84db28d0f65fc`
- Text SHA256: `0d6c645ba182239253431e7527f6738c514c1a4bc34503797cb7cafa73777905`


## Content

---
title: "How BAC(Broken Access Control) got me a Pre Account Takeover"
url: "https://bharat-singh.medium.com/how-bac-broken-access-control-got-me-a-pre-account-takeover-2481931b7b3a"
authors: ["Bharat Singh"]
bugs: ["Pre-account takeover", "IDOR"]
publication_date: "2023-06-27"
added_date: "2023-06-27"
source: "pentester.land/writeups.json"
original_index: 999
scraped_via: "browseros"
---

# How BAC(Broken Access Control) got me a Pre Account Takeover

Top highlight

How BAC(Broken Access Control) got me a Pre Account Takeover
Bharat Singh
Follow
3 min read
·
Jun 27, 2023

1.2K

2

Press enter or click to view image in full size
Introduction:

Hey Hackers!!!

This is a writeup about one of my recent findings on a VDP. I found a Broken Access Control bug which was eventually leading to Pre-Account Takeover. Lets head on to our main story…

Story of the Bug:

It was a typical, boring and unexciting Saturday, I was looking for something to kill the time. So, I decided to do some bug hunting. With the help of this Bug Bounty Google Dork list I found a program to test my skills.

When I signed up on the web application, I discovered some interesting features like creating groups and inviting users. As a bug hunter, it felt like stumbling upon a treasure chest of possibilities, I started manually hunting for Vulnerabilities in Password Reset and 2FA Functionality but I got nothing there. So I went for User Manager option to test without wasting any more time.

Next, using a test account called “attacker@778899gmail.com” I invited myself to the platform. Then, I explored the User Manager option to see what information I could find.

There we got some basic info about the invited user like name, login, email… Here the login field is responsible for password change, But I was not allowed to change the login and email field of the invited user.

Press enter or click to view image in full size
Not allowed to change Login and Email

I intercepted the request and attempted to modify the login parameter, hoping it would give me Account Takeover to the invited user’s account. Unfortunately, my plan didn’t work out as expected. However, I didn’t give up just yet.

Get Bharat Singh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I went to change the Email address to “victim778899@gmail.com” by intercepting the request and to my surprize it actually changed the email address of the invited user on the front-end as well as on back-end.

Press enter or click to view image in full size
Change the email parameter in request body
Press enter or click to view image in full size
Email Successfully changed

I know this is a Low Severity bug, but this is an intresting find for me, So I couldn’t resist sharing this writeup with all of you.

Impact:

This vulnerability can lead to Per Account Takeover of any unregistered user and an attacker can misuse the identity of the victim.

Timeline:

25-March-2023 >> Bug Reported

20-June-2023 >> They patched the vulnerability & marked it as low severity.

Press enter or click to view image in full size
Their Response

If you guys like this writeup and learned something valuable then do hit the clap 👏 X 50 times.

Feel free to connect with me on Linkedin and Twitter.
