---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-24_bug-bounty-fastmail-poboxcom-account-takeover.md
original_filename: 2021-09-24_bug-bounty-fastmail-poboxcom-account-takeover.md
title: 'Bug-Bounty | FASTMAIL [pobox.com : account takeover]'
category: documents
detected_topics:
- command-injection
- password-reset
tags:
- imported
- documents
- command-injection
- password-reset
language: en
raw_sha256: ed07b4289b825d265c87308cac9fc95e21a2bac59d306a8258da21e8b05cfcd2
text_sha256: 4529866a3aa2ae470edfa5043a74cda37d9bdb68eaaffffc70fb1127376d7632
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Bug-Bounty | FASTMAIL [pobox.com : account takeover]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-24_bug-bounty-fastmail-poboxcom-account-takeover.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `ed07b4289b825d265c87308cac9fc95e21a2bac59d306a8258da21e8b05cfcd2`
- Text SHA256: `4529866a3aa2ae470edfa5043a74cda37d9bdb68eaaffffc70fb1127376d7632`


## Content

---
title: "Bug-Bounty | FASTMAIL [pobox.com : account takeover]"
url: "https://medium.com/@the.white.soul.0/bug-bounty-fastmail-pobox-com-account-takeover-e1e2fd190a2"
authors: ["Mohammed ELdawody"]
programs: ["Fastmail"]
bugs: ["Account takeover", "Password reset"]
publication_date: "2021-09-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3289
scraped_via: "browseros"
---

# Bug-Bounty | FASTMAIL [pobox.com : account takeover]

Bug-Bounty | FASTMAIL [pobox.com : account takeover]
Mohammed Eldawody
Follow
2 min read
·
Sep 24, 2021

7

Hi everyone

I would like to share with you one of my findings in Fastmail company, I was able to find an account takeover vulnerability in one of their services “pobox.com”

First I want to explain how the site works. The website provides an email service where u can create your own email address and use it to send and receive emails “Like G-mail”

IF you lose access to your email address you can provide some information to recover it and you can choose where to send the reset password link

After searching for a while and understanding how the website works, I was able to find a page where we can reset the password using user account information. Reset link

As you can see, we can choose the email address that we want to recover, and choose where the reset link will be sent

Get Mohammed Eldawody’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The next step is: fill in the account information

As we can see, there are many data that are required. after testing for a while I found the following:

The server only checks the “Security-Question”, all the other data are not important
If the Security-Question is correct you will receive the reset link, if not you won’t

Well…

what if the user doesn’t have a security question? that means its value in the DB is “NULL” or “Empty” or “ ”

So I tried to submit the security question as an Empty value, and the password reset link was sent to me and I was able to take over the account

“The email address that is being used to send reset password links to users wasn’t using a SECURITY-QUESTION and that could lead to take over any account in the website doesn’t matter it has a security question or not”

The report was accepted as a critical bug

Mohammed ELdawody
Discord : MoEldawody#4147
