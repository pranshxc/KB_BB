---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-03_the-invincible-kid.md
original_filename: 2021-03-03_the-invincible-kid.md
title: The Invincible Kid
category: documents
detected_topics:
- command-injection
- business-logic
tags:
- imported
- documents
- command-injection
- business-logic
language: en
raw_sha256: 024d04812300aa3eebc7ebf27f453b696c33395e3288cb5d6d3c599935bacabf
text_sha256: 0a190906ce0b074ecab9aed4df87114df67c33cdd37ec2095a9c98ad5faa1091
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# The Invincible Kid

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-03_the-invincible-kid.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `024d04812300aa3eebc7ebf27f453b696c33395e3288cb5d6d3c599935bacabf`
- Text SHA256: `0a190906ce0b074ecab9aed4df87114df67c33cdd37ec2095a9c98ad5faa1091`


## Content

---
title: "The Invincible Kid"
page_title: "THE INVINCIBLE KID. This short write-up is about a… | by Samip Aryal | InfoSec Write-ups"
url: "https://infosecwriteups.com/the-invincible-kid-7ac1ce2887c0"
authors: ["Samip Aryal (@samiparyal_)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
bounty: "500"
publication_date: "2021-03-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3844
scraped_via: "browseros"
---

# The Invincible Kid

THE INVINCIBLE KID
Samip Aryal
Follow
3 min read
·
Mar 3, 2021

224

1

…

This short write-up is about a vulnerability in Facebook Lite that allowed anyone to be invincible to blocking for Facebook Lite Users.

…

U
sing Messenger Kids; users can create a messaging account of their children. Users can also choose to add any of their Facebook friends as a parent/guardian of the kid. After this, they are automatically added as one of the kid’s guardians without their consent or without any sort of invitation. However, they can remove themselves from the guardian role if they want; using the Facebook web or the Facebook app. But, there was no such feature in Facebook lite to remove oneself from the role when added as a guardian of a kid.

> Why was this thing a problem?

Because there’s a policy in Facebook that a parent account cannot block the messages of its own kid’s account.

Now, Using these two main points, an attacker could simply create an attack scenario where he could victimize any user with whom s/he is a friend. Simply, he could make a Messenger Kid Account and add the victim in the parent role of the Kid. This will allow him/her to message the victim unlimitedly using the kid account without ever being blocked.

Even if the victim blocks the attacker’s real account, there was no way for the victim to block the messages of the Kid Account using Facebook Lite.

#THE_INVINCIBLE_KID.

REPRODUCTION STEPS
==
1. Attacker goes to the messenger kids control section (using web or app).
2. Attacker then adds Victim as a guardian of the kid’s account.
3. Victim gets the notification (User A has added you as a guardian of the ….).
4. Victim finds no way to remove himself from the role.
5. Attacker then opens the kid’s account using Messenger Kids and messages the Victim.
6. Victim tries to block the kid’s messages, but cannot.
7. Victim then blocks Attacker from messaging as well as from Facebook.
8. Attacker can still message Victim using the kid’s account forever without ever being blocked or without the fear of being blocked.

Or, you can see the POC Video HERE.

…

Get Samip Aryal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Timeline of the report thread

Reported — Friday, 20 November 2020

Pre-Triaged — Wednesday, 25 November 2020

Triaged — Thursday, 26 November 2020

Shared additional info — Thursday, 17 December 2020

Asked for an update — Friday, 1 January 2021

Bounty Awarded —Monday, 1 February 2021

Facebook Reward Message

Fixed — Wednesday, 17 February 2021

Facebook Added a new feature in FBLite to resolve the issue

Fixed confirmed — Tuesday, 23 February 2021

Bypass sent [producable in mbasic.facebook.com & m.facebook.com] — — Tuesday, 23 February 2021

Bypass not accepted [Reason: Not high impact for those sites] & report finally closed — Monday, 1 March 2021

…
Thank you for reading this write-up about a simple vulnerability. If you have any suggestions/queries, I’m available on Facebook/ Instagram.
…
