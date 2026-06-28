---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-20_a-possibility-of-account-takeover-in-medium.md
original_filename: 2018-10-20_a-possibility-of-account-takeover-in-medium.md
title: A possibility of Account Takeover in Medium
category: documents
detected_topics:
- oauth
- command-injection
- otp
- business-logic
tags:
- imported
- documents
- oauth
- command-injection
- otp
- business-logic
language: en
raw_sha256: e8a99cba62828bc9460c3ccc7a91d945734a2c204985be56eb6d0353db85eb06
text_sha256: 9edd36080254eac75585a7ae7cd10b7f25222946b9068baf1a00422c47ab129c
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# A possibility of Account Takeover in Medium

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-20_a-possibility-of-account-takeover-in-medium.md
- Source Type: markdown
- Detected Topics: oauth, command-injection, otp, business-logic
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `e8a99cba62828bc9460c3ccc7a91d945734a2c204985be56eb6d0353db85eb06`
- Text SHA256: `9edd36080254eac75585a7ae7cd10b7f25222946b9068baf1a00422c47ab129c`


## Content

---
title: "A possibility of Account Takeover in Medium"
url: "https://medium.com/@notsoshant/a-possibility-of-account-takeover-in-medium-8d950e547639"
authors: ["Prashant Kumar (@notsoshant)"]
programs: ["Medium"]
bugs: ["Account takeover", "Logic flaw"]
publication_date: "2018-10-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5636
scraped_via: "browseros"
---

# A possibility of Account Takeover in Medium

A possibility of Account Takeover in Medium
Prashant Kumar
Follow
3 min read
·
Oct 20, 2018

15

Press enter or click to view image in full size

There are times when you discover something that is very common and ordinary which just blows your mind and you start thinking, “How come I didn’t knew this before!?”. I recently had that kind of a moment when I came to know that Twitter allows users to change their username. This immediately triggered a thought, “What if somewhere Twitter integration in a website is depending on Twitter username?”. I know this sounds crazy, but I thought this was worth a try.

The Vulnerability

Long story short, turns out the login from Twitter on Medium depends on the Twitter username! Since Twitter allows users to change their username, if someone having his medium account connected to Twitter changes his username, we can change our Twitter username to his and by logging in via Twitter in Medium, we’ll log into their account.

Here’s how it would look like:

Get Prashant Kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1. Login to Medium, go to Settings and link the account to Twitter:

Press enter or click to view image in full size
Medium account before connecting to Twitter
Twitter profile being connected to Medium
Press enter or click to view image in full size
After connecting Medium to Twitter

2. Now let’s say this Twitter user changed his username to something else. I as an attacker will change my Twitter username to notsoshant.

Attacker’s profile

3. Now go to Medium and choose the Sign In with Twitter option. By using attacker’s Twitter profile to log in, we can notice Medium actually logs in to victim’s Medium account.

Press enter or click to view image in full size
Attacker’s Twitter profile highlighted in victim’s profile

As stupid this vulnerability may look like, this obviously shows implementing OAuth can go very wrong sometimes. I don’t prefer OAuth in general because if an OAuth provider gets compromised, all the connected accounts will get compromised automatically. A recent Facebook vulnerability allowed attackers to access token for millions of users. If you are logged in to any service through Facebook, that account was compromised too! So folks, always prefer a new account for each website and avoid OAuth! And experts recommend this too.

Vulnerability Disclosure Timeline

September 13th, 2018: Vulnerability disclosed to Medium
September 25th, 2018: Vulnerability patched by Medium. No rewards or credits given.

Yeah, no rewards or credits because they concluded:

“Report does not meet the criteria outlined in the Bug Bounty program (https://medium.com/policy/mediums-bug-bounty-disclosure-program-34b1c80764c2), and therefore is not eligible for a reward.”

I guess it’s because it falls in the category of “Bugs that require unlikely user interaction or phishing”.
