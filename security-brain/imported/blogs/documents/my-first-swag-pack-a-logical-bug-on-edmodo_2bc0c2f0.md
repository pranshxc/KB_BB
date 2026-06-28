---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-05_my-first-swag-pack-a-logical-bug-on-edmodo.md
original_filename: 2018-08-05_my-first-swag-pack-a-logical-bug-on-edmodo.md
title: 'My First Swag Pack : A Logical Bug on Edmodo'
category: documents
detected_topics:
- idor
- xss
- command-injection
- business-logic
tags:
- imported
- documents
- idor
- xss
- command-injection
- business-logic
language: en
raw_sha256: 2bc0c2f013a256f1916fa01c0924eda6f9125840cd21121379fcaeccfc3a7c4f
text_sha256: 81f2e22cddfb9b2598e79374ccc6f7e7de4eb4c523a30c48828c8f2d5c88eccc
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# My First Swag Pack : A Logical Bug on Edmodo

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-05_my-first-swag-pack-a-logical-bug-on-edmodo.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, business-logic
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `2bc0c2f013a256f1916fa01c0924eda6f9125840cd21121379fcaeccfc3a7c4f`
- Text SHA256: `81f2e22cddfb9b2598e79374ccc6f7e7de4eb4c523a30c48828c8f2d5c88eccc`


## Content

---
title: "My First Swag Pack : A Logical Bug on Edmodo"
url: "https://www.secjuice.com/logical-bug-at-edmodo/"
final_url: "https://www.secjuice.com/logical-bug-at-edmodo/"
authors: ["Abartan Dhakal (@imhaxormad)"]
programs: ["Edmodo"]
bugs: ["Logic flaw"]
publication_date: "2018-08-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5773
---

[CYBERSEC](/tag/cybersec/)

# My First Swag Pack : A Logical Bug on Edmodo

A very short story about the first swag pack that security researcher Abartan Dhakal ever won, when he found a logical bug at Edmodo.

  * [ ![Abartan Dhakal](/content/images/size/w100/2018/12/profile.jpg) ](/author/abartan/)

#### [Abartan Dhakal](/author/abartan/)

Aug 5, 2018

[Tip Writer](https://ko-fi.com/abartandhakal)

![My First Swag Pack : A Logical Bug on Edmodo](/content/images/size/w2000/2018/08/london_phone-booth.jpg)

This is the short story of my first swag pack. Not so long ago, I was focused only on bounty sites, I saw some stories on facebook of my friends who were getting their 3-4th swags and I was like, wow I need to get in on this too. It all started with my plan to test edmodo, as their response time is awesome.

## THE BUG

I went through the edmodo site, signed up as a teacher, and started exploring its functionalities. I tried xss in the post page, NO LUCK. Tried idor from setting page, again NO LUCK. I thought ok, lets try some other target.

![](https://i.imgur.com/o6zDNf9.gif)

It was at just 5-7minutes, when I saw an "add a phone" option and I added my number and didn't verify because I wanted to check if I could bypass that. But still NO LUCK.

Then I created another account, tried to add the same number, it said : Its already in use.

[![Screenshot_from_2018_04_23_08_30_50](https://preview.ibb.co/c0mu4H/Screenshot_from_2018_04_23_08_30_50.png)](https://ibb.co/hcXZ4H?ref=secjuice.com)

Now I just managed to find a simple logical flaw where I could just add your number, not verify, and you can't use that at all when you wanna signup. It allows me to effectively block you from using two factor authentication on Edmodo if I know your phone number.For sure its not the most technically impressive hack you have ever seen, but its mine and I was proud of it.

## The Reward

Chip benson replied to confirm its validity and asked I not duplicate it within 24hrs. He rewarded me with an awesome Swag pack ;) It took 1 week for the swag pack to get to me but it was an awesome feeling seeing it arrive!!

Thanks for reading.

Happy Hunting <3

_Main Image Credit : The awesome piece of artwork used to head this article is called 'Red Phone Booth' and it was created by graphic designer[Mary-Ann Ramirez](https://dribbble.com/maryanneramirez?ref=secjuice.com)._
