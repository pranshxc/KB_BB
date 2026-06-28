---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-05_i-want-all-these-features.md
original_filename: 2020-08-05_i-want-all-these-features.md
title: I want all these features
category: documents
detected_topics:
- command-injection
- automation-abuse
- business-logic
tags:
- imported
- documents
- command-injection
- automation-abuse
- business-logic
language: en
raw_sha256: 5568943e1b3f23740f8952a94364635dd5b02a6d524a8980c153fcec953edeca
text_sha256: fa0a0c2237241fd5544cc57368fb8fda454438059cb9cc0158a0f31a18706e07
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# I want all these features

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-05_i-want-all-these-features.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `5568943e1b3f23740f8952a94364635dd5b02a6d524a8980c153fcec953edeca`
- Text SHA256: `fa0a0c2237241fd5544cc57368fb8fda454438059cb9cc0158a0f31a18706e07`


## Content

---
title: "I want all these features"
url: "https://medium.com/@mohamedayad_72488/i-want-all-these-features-bb41e8252020"
authors: ["Mohamed Ayad"]
bugs: ["Logic flaw", "Payment tampering"]
publication_date: "2020-08-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4352
scraped_via: "browseros"
---

# I want all these features

I want all these features
Mohamed Ayad
Follow
2 min read
·
Aug 5, 2020

65

السلام عليكم ورحمة الله وبركاته

Peace upon you everybody,

today we are going to discuss 2 logic bug that awards me 3 digit bounty in an eCommerce site designed for engineers to ease their life.

Press enter or click to view image in full size
TL;DR:

After finishing 15-day trial site asked you to subscribe for some of its offers, we have entry subscription and pro one, each one has its own features once you choose, the sever gives you back a link to the payment site. but we from entry subscription need all pro features, we are hackers yoo. the misconfigurations are that site doesn’t have server side checks .. so what if we in the middle manipulate the request sent to the server.

Attack scenario:

after going to subscription page click entry one send the request to intruder, doing the same with pro one. the request which is going to the server was JSON format and has key called features with some values for each subscription level, so what about getting all pro features and putting them in the entry one then the request, hence we got a all pro features.

Steps:

1- go to subscription page choose entry level, intercept the request and send it to repeater

Get Mohamed Ayad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

2- do the same with pro one

3- from JSON body request and with pro tab copy all features and paste it in entry tab

4- send the request and open the link of the subscription in the browser and bingoooo!!….

Note:

you can noticed in the begging i said 2 bugs, honestly the site consider it the same issue for both bugs so in summery problem was that the site allow you to add more users to your account, in the subscription each added user will pay 500$, and users key was send also with the JSON body so simply i deleted the key&value and request sent successfully.

Press enter or click to view image in full size

and that’s it

thank you for reading! hope you enjoyed it…

you can find me on twitter @0xMohamed_Ayad

also, Linkedin @0xmh3yad
