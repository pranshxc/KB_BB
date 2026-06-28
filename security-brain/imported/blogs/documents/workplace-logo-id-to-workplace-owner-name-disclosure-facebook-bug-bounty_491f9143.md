---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-11_workplace-logo-id-to-workplace-owner-name-disclosure-facebook-bug-bounty.md
original_filename: 2019-01-11_workplace-logo-id-to-workplace-owner-name-disclosure-facebook-bug-bounty.md
title: Workplace Logo ID to workplace owner name Disclosure Facebook Bug Bounty
category: documents
detected_topics:
- idor
- command-injection
tags:
- imported
- documents
- idor
- command-injection
language: en
raw_sha256: 491f91433f7a26f096df6d880792fc4f61756b3e750e1068be5f2a298e5758ac
text_sha256: ee10be70e52f8067297c4bf41a6f6a80678a69257a4da5f08bd4330e4b86953a
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Workplace Logo ID to workplace owner name Disclosure Facebook Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-11_workplace-logo-id-to-workplace-owner-name-disclosure-facebook-bug-bounty.md
- Source Type: markdown
- Detected Topics: idor, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `491f91433f7a26f096df6d880792fc4f61756b3e750e1068be5f2a298e5758ac`
- Text SHA256: `ee10be70e52f8067297c4bf41a6f6a80678a69257a4da5f08bd4330e4b86953a`


## Content

---
title: "Workplace Logo ID to workplace owner name Disclosure Facebook Bug Bounty"
url: "https://medium.com/@evilboyajay/workplace-logo-id-to-workplace-owner-name-disclosurefacebook-bug-bounty-e745db59d0bd"
authors: ["Ajay Gautam (@evilboyajay)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
publication_date: "2019-01-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5479
scraped_via: "browseros"
---

# Workplace Logo ID to workplace owner name Disclosure Facebook Bug Bounty

Workplace Logo ID to workplace owner name Disclosure Facebook Bug Bounty
Ajay Gautam
Follow
1 min read
·
Jan 11, 2019

312

1

Hi
It’s me Ajay Gautam, Security Researcher at Nass and currently studying BIT (Hons) Computing. Today, I am going to share one of mine Facebook valid issue that I discovered in 2018.

I was able to see the workplace owner name via their logo ID, if the ID of the workplace logo was identified.

While we replace the event’s cover picture id to workplace logo id of other’s then, guess what happened? I was surprised seeing owner’s name in the response.

Workplace owner can only upload the logo of its workplace and the ID disclosed in workplace is the ID of admin itself.

So, during the journey of the vulnerability, Firstly, i created an event on my own workplace…

Then after, I uploaded a cover picture in the event and opened it in new tab.

Get Ajay Gautam’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After the cover picture was uploaded successfully, I replaced the fbid with the workplace logo id of another workplace
and the url link displayed as mentioned below:
https://workplace.facebook.com/photo.php?fbid=111128102791845&set=gm.1078085585673352&type=3&theater

And finally owner name was disclosed.

Timeline
Reported — May 31, 2018
Triaged — Jun 16, 2018
Bounty Awarded — Oct 9, 2018

Please see the POC video for the detail clarification of the vulnerability.
