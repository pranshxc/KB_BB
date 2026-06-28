---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-16_weak-session-validation-bug-let-you-login-even-after-changing-the-session-ids-an.md
original_filename: 2020-03-16_weak-session-validation-bug-let-you-login-even-after-changing-the-session-ids-an.md
title: Weak session validation bug let you login even after changing the session IDs
  and logging out from the accounts
category: documents
detected_topics:
- command-injection
- automation-abuse
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- business-logic
- api-security
language: en
raw_sha256: c81845e3816f2edf295798dd8defc85a11f5e0628d8faac16d53322ba1f06197
text_sha256: 51508ad7b01d195eb700cab167c401ed30c22ff4c3d4023d12230124bdb4856f
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Weak session validation bug let you login even after changing the session IDs and logging out from the accounts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-16_weak-session-validation-bug-let-you-login-even-after-changing-the-session-ids-an.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, business-logic, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `c81845e3816f2edf295798dd8defc85a11f5e0628d8faac16d53322ba1f06197`
- Text SHA256: `51508ad7b01d195eb700cab167c401ed30c22ff4c3d4023d12230124bdb4856f`


## Content

---
title: "Weak session validation bug let you login even after changing the session IDs and logging out from the accounts"
url: "https://medium.com/@manasjha7965/weak-session-validation-bug-let-you-login-even-after-changing-the-session-ids-and-logging-out-from-4bb3ee29a598"
authors: ["Manasjha (@manas_hunter)"]
programs: ["viator.com"]
bugs: ["Logic flaw", "Session management issue"]
publication_date: "2020-03-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4707
scraped_via: "browseros"
---

# Weak session validation bug let you login even after changing the session IDs and logging out from the accounts

Weak session validation bug let you login even after changing the session IDs and logging out from the accounts
Manas Harsh
Follow
1 min read
·
Mar 16, 2020

184

2

Hi friends,

While searching for bounties, I found an interesting bug which gave me $200 and it was a cool one. It was a logical bug and I learnt that we must see the session IDs while hunting for bugs.

So, I was hunting on a Hackerone and chose a random program. It was viator.com. So I started checking into logical bugs and suddenly I thought about creating two different accounts and play with them. What I did is, I exchanged the session ID of each other and still able to login. The worst part was it was working even after 4 hours once we logout and quit the browser.

So, here are the steps:-

Create two accounts on Viator.com
Login with both of them in different tabs.

3. Capture the request in burp after logging in for both of the accounts. Send the request to repeater

Get Manas Harsh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

4. Now, you can logout from both of the accounts. Clear the cookie and quit the browser.

5. In burp, exchange the session ID of the first account with another one. Once you check the response, you would be able to login successfully with the first account.

:-)

So, it was a 10 min bug and you just need to observer the things closely. Bugs are everywhere.

Peace:)

Follow me on twitter: @manas_hunter

LinkedIn:- https://www.linkedin.com/in/manas-harsh-05636a154
