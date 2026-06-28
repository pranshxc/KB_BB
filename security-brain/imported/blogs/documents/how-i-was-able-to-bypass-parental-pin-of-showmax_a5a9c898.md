---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-09_how-i-was-able-to-bypass-parental-pin-of-showmax.md
original_filename: 2021-06-09_how-i-was-able-to-bypass-parental-pin-of-showmax.md
title: How i was able to bypass parental pin of showmax
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: a5a9c8986c7542688b9392558029c34b8967289b88f88d39a750a736262fb500
text_sha256: f6e6657880c5c6a8955c67619a5b2c6c4323a28bd1f62ab3563977b5f37d0382
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# How i was able to bypass parental pin of showmax

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-09_how-i-was-able-to-bypass-parental-pin-of-showmax.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `a5a9c8986c7542688b9392558029c34b8967289b88f88d39a750a736262fb500`
- Text SHA256: `f6e6657880c5c6a8955c67619a5b2c6c4323a28bd1f62ab3563977b5f37d0382`


## Content

---
title: "How i was able to bypass parental pin of showmax"
url: "https://infosecwriteups.com/how-i-was-able-to-bypass-parental-pin-of-showmax-e6d6ec3af92d"
authors: ["abdulsec (@moodiAbdoul)"]
programs: ["Showmax"]
bugs: ["Broken authorization"]
bounty: "200"
publication_date: "2021-06-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3591
scraped_via: "browseros"
---

# How i was able to bypass parental pin of showmax

How i was able to bypass parental pin of showmax
abdulsec
Follow
1 min read
·
Jun 9, 2021

201

Showmax is a streaming service that offers a wide variety of award-winning TV shows, movies, anime, documentaries,

After i saw a disclosed report in Twitter by @lordjerry0x01 https://hackerone.com/reports/1077520
I said wawww , 2000$. for parental pin bypass , let me bypass the pin too As i have the same flow of @zseano, i hack the main app

The game begin

I started by create an account then clicking in each button to understand how the app works
after a few minute i found the parental control endpoint , now i added a code pin in kids profile so that, kids who dont has 18+ can’t watch adults serie

when browsing my burp history , i have found this https://www.showmax.com/eng/parentalControlForm/%2Fhome/true

i decide to take a look this url , because most of the time you can bypass the protecting by changing from True to false , false to true

Get abdulsec’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

when i copied and paste the url in kids profile , its disclose the parental pin

Steps To Reproduce:
login in to your showmax account
add parental pin
Go to https://www.showmax.com/eng/home
click watch triller
you will asked for parental pin
enter this url in your brower https://www.showmax.com/eng/parentalControlForm/%2Fhome/true
you will get the parental pin without confirming your password
now you change the parental pin , and you can bypass the password confirmation , for parental control

here the disclosed report https://hackerone.com/reports/1121169

thank you for taking your time to my report

you can found me in twitter https://twitter.com/moodiAbdoul
