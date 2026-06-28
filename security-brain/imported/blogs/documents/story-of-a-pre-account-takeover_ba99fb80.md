---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-06_story-of-a-pre-account-takeover.md
original_filename: 2020-11-06_story-of-a-pre-account-takeover.md
title: Story of a Pre-Account Takeover
category: documents
detected_topics:
- oauth
- sso
- command-injection
- api-security
tags:
- imported
- documents
- oauth
- sso
- command-injection
- api-security
language: en
raw_sha256: ba99fb80aef94b766398857d26f58675eef60b33d1f542a61615ba9131fb0f39
text_sha256: 5a86c2163604815a11af5bad2ab58f8ca5bf7a0f519a8361944b35d6faab2c25
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Story of a Pre-Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-06_story-of-a-pre-account-takeover.md
- Source Type: markdown
- Detected Topics: oauth, sso, command-injection, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `ba99fb80aef94b766398857d26f58675eef60b33d1f542a61615ba9131fb0f39`
- Text SHA256: `5a86c2163604815a11af5bad2ab58f8ca5bf7a0f519a8361944b35d6faab2c25`


## Content

---
title: "Story of a Pre-Account Takeover"
url: "https://dhakal0kushal.medium.com/story-of-a-pre-account-takeover-33e3d5b4c33f"
authors: ["Kushal Dhakal (@dhakal0kushal)"]
bugs: ["Account takeover", "OAuth"]
publication_date: "2020-11-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4155
scraped_via: "browseros"
---

# Story of a Pre-Account Takeover

Press enter or click to view image in full size
Story of a Pre-Account Takeover
Kushal Dhakal
Follow
Nov 5, 2020

303

1

Hello everyone, hope you are having a great day. Today I am going to talk to you about an interesting bug that I found on a private program on HackerOne.

Get Kushal Dhakal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

It is one of the most popular investing apps on the market. I can not disclose the name of the program since the vulnerability is not fixed yet. The application allowed its users to login with its own authentication system or Social Authentication (Google and Facebook). The flaw was in the ‘Login with Google/ Facebook’ functionality as there was no ‘Disconnect from Google/ Facebook’ feature available. Once a social account was associated with an email, it was forever added and can't be unlinked. Let me walk you through the steps to reproduction:

Sign Up for an account with the attacker’s Google account.
After signup, the attacker will be prompted to set a username, email, and password for the account.
The attacker changes the email to the victim’s email, sets his username and password, and completes the signup process.

4. When the victim tries to create an account, the email already exists message pops up. Now the victim tries to reset the account password and successfully does so.

The victim is unaware of the fact that the Google account of the attacker is still connected to his account. There is no way he can unlink the attacker’s Google account from his account.

The attacker just needs to use Google Login functionality to access the victim’s account and boom.

This was it for my first bug bounty writeup. Hope this will help you learn something new. Peace.
