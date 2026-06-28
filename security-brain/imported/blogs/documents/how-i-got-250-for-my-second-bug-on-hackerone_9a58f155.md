---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-09-01_how-i-got-250-for-my-second-bug-on-hackerone.md
original_filename: 2024-09-01_how-i-got-250-for-my-second-bug-on-hackerone.md
title: How I Got $250 For My Second Bug on HackerOne
category: documents
detected_topics:
- oauth
- sso
- command-injection
tags:
- imported
- documents
- oauth
- sso
- command-injection
language: en
raw_sha256: 9a58f1552086088c2749e8e22d3169dd20599b9690f7064fad1e6d84f5774ffc
text_sha256: e76f13e21f0bd43bd1342ce82430d7076d94a0c99b4015a9a7a788a4defe47ac
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# How I Got $250 For My Second Bug on HackerOne

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-09-01_how-i-got-250-for-my-second-bug-on-hackerone.md
- Source Type: markdown
- Detected Topics: oauth, sso, command-injection
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `9a58f1552086088c2749e8e22d3169dd20599b9690f7064fad1e6d84f5774ffc`
- Text SHA256: `e76f13e21f0bd43bd1342ce82430d7076d94a0c99b4015a9a7a788a4defe47ac`


## Content

---
title: "How I Got $250 For My Second Bug on HackerOne"
url: "https://medium.com/@likithteki76/how-i-got-250-for-my-second-bug-in-hackerone-35c75cbd84bd"
authors: ["Likith Teki"]
bugs: ["OAuth", "Session expiration issue"]
bounty: "250"
publication_date: "2024-09-01"
added_date: "2024-09-04"
source: "pentester.land/writeups.json"
original_index: 28
scraped_via: "browseros"
---

# How I Got $250 For My Second Bug on HackerOne

How I Got $250 For My Second Bug on HackerOne
Likith Teki
Follow
2 min read
·
Sep 1, 2024

243

4

Hello everyone, I hope you all are doing Great! Today’s writeup explains how I earned $250 from my second bug report on HackerOne.

If you haven’t read my first article, please check it out by clicking the link below:

How I Got $150 on HackerOne for My First Bug
Hello everyone, I’m Likith Teki A bug bounty Hunter and Ethical Hacker

medium.com

Title : Removing linked identity does not invalidate associated sessions

While hunting on a private program on HackerOne, let’s call the target domain “domain.com.” On domain.com, I discovered a functionality where users could add two emails: a primary email used to create the account and a secondary one added via account settings. I was intrigued by this setup and decided to test it out.

I initially attempted to log in using the secondary email and password, but since the account was created with the primary email, I couldn’t log in. Next, I tried logging in with the secondary email using OAuth via Google. To my surprise, I successfully logged in!

At this point, I had the account logged in across two browsers:

Chrome: using the primary email (attacker1@gmail.com).
Firefox: using the secondary email (attacker2@gmail.com) via Google OAuth.

In Chrome, I changed the secondary email to mine (mine@gmail.com), and also disabled the option to disconnect Google accounts. When I reloaded the session in Firefox, the session was still active! I was able to change the account details, including reverting the secondary email back to attacker2@gmail.com. Reloading Chrome showed that all changes were reflected.

Get Likith Teki’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This confirmed a session management vulnerability. I reported it to the program via HackerOne, and a week later, I was awarded $250!

Steps to Reproduce:
Victim’s Actions:
Log in to the application using primary account credentials.
Add a secondary email address to the account.
Link the account to the secondary email’s Google account using OAuth.

2. Attacker’s Actions:

Gain access to the victim’s session via Google authentication of the secondary email.

3. Victim’s Actions:

Log in to the primary account.
Delete the secondary email address from the account.
Disconnect the Google account from the primary account.

4. Attacker’s Actions:

Refresh the session in the attacker’s browser.

5. Observation:

The session remains active despite the disconnection.
The attacker can modify the victim’s account data.
Impact
Unauthorised access: Attackers can gain unauthorised access to the victim’s account by exploiting this vulnerability.
Privacy breach: This vulnerability compromises the privacy and security of user accounts by allowing access via a deleted, but previously verified email address.
Press enter or click to view image in full size

Tip: Always try to check all functionalities and attempt to bypass them. You might discover critical vulnerabilities that could lead to significant rewards.

Thank you So much for reading! Happy Hacking!

Connect with me:

Twitter: @likith_teki
LinkedIn: likithteki
