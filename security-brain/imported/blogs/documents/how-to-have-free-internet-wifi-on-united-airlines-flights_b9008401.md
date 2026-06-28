---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-17_how-to-have-free-internet-wifi-on-united-airlines-flights.md
original_filename: 2021-09-17_how-to-have-free-internet-wifi-on-united-airlines-flights.md
title: How to have free Internet WIFI on United Airlines flights
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
raw_sha256: b900840111b4cb1baf25ba65acadd0ba6ee63417a83acd7afd811314dae34072
text_sha256: 73de12994dc49bc01b7828343be0628c45da5e06ed208db2849572e6c6765fc4
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How to have free Internet WIFI on United Airlines flights

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-17_how-to-have-free-internet-wifi-on-united-airlines-flights.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `b900840111b4cb1baf25ba65acadd0ba6ee63417a83acd7afd811314dae34072`
- Text SHA256: `73de12994dc49bc01b7828343be0628c45da5e06ed208db2849572e6c6765fc4`


## Content

---
title: "How to have free Internet WIFI on United Airlines flights"
url: "https://medium.com/hacking-info-sec/how-to-have-free-internet-wifi-on-united-airlines-flights-65ead4087bc9"
authors: ["Philippe Delteil (@PhilippeDelteil)"]
programs: ["United Airlines"]
bugs: ["Payment tampering", "Logic flaw"]
publication_date: "2021-09-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3308
scraped_via: "browseros"
---

# How to have free Internet WIFI on United Airlines flights

Member-only story

How to have free Internet WIFI on United Airlines flights
Philippe Delteil
Follow
3 min read
·
Sep 18, 2021

35

This issue is out of their Bug bounty program, so I will just write it here.

Last September (2021) I was travelling from New York City to Las Vegas to attend DEFCON 29, my flight was canceled two times by Spirit. They managed to put my in another flight, a United Airlines one.

The flight had Wifi, but the price was around 14.99 dollars for 1 or 2 hours. I don't remember. I decided to find a way to get online for free, here's how I did it.

In order to pay for the WIFI service the 'system' needs to check for your credit card information and process the payment. But that means this website is using my browser to send data to their payment processing blabla. Well, that's the key, I thought it might be possible to keep that gate open.

Step 1 Browse and enter your credit card information

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
