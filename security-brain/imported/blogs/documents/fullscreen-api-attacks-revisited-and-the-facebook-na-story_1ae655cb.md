---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-15_fullscreen-api-attacks-revisited-and-the-facebook-na-story.md
original_filename: 2019-06-15_fullscreen-api-attacks-revisited-and-the-facebook-na-story.md
title: Fullscreen API Attack’s Revisited and the FaceBook NA Story
category: documents
detected_topics:
- command-injection
- mobile-security
tags:
- imported
- documents
- command-injection
- mobile-security
language: en
raw_sha256: 1ae655cb34681dcfce5d84919962961846185e31c7e607caef43fcabfb637f0b
text_sha256: 5f486b7c1747a52defedb8f05cb0b19b1b92a03e39f7764003bb443265ec9d2d
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Fullscreen API Attack’s Revisited and the FaceBook NA Story

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-15_fullscreen-api-attacks-revisited-and-the-facebook-na-story.md
- Source Type: markdown
- Detected Topics: command-injection, mobile-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `1ae655cb34681dcfce5d84919962961846185e31c7e607caef43fcabfb637f0b`
- Text SHA256: `5f486b7c1747a52defedb8f05cb0b19b1b92a03e39f7764003bb443265ec9d2d`


## Content

---
title: "Fullscreen API Attack’s Revisited and the FaceBook NA Story"
url: "https://medium.com/bug-bounty-hunting/fullscreen-api-attacks-revisited-and-the-fb-na-story-cbea3ca383c5"
authors: ["Circle Ninja (@circleninja)"]
programs: ["Meta / Facebook"]
bugs: ["Phishing"]
publication_date: "2019-06-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5214
scraped_via: "browseros"
---

# Fullscreen API Attack’s Revisited and the FaceBook NA Story

Fullscreen API Attack’s Revisited and the FaceBook NA Story
Ronnie Joseph
Follow
2 min read
·
Jun 16, 2019

50

Hello all, hope all is well on the other side of the terminal. :=}

I will be writing about a report sent to Facebook which was marked as NA. Feel free to use this if you wish as it is not “worth” by Facebook.

I am a bit short of time so I will try to make this very crisp and short. And sorry for any mistakes in grammar as I have posted it in one sitting.

Recently I saw some Facebook phishing bugs which got accepted by FB especially , Rahul Kankrale’s report .

I reused a method known as Fullscreen API Attacks floated by Feross Aboukhadijeh about seven years back.

Get Ronnie Joseph’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

You can read about his post here to learn more about this attack. Thanks to him for his excellent work. (must read.)

Using the HTML5 Fullscreen API for Phishing Attacks " Feross.org
Quick! Click this link to Bank Of America. There's nothing fishy about it at all! I promise! Go ahead - hover your…

feross.org

This issue was more of a browser issue at that time. Now most of them have fixed it like Chrome , Safari and Firefox by showing the site has gone to fullscreen or show time gap when going to fullscreen.

Later I realized that FB Android app also has inbuilt browser.

The Facebook browser never shows any delay nor any warning while going to fullscreen mode. So there was possibility to do phishing. I tested it with some friends and about half were victims of this method.

After some ok and no’s with the security team , it was marked as NA. What they said was that the url shows third party site while loading so it’s not an issue.

Due to time constraints I am directly giving the POC. YOU be the judge. (The initial link in video asks to “Signup to FB to Continue”).

Spread LOVE. Bye .
