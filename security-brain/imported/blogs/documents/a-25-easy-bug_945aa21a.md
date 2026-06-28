---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-12_a-25-easy-bug.md
original_filename: 2019-12-12_a-25-easy-bug.md
title: A $25 Easy Bug.
category: documents
detected_topics:
- command-injection
- automation-abuse
tags:
- imported
- documents
- command-injection
- automation-abuse
language: en
raw_sha256: 945aa21a66d9b7a8ef0463ddc5217722239674c178a57bb5d9236c6fded9fa80
text_sha256: ae589490c4ecf77ae1beaa154e47407b7ffd36d79ad3b88d91748c2a3d4d4605
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# A $25 Easy Bug.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-12_a-25-easy-bug.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `945aa21a66d9b7a8ef0463ddc5217722239674c178a57bb5d9236c6fded9fa80`
- Text SHA256: `ae589490c4ecf77ae1beaa154e47407b7ffd36d79ad3b88d91748c2a3d4d4605`


## Content

---
title: "A $25 Easy Bug."
url: "https://medium.com/@navne3t/a-25-easy-bug-bdfcde4d1370"
authors: ["Navneet (@na5n33t)"]
bugs: ["Session management issue"]
bounty: "25"
publication_date: "2019-12-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4894
scraped_via: "browseros"
---

# A $25 Easy Bug.

A $25 Easy Bug.
Navneet
Follow
1 min read
·
Dec 13, 2019

57

This post is about a security bug i have found in one of the bug bounty program which was very easy to find and accepted by the company which leads to $25 bounty.

So, i was exploring the programs at openbugbounty.org where i got a website which have responsible disclosure. So, i decided to look for the bugs at that website.

So , after login i notice there was a button which allows user to delete his/her account. Which gives me the idea to test for “failure to invalidate session after deletion of account”

Get Navneet’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So , i try to look for some other domain of the website which uses the same credentials for login. And luckily I found one.

So, the functionality/flow was like this
User login using account.SomeWebsite.com
Then , also login at forums.SomeWebsite.com with same credentials.
Now , once you delete the user account from accounts.SomeWebsite.com
Still, session at forums.SomeWebsite.com is usable and also even able to post the commente and can perform other functionalities.
Also tried it with two different browser , login on both domain from both the browser then deletes from one browser and closed it. Still, session on other browser was usable.

Submitted the report and thought this will not be accepted but i give a try and they accepted it, fixed it and gave $25. Few days back i have found same issue with their another domain and got another $25. So ,it is now “A Easy $50 bug”

Feedback and comments are welcomed.
