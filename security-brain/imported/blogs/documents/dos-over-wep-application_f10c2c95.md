---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-19_dos-over-wep-application.md
original_filename: 2020-07-19_dos-over-wep-application.md
title: DOS over wep application
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: f10c2c95de4d49ce5d79734860a32ed7b775bf0ec8c1ff96c26ad3f1f8be5f52
text_sha256: b530f203ebe015c62860aa5ff924856532b62708822cdc921a895672d66bb495
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# DOS over wep application

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-19_dos-over-wep-application.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `f10c2c95de4d49ce5d79734860a32ed7b775bf0ec8c1ff96c26ad3f1f8be5f52`
- Text SHA256: `b530f203ebe015c62860aa5ff924856532b62708822cdc921a895672d66bb495`


## Content

---
title: "DOS over wep application"
url: "https://medium.com/@mohamedayad_72488/dos-over-wep-application-c5176dc29035"
authors: ["Mohamed Ayad"]
bugs: ["DoS"]
publication_date: "2020-07-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4396
scraped_via: "browseros"
---

# DOS over wep application

DOS over wep application
Mohamed Ayad
Follow
2 min read
·
Jul 19, 2020

13

1

peace upon you guys

today i will share with you a bug i have recently found in some target which was depending on Denial Of Service over web app

so without wasting any time, let’s jump in…

our target was having a feature that allowd you to add contacts in your contact page just by their names only // enter contact name , if it exists in the DB it will be added, the issue was that page splitting wasn’t enabled meaning all your added contacts will be in the same page.

so if we able to add for example 10K contact in the same page u can guess how much it takes the server to load the whole page.

what i did is that i have collected about 200K valid names from some github repos and txt files on Google, then i tried the whole wordlist againts our taget

Get Mohamed Ayad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

finally i was able to add just 10K contact but at the end it was sufficient POC for our attack as there was a delay from a server about 10 seconds

Press enter or click to view image in full size
10 seconds delay

steps:

1- go to contact page add some user

2- intercept your request with burp and send it to intruder

3- in the payload section of intruder tab paste your wordlist

4- start your attack and monitor server delay while loading the page

and yeah we have able to trigger a delay of about 10 seconds !!

thank you for reading ! hope you enjoyed it…

you can find me on twitter @0xMohamed_Ayad

also linkedin @0xmh3yad
