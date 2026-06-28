---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-05_spoof-as-another-facebook-user-to-report-an-impostor-account.md
original_filename: 2022-04-05_spoof-as-another-facebook-user-to-report-an-impostor-account.md
title: Spoof as another Facebook user to report an impostor account
category: blogs
detected_topics:
- command-injection
tags:
- imported
- blogs
- command-injection
language: en
raw_sha256: f3bd3fe85d1c77e93f55f1907a1913b5f0c2242e769ea075074754396edc875b
text_sha256: dd51fe5873cf2d2b9aae469770dc47672df301d9dddc950a14ee706fa571ce72
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Spoof as another Facebook user to report an impostor account

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-05_spoof-as-another-facebook-user-to-report-an-impostor-account.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `f3bd3fe85d1c77e93f55f1907a1913b5f0c2242e769ea075074754396edc875b`
- Text SHA256: `dd51fe5873cf2d2b9aae469770dc47672df301d9dddc950a14ee706fa571ce72`


## Content

---
title: "Spoof as another Facebook user to report an impostor account"
url: "https://zerocode-ph.medium.com/spoof-as-another-facebook-user-to-report-an-impostor-account-f2dd6683744d"
authors: ["Syd Ricafort (@devsyd11)"]
programs: ["Meta / Facebook"]
bugs: ["Spoofing"]
publication_date: "2022-04-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2749
scraped_via: "browseros"
---

# Spoof as another Facebook user to report an impostor account

Spoof as another Facebook user to report an impostor account
Syd Ricafort (0cod3)
Follow
2 min read
·
Apr 5, 2022

5

1

Press enter or click to view image in full size

When I was helping someone take down a poser/impostor account. I tried to check the request body on what’s going on behind the scene. The endpoint required user to enter a contact email address and the link of the profile the user wanted to report.

Get Syd Ricafort (0cod3)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This is where I noticed something strange. When I try to supply a contact email address owned by another Facebook User, the user will get notified that he/she reported someone without his knowledge.

An FB Auto Response received by Unaware Victim

The “your_email” param does not check if the user issuing the request has active session or the email used is already owned by other Facebook user. Ideally the response should be something like “Please login to continue” or “The email address provided is already in used”, since the fb auto response is directly sent to the support inbox of the user who owns the email. This can be abuse in a large scale, an attacker can simply create a wordlist that contains email address and start the attack.

Follow me on twitter : https://twitter.com/devsyd11
